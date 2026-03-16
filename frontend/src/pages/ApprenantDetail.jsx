import React, { useState, useEffect } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { 
    ArrowLeft,
    User,
    Mail,
    Calendar,
    Trophy,
    CheckCircle2,
    XCircle,
    Star
} from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { Progress } from '../components/ui/progress';
import Layout from '../components/Layout';
import { getApprenantDetail, getUser, getChapters } from '../lib/api';
import { toast } from 'sonner';

const ApprenantDetail = () => {
    const { apprenantId } = useParams();
    const navigate = useNavigate();
    const user = getUser();
    const [loading, setLoading] = useState(true);
    const [data, setData] = useState(null);
    const [chapters, setChapters] = useState([]);

    useEffect(() => {
        if (!user || user.role !== 'formateur') {
            navigate('/login');
            return;
        }
        loadData();
    }, [apprenantId]);

    const loadData = async () => {
        try {
            const [detailData, chaptersData] = await Promise.all([
                getApprenantDetail(apprenantId),
                getChapters()
            ]);
            setData(detailData);
            setChapters(chaptersData);
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors du chargement des données');
        } finally {
            setLoading(false);
        }
    };

    const getChapterTitle = (chapterId) => {
        const chapter = chapters.find(c => c.id === chapterId);
        return chapter?.titre || chapterId;
    };

    const getScoreColor = (score) => {
        if (score >= 80) return 'text-green-600 bg-green-100';
        if (score >= 60) return 'text-yellow-600 bg-yellow-100';
        return 'text-red-600 bg-red-100';
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

    if (!data) {
        return (
            <Layout>
                <div className="max-w-7xl mx-auto px-4 py-8 text-center">
                    <p className="text-slate-600 mb-4">Apprenant non trouvé</p>
                    <Link to="/formateur">
                        <Button variant="outline">Retour au tableau de bord</Button>
                    </Link>
                </div>
            </Layout>
        );
    }

    const { apprenant, stats, results } = data;
    const progressPercentage = (stats.chapters_completed / chapters.length) * 100;

    return (
        <Layout>
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8" data-testid="apprenant-detail">
                {/* Back Button */}
                <Link 
                    to="/formateur"
                    className="text-sm text-slate-600 hover:text-red-600 flex items-center gap-1 mb-6"
                >
                    <ArrowLeft className="w-4 h-4" />
                    Retour au tableau de bord
                </Link>

                {/* Header */}
                <div className="grid lg:grid-cols-3 gap-8 mb-8">
                    {/* Profile Card */}
                    <Card className="lg:col-span-1" data-testid="profile-card">
                        <CardContent className="p-6">
                            <div className="text-center">
                                <div className="w-20 h-20 bg-slate-100 rounded-full flex items-center justify-center mx-auto mb-4">
                                    <User className="w-10 h-10 text-slate-400" />
                                </div>
                                <h2 className="text-xl font-bold text-slate-900">
                                    {apprenant.prenom} {apprenant.nom}
                                </h2>
                                <div className="flex items-center justify-center gap-2 text-slate-500 mt-2">
                                    <Mail className="w-4 h-4" />
                                    <span className="text-sm">{apprenant.email}</span>
                                </div>
                                <div className="flex items-center justify-center gap-2 text-slate-500 mt-1">
                                    <Calendar className="w-4 h-4" />
                                    <span className="text-sm">
                                        Inscrit le {new Date(apprenant.created_at).toLocaleDateString('fr-FR')}
                                    </span>
                                </div>
                            </div>
                        </CardContent>
                    </Card>

                    {/* Stats Cards */}
                    <div className="lg:col-span-2 grid grid-cols-1 md:grid-cols-3 gap-4">
                        <Card data-testid="stat-progression">
                            <CardContent className="p-6">
                                <div className="flex items-center justify-between mb-2">
                                    <span className="text-sm text-slate-600">Progression</span>
                                    <span className="text-2xl font-bold text-slate-900">
                                        {Math.round(progressPercentage)}%
                                    </span>
                                </div>
                                <Progress value={progressPercentage} className="h-2" />
                                <p className="text-xs text-slate-500 mt-2">
                                    {stats.chapters_completed}/{chapters.length} chapitres
                                </p>
                            </CardContent>
                        </Card>

                        <Card data-testid="stat-quizzes">
                            <CardContent className="p-6">
                                <div className="flex items-center gap-3">
                                    <div className="w-10 h-10 bg-green-100 rounded-lg flex items-center justify-center">
                                        <CheckCircle2 className="w-5 h-5 text-green-600" />
                                    </div>
                                    <div>
                                        <p className="text-2xl font-bold text-slate-900">
                                            {stats.quizzes_completed}
                                        </p>
                                        <p className="text-xs text-slate-500">Quiz réalisés</p>
                                    </div>
                                </div>
                            </CardContent>
                        </Card>

                        <Card data-testid="stat-average">
                            <CardContent className="p-6">
                                <div className="flex items-center gap-3">
                                    <div className="w-10 h-10 bg-yellow-100 rounded-lg flex items-center justify-center">
                                        <Trophy className="w-5 h-5 text-yellow-600" />
                                    </div>
                                    <div>
                                        <p className={`text-2xl font-bold ${
                                            stats.average_score >= 80 ? 'text-green-600' :
                                            stats.average_score >= 60 ? 'text-yellow-600' :
                                            'text-red-600'
                                        }`}>
                                            {stats.average_score}%
                                        </p>
                                        <p className="text-xs text-slate-500">Score moyen</p>
                                    </div>
                                </div>
                            </CardContent>
                        </Card>
                    </div>
                </div>

                {/* Results History */}
                <Card data-testid="results-history">
                    <CardHeader>
                        <CardTitle>Historique des quiz</CardTitle>
                    </CardHeader>
                    <CardContent>
                        {results.length === 0 ? (
                            <div className="empty-state py-8">
                                <Star className="w-12 h-12 mx-auto text-slate-300 mb-3" />
                                <p className="text-slate-500">Aucun quiz réalisé</p>
                            </div>
                        ) : (
                            <div className="space-y-3">
                                {results.map((result) => (
                                    <div 
                                        key={result.id}
                                        className="flex items-center justify-between p-4 bg-slate-50 rounded-lg"
                                    >
                                        <div className="flex items-center gap-4">
                                            <div className={`w-10 h-10 rounded-lg flex items-center justify-center ${getScoreColor(result.percentage)}`}>
                                                {result.percentage >= 60 ? (
                                                    <CheckCircle2 className="w-5 h-5" />
                                                ) : (
                                                    <XCircle className="w-5 h-5" />
                                                )}
                                            </div>
                                            <div>
                                                <p className="font-medium text-slate-900">
                                                    {getChapterTitle(result.chapter_id)}
                                                </p>
                                                <p className="text-xs text-slate-500">
                                                    {new Date(result.completed_at).toLocaleDateString('fr-FR', {
                                                        day: 'numeric',
                                                        month: 'long',
                                                        year: 'numeric',
                                                        hour: '2-digit',
                                                        minute: '2-digit'
                                                    })}
                                                </p>
                                            </div>
                                        </div>
                                        <div className="text-right">
                                            <p className={`text-lg font-bold ${
                                                result.percentage >= 80 ? 'text-green-600' :
                                                result.percentage >= 60 ? 'text-yellow-600' :
                                                'text-red-600'
                                            }`}>
                                                {result.percentage}%
                                            </p>
                                            <p className="text-xs text-slate-500">
                                                {result.score}/{result.total} réponses
                                            </p>
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

export default ApprenantDetail;
