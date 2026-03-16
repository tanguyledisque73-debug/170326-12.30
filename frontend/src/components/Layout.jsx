import React, { useState } from 'react';
import { Link, useLocation, useNavigate } from 'react-router-dom';
import { 
    Heart, 
    Menu, 
    X, 
    LogOut, 
    User, 
    BookOpen, 
    LayoutDashboard,
    Users,
    Settings,
    FolderOpen,
    Waves,
    Shield,
    HelpCircle,
    Mail,
    FileText,
    Send
} from 'lucide-react';
import { Button } from './ui/button';
import { getUser, clearAuth } from '../lib/api';

export const Navbar = () => {
    const [mobileMenuOpen, setMobileMenuOpen] = useState(false);
    const location = useLocation();
    const navigate = useNavigate();
    const user = getUser();

    const handleLogout = () => {
        clearAuth();
        navigate('/');
        setMobileMenuOpen(false);
    };

    const isActive = (path) => location.pathname.startsWith(path);

    const getNavLinks = () => {
        if (!user) return [];
        
        switch (user.role) {
            case 'admin':
                return [
                    { path: '/admin', label: 'Tableau de bord', icon: LayoutDashboard },
                    { path: '/admin/formateurs', label: 'Formateurs', icon: Users },
                    { path: '/admin/quizzes', label: 'Quiz', icon: BookOpen },
                    { path: '/messages', label: 'Messagerie', icon: Mail },
                    { path: '/admin/settings', label: 'Paramètres', icon: Settings },
                ];
            case 'formateur':
                return [
                    { path: '/formateur', label: 'Tableau de bord', icon: LayoutDashboard },
                    { path: '/formateur/groupes', label: 'Mes groupes', icon: FolderOpen },
                    { path: '/formateur/documents', label: 'Documents', icon: FileText },
                    { path: '/formateur/send-email', label: 'Envoyer email', icon: Send },
                    { path: '/messages', label: 'Messagerie', icon: Mail },
                ];
            case 'stagiaire':
                return [
                    { path: '/stagiaire', label: 'Tableau de bord', icon: LayoutDashboard },
                    { path: '/stagiaire/chapitres', label: 'Chapitres', icon: BookOpen },
                    { path: '/stagiaire/documents', label: 'Mes documents', icon: FileText },
                    { path: '/messages', label: 'Messagerie', icon: Mail },
                ];
            case 'visiteur':
                return [
                    { path: '/visiteur', label: 'Mon espace', icon: LayoutDashboard },
                    { path: '/psc', label: 'PSC', icon: Heart },
                    { path: '/decouvrir', label: 'Aperçu PSE', icon: Shield },
                    { path: '/messages', label: 'Messagerie', icon: Mail },
                ];
            default:
                return [];
        }
    };

    const navLinks = getNavLinks();

    const getRoleBadge = () => {
        if (!user) return null;
        const badges = {
            admin: { bg: 'bg-purple-100', text: 'text-purple-700', label: 'Admin' },
            formateur: { bg: 'bg-blue-100', text: 'text-blue-700', label: 'Formateur' },
            stagiaire: { bg: 'bg-green-100', text: 'text-green-700', label: 'Stagiaire' },
            visiteur: { bg: 'bg-slate-100', text: 'text-slate-700', label: 'Visiteur' }
        };
        const badge = badges[user.role] || badges.visiteur;
        return (
            <span className={`ml-2 px-2 py-0.5 rounded-full text-xs font-medium ${badge.bg} ${badge.text}`}>
                {badge.label}
            </span>
        );
    };

    return (
        <nav className="sticky top-0 z-40 glass border-b border-slate-200/50" data-testid="navbar">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="flex items-center justify-between h-16">
                    {/* Logo */}
                    <Link 
                        to={user ? (
                            user.role === 'admin' ? '/admin' :
                            user.role === 'formateur' ? '/formateur' :
                            user.role === 'stagiaire' ? '/stagiaire' :
                            user.role === 'visiteur' ? '/visiteur' : '/'
                        ) : '/'} 
                        className="flex items-center gap-2 group"
                        data-testid="logo-link"
                    >
                        <img 
                            src="/images/logo-secours73.png" 
                            alt="Secours Alpes 73" 
                            className="h-12 w-auto"
                        />
                    </Link>

                    {/* Desktop Navigation */}
                    <div className="hidden md:flex items-center gap-6">
                        {navLinks.map(({ path, label, icon: Icon }) => (
                            <Link
                                key={path}
                                to={path}
                                className={`flex items-center gap-2 text-sm font-medium transition-colors ${
                                    isActive(path) 
                                        ? 'text-red-600' 
                                        : 'text-slate-600 hover:text-slate-900'
                                }`}
                                data-testid={`nav-${path.replace(/\//g, '-')}`}
                            >
                                <Icon className="w-4 h-4" />
                                {label}
                            </Link>
                        ))}
                    </div>

                    {/* User Menu */}
                    <div className="flex items-center gap-4">
                        {user ? (
                            <>
                                <div className="hidden md:flex items-center gap-2 text-sm text-slate-600">
                                    <User className="w-4 h-4" />
                                    <span>{user.prenom} {user.nom}</span>
                                    {getRoleBadge()}
                                </div>
                                <Link to="/aide" className="hidden md:flex">
                                    <Button variant="ghost" size="sm" className="text-slate-600">
                                        <HelpCircle className="w-4 h-4" />
                                    </Button>
                                </Link>
                                <Button 
                                    variant="ghost" 
                                    size="sm" 
                                    onClick={handleLogout}
                                    className="hidden md:flex items-center gap-2"
                                    data-testid="logout-btn"
                                >
                                    <LogOut className="w-4 h-4" />
                                    Déconnexion
                                </Button>
                            </>
                        ) : (
                            <div className="hidden md:flex items-center gap-3">
                                <Link to="/aide">
                                    <Button variant="ghost" size="sm" className="text-slate-600">
                                        <HelpCircle className="w-4 h-4 mr-1" />
                                        Aide
                                    </Button>
                                </Link>
                                <Link to="/login">
                                    <Button variant="ghost" size="sm" data-testid="login-btn">
                                        Connexion
                                    </Button>
                                </Link>
                                <Link to="/register">
                                    <Button size="sm" className="bg-red-600 hover:bg-red-700" data-testid="register-btn">
                                        S'inscrire
                                    </Button>
                                </Link>
                            </div>
                        )}

                        {/* Mobile menu button */}
                        <button
                            className="md:hidden p-2 rounded-lg hover:bg-slate-100"
                            onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
                            data-testid="mobile-menu-btn"
                        >
                            {mobileMenuOpen ? (
                                <X className="w-6 h-6 text-slate-600" />
                            ) : (
                                <Menu className="w-6 h-6 text-slate-600" />
                            )}
                        </button>
                    </div>
                </div>
            </div>

            {/* Mobile Menu */}
            {mobileMenuOpen && (
                <div className="md:hidden bg-white border-t border-slate-200 animate-fade-in" data-testid="mobile-menu">
                    <div className="px-4 py-4 space-y-2">
                        {user && (
                            <div className="flex items-center gap-2 px-3 py-2 text-sm text-slate-600 border-b border-slate-100 mb-2 pb-4">
                                <User className="w-4 h-4" />
                                <span>{user.prenom} {user.nom}</span>
                                {getRoleBadge()}
                            </div>
                        )}
                        
                        {navLinks.map(({ path, label, icon: Icon }) => (
                            <Link
                                key={path}
                                to={path}
                                onClick={() => setMobileMenuOpen(false)}
                                className={`flex items-center gap-3 px-3 py-2 rounded-lg text-sm font-medium transition-colors ${
                                    isActive(path) 
                                        ? 'bg-red-50 text-red-600' 
                                        : 'text-slate-600 hover:bg-slate-50'
                                }`}
                            >
                                <Icon className="w-5 h-5" />
                                {label}
                            </Link>
                        ))}
                        
                        {user ? (
                            <button
                                onClick={handleLogout}
                                className="w-full flex items-center gap-3 px-3 py-2 rounded-lg text-sm font-medium text-slate-600 hover:bg-slate-50"
                            >
                                <LogOut className="w-5 h-5" />
                                Déconnexion
                            </button>
                        ) : (
                            <div className="space-y-2 pt-2 border-t border-slate-100">
                                <Link 
                                    to="/login" 
                                    onClick={() => setMobileMenuOpen(false)}
                                    className="block"
                                >
                                    <Button variant="outline" className="w-full">
                                        Connexion
                                    </Button>
                                </Link>
                                <Link 
                                    to="/register" 
                                    onClick={() => setMobileMenuOpen(false)}
                                    className="block"
                                >
                                    <Button className="w-full bg-red-600 hover:bg-red-700">
                                        S'inscrire
                                    </Button>
                                </Link>
                            </div>
                        )}
                    </div>
                </div>
            )}
        </nav>
    );
};

