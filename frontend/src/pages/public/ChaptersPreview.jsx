import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { BookOpen, Lock, ArrowRight, Shield } from 'lucide-react';
import { Button } from '../../components/ui/button';
import { Card, CardContent } from '../../components/ui/card';
import Layout from '../../components/Layout';
import { getChaptersPreview } from '../../lib/api';

const ChaptersPreview = () => {
    const [chapters, setChapters] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        loadData();
    }, []);

    const loadData = async () => {
        try {
            const data = await getChaptersPreview();
            setChapters(data);
        } catch (error) {
            console.error('Erreur:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <Layout>
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8" data-testid="chapters-preview">
                {/* Header */}
                <div className="text-center mb-12">
                    <div className="w-16 h-16 bg-red-100 rounded-2xl flex items-center justify-center mx-auto mb-4">
                        <Shield className="w-8 h-8 text-red-600" />
                    </div>
                    <h1 className="text-3xl md:text-4xl font-bold text-slate-900 mb-2">
                        Aperçu PSE
                    </h1>
                    <p className="text-lg text-slate-600 max-w-2xl mx-auto">
                        Découvrez un extrait du contenu de la formation Premiers Secours en Équipe.
                    </p>
                </div>

                {/* Info Banner */}
                <Card className="mb-8 bg-yellow-50 border-yellow-200">
                    <CardContent className="p-4">
                        <div className="flex items-center gap-3">
                            <Lock className="w-5 h-5 text-yellow-600" />
                            <div className="flex-1">
                                <p className="text-sm text-yellow-800">
                                    <strong>Accès limité</strong> - Vous consultez un aperçu. Pour accéder à l'ensemble du contenu et aux quiz, inscrivez-vous avec un code groupe.
                                </p>
                            </div>
                            <Link to="/register">
                                <Button size="sm" className="bg-yellow-600 hover:bg-yellow-700">
                                    S'inscrire
                                </Button>
                            </Link>
                        </div>
                    </CardContent>
                </Card>

                {/* Content */}
                {loading ? (
                    <div className="flex justify-center py-12">
                        <div className="spinner"></div>
                    </div>
                ) : (
                    <div className="space-y-6">
                        {chapters.map((chapter) => (
                            <Card key={chapter.id} className="overflow-hidden">
                                <CardContent className="p-6">
                                    <div className="flex items-start gap-4">
                                        <div className="w-12 h-12 bg-red-100 rounded-xl flex items-center justify-center flex-shrink-0">
                                            <span className="text-lg font-bold text-red-600">{chapter.numero}</span>
                                        </div>
                                        <div className="flex-1">
                                            <div className="flex items-center gap-2 mb-2">
                                                <h3 className="font-semibold text-lg text-slate-900">{chapter.titre}</h3>
                                                <span className="px-2 py-0.5 bg-yellow-100 text-yellow-700 text-xs rounded font-medium">
                                                    Aperçu
                                                </span>
                                            </div>
                                            <p className="text-slate-600 mb-4">{chapter.description}</p>
                                            
                                            {chapter.fiches && chapter.fiches.length > 0 && (
                                                <div className="bg-slate-50 rounded-lg p-4">
                                                    <h4 className="font-medium text-slate-900 mb-2">
                                                        {chapter.fiches[0].titre}
                                                    </h4>
                                                    <p className="text-sm text-slate-600 line-clamp-4">
                                                        {chapter.fiches[0].contenu.substring(0, 300)}...
                                                    </p>
                                                    <div className="mt-3 pt-3 border-t border-slate-200 flex items-center justify-between">
                                                        <span className="text-xs text-slate-500">
                                                            Contenu complet réservé aux stagiaires
                                                        </span>
                                                        <Lock className="w-4 h-4 text-slate-400" />
                                                    </div>
                                                </div>
                                            )}
                                        </div>
                                    </div>
                                </CardContent>
                            </Card>
                        ))}
                        
                        {/* More chapters indicator */}
                        <Card className="bg-slate-50 border-dashed">
                            <CardContent className="py-8 text-center">
                                <Lock className="w-8 h-8 mx-auto text-slate-400 mb-3" />
                                <p className="font-medium text-slate-700 mb-1">Et 9 autres chapitres...</p>
                                <p className="text-sm text-slate-500 mb-4">
                                    Inscrivez-vous pour accéder à la formation complète avec quiz interactifs
                                </p>
                                <Link to="/register">
                                    <Button className="bg-red-600 hover:bg-red-700">
                                        S'inscrire avec un code
                                        <ArrowRight className="w-4 h-4 ml-2" />
                                    </Button>
                                </Link>
                            </CardContent>
                        </Card>
                    </div>
                )}
            </div>
        </Layout>
    );
};

export default ChaptersPreview;
