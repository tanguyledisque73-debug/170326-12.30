import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { Heart, BookOpen, ArrowRight, Construction, AlertCircle } from 'lucide-react';
import { Button } from '../../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/card';
import Layout from '../../components/Layout';
import { getPSCChapters } from '../../lib/api';

const PSCChapters = () => {
    const [chapters, setChapters] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        loadData();
    }, []);

    const loadData = async () => {
        try {
            const data = await getPSCChapters();
            setChapters(data);
        } catch (error) {
            console.error('Erreur:', error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <Layout>
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8" data-testid="psc-chapters">
                {/* Header */}
                <div className="text-center mb-8">
                    <div className="w-16 h-16 bg-green-100 rounded-2xl flex items-center justify-center mx-auto mb-4">
                        <Heart className="w-8 h-8 text-green-600" />
                    </div>
                    <h1 className="text-3xl md:text-4xl font-bold text-slate-900 mb-2">
                        PSC - Premiers Secours Citoyen
                    </h1>
                    <p className="text-lg text-slate-600 max-w-2xl mx-auto mb-6">
                        Plateforme de révision des gestes qui sauvent.
                    </p>
                    
                    {/* Disclaimer important */}
                    <div className="max-w-2xl mx-auto bg-amber-50 border border-amber-200 rounded-xl p-4">
                        <div className="flex items-start gap-3 text-left">
                            <AlertCircle className="w-5 h-5 text-amber-600 flex-shrink-0 mt-0.5" />
                            <div>
                                <p className="font-medium text-amber-800">Important</p>
                                <p className="text-sm text-amber-700">
                                    Cette plateforme est un outil de révision. Elle ne remplace en aucun cas une formation 
                                    en centre de formation agréé. Aucun compte ni suivi formateur n'est nécessaire.
                                </p>
                            </div>
                        </div>
                    </div>
                </div>

                {/* Content */}
                {loading ? (
                    <div className="flex justify-center py-12">
                        <div className="spinner"></div>
                    </div>
                ) : chapters.length === 0 ? (
                    <Card className="max-w-2xl mx-auto">
                        <CardContent className="py-12">
                            <div className="text-center">
                                <Construction className="w-16 h-16 mx-auto text-yellow-500 mb-4" />
                                <h2 className="text-xl font-semibold text-slate-900 mb-2">
                                    Contenu en préparation
                                </h2>
                                <p className="text-slate-600 mb-6">
                                    Cette section sera bientôt disponible avec du contenu gratuit sur les gestes de premiers secours citoyens.
                                </p>
                                <Link to="/">
                                    <Button variant="outline">
                                        Retour à l'accueil
                                    </Button>
                                </Link>
                            </div>
                        </CardContent>
                    </Card>
                ) : (
                    <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
                        {chapters.map((chapter) => (
                            <Card key={chapter.id} className="card-hover">
                                <CardContent className="p-6">
                                    {chapter.image_url && (
                                        <div className="w-full h-40 rounded-lg overflow-hidden mb-4">
                                            <img 
                                                src={chapter.image_url} 
                                                alt={chapter.titre}
                                                className="w-full h-full object-cover"
                                            />
                                        </div>
                                    )}
                                    <div className="flex items-center gap-2 mb-3">
                                        <div className="w-10 h-10 bg-green-100 rounded-lg flex items-center justify-center">
                                            <BookOpen className="w-5 h-5 text-green-600" />
                                        </div>
                                        <span className="text-sm font-medium text-green-600">Chapitre {chapter.numero}</span>
                                    </div>
                                    <h3 className="font-semibold text-slate-900 mb-2">{chapter.titre}</h3>
                                    <p className="text-sm text-slate-600 mb-4 line-clamp-2">{chapter.description}</p>
                                    <p className="text-xs text-slate-500 mb-4">
                                        {chapter.fiches?.length || 0} fiches de révision
                                    </p>
                                    <Link to={`/psc/chapitre/${chapter.id}`} className="block">
                                        <Button variant="outline" className="w-full hover:bg-green-50 hover:text-green-700 hover:border-green-200">
                                            Consulter
                                            <ArrowRight className="w-4 h-4 ml-2" />
                                        </Button>
                                    </Link>
                                </CardContent>
                            </Card>
                        ))}
                    </div>
                )}
            </div>
        </Layout>
    );
};

export default PSCChapters;
