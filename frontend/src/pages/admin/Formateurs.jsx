import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { 
    UserPlus,
    Trash2,
    Copy,
    AlertTriangle
} from 'lucide-react';
import { Button } from '../../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/card';
import { Input } from '../../components/ui/input';
import { Label } from '../../components/ui/label';
import Layout from '../../components/Layout';
import { adminGetFormateurs, adminCreateFormateur, adminDeleteFormateur, getUser } from '../../lib/api';
import { toast } from 'sonner';

const AdminFormateurs = () => {
    const navigate = useNavigate();
    const user = getUser();
    const [loading, setLoading] = useState(true);
    const [formateurs, setFormateurs] = useState([]);
    const [showCreate, setShowCreate] = useState(false);
    const [creating, setCreating] = useState(false);
    const [deleteConfirm, setDeleteConfirm] = useState(null);
    const [formData, setFormData] = useState({
        email: '',
        nom: '',
        prenom: ''
    });
    const [tempPassword, setTempPassword] = useState(null);

    useEffect(() => {
        if (!user || user.role !== 'admin') {
            navigate('/login');
            return;
        }
        loadData();
    }, []);

    const loadData = async () => {
        try {
            const data = await adminGetFormateurs();
            setFormateurs(data);
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors du chargement');
        } finally {
            setLoading(false);
        }
    };

    const handleCreate = async (e) => {
        e.preventDefault();
        setCreating(true);
        try {
            const result = await adminCreateFormateur(formData);
            setTempPassword(result.temp_password);
            toast.success('Formateur créé avec succès !');
            loadData();
            setFormData({ email: '', nom: '', prenom: '' });
        } catch (error) {
            console.error('Erreur:', error);
            toast.error(error.response?.data?.detail || 'Erreur lors de la création');
        } finally {
            setCreating(false);
        }
    };

    const handleDelete = async (formateurId) => {
        try {
            await adminDeleteFormateur(formateurId);
            toast.success('Formateur supprimé');
            setDeleteConfirm(null);
            loadData();
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors de la suppression');
        }
    };

    const copyPassword = () => {
        navigator.clipboard.writeText(tempPassword);
        toast.success('Mot de passe copié !');
    };

    if (loading) {
        return (
            <Layout>
                <div className="flex items-center justify-center min-h-[60vh]">
                    <div className="spinner"></div>
                </div>
            </Layout>
        );
    }

    return (
        <Layout>
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8" data-testid="admin-formateurs">
                {/* Header */}
                <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-8">
                    <div>
                        <h1 className="text-3xl font-bold text-slate-900 mb-2">
                            Gestion des Formateurs
                        </h1>
                        <p className="text-slate-600">
                            Créez et gérez les comptes formateurs de la plateforme.
                        </p>
                    </div>
                    <Button 
                        className="bg-red-600 hover:bg-red-700"
                        onClick={() => { setShowCreate(true); setTempPassword(null); }}
                    >
                        <UserPlus className="w-4 h-4 mr-2" />
                        Nouveau formateur
                    </Button>
                </div>

                {/* Temp Password Alert */}
                {tempPassword && (
                    <Card className="mb-6 border-yellow-200 bg-yellow-50">
                        <CardContent className="p-4">
                            <div className="flex items-start gap-3">
                                <AlertTriangle className="w-5 h-5 text-yellow-600 mt-0.5" />
                                <div className="flex-1">
                                    <p className="font-medium text-yellow-800">Mot de passe temporaire créé</p>
                                    <p className="text-sm text-yellow-700 mt-1">
                                        Communiquez ce mot de passe au formateur. Il devra le changer à sa première connexion.
                                    </p>
                                    <div className="flex items-center gap-2 mt-3">
                                        <code className="px-3 py-2 bg-white rounded border font-mono text-lg">{tempPassword}</code>
                                        <Button variant="outline" size="sm" onClick={copyPassword}>
                                            <Copy className="w-4 h-4 mr-1" />
                                            Copier
                                        </Button>
                                    </div>
                                </div>
                                <Button variant="ghost" size="sm" onClick={() => setTempPassword(null)}>
                                    ✕
                                </Button>
                            </div>
                        </CardContent>
                    </Card>
                )}

                {/* Create Form */}
                {showCreate && (
                    <Card className="mb-8 animate-fade-in">
                        <CardHeader>
                            <CardTitle>Créer un nouveau formateur</CardTitle>
                        </CardHeader>
                        <CardContent>
                            <form onSubmit={handleCreate} className="space-y-4">
                                <div className="grid md:grid-cols-3 gap-4">
                                    <div className="space-y-2">
                                        <Label htmlFor="prenom">Prénom</Label>
                                        <Input
                                            id="prenom"
                                            placeholder="Jean"
                                            value={formData.prenom}
                                            onChange={(e) => setFormData({...formData, prenom: e.target.value})}
                                            required
                                        />
                                    </div>
                                    <div className="space-y-2">
                                        <Label htmlFor="nom">Nom</Label>
                                        <Input
                                            id="nom"
                                            placeholder="Dupont"
                                            value={formData.nom}
                                            onChange={(e) => setFormData({...formData, nom: e.target.value})}
                                            required
                                        />
                                    </div>
                                    <div className="space-y-2">
                                        <Label htmlFor="email">Email</Label>
                                        <Input
                                            id="email"
                                            type="email"
                                            placeholder="jean.dupont@example.com"
                                            value={formData.email}
                                            onChange={(e) => setFormData({...formData, email: e.target.value})}
                                            required
                                        />
                                    </div>
                                </div>
                                
                                <p className="text-sm text-slate-500">
                                    Un mot de passe temporaire sera généré. Le formateur devra le changer à sa première connexion.
                                </p>

                                <div className="flex gap-3 pt-4">
                                    <Button type="submit" className="bg-red-600 hover:bg-red-700" disabled={creating}>
                                        {creating ? <div className="spinner w-5 h-5 border-2 border-white/30 border-t-white"></div> : 'Créer le formateur'}
                                    </Button>
                                    <Button type="button" variant="outline" onClick={() => setShowCreate(false)}>
                                        Annuler
                                    </Button>
                                </div>
                            </form>
                        </CardContent>
                    </Card>
                )}

                {/* Formateurs List */}
                <Card>
                    <CardHeader>
                        <CardTitle>Liste des formateurs ({formateurs.length})</CardTitle>
                    </CardHeader>
                    <CardContent>
                        {formateurs.length === 0 ? (
                            <div className="empty-state py-8">
                                <UserPlus className="w-12 h-12 mx-auto text-slate-300 mb-3" />
                                <p className="text-slate-500">Aucun formateur</p>
                            </div>
                        ) : (
                            <div className="space-y-3">
                                {formateurs.map((formateur) => (
                                    <div 
                                        key={formateur.id}
                                        className="flex items-center justify-between p-4 bg-slate-50 rounded-lg"
                                    >
                                        <div className="flex-1">
                                            <div className="flex items-center gap-2">
                                                <p className="font-medium text-slate-900">
                                                    {formateur.prenom} {formateur.nom}
                                                </p>
                                                {formateur.must_set_password && (
                                                    <span className="px-2 py-0.5 bg-yellow-100 text-yellow-700 text-xs rounded font-medium">
                                                        En attente
                                                    </span>
                                                )}
                                            </div>
                                            <p className="text-sm text-slate-500">{formateur.email}</p>
                                        </div>
                                        <div className="flex items-center gap-4">
                                            <div className="text-right">
                                                <p className="font-medium text-slate-900">{formateur.nb_groupes || 0}</p>
                                                <p className="text-xs text-slate-500">groupes</p>
                                            </div>
                                            
                                            {deleteConfirm === formateur.id ? (
                                                <div className="flex gap-2">
                                                    <Button 
                                                        size="sm" 
                                                        variant="destructive"
                                                        onClick={() => handleDelete(formateur.id)}
                                                    >
                                                        Confirmer
                                                    </Button>
                                                    <Button 
                                                        size="sm" 
                                                        variant="outline"
                                                        onClick={() => setDeleteConfirm(null)}
                                                    >
                                                        Annuler
                                                    </Button>
                                                </div>
                                            ) : (
                                                <Button 
                                                    size="sm" 
                                                    variant="ghost"
                                                    className="text-red-600 hover:text-red-700 hover:bg-red-50"
                                                    onClick={() => setDeleteConfirm(formateur.id)}
                                                >
                                                    <Trash2 className="w-4 h-4" />
                                                </Button>
                                            )}
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

export default AdminFormateurs;
