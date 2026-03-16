import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { 
    BookOpen, 
    Heart,
    Lock,
    ArrowRight
} from 'lucide-react';
import { Button } from '../../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/card';
import Layout from '../../components/Layout';
import { getChaptersPreview, getPSCChapters, getUser } from '../../lib/api';
import { toast } from 'sonner';

const VisiteurDashboard = () => {
    const navigate = useNavigate();
    const user = getUser();
    const [loading, setLoading] = useState(true);
    const [previewChapters, setPreviewChapters] = useState([]);
    const [pscChapters, setPscChapters] = useState([]);

    useEffect(() => {
        if (!user || user.role !== 'visiteur') {
            navigate('/login');
            return;
        }
        loadData();
    }, []);

    const loadData = async () => {
        try {
            const [preview, psc] = await Promise.all([
                getChaptersPreview(),
                getPSCChapters()
            ]);
            setPreviewChapters(preview);
            setPscChapters(psc);
        } catch (error) {
            console.error('Erreur:', error);
        } finally {
            setLoading(false);
        }
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
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8" data-testid="visiteur-dashboard">
                {/* Header */}
                <div className="mb-8">
                    <h1 className="text-3xl font-bold text-slate-900 mb-2">
                        Bienvenue, {user?.prenom} !
                    </h1>
                    <p className="text-slate-600">
                        Vous avez un compte gratuit. Découvrez un aperçu du contenu PSE et accédez librement au PSC.
                    </p>
                </div>

                {/* Upgrade Banner */}
                <Card className="mb-8 bg-gradient-to-r from-red-50 to-red-100 border-red-200">
                    <CardContent className="p-6">
                        <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
                            <div>
                                <h3 className="font-semibold text-red-900 mb-1">Accès complet à la formation</h3>
                                <p className="text-sm text-red-700">
                                    Pour accéder aux quiz et à l'ensemble du contenu PSE, demandez un code groupe à votre formateur.
                                </p>
                            </div>
                            <Link to="/register">
                                <Button className="bg-red-600 hover:bg-red-700">
                                    J'ai un code groupe
                                    <ArrowRight className="w-4 h-4 ml-2" />
                                </Button>
                            </Link>
                        </div>
                    </CardContent>
                </Card>

                <div className="grid md:grid-cols-2 gap-8">
                    {/* PSC - Free Access */}
                    <div>
                        <Card data-testid="psc-section">
                            <CardHeader>
                                <CardTitle className="flex items-center gap-2">
                                    <Heart className="w-5 h-5 text-green-600" />
                                    PSC - Premiers Secours Citoyen
                                    <span className="ml-auto px-2 py-0.5 bg-green-100 text-green-700 text-xs rounded font-medium">
                                        Accès illimité
                                    </span>
                                </CardTitle>
                            </CardHeader>
                            <CardContent>
                                {pscChapters.length === 0 ? (
                                    <div className="empty-state py-6">
                                        <Heart className="w-10 h-10 mx-auto text-slate-300 mb-2" />
                                        <p className="text-sm text-slate-500">Contenu à venir</p>
                                        <p className="text-xs text-slate-400 mt-1">
                                            Cette section sera bientôt disponible
                                        </p>
                                    </div>
                                ) : (
                                    <div className="space-y-3">
                                        {pscChapters.map((chapter) => (
                                            <div 
                                                key={chapter.id}
                                                className="p-4 bg-green-50 rounded-lg border border-green-200"
                                            >
                                                <h4 className="font-medium text-slate-900">{chapter.titre}</h4>
                                                <p className="text-sm text-slate-600 mt-1">{chapter.description}</p>
                                            </div>
                                        ))}
                                    </div>
                                )}
                                <Link to="/psc" className="block mt-4">
                                    <Button variant="outline" className="w-full">
                                        Accéder au PSC
                                        <ArrowRight className="w-4 h-4 ml-2" />
                                    </Button>
                                </Link>
                            </CardContent>
                        </Card>
                    </div>

                    {/* PSE - Preview Only */}
                    <div>
                        <Card data-testid="pse-preview-section">
                            <CardHeader>
                                <CardTitle className="flex items-center gap-2">
                                    <BookOpen className="w-5 h-5 text-red-600" />
                                    PSE - Aperçu
                                    <span className="ml-auto px-2 py-0.5 bg-yellow-100 text-yellow-700 text-xs rounded font-medium flex items-center gap-1">
                                        <Lock className="w-3 h-3" />
                                        Limité
                                    </span>
                                </CardTitle>
                            </CardHeader>
                            <CardContent>
                                <div className="space-y-3">
                                    {previewChapters.map((chapter) => (
                                        <div 
                                            key={chapter.id}
                                            className="p-4 bg-slate-50 rounded-lg border border-slate-200"
                                        >
                                            <div className="flex items-center gap-2 mb-1">
                                                <span className="text-xs font-medium text-slate-500">
                                                    Chapitre {chapter.numero}
                                                </span>
                                                {chapter.is_preview && (
                                                    <span className="px-1.5 py-0.5 bg-yellow-100 text-yellow-700 text-xs rounded">
                                                        Aperçu
                                                    </span>
                                                )}
                                            </div>
                                            <h4 className="font-medium text-slate-900">{chapter.titre}</h4>
                                            <p className="text-sm text-slate-600 mt-1 line-clamp-2">{chapter.description}</p>
                                        </div>
                                    ))}
                                </div>
                                <Link to="/decouvrir" className="block mt-4">
                                    <Button variant="outline" className="w-full">
                                        Voir l'aperçu complet
                                        <ArrowRight className="w-4 h-4 ml-2" />
                                    </Button>
                                </Link>
                            </CardContent>
                        </Card>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default VisiteurDashboard;
