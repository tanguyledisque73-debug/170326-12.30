import React from 'react';
import { Link } from 'react-router-dom';
import { 
    Waves, 
    BookOpen, 
    CheckCircle, 
    Users, 
    Lock,
    Award,
    AlertCircle
} from 'lucide-react';
import { Button } from '../../components/ui/button';
import Layout from '../../components/Layout';
import { getUser } from '../../lib/api';

const BNSSAInfo = () => {
    const user = getUser();

    const features = [
        {
            icon: BookOpen,
            title: 'Contenu spécialisé',
            description: 'Formation complète au sauvetage et secourisme en milieu aquatique.'
        },
        {
            icon: CheckCircle,
            title: 'Quiz interactifs',
            description: 'QCM et Vrai/Faux pour tester vos connaissances spécifiques au milieu aquatique.'
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
            <section className="bg-gradient-to-br from-blue-50 to-white py-16" data-testid="bnssa-hero">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="grid lg:grid-cols-2 gap-12 items-center">
                        <div>
                            <div className="flex items-center gap-2 mb-4">
                                <div className="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center">
                                    <Waves className="w-6 h-6 text-blue-600" />
                                </div>
                                <span className="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-sm font-medium">
                                    Formation BNSSA
                                </span>
                            </div>
                            
                            <h1 className="text-4xl md:text-5xl font-bold text-slate-900 mb-6">
                                BNSSA - Sauvetage Aquatique
                            </h1>
                            
                            <p className="text-lg text-slate-600 mb-8 leading-relaxed">
                                Plateforme de formation ouverte à distance pour le sauvetage aquatique. 
                                Progression guidée, quiz interactifs et suivi personnalisé par votre formateur.
                            </p>
                            
                            <div className="bg-amber-50 border border-amber-200 rounded-xl p-4 mb-8">
                                <div className="flex items-start gap-3">
                                    <AlertCircle className="w-5 h-5 text-amber-600 flex-shrink-0 mt-0.5" />
                                    <div>
                                        <p className="font-medium text-amber-800">Accès restreint</p>
                                        <p className="text-sm text-amber-700">
                                            Cette formation est accessible uniquement aux stagiaires autorisés par leur formateur.
                                        </p>
                                    </div>
                                </div>
                            </div>
                            
                            <div className="flex flex-wrap gap-4">
                                <Link to="/login">
                                    <Button size="lg" className="bg-blue-600 hover:bg-blue-700">
                                        <Lock className="w-4 h-4 mr-2" />
                                        Se connecter
                                    </Button>
                                </Link>
                            </div>
                        </div>
                        
                        <div className="hidden lg:block">
                            <img 
                                src="https://images.unsplash.com/photo-1530549387789-4c1017266635?w=600&q=80"
                                alt="Sauvetage aquatique"
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
                                <div className="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-4">
                                    <feature.icon className="w-6 h-6 text-blue-600" />
                                </div>
                                <h3 className="font-semibold text-slate-900 mb-2">{feature.title}</h3>
                                <p className="text-sm text-slate-600">{feature.description}</p>
                            </div>
                        ))}
                    </div>
                </div>
            </section>

            {/* Info */}
            <section className="py-16 bg-slate-50">
                <div className="max-w-4xl mx-auto px-4 text-center">
                    <h2 className="text-2xl font-bold text-slate-900 mb-4">
                        Comment accéder à la formation BNSSA ?
                    </h2>
                    <p className="text-slate-600 mb-8">
                        Pour accéder à cette formation, vous devez être inscrit dans un groupe BNSSA créé par votre formateur.
                        Contactez votre formateur pour obtenir un code d'accès.
                    </p>
                    <div className="flex flex-wrap justify-center gap-4">
                        <Link to="/register">
                            <Button size="lg" className="bg-blue-600 hover:bg-blue-700">
                                S'inscrire avec un code
                            </Button>
                        </Link>
                        <Link to="/login">
                            <Button size="lg" variant="outline">
                                J'ai déjà un compte
                            </Button>
                        </Link>
                    </div>
                </div>
            </section>
        </Layout>
    );
};

export default BNSSAInfo;
