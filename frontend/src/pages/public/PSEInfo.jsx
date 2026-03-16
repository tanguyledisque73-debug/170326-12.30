import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { 
    Shield, 
    BookOpen, 
    CheckCircle, 
    Users, 
    ArrowRight,
    Lock,
    Unlock,
    Award
} from 'lucide-react';
import { Button } from '../../components/ui/button';
import Layout from '../../components/Layout';
import { getChaptersPreview, getUser } from '../../lib/api';

const PSEInfo = () => {
    const [chapters, setChapters] = useState([]);
    const [loading, setLoading] = useState(true);
    const user = getUser();

    useEffect(() => {
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
        loadData();
    }, []);

    const features = [
        {
            icon: BookOpen,
            title: '11 Chapitres complets',
            description: 'Formation complète aux Premiers Secours en Équipe basée sur les recommandations officielles PSE1 & PSE2.'
        },
        {
            icon: CheckCircle,
            title: 'Quiz interactifs',
            description: 'QCM et Vrai/Faux pour tester vos connaissances avec correction détaillée.'
        },
        {
            icon: Users,
            title: 'Suivi formateur',
            description: 'Progression guidée par votre formateur avec déblocage conditionnel des chapitres.'
        },
        {
            icon: Award,
            title: 'Seuil de validation',
            description: 'Score minimum de 80% requis pour valider chaque chapitre et débloquer le suivant.'
        }
    ];

    return (
        <Layout>
            {/* Hero */}
            <section className="bg-gradient-to-br from-red-50 to-white py-16" data-testid="pse-hero">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="grid lg:grid-cols-2 gap-12 items-center">
                        <div>
                            <div className="flex items-center gap-2 mb-4">
                                <div className="w-12 h-12 bg-red-100 rounded-xl flex items-center justify-center">
                                    <Shield className="w-6 h-6 text-red-600" />
                                </div>
                                <span className="px-3 py-1 bg-red-100 text-red-700 rounded-full text-sm font-medium">
                                    Formation PSE
                                </span>
                            </div>
                            
                            <h1 className="text-4xl md:text-5xl font-bold text-slate-900 mb-6">
                                PSE - Premiers Secours en Équipe
                            </h1>
                            
                            <p className="text-lg text-slate-600 mb-8 leading-relaxed">
                                Plateforme de formation ouverte à distance pour les premiers secours. 
                                Progression guidée, quiz interactifs et suivi personnalisé par votre formateur.
                            </p>
                            
                            <div className="flex flex-wrap gap-4">
                                <Link to="/register">
                                    <Button size="lg" className="bg-red-600 hover:bg-red-700">
                                        <Lock className="w-4 h-4 mr-2" />
                                        J'ai un code groupe
                                    </Button>
                                </Link>
                                <Link to="/decouvrir">
                                    <Button size="lg" variant="outline">
                                        <Unlock className="w-4 h-4 mr-2" />
                                        Accès gratuit limité
                                    </Button>
                                </Link>
                            </div>
                        </div>
                        
                        <div className="hidden lg:block">
                            <img 
                                src="https://images.unsplash.com/photo-1564144573017-8dc932e0039e?w=600&q=80"
                                alt="Premiers secours"
                                className="rounded-2xl shadow-xl"
                            />
                        </div>
                    </div>
                </div>
            </section>

            {/* Features */}
            <section className="py-16 bg-white">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <h2 className="text-2xl font-bold text-slate-900 mb-8 text-center">
                        Ce que propose la formation
                    </h2>
                    <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
                        {features.map((feature, index) => (
                            <div key={index} className="bg-slate-50 rounded-xl p-6 border border-slate-200">
                                <div className="w-12 h-12 bg-red-100 rounded-lg flex items-center justify-center mb-4">
                                    <feature.icon className="w-6 h-6 text-red-600" />
                                </div>
                                <h3 className="font-semibold text-slate-900 mb-2">{feature.title}</h3>
                                <p className="text-sm text-slate-600">{feature.description}</p>
                            </div>
                        ))}
                    </div>
                </div>
            </section>

            {/* Aperçu chapitres */}
            <section className="py-16 bg-slate-50">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex items-center justify-between mb-8">
                        <h2 className="text-2xl font-bold text-slate-900">
                            Aperçu du contenu
                        </h2>
                        <Link to="/decouvrir">
                            <Button variant="outline" size="sm">
                                Voir plus
                                <ArrowRight className="w-4 h-4 ml-2" />
                            </Button>
                        </Link>
                    </div>
                    
                    {loading ? (
                        <div className="flex justify-center py-8">
                            <div className="spinner"></div>
                        </div>
                    ) : (
                        <div className="grid md:grid-cols-3 gap-6">
                            {chapters.map((chapter) => (
                                <Link 
                                    key={chapter.id} 
                                    to="/decouvrir"
                                    className="group"
                                >
                                    <div className="bg-white border border-slate-200 rounded-xl p-6 h-full transition-all hover:shadow-lg hover:border-red-200">
                                        <div className="flex items-center gap-2 mb-3">
                                            <span className="px-2 py-0.5 bg-red-100 text-red-700 text-xs font-medium rounded">
                                                Chapitre {chapter.numero}
                                            </span>
                                            <span className="px-2 py-0.5 bg-yellow-100 text-yellow-700 text-xs font-medium rounded">
                                                Aperçu gratuit
                                            </span>
                                        </div>
                                        <h3 className="font-semibold text-slate-900 mb-2 group-hover:text-red-600">
                                            {chapter.titre}
                                        </h3>
                                        <p className="text-sm text-slate-600 line-clamp-2">
                                            {chapter.description}
                                        </p>
                                    </div>
                                </Link>
                            ))}
                        </div>
                    )}
                </div>
            </section>

            {/* CTA */}
            <section className="py-16 bg-red-600">
                <div className="max-w-4xl mx-auto px-4 text-center">
                    <h2 className="text-2xl md:text-3xl font-bold text-white mb-4">
                        Prêt à commencer votre formation PSE ?
                    </h2>
                    <p className="text-red-100 mb-8">
                        Contactez votre formateur pour obtenir un code d'accès à votre groupe de formation.
                    </p>
                    <div className="flex flex-wrap justify-center gap-4">
                        <Link to="/register">
                            <Button size="lg" variant="secondary">
                                S'inscrire avec un code
                            </Button>
                        </Link>
                        <Link to="/login">
                            <Button size="lg" variant="outline" className="border-white text-white hover:bg-red-700">
                                J'ai déjà un compte
                            </Button>
                        </Link>
                    </div>
                </div>
            </section>
        </Layout>
    );
};

export default PSEInfo;
