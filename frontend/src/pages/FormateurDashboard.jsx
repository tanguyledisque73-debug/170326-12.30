import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { 
    Users, 
    TrendingUp, 
    CheckCircle2, 
    Trophy,
    ArrowRight,
    Search,
    ChevronRight,
    BarChart3,
    Eye
} from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { Input } from '../components/ui/input';
import { Progress } from '../components/ui/progress';
import Layout from '../components/Layout';
import { getApprenants, getFormateurStats, getUser, getChapters } from '../lib/api';
import { toast } from 'sonner';

const FormateurDashboard = () => {
    const navigate = useNavigate();
    const user = getUser();
    const [loading, setLoading] = useState(true);
    const [apprenants, setApprenants] = useState([]);
    const [stats, setStats] = useState(null);
    const [chapters, setChapters] = useState([]);
    const [searchQuery, setSearchQuery] = useState('');

    useEffect(() => {
        if (!user || user.role !== 'formateur') {
            navigate('/login');
            return;
        }
        loadData();
    }, []);

    const loadData = async () => {
        try {
            const [apprenantsData, statsData, chaptersData] = await Promise.all([
                getApprenants(),
                getFormateurStats(),
                getChapters()
            ]);
            setApprenants(apprenantsData);
            setStats(statsData);
            setChapters(chaptersData);
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors du chargement des données');
        } finally {
            setLoading(false);
        }
    };

    const filteredApprenants = apprenants.filter(apprenant =>
        apprenant.nom.toLowerCase().includes(searchQuery.toLowerCase()) ||
        apprenant.prenom.toLowerCase().includes(searchQuery.toLowerCase()) ||
        apprenant.email.toLowerCase().includes(searchQuery.toLowerCase())
    );

    const getScoreColor = (score) => {
        if (score >= 80) return 'text-green-600';
        if (score >= 60) return 'text-yellow-600';
        return 'text-red-600';
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
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8" data-testid="formateur-dashboard">
                {/* Header */}
                <div className="mb-8">
                    <h1 className="text-3xl font-bold text-slate-900 mb-2">
                        Tableau de bord Formateur
                    </h1>
                    <p className="text-slate-600">
                        Suivez la progression de vos apprenants et les statistiques globales.
                    </p>
                </div>

                {/* Stats Cards */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8 stagger-children">
                    <Card className="card-hover" data-testid="stat-total-apprenants">
                        <CardContent className="p-6">
                            <div className="flex items-center justify-between mb-4">
                                <div className="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center">
                                    <Users className="w-6 h-6 text-blue-600" />
                                </div>
                                <span className="text-3xl font-bold text-slate-900">
                                    {stats?.total_apprenants || 0}
                                </span>
                            </div>
                            <p className="text-sm text-slate-600">Apprenants inscrits</p>
                        </CardContent>
                    </Card>

                    <Card className="card-hover" data-testid="stat-total-quizzes">
                        <CardContent className="p-6">
                            <div className="flex items-center justify-between mb-4">
                                <div className="w-12 h-12 bg-green-100 rounded-xl flex items-center justify-center">
                                    <CheckCircle2 className="w-6 h-6 text-green-600" />
                                </div>
                                <span className="text-3xl font-bold text-slate-900">
                                    {stats?.total_quizzes_completed || 0}
                                </span>
                            </div>
                            <p className="text-sm text-slate-600">Quiz complétés</p>
                        </CardContent>
                    </Card>

                    <Card className="card-hover" data-testid="stat-average-score">
                        <CardContent className="p-6">
                            <div className="flex items-center justify-between mb-4">
                                <div className="w-12 h-12 bg-yellow-100 rounded-xl flex items-center justify-center">
                                    <Trophy className="w-6 h-6 text-yellow-600" />
                                </div>
                                <span className="text-3xl font-bold text-slate-900">
                                    {stats?.average_global_score || 0}%
                                </span>
                            </div>
                            <p className="text-sm text-slate-600">Score moyen global</p>
                        </CardContent>
                    </Card>

                    <Card className="card-hover" data-testid="stat-chapters">
                        <CardContent className="p-6">
                            <div className="flex items-center justify-between mb-4">
                                <div className="w-12 h-12 bg-red-100 rounded-xl flex items-center justify-center">
                                    <BarChart3 className="w-6 h-6 text-red-600" />
                                </div>
                                <span className="text-3xl font-bold text-slate-900">
                                    {chapters.length}
                                </span>
                            </div>
                            <p className="text-sm text-slate-600">Chapitres disponibles</p>
                        </CardContent>
                    </Card>
                </div>

                <div className="grid lg:grid-cols-3 gap-8">
                    {/* Apprenants List */}
                    <div className="lg:col-span-2">
                        <Card data-testid="apprenants-list">
                            <CardHeader className="flex flex-row items-center justify-between">
                                <CardTitle className="text-lg">Liste des apprenants</CardTitle>
                                <div className="relative w-64">
                                    <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400" />
                                    <Input
                                        placeholder="Rechercher..."
                                        value={searchQuery}
                                        onChange={(e) => setSearchQuery(e.target.value)}
                                        className="pl-9 h-9"
                                        data-testid="search-apprenants"
                                    />
                                </div>
                            </CardHeader>
                            <CardContent>
                                {filteredApprenants.length === 0 ? (
                                    <div className="empty-state py-8">
                                        <Users className="w-12 h-12 mx-auto text-slate-300 mb-3" />
                                        <p className="text-slate-500">
                                            {searchQuery ? 'Aucun apprenant trouvé' : 'Aucun apprenant inscrit'}
                                        </p>
                                    </div>
                                ) : (
                                    <div className="overflow-x-auto">
                                        <table className="data-table">
                                            <thead>
                                                <tr>
                                                    <th>Apprenant</th>
                                                    <th>Quiz réalisés</th>
                                                    <th>Score moyen</th>
                                                    <th>Dernière activité</th>
                                                    <th></th>
                                                </tr>
                                            </thead>
                                            <tbody>
                                                {filteredApprenants.map((apprenant) => (
                                                    <tr key={apprenant.id} data-testid={`apprenant-row-${apprenant.id}`}>
                                                        <td>
                                                            <div>
                                                                <p className="font-medium text-slate-900">
                                                                    {apprenant.prenom} {apprenant.nom}
                                                                </p>
                                                                <p className="text-xs text-slate-500">
                                                                    {apprenant.email}
                                                                </p>
                                                            </div>
                                                        </td>
                                                        <td>
                                                            <span className="font-medium">
                                                                {apprenant.quizzes_completed}
                                                            </span>
                                                        </td>
                                                        <td>
                                                            <span className={`font-semibold ${getScoreColor(apprenant.average_score)}`}>
                                                                {apprenant.average_score}%
                                                            </span>
                                                        </td>
                                                        <td className="text-sm text-slate-500">
                                                            {apprenant.last_activity 
                                                                ? new Date(apprenant.last_activity).toLocaleDateString('fr-FR')
                                                                : '-'}
                                                        </td>
                                                        <td>
                                                            <Link to={`/formateur/apprenant/${apprenant.id}`}>
                                                                <Button variant="ghost" size="sm">
                                                                    <Eye className="w-4 h-4" />
                                                                </Button>
                                                            </Link>
                                                        </td>
                                                    </tr>
                                                ))}
                                            </tbody>
                                        </table>
                                    </div>
                                )}
                            </CardContent>
                        </Card>
                    </div>

                    {/* Chapter Stats */}
                    <div>
                        <Card data-testid="chapter-stats">
                            <CardHeader>
                                <CardTitle className="text-lg">Scores par chapitre</CardTitle>
                            </CardHeader>
                            <CardContent>
                                {stats?.chapter_stats?.length === 0 ? (
                                    <div className="empty-state py-4">
                                        <p className="text-sm text-slate-500">Aucune donnée disponible</p>
                                    </div>
                                ) : (
                                    <div className="space-y-4">
                                        {stats?.chapter_stats?.map((chapterStat) => (
                                            <div key={chapterStat.chapter_id}>
                                                <div className="flex items-center justify-between mb-1">
                                                    <span className="text-sm font-medium text-slate-700 truncate max-w-[180px]">
                                                        {chapterStat.chapter_titre}
                                                    </span>
                                                    <span className={`text-sm font-semibold ${getScoreColor(chapterStat.average_score)}`}>
                                                        {chapterStat.average_score}%
                                                    </span>
                                                </div>
                                                <Progress 
                                                    value={chapterStat.average_score} 
                                                    className="h-2"
                                                />
                                                <p className="text-xs text-slate-400 mt-1">
                                                    {chapterStat.attempts} tentative(s)
                                                </p>
                                            </div>
                                        ))}
                                    </div>
                                )}
                            </CardContent>
                        </Card>

                        {/* Quick Access */}
                        <Card className="mt-6" data-testid="quick-access">
                            <CardHeader>
                                <CardTitle className="text-lg">Accès rapide</CardTitle>
                            </CardHeader>
                            <CardContent className="space-y-2">
                                <Link to="/chapitres" className="block">
                                    <Button variant="outline" className="w-full justify-between">
                                        Voir les chapitres
                                        <ChevronRight className="w-4 h-4" />
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

export default FormateurDashboard;
