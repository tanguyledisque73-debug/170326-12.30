import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { 
    Users, 
    TrendingUp, 
    FolderPlus,
    ArrowRight,
    Copy,
    CheckCircle2
} from 'lucide-react';
import { Button } from '../../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/card';
import Layout from '../../components/Layout';
import { formateurGetGroupes, getUser } from '../../lib/api';
import { toast } from 'sonner';

const FormateurDashboard = () => {
    const navigate = useNavigate();
    const user = getUser();
    const [loading, setLoading] = useState(true);
    const [groupes, setGroupes] = useState([]);

    useEffect(() => {
        if (!user || user.role !== 'formateur') {
            navigate('/login');
            return;
        }
        loadData();
    }, []);

    const loadData = async () => {
        try {
            const data = await formateurGetGroupes();
            setGroupes(data);
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors du chargement');
        } finally {
            setLoading(false);
        }
    };

    const copyCode = (code) => {
        navigator.clipboard.writeText(code);
        toast.success('Code copié !');
    };

    const totalStagiaires = groupes.reduce((acc, g) => acc + (g.nb_stagiaires || 0), 0);

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
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8" data-testid="formateur-dashboard">
                {/* Header */}
                <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-8">
                    <div>
                        <h1 className="text-3xl font-bold text-slate-900 mb-2">
                            Espace Formateur
                        </h1>
                        <p className="text-slate-600">
                            Bienvenue {user?.prenom}. Gérez vos groupes de formation.
                        </p>
                    </div>
                    <Link to="/formateur/groupes">
                        <Button className="bg-red-600 hover:bg-red-700">
                            <FolderPlus className="w-4 h-4 mr-2" />
                            Créer un groupe
                        </Button>
                    </Link>
                </div>

                {/* Stats */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                    <Card className="card-hover">
                        <CardContent className="p-6">
                            <div className="flex items-center justify-between">
                                <div className="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center">
                                    <Users className="w-6 h-6 text-blue-600" />
                                </div>
                                <span className="text-3xl font-bold text-slate-900">{totalStagiaires}</span>
                            </div>
                            <p className="text-sm text-slate-600 mt-2">Stagiaires inscrits</p>
                        </CardContent>
                    </Card>
                    
                    <Card className="card-hover">
                        <CardContent className="p-6">
                            <div className="flex items-center justify-between">
                                <div className="w-12 h-12 bg-green-100 rounded-xl flex items-center justify-center">
                                    <TrendingUp className="w-6 h-6 text-green-600" />
                                </div>
                                <span className="text-3xl font-bold text-slate-900">{groupes.length}</span>
                            </div>
                            <p className="text-sm text-slate-600 mt-2">Groupes actifs</p>
                        </CardContent>
                    </Card>
                    
                    <Card className="card-hover">
                        <CardContent className="p-6">
                            <div className="flex items-center justify-between">
                                <div className="w-12 h-12 bg-purple-100 rounded-xl flex items-center justify-center">
                                    <CheckCircle2 className="w-6 h-6 text-purple-600" />
                                </div>
                                <span className="text-3xl font-bold text-slate-900">
                                    {groupes.filter(g => g.formateur_id === user?.id).length}
                                </span>
                            </div>
                            <p className="text-sm text-slate-600 mt-2">Mes groupes</p>
                        </CardContent>
                    </Card>
                </div>

                {/* Groupes */}
                <Card data-testid="groupes-list">
                    <CardHeader className="flex flex-row items-center justify-between">
                        <CardTitle>Mes groupes de formation</CardTitle>
                        <Link to="/formateur/groupes">
                            <Button variant="ghost" size="sm">
                                Gérer
                                <ArrowRight className="w-4 h-4 ml-1" />
                            </Button>
                        </Link>
                    </CardHeader>
                    <CardContent>
                        {groupes.length === 0 ? (
                            <div className="empty-state py-8">
                                <Users className="w-12 h-12 mx-auto text-slate-300 mb-3" />
                                <p className="text-slate-500 mb-4">Aucun groupe créé</p>
                                <Link to="/formateur/groupes">
                                    <Button size="sm" className="bg-red-600 hover:bg-red-700">
                                        Créer mon premier groupe
                                    </Button>
                                </Link>
                            </div>
                        ) : (
                            <div className="space-y-4">
                                {groupes.map((groupe) => (
                                    <div 
                                        key={groupe.id}
                                        className="flex items-center justify-between p-4 bg-slate-50 rounded-lg hover:bg-slate-100 transition-colors"
                                    >
                                        <div className="flex-1">
                                            <div className="flex items-center gap-2 mb-1">
                                                <h3 className="font-semibold text-slate-900">{groupe.nom}</h3>
                                                <span className={`px-2 py-0.5 rounded text-xs font-medium ${
                                                    groupe.formation_type === 'PSE' ? 'bg-red-100 text-red-700' :
                                                    groupe.formation_type === 'PSC' ? 'bg-green-100 text-green-700' :
                                                    'bg-blue-100 text-blue-700'
                                                }`}>
                                                    {groupe.formation_type}
                                                </span>
                                                {groupe.formateur_id !== user?.id && (
                                                    <span className="px-2 py-0.5 bg-purple-100 text-purple-700 rounded text-xs font-medium">
                                                        Collaborateur
                                                    </span>
                                                )}
                                            </div>
                                            <div className="flex items-center gap-4 text-sm text-slate-500">
                                                <span>{groupe.nb_stagiaires || 0}/{groupe.max_stagiaires} stagiaires</span>
                                                <span>Seuil: {groupe.seuil_reussite}%</span>
                                            </div>
                                        </div>
                                        
                                        <div className="flex items-center gap-3">
                                            <div className="text-right">
                                                <p className="text-xs text-slate-500">Code d'accès</p>
                                                <button 
                                                    onClick={() => copyCode(groupe.code_acces)}
                                                    className="flex items-center gap-1 font-mono text-sm font-bold text-slate-900 hover:text-red-600"
                                                >
                                                    {groupe.code_acces}
                                                    <Copy className="w-3 h-3" />
                                                </button>
                                            </div>
                                            <Link to={`/formateur/groupe/${groupe.id}`}>
                                                <Button variant="outline" size="sm">
                                                    Voir
                                                </Button>
                                            </Link>
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

export default FormateurDashboard;