export const Footer = () => {
    return (
        <footer className="bg-slate-900 text-slate-400 py-12 mt-auto" data-testid="footer">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
                    <div>
                        <div className="flex items-center gap-2 mb-4">
                            <img 
                                src="/images/logo-secours73.png" 
                                alt="Secours Alpes 73" 
                                className="h-12 w-auto"
                            />
                        </div>
                        <p className="text-sm">
                            Plateforme de formation ouverte à distance pour les premiers secours.
                        </p>
                        <p className="text-xs mt-2 text-slate-500">
                            Développé par <strong className="text-slate-400">Secours Alpes 73</strong>
                        </p>
                    </div>
                    
                    <div>
                        <h4 className="font-semibold text-white mb-4">Formations</h4>
                        <ul className="space-y-2 text-sm">
                            <li className="flex items-center gap-2">
                                <Shield className="w-4 h-4 text-red-500" />
                                <span>PSE - Premiers Secours en Équipe</span>
                            </li>
                            <li className="flex items-center gap-2">
                                <Heart className="w-4 h-4 text-green-500" />
                                <Link to="/psc" className="hover:text-white transition-colors">PSC - Premiers Secours Citoyen</Link>
                            </li>
                            <li className="flex items-center gap-2">
                                <Waves className="w-4 h-4 text-blue-500" />
                                <span>BNSSA - Sauvetage Aquatique</span>
                            </li>
                        </ul>
                    </div>
                    
                    <div>
                        <h4 className="font-semibold text-white mb-4">À propos</h4>
                        <p className="text-sm">
                            Association habilitée pour la formation aux premiers secours.
                        </p>
                        <p className="text-xs mt-4 text-slate-500">
                            Basé sur les recommandations PSE de la Direction Générale de la Sécurité Civile.
                        </p>
                    </div>
                </div>
                
                <div className="border-t border-slate-800 mt-8 pt-8 text-center text-sm">
                    <p>© {new Date().getFullYear()} Secours 73 - Secours Alpes 73. Tous droits réservés.</p>
                </div>
            </div>
        </footer>
    );
};

const Layout = ({ children }) => {
    return (
        <div className="min-h-screen flex flex-col">
            <Navbar />
            <main className="flex-1">
                {children}
            </main>
            <Footer />
        </div>
    );
};

export default Layout;
