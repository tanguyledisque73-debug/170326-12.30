import React, { useState, useEffect } from 'react';
import { Upload, FileText, Trash2, Download, Users, User } from 'lucide-react';
import { Button } from '../../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/card';
import { Input } from '../../components/ui/input';
import { Label } from '../../components/ui/label';
import { Textarea } from '../../components/ui/textarea';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../components/ui/select';
import Layout from '../../components/Layout';
import { uploadDocument, getFormateurDocuments, deleteDocument, formateurGetGroupes, downloadDocument } from '../../lib/api';
import { toast } from 'sonner';

const Documents = () => {
    const [documents, setDocuments] = useState([]);
    const [groupes, setGroupes] = useState([]);
    const [loading, setLoading] = useState(true);
    const [uploading, setUploading] = useState(false);
    const [showUploadForm, setShowUploadForm] = useState(false);
    
    const [formData, setFormData] = useState({
        titre: '',
        categorie: 'Cours',
        description: '',
        destinataire_type: 'groupe',
        groupe_id: '',
        stagiaire_id: '',
        file: null
    });

    useEffect(() => {
        loadData();
    }, []);

    const loadData = async () => {
        setLoading(true);
        try {
            const [docs, grps] = await Promise.all([
                getFormateurDocuments(),
                formateurGetGroupes()
            ]);
            setDocuments(docs);
            setGroupes(grps);
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors du chargement');
        } finally {
            setLoading(false);
        }
    };

    const handleFileChange = (e) => {
        const file = e.target.files[0];
        if (file) {
            setFormData({ ...formData, file });
        }
    };

    const handleUpload = async (e) => {
        e.preventDefault();
        
        if (!formData.file || !formData.titre) {
            toast.error('Veuillez remplir tous les champs requis');
            return;
        }

        if (formData.destinataire_type === 'groupe' && !formData.groupe_id) {
            toast.error('Veuillez sélectionner un groupe');
            return;
        }

        if (formData.destinataire_type === 'stagiaire' && !formData.stagiaire_id) {
            toast.error('Veuillez entrer l\'ID du stagiaire');
            return;
        }

        setUploading(true);
        try {
            const data = new FormData();
            data.append('file', formData.file);
            data.append('titre', formData.titre);
            data.append('categorie', formData.categorie);
            data.append('description', formData.description || '');
            data.append('destinataire_type', formData.destinataire_type);
            
            if (formData.destinataire_type === 'groupe') {
                data.append('groupe_id', formData.groupe_id);
            } else {
                data.append('stagiaire_id', formData.stagiaire_id);
            }

            const formDataObj = {};
            for (let [key, value] of data.entries()) {
                if (key !== 'file') {
                    formDataObj[key] = value;
                }
            }

            const queryParams = new URLSearchParams(formDataObj).toString();
            const uploadUrl = `/formateur/document/upload?${queryParams}`;
            
            const token = localStorage.getItem('secours73_token');
            const response = await fetch(process.env.REACT_APP_BACKEND_URL + '/api' + uploadUrl + `&token=${token}`, {
                method: 'POST',
                body: data
            });

            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.detail || 'Erreur upload');
            }

            toast.success('Document uploadé avec succès !');
            setShowUploadForm(false);
            setFormData({
                titre: '',
                categorie: 'Cours',
                description: '',
                destinataire_type: 'groupe',
                groupe_id: '',
                stagiaire_id: '',
                file: null
            });
            loadData();
        } catch (error) {
            console.error('Erreur:', error);
            toast.error(error.message || 'Erreur lors de l\'upload');
        } finally {
            setUploading(false);
        }
    };

    const handleDelete = async (docId) => {
        if (!window.confirm('Êtes-vous sûr de vouloir supprimer ce document ?')) {
            return;
        }

        try {
            await deleteDocument(docId);
            toast.success('Document supprimé');
            loadData();
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors de la suppression');
        }
    };

    const handleDownload = async (doc) => {
        try {
            const blob = await downloadDocument(doc.id);
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = doc.original_filename || doc.titre;
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors du téléchargement');
        }
    };

    const formatFileSize = (bytes) => {
        if (bytes < 1024) return bytes + ' B';
        if (bytes < 1024 * 1024) return (bytes / 1024).toFixed(1) + ' KB';
        return (bytes / (1024 * 1024)).toFixed(1) + ' MB';
    };

    return (
        <Layout>
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                <div className="flex items-center justify-between mb-6">
                    <h1 className="text-3xl font-bold text-slate-900">Base documentaire</h1>
                    <Button 
                        onClick={() => setShowUploadForm(!showUploadForm)}
                        className="bg-red-600 hover:bg-red-700"
                    >
                        <Upload className="w-4 h-4 mr-2" />
                        {showUploadForm ? 'Annuler' : 'Nouveau document'}
                    </Button>
                </div>

                {showUploadForm && (
                    <Card className="mb-6">
                        <CardHeader>
                            <CardTitle>Uploader un document</CardTitle>
                        </CardHeader>
                        <CardContent>
                            <form onSubmit={handleUpload} className="space-y-4">
                                <div className="grid md:grid-cols-2 gap-4">
                                    <div>
                                        <Label htmlFor="titre">Titre du document *</Label>
                                        <Input
                                            id="titre"
                                            value={formData.titre}
                                            onChange={(e) => setFormData({ ...formData, titre: e.target.value })}
                                            placeholder="Ex: Support de cours PSE1"
                                            required
                                        />
                                    </div>
                                    <div>
                                        <Label htmlFor="categorie">Catégorie *</Label>
                                        <Select 
                                            value={formData.categorie}
                                            onValueChange={(value) => setFormData({ ...formData, categorie: value })}
                                        >
                                            <SelectTrigger>
                                                <SelectValue />
                                            </SelectTrigger>
                                            <SelectContent>
                                                <SelectItem value="Cours">Cours</SelectItem>
                                                <SelectItem value="Certificats">Certificats</SelectItem>
                                                <SelectItem value="Évaluations">Évaluations</SelectItem>
                                            </SelectContent>
                                        </Select>
                                    </div>
                                </div>

                                <div>
                                    <Label htmlFor="description">Description</Label>
                                    <Textarea
                                        id="description"
                                        value={formData.description}
                                        onChange={(e) => setFormData({ ...formData, description: e.target.value })}
                                        placeholder="Description du document (optionnel)"
                                        rows={3}
                                    />
                                </div>

                                <div className="grid md:grid-cols-2 gap-4">
                                    <div>
                                        <Label htmlFor="destinataire_type">Destinataire *</Label>
                                        <Select 
                                            value={formData.destinataire_type}
                                            onValueChange={(value) => setFormData({ ...formData, destinataire_type: value })}
                                        >
                                            <SelectTrigger>
                                                <SelectValue />
                                            </SelectTrigger>
                                            <SelectContent>
                                                <SelectItem value="groupe">Pour tout un groupe</SelectItem>
                                                <SelectItem value="stagiaire">Pour un stagiaire spécifique</SelectItem>
                                            </SelectContent>
                                        </Select>
                                    </div>

                                    {formData.destinataire_type === 'groupe' ? (
                                        <div>
                                            <Label htmlFor="groupe_id">Sélectionner le groupe *</Label>
                                            <Select 
                                                value={formData.groupe_id}
                                                onValueChange={(value) => setFormData({ ...formData, groupe_id: value })}
                                            >
                                                <SelectTrigger>
                                                    <SelectValue placeholder="Choisir un groupe" />
                                                </SelectTrigger>
                                                <SelectContent>
                                                    {groupes.map(groupe => (
                                                        <SelectItem key={groupe.id} value={groupe.id}>
                                                            {groupe.nom}
                                                        </SelectItem>
                                                    ))}
                                                </SelectContent>
                                            </Select>
                                        </div>
                                    ) : (
                                        <div>
                                            <Label htmlFor="stagiaire_id">ID du stagiaire *</Label>
                                            <Input
                                                id="stagiaire_id"
                                                value={formData.stagiaire_id}
                                                onChange={(e) => setFormData({ ...formData, stagiaire_id: e.target.value })}
                                                placeholder="Entrer l'ID du stagiaire"
                                                required={formData.destinataire_type === 'stagiaire'}
                                            />
                                        </div>
                                    )}
                                </div>

                                <div>
                                    <Label htmlFor="file">Fichier *</Label>
                                    <Input
                                        id="file"
                                        type="file"
                                        onChange={handleFileChange}
                                        required
                                    />
                                    <p className="text-xs text-slate-500 mt-1">
                                        Tous types de fichiers acceptés (PDF, Word, Excel, Images, etc.)
                                    </p>
                                </div>

                                <div className="flex gap-2">
                                    <Button 
                                        type="submit" 
                                        className="bg-red-600 hover:bg-red-700"
                                        disabled={uploading}
                                    >
                                        {uploading ? 'Upload en cours...' : 'Uploader'}
                                    </Button>
                                    <Button 
                                        type="button" 
                                        variant="outline"
                                        onClick={() => setShowUploadForm(false)}
                                    >
                                        Annuler
                                    </Button>
                                </div>
                            </form>
                        </CardContent>
                    </Card>
                )}

                <Card>
                    <CardHeader>
                        <CardTitle>Mes documents uploadés ({documents.length})</CardTitle>
                    </CardHeader>
                    <CardContent>
                        {loading ? (
                            <div className="text-center py-8">
                                <div className="spinner mx-auto"></div>
                            </div>
                        ) : documents.length === 0 ? (
                            <div className="text-center py-8 text-slate-500">
                                <FileText className="w-12 h-12 mx-auto mb-2 text-slate-300" />
                                <p>Aucun document uploadé</p>
                            </div>
                        ) : (
                            <div className="space-y-2">
                                {documents.map((doc) => (
                                    <div
                                        key={doc.id}
                                        className="flex items-center justify-between p-4 border rounded-lg hover:bg-slate-50"
                                    >
                                        <div className="flex items-start gap-3 flex-1">
                                            <FileText className="w-5 h-5 text-red-600 mt-1" />
                                            <div className="flex-1">
                                                <div className="flex items-center gap-2">
                                                    <h3 className="font-medium text-slate-900">{doc.titre}</h3>
                                                    <span className="px-2 py-0.5 bg-blue-100 text-blue-700 text-xs rounded">
                                                        {doc.categorie}
                                                    </span>
                                                </div>
                                                {doc.description && (
                                                    <p className="text-sm text-slate-600 mt-1">{doc.description}</p>
                                                )}
                                                <div className="flex items-center gap-4 mt-2 text-xs text-slate-500">
                                                    <span>{formatFileSize(doc.file_size)}</span>
                                                    <span>•</span>
                                                    <span>{new Date(doc.uploaded_at).toLocaleDateString('fr-FR')}</span>
                                                    <span>•</span>
                                                    {doc.destinataire_type === 'groupe' ? (
                                                        <span className="flex items-center gap-1">
                                                            <Users className="w-3 h-3" />
                                                            Groupe
                                                        </span>
                                                    ) : (
                                                        <span className="flex items-center gap-1">
                                                            <User className="w-3 h-3" />
                                                            Individuel
                                                        </span>
                                                    )}
                                                </div>
                                            </div>
                                        </div>
                                        <div className="flex gap-2">
                                            <Button
                                                variant="ghost"
                                                size="sm"
                                                onClick={() => handleDownload(doc)}
                                            >
                                                <Download className="w-4 h-4" />
                                            </Button>
                                            <Button
                                                variant="ghost"
                                                size="sm"
                                                onClick={() => handleDelete(doc.id)}
                                                className="text-red-600 hover:text-red-700 hover:bg-red-50"
                                            >
                                                <Trash2 className="w-4 h-4" />
                                            </Button>
                                        </div>
                                    </div>
                                ))}
                            </div>
                        )}
                    </CardContent>
                </Card>
            </div>
        </Layout>
    );
};

export default Documents;
