import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { 
    Plus,
    Pencil,
    Trash2,
    BookOpen,
    FileText,
    Shield,
    Heart
} from 'lucide-react';
import { Button } from '../../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/card';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../../components/ui/tabs';
import Layout from '../../components/Layout';
import { getChapters, adminDeleteChapter, getUser } from '../../lib/api';
import { toast } from 'sonner';

const AdminChapters = () => {
    const navigate = useNavigate();
    const user = getUser();
    const [loading, setLoading] = useState(true);
    const [pseChapters, setPseChapters] = useState([]);
    const [pscChapters, setPscChapters] = useState([]);
    const [deleteConfirm, setDeleteConfirm] = useState(null);
    const [activeTab, setActiveTab] = useState('PSE');

    useEffect(() => {
        if (!user || user.role !== 'admin') {
            navigate('/login');
            return;
        }
        loadData();
    }, []);

    const loadData = async () => {
        try {
            const [pseData, pscData] = await Promise.all([
                getChapters('PSE'),
                getChapters('PSC')
            ]);
            setPseChapters(pseData);
            setPscChapters(pscData);
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors du chargement');
        } finally {
            setLoading(false);
        }
    };

    const handleDelete = async (chapterId) => {
        try {
            await adminDeleteChapter(chapterId);
            toast.success('Chapitre supprimé');
            setDeleteConfirm(null);
            loadData();
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors de la suppression');
        }
    };

    const renderChaptersList = (chapters, formationType) => {
        if (chapters.length === 0) {
            return (
                <div className="empty-state py-8">
                    <FileText className="w-12 h-12 mx-auto text-slate-300 mb-3" />
                    <p className="text-slate-500 mb-4">Aucun chapitre {formationType}</p>
                    <Link to={`/admin/chapter?type=${formationType}`}>
                        <Button size="sm" className="bg-red-600 hover:bg-red-700">
                            Créer un chapitre
                        </Button>
                    </Link>
                </div>
            );
        }

        return (
            <div className="space-y-3">
                {chapters.map((chapter) => (
                    <div 
                        key={chapter.id}
                        className="flex items-center justify-between p-4 bg-slate-50 rounded-lg hover:bg-slate-100 transition-colors"
                    >
                        <div className="flex items-center gap-4 flex-1">
                            <div className={`w-12 h-12 rounded-xl flex items-center justify-center ${
                                formationType === 'PSE' ? 'bg-red-100' : 'bg-green-100'
                            }`}>
                                {formationType === 'PSE' ? (
                                    <Shield className={`w-6 h-6 ${formationType === 'PSE' ? 'text-red-600' : 'text-green-600'}`} />
                                ) : (
                                    <Heart className="w-6 h-6 text-green-600" />
                                )}
                            </div>
                            <div className="flex-1">
                                <div className="flex items-center gap-2 mb-1">
                                    <span className="text-xs font-medium px-2 py-0.5 bg-slate-200 text-slate-700 rounded">
                                        Chapitre {chapter.numero}
                                    </span>
                                    <p className="font-medium text-slate-900">{chapter.titre}</p>
                                </div>
                                <p className="text-sm text-slate-500">
                                    {chapter.description}
                                </p>
                                <p className="text-xs text-slate-400 mt-1">
                                    {chapter.fiches?.length || 0} fiches • {chapter.icon}
                                </p>
                            </div>
                        </div>
                        <div className="flex items-center gap-2">
                            <Link to={`/admin/chapter/${chapter.id}`}>
                                <Button variant="outline" size="sm">
                                    <Pencil className="w-4 h-4 mr-1" />
                                    Modifier
                                </Button>
                            </Link>
                            
                            {deleteConfirm === chapter.id ? (
                                <div className="flex gap-2">
                                    <Button 
                                        size="sm" 
                                        variant="destructive"
                                        onClick={() => handleDelete(chapter.id)}
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
                                    onClick={() => setDeleteConfirm(chapter.id)}
                                >
                                    <Trash2 className="w-4 h-4" />
                                </Button>
                            )}
                        </div>
                    </div>
                ))}
            </div>
        );
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
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8" data-testid="admin-chapters">
                {/* Header */}
                <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-8">
                    <div>
                        <h1 className="text-3xl font-bold text-slate-900 mb-2">
                            Gestion des Chapitres et Contenu
                        </h1>
                        <p className="text-slate-600">
                            Créez, modifiez ou supprimez des chapitres avec leurs fiches, textes, images et vidéos.
                        </p>
                    </div>
                    <Link to={`/admin/chapter?type=${activeTab}`}>
                        <Button className="bg-red-600 hover:bg-red-700">
                            <Plus className="w-4 h-4 mr-2" />
                            Nouveau chapitre
                        </Button>
                    </Link>
                </div>

                {/* Tabs for PSE / PSC */}
                <Tabs value={activeTab} onValueChange={setActiveTab}>
                    <TabsList className="grid w-full max-w-md grid-cols-2">
                        <TabsTrigger value="PSE">
                            <Shield className="w-4 h-4 mr-2" />
                            PSE ({pseChapters.length})
                        </TabsTrigger>
                        <TabsTrigger value="PSC">
                            <Heart className="w-4 h-4 mr-2" />
                            PSC ({pscChapters.length})
                        </TabsTrigger>
                    </TabsList>

                    <TabsContent value="PSE" className="mt-6">
                        <Card>
                            <CardHeader>
                                <CardTitle className="flex items-center gap-2">
                                    <Shield className="w-5 h-5 text-red-600" />
                                    Chapitres PSE - Premiers Secours en Équipe
                                </CardTitle>
                            </CardHeader>
                            <CardContent>
                                {renderChaptersList(pseChapters, 'PSE')}
                            </CardContent>
                        </Card>
                    </TabsContent>

                    <TabsContent value="PSC" className="mt-6">
                        <Card>
                            <CardHeader>
                                <CardTitle className="flex items-center gap-2">
                                    <Heart className="w-5 h-5 text-green-600" />
                                    Chapitres PSC - Premiers Secours Citoyen
                                </CardTitle>
                            </CardHeader>
                            <CardContent>
                                {renderChaptersList(pscChapters, 'PSC')}
                            </CardContent>
                        </Card>
                    </TabsContent>
                </Tabs>
            </div>
        </Layout>
    );
};

export default AdminChapters;
