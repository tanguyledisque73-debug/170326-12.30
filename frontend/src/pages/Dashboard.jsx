import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { 
    BookOpen, 
    CheckCircle2, 
    Trophy, 
    TrendingUp, 
    ArrowRight,
    Clock,
    Target,
    Star
} from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { Progress } from '../components/ui/progress';
import Layout from '../components/Layout';
import { getChapters, getProgress, getQuizResults, getUser } from '../lib/api';
import { toast } from 'sonner';

const Dashboard = () => {
    const navigate = useNavigate();
    const user = getUser();
    const [loading, setLoading] = useState(true);
    const [chapters, setChapters] = useState([]);
    const [progress, setProgress] = useState(null);
    const [recentResults, setRecentResults] = useState([]);

    useEffect(() => {
        if (!user || user.role !== 'apprenant') {
            navigate('/login');
            return;
        }
        loadData();
    }, []);

    const loadData = async () => {
        try {
            const [chaptersData, progressData, resultsData] = await Promise.all([
                getChapters(),
                getProgress(),
                getQuizResults()
            ]);
            setChapters(chaptersData);
            setProgress(progressData);
            setRecentResults(resultsData.slice(0, 5));
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors du chargement des données');
        } finally {
            setLoading(false);
        }
    };

    const totalChapters = chapters.length;
    const completedChapters = progress?.chapters_completed?.length || 0;
    const progressPercentage = totalChapters > 0 ? (completedChapters / totalChapters) * 100 : 0;

    const getScoreColor = (score) => {
        if (score >= 80) return 'text-green-600 bg-green-100';
        if (score >= 60) return 'text-yellow-600 bg-yellow-100';
        return 'text-red-600 bg-red-100';
    };

    const getChapterTitle = (chapterId) => {
        const chapter = chapters.find(c => c.id === chapterId);
        return chapter?.titre || chapterId;
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
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8" data-testid="dashboard-apprenant">
                {/* Header */}
                <div className="mb-8">
                    <h1 className="text-3xl font-bold text-slate-900 mb-2">
                        Bonjour, {user?.prenom} !
                    </h1>
                    <p className="text-slate-600">
                        Suivez votre progression et continuez votre formation aux premiers secours.
                    </p>
                </div>

                {/* Stats Cards */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8 stagger-children">
                    <Card className="card-hover" data-testid="stat-progress">
                        <CardContent className="p-6">
                            <div className="flex items-center justify-between mb-4">
                                <div className="w-12 h-12 bg-red-100 rounded-xl flex items-center justify-center">
                                    <TrendingUp className="w-6 h-6 text-red-600" />
                                </div>
                                <span className="text-3xl font-bold text-slate-900">
                                    {Math.round(progressPercentage)}%
                                </span>
                            </div>
                            <p className="text-sm text-slate-600">Progression globale</p>
                            <Progress value={progressPercentage} className="mt-2 h-2" />
                        </CardContent>
                    </Card>

                    <Card className="card-hover" data-testid="stat-chapters">
                        <CardContent className="p-6">
                            <div className="flex items-center justify-between mb-4">
                                <div className="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center">
                                    <BookOpen className="w-6 h-6 text-blue-600" />
                                </div>
                                <span className="text-3xl font-bold text-slate-900">
                                    {completedChapters}/{totalChapters}
                                </span>
                            </div>
                            <p className="text-sm text-slate-600">Chapitres complétés</p>
                        </CardContent>
                    </Card>

                    <Card className="card-hover" data-testid="stat-quizzes">
                        <CardContent className="p-6">
                            <div className="flex items-center justify-between mb-4">
                                <div className="w-12 h-12 bg-green-100 rounded-xl flex items-center justify-center">
                                    <CheckCircle2 className="w-6 h-6 text-green-600" />
                                </div>
                                <span className="text-3xl font-bold text-slate-900">
                                    {progress?.quizzes_completed || 0}
                                </span>
                            </div>
                            <p className="text-sm text-slate-600">Quiz réalisés</p>
                        </CardContent>
                    </Card>

                    <Card className="card-hover" data-testid="stat-score">
                        <CardContent className="p-6">
                            <div className="flex items-center justify-between mb-4">
                                <div className="w-12 h-12 bg-yellow-100 rounded-xl flex items-center justify-center">
                                    <Trophy className="w-6 h-6 text-yellow-600" />
                                </div>
                                <span className="text-3xl font-bold text-slate-900">
                                    {progress?.average_score || 0}%
                                </span>
                            </div>
                            <p className="text-sm text-slate-600">Score moyen</p>
                        </CardContent>
                    </Card>
                </div>

                <div className="grid lg:grid-cols-3 gap-8">
                    {/* Recent Results */}
                    <div className="lg:col-span-2">
                        <Card data-testid="recent-results">
                            <CardHeader className="flex flex-row items-center justify-between">
                                <CardTitle className="text-lg">Derniers quiz</CardTitle>
                                <Link to="/chapitres">
                                    <Button variant="ghost" size="sm">
                                        Tous les chapitres
                                        <ArrowRight className="w-4 h-4 ml-1" />
                                    </Button>
                                </Link>
                            </CardHeader>
                            <CardContent>
                                {recentResults.length === 0 ? (
                                    <div className="empty-state py-8">
                                        <Target className="w-12 h-12 mx-auto text-slate-300 mb-3" />
                                        <p className="text-slate-500">Aucun quiz réalisé pour le moment</p>
                                        <Link to="/chapitres" className="mt-4 inline-block">
                                            <Button size="sm" className="bg-red-600 hover:bg-red-700">
                                                Commencer un quiz
                                            </Button>
                                        </Link>
                                    </div>
                                ) : (
                                    <div className="space-y-3">
                                        {recentResults.map((result) => (
                                            <div 
                                                key={result.id}
                                                className="flex items-center justify-between p-4 bg-slate-50 rounded-lg hover:bg-slate-100 transition-colors"
                                            >
                                                <div className="flex items-center gap-4">
                                                    <div className={`w-10 h-10 rounded-lg flex items-center justify-center ${getScoreColor(result.percentage)}`}>
                                                        <Star className="w-5 h-5" />
                                                    </div>
                                                    <div>
                                                        <p className="font-medium text-slate-900">
                                                            {getChapterTitle(result.chapter_id)}
                                                        </p>
                                                        <p className="text-xs text-slate-500 flex items-center gap-1">
                                                            <Clock className="w-3 h-3" />
                                                            {new Date(result.completed_at).toLocaleDateString('fr-FR')}
                                                        </p>
                                                    </div>
                                                </div>
                                                <div className="text-right">
                                                    <p className={`text-lg font-bold ${result.percentage >= 80 ? 'text-green-600' : result.percentage >= 60 ? 'text-yellow-600' : 'text-red-600'}`}>
                                                        {result.percentage}%
                                                    </p>
                                                    <p className="text-xs text-slate-500">
                                                        {result.score}/{result.total}
                                                    </p>
                                                </div>
                                            </div>
                                        ))}
                                    </div>
                                )}
                            </CardContent>
                        </Card>
                    </div>

                    {/* Quick Actions */}
                    <div>
                        <Card data-testid="quick-actions">
                            <CardHeader>
                                <CardTitle className="text-lg">Actions rapides</CardTitle>
                            </CardHeader>
                            <CardContent className="space-y-3">
                                <Link to="/chapitres" className="block">
                                    <Button variant="outline" className="w-full justify-start">
                                        <BookOpen className="w-4 h-4 mr-2" />
                                        Voir tous les chapitres
                                    </Button>
                                </Link>
                                
                                {chapters.length > 0 && (
                                    <>
                                        <p className="text-sm text-slate-500 pt-2">Continuer avec :</p>
                                        {chapters.slice(0, 3).map((chapter) => {
                                            const isCompleted = progress?.chapters_completed?.includes(chapter.id);
                                            return (
                                                <Link 
                                                    key={chapter.id} 
                                                    to={`/chapitre/${chapter.id}`}
                                                    className="block"
                                                >
                                                    <div className="p-3 rounded-lg border border-slate-200 hover:border-red-200 hover:bg-red-50/50 transition-colors cursor-pointer">
                                                        <div className="flex items-center justify-between">
                                                            <span className="text-sm font-medium text-slate-700">
                                                                Ch. {chapter.numero}
                                                            </span>
                                                            {isCompleted && (
                                                                <CheckCircle2 className="w-4 h-4 text-green-600" />
                                                            )}
                                                        </div>
                                                        <p className="text-sm text-slate-600 mt-1 line-clamp-1">
                                                            {chapter.titre}
                                                        </p>
                                                    </div>
                                                </Link>
                                            );
                                        })}
                                    </>
                                )}
                            </CardContent>
                        </Card>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default Dashboard;
