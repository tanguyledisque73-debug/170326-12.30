import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { 
    HelpCircle,
    Shield,
    Users,
    GraduationCap,
    ChevronDown,
    ChevronRight,
    BookOpen,
    Key,
    CheckCircle,
    Settings,
    FolderPlus,
    Copy,
    ArrowRight,
    Play,
    Award,
    Mail
} from 'lucide-react';
import { Button } from '../components/ui/button';
import Layout from '../components/Layout';
import { getUser } from '../lib/api';

const HelpPage = () => {
    const user = getUser();
    const [openSections, setOpenSections] = useState({
        admin: false,
        formateur: true,
        stagiaire: true,
        general: false
    });

    const toggleSection = (section) => {
        setOpenSections(prev => ({ ...prev, [section]: !prev[section] }));
    };

    const Section = ({ id, title, icon: Icon, color, children }) => (
        <div className="border rounded-xl overflow-hidden mb-4">
            <button
                onClick={() => toggleSection(id)}
                className={`w-full flex items-center justify-between p-4 bg-${color}-50 hover:bg-${color}-100 transition-colors`}
            >
                <div className="flex items-center gap-3">
                    <div className={`w-10 h-10 bg-${color}-100 rounded-lg flex items-center justify-center`}>
                        <Icon className={`w-5 h-5 text-${color}-600`} />
                    </div>
                    <span className="font-semibold text-slate-900">{title}</span>
                </div>
                {openSections[id] ? (
                    <ChevronDown className="w-5 h-5 text-slate-400" />
                ) : (
                    <ChevronRight className="w-5 h-5 text-slate-400" />
                )}
            </button>
            {openSections[id] && (
                <div className="p-6 bg-white">
                    {children}
                </div>
            )}
        </div>
    );

    const Step = ({ number, title, children }) => (
        <div className="flex gap-4 mb-4">
            <div className="flex-shrink-0 w-8 h-8 bg-red-100 rounded-full flex items-center justify-center">
                <span className="text-sm font-bold text-red-600">{number}</span>
            </div>
            <div className="flex-1">
                <h4 className="font-medium text-slate-900 mb-1">{title}</h4>
                <p className="text-sm text-slate-600">{children}</p>
            </div>
        </div>
    );

    return (
        <Layout>
            <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8" data-testid="help-page">
                {/* Header */}
                <div className="text-center mb-10">
                    <div className="w-16 h-16 bg-red-100 rounded-2xl flex items-center justify-center mx-auto mb-4">
                        <HelpCircle className="w-8 h-8 text-red-600" />
                    </div>
                    <h1 className="text-3xl font-bold text-slate-900 mb-2">
                        Centre d'aide
                    </h1>
                    <p className="text-slate-600 max-w-2xl mx-auto">
                        Bienvenue sur Secours 73 ! Retrouvez ici toutes les informations pour utiliser la plateforme.
                    </p>
                </div>

                {/* Quick Start based on role */}
                {!user && (
                    <div className="bg-gradient-to-r from-red-50 to-orange-50 border border-red-100 rounded-xl p-6 mb-8">
                        <h2 className="font-semibold text-slate-900 mb-3">🚀 Démarrage rapide</h2>
                        <div className="grid md:grid-cols-2 gap-4">
                            <Link to="/register">
                                <div className="bg-white p-4 rounded-lg border border-red-200 hover:border-red-400 transition-colors">
                                    <div className="flex items-center gap-2 mb-2">
                                        <Key className="w-5 h-5 text-red-600" />
                                        <span className="font-medium">J'ai un code groupe</span>
                                    </div>
                                    <p className="text-sm text-slate-600">Inscrivez-vous avec le code fourni par votre formateur</p>
                                </div>
                            </Link>
                            <Link to="/login">
                                <div className="bg-white p-4 rounded-lg border border-slate-200 hover:border-slate-400 transition-colors">
                                    <div className="flex items-center gap-2 mb-2">
                                        <Users className="w-5 h-5 text-slate-600" />
                                        <span className="font-medium">J'ai déjà un compte</span>
                                    </div>
                                    <p className="text-sm text-slate-600">Connectez-vous pour accéder à votre formation</p>
                                </div>
                            </Link>
                        </div>
                    </div>
                )}

                {/* Guide Stagiaire */}
                <Section id="stagiaire" title="Guide Stagiaire" icon={GraduationCap} color="green">
                    <div className="space-y-6">
                        <div>
                            <h3 className="font-semibold text-slate-900 mb-4 flex items-center gap-2">
                                <Play className="w-5 h-5 text-green-600" />
                                Comment s'inscrire ?
                            </h3>
                            <Step number="1" title="Obtenir votre code groupe">
                                Votre formateur vous fournit un code à 8 caractères (ex: ABC12XYZ).
                            </Step>
                            <Step number="2" title="S'inscrire sur la plateforme">
                                Cliquez sur "J'ai un code groupe", entrez vos informations et le code reçu.
                            </Step>
                            <Step number="3" title="Accéder à votre formation">
                                Connectez-vous et commencez votre parcours de formation !
                            </Step>
                        </div>

                        <hr className="my-6" />

                        <div>
                            <h3 className="font-semibold text-slate-900 mb-4 flex items-center gap-2">
                                <BookOpen className="w-5 h-5 text-green-600" />
                                Comment progresser ?
                            </h3>
                            <div className="bg-green-50 border border-green-200 rounded-lg p-4 mb-4">
                                <p className="text-sm text-green-800">
                                    <strong>Progression conditionnelle :</strong> Vous devez obtenir le score minimum fixé par votre formateur (généralement 80%) pour débloquer le chapitre suivant.
                                </p>
                            </div>
                            <Step number="1" title="Lire le chapitre">
                                Consultez les fiches de révision du chapitre en cours.
                            </Step>
                            <Step number="2" title="Passer le quiz">
                                Testez vos connaissances avec le quiz du chapitre.
                            </Step>
                            <Step number="3" title="Valider et continuer">
                                Si votre score est suffisant, le chapitre suivant se débloque automatiquement.
                            </Step>
                        </div>
                    </div>
                </Section>

                {/* Guide Formateur */}
                <Section id="formateur" title="Guide Formateur" icon={Users} color="blue">
                    <div className="space-y-6">
                        <div>
                            <h3 className="font-semibold text-slate-900 mb-4 flex items-center gap-2">
                                <FolderPlus className="w-5 h-5 text-blue-600" />
                                Créer un groupe de formation
                            </h3>
                            <Step number="1" title="Accéder à 'Mes groupes'">
                                Depuis votre tableau de bord, cliquez sur "Mes groupes".
                            </Step>
                            <Step number="2" title="Créer un nouveau groupe">
                                Cliquez sur "Nouveau groupe" et remplissez le formulaire :
                                <ul className="list-disc list-inside mt-2 ml-4 text-slate-600">
                                    <li>Nom du groupe (ex: "PSE1 - Janvier 2026")</li>
                                    <li>Type de formation (PSE ou BNSSA)</li>
                                    <li>Seuil de réussite (minimum 80%)</li>
                                    <li>Sélectionnez et ordonnez les chapitres</li>
                                </ul>
                            </Step>
                            <Step number="3" title="Partager le code d'accès">
                                Un code unique à 8 caractères est généré. Partagez-le à vos stagiaires pour qu'ils s'inscrivent.
                            </Step>
                        </div>

                        <hr className="my-6" />

                        <div>
                            <h3 className="font-semibold text-slate-900 mb-4 flex items-center gap-2">
                                <Award className="w-5 h-5 text-blue-600" />
                                Suivre la progression
                            </h3>
                            <p className="text-slate-600 mb-4">
                                Depuis la page détail d'un groupe, vous pouvez :
                            </p>
                            <ul className="space-y-2">
                                <li className="flex items-start gap-2">
                                    <CheckCircle className="w-5 h-5 text-green-500 flex-shrink-0 mt-0.5" />
                                    <span>Voir la liste de vos stagiaires inscrits</span>
                                </li>
                                <li className="flex items-start gap-2">
                                    <CheckCircle className="w-5 h-5 text-green-500 flex-shrink-0 mt-0.5" />
                                    <span>Consulter leur progression (chapitres validés, scores)</span>
                                </li>
                                <li className="flex items-start gap-2">
                                    <CheckCircle className="w-5 h-5 text-green-500 flex-shrink-0 mt-0.5" />
                                    <span>Identifier les stagiaires en difficulté</span>
                                </li>
                            </ul>
                        </div>

                        <div className="bg-blue-50 border border-blue-200 rounded-lg p-4">
                            <p className="text-sm text-blue-800">
                                <strong>💡 Astuce :</strong> Vous pouvez personnaliser l'ordre des chapitres lors de la création du groupe pour adapter le parcours à votre pédagogie.
                            </p>
                        </div>
                    </div>
                </Section>

                {/* Guide Admin */}
                <Section id="admin" title="Guide Administrateur" icon={Shield} color="red">
                    <div className="space-y-6">
                        <div>
                            <h3 className="font-semibold text-slate-900 mb-4 flex items-center gap-2">
                                <Users className="w-5 h-5 text-red-600" />
                                Gérer les formateurs
                            </h3>
                            <Step number="1" title="Créer un compte formateur">
                                Depuis "Formateurs", cliquez sur "Ajouter un formateur" et entrez son email et nom.
                            </Step>
                            <Step number="2" title="Communiquer les identifiants">
                                Un mot de passe temporaire est généré. Transmettez-le au formateur qui devra le changer à sa première connexion.
                            </Step>
                        </div>

                        <hr className="my-6" />

                        <div>
                            <h3 className="font-semibold text-slate-900 mb-4 flex items-center gap-2">
                                <BookOpen className="w-5 h-5 text-red-600" />
                                Gérer les quiz
                            </h3>
                            <p className="text-slate-600 mb-4">
                                Depuis la section "Quiz", vous pouvez créer, modifier ou supprimer des quiz pour chaque chapitre.
                            </p>
                            <ul className="space-y-2">
                                <li className="flex items-start gap-2">
                                    <CheckCircle className="w-5 h-5 text-green-500 flex-shrink-0 mt-0.5" />
                                    <span>Ajouter des questions QCM ou Vrai/Faux</span>
                                </li>
                                <li className="flex items-start gap-2">
                                    <CheckCircle className="w-5 h-5 text-green-500 flex-shrink-0 mt-0.5" />
                                    <span>Rédiger des explications pour chaque réponse</span>
                                </li>
                                <li className="flex items-start gap-2">
                                    <CheckCircle className="w-5 h-5 text-green-500 flex-shrink-0 mt-0.5" />
                                    <span>Associer des vidéos aux quiz</span>
                                </li>
                            </ul>
                        </div>

                        <hr className="my-6" />

                        <div>
                            <h3 className="font-semibold text-slate-900 mb-4 flex items-center gap-2">
                                <Settings className="w-5 h-5 text-red-600" />
                                Paramètres du site
                            </h3>
                            <p className="text-slate-600 mb-4">
                                Depuis "Paramètres", vous pouvez :
                            </p>
                            <ul className="space-y-2">
                                <li className="flex items-start gap-2">
                                    <CheckCircle className="w-5 h-5 text-green-500 flex-shrink-0 mt-0.5" />
                                    <span>Configurer le lien HelloAsso pour les dons</span>
                                </li>
                                <li className="flex items-start gap-2">
                                    <CheckCircle className="w-5 h-5 text-green-500 flex-shrink-0 mt-0.5" />
                                    <span>Gérer les images de présentation du site</span>
                                </li>
                            </ul>
                        </div>
                    </div>
                </Section>

                {/* FAQ */}
                <Section id="general" title="Questions fréquentes" icon={HelpCircle} color="slate">
                    <div className="space-y-4">
                        <div className="border-b pb-4">
                            <h4 className="font-medium text-slate-900 mb-2">J'ai perdu mon mot de passe</h4>
                            <p className="text-sm text-slate-600">
                                Contactez votre formateur ou l'administrateur de la plateforme pour réinitialiser votre mot de passe.
                            </p>
                        </div>
                        <div className="border-b pb-4">
                            <h4 className="font-medium text-slate-900 mb-2">Mon code groupe ne fonctionne pas</h4>
                            <p className="text-sm text-slate-600">
                                Vérifiez que vous avez bien saisi les 8 caractères (attention aux majuscules). Si le problème persiste, contactez votre formateur.
                            </p>
                        </div>
                        <div className="border-b pb-4">
                            <h4 className="font-medium text-slate-900 mb-2">Je n'arrive pas à débloquer le chapitre suivant</h4>
                            <p className="text-sm text-slate-600">
                                Vous devez obtenir le score minimum au quiz du chapitre actuel. Révisez les fiches et réessayez le quiz.
                            </p>
                        </div>
                        <div>
                            <h4 className="font-medium text-slate-900 mb-2">Le groupe est complet (18 stagiaires)</h4>
                            <p className="text-sm text-slate-600">
                                Chaque groupe est limité à 18 stagiaires. Le formateur doit créer un nouveau groupe pour accueillir d'autres apprenants.
                            </p>
                        </div>
                    </div>
                </Section>

                {/* Contact */}
                <div className="bg-slate-50 rounded-xl p-6 text-center mt-8">
                    <Mail className="w-8 h-8 text-slate-400 mx-auto mb-3" />
                    <h3 className="font-semibold text-slate-900 mb-2">Besoin d'aide supplémentaire ?</h3>
                    <p className="text-sm text-slate-600 mb-4">
                        Contactez Secours Alpes 73 pour toute question.
                    </p>
                    <Button variant="outline" asChild>
                        <a href="https://secours73.fr" target="_blank" rel="noopener noreferrer">
                            Visiter secours73.fr
                        </a>
                    </Button>
                </div>
            </div>
        </Layout>
    );
};

export default HelpPage;
