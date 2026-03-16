import React, { useState, useEffect } from 'react';
import { FileText, Download, User } from 'lucide-react';
import { Button } from '../../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/card';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../../components/ui/tabs';
import Layout from '../../components/Layout';
import { getStagiaireDocuments, downloadDocument } from '../../lib/api';
import { toast } from 'sonner';

const StagiaireDocuments = () => {
    const [documents, setDocuments] = useState([]);
    const [loading, setLoading] = useState(true);
    const [activeTab, setActiveTab] = useState('all');

    useEffect(() => {
        loadDocuments();
    }, []);

    const loadDocuments = async () => {
        setLoading(true);
        try {
            const docs = await getStagiaireDocuments();
            setDocuments(docs);
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors du chargement');
        } finally {
            setLoading(false);
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
            toast.success('Téléchargement démarré');
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

    const getDocumentsByCategory = (category) => {
        if (category === 'all') return documents;
        return documents.filter(doc => doc.categorie === category);
    };

    const renderDocumentList = (docs) => {
        if (docs.length === 0) {
            return (
                <div className="text-center py-12 text-slate-500">
                    <FileText className="w-12 h-12 mx-auto mb-2 text-slate-300" />
                    <p>Aucun document disponible</p>
                </div>
            );
        }

        return (
            <div className="space-y-2">
                {docs.map((doc) => (
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
                                    <span className="flex items-center gap-1">
                                        <User className="w-3 h-3" />
                                        {doc.formateur_nom}
                                    </span>
                                    <span>•</span>
                                    <span>{formatFileSize(doc.file_size)}</span>
                                    <span>•</span>
                                    <span>{new Date(doc.uploaded_at).toLocaleDateString('fr-FR')}</span>
                                </div>
                            </div>
                        </div>
                        <Button
                            variant="outline"
                            size="sm"
                            onClick={() => handleDownload(doc)}
                            className="border-red-600 text-red-600 hover:bg-red-50"
                        >
                            <Download className="w-4 h-4 mr-2" />
                            Télécharger
                        </Button>
                    </div>
                ))}
            </div>
        );
    };

    return (
        <Layout>
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                <h1 className="text-3xl font-bold text-slate-900 mb-6">Mes documents</h1>

                <Card>
                    <CardHeader>
                        <CardTitle>Documents de formation</CardTitle>
                        <p className="text-sm text-slate-600 mt-1">
                            Retrouvez ici tous les documents mis à disposition par vos formateurs
                        </p>
                    </CardHeader>
                    <CardContent>
                        {loading ? (
                            <div className="text-center py-8">
                                <div className="spinner mx-auto"></div>
                            </div>
                        ) : (
                            <Tabs value={activeTab} onValueChange={setActiveTab}>
                                <TabsList className="grid w-full grid-cols-4 mb-6">
                                    <TabsTrigger value="all">
                                        Tous ({documents.length})
                                    </TabsTrigger>
                                    <TabsTrigger value="Cours">
                                        Cours ({getDocumentsByCategory('Cours').length})
                                    </TabsTrigger>
                                    <TabsTrigger value="Certificats">
                                        Certificats ({getDocumentsByCategory('Certificats').length})
                                    </TabsTrigger>
                                    <TabsTrigger value="Évaluations">
                                        Évaluations ({getDocumentsByCategory('Évaluations').length})
                                    </TabsTrigger>
                                </TabsList>

                                <TabsContent value="all">
                                    {renderDocumentList(documents)}
                                </TabsContent>
                                <TabsContent value="Cours">
                                    {renderDocumentList(getDocumentsByCategory('Cours'))}
                                </TabsContent>
                                <TabsContent value="Certificats">
                                    {renderDocumentList(getDocumentsByCategory('Certificats'))}
                                </TabsContent>
                                <TabsContent value="Évaluations">
                                    {renderDocumentList(getDocumentsByCategory('Évaluations'))}
                                </TabsContent>
                            </Tabs>
                        )}
                    </CardContent>
                </Card>
            </div>
        </Layout>
    );
};

export default StagiaireDocuments;
