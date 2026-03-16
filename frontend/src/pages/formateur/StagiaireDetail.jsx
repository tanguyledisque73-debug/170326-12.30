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
import { Button } from '../../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/card';
import { Progress } from '../../components/ui/progress';
import Layout from '../../components/Layout';
import { formateurGetStagiaireDetail, getUser, getChapters } from '../../lib/api';
import { toast } from 'sonner';

const FormateurStagiaireDetail = () => {
    const { stagiaireId } = useParams();
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
    }, [stagiaireId]);

    const loadData = async () => {
        try {
            const [detailData, chaptersData] = await Promise.all([
                formateurGetStagiaireDetail(stagiaireId),
                getChapters()
            ]);
            setData(detailData);
            setChapters(chaptersData);
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors du chargement');
            navigate('/formateur');
        } finally {
            setLoading(false);
        }
    };

    const getChapterTitle = (chapterId) => {
        const chapter = chapters.find(c => c.id === chapterId);
        return chapter?.titre || chapterId;
    };

    const getScoreColor = (score, seuil = 80) => {
        if (score >= seuil) return 'text-green-600 bg-green-100';
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
                    <p className="text-slate-600">Stagiaire non trouvé</p>
                    <Link to="/formateur" className="mt-4 inline-block">
                        <Button variant="outline">Retour</Button>
                    </Link>
                </div>
            </Layout>
        );
    }

    const { stagiaire, groupe, progress, quiz_results } = data;
    const totalChapters = groupe?.chapitres_ordre?.length || 0;
    const completedChapters = progress?.chapitres_completes?.length || 0;
    const progressPct = totalChapters > 0 ? (completedChapters / totalChapters) * 100 : 0;
    const avgScore = quiz_results?.length > 0 
        ? quiz_results.reduce((acc, r) => acc + r.percentage, 0) / quiz_results.length 
        : 0;

    return (
        <Layout>
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8" data-testid="stagiaire-detail">
                {/* Back */}
                <Link 
                    to={`/formateur/groupe/${groupe?.id}`}
                    className="text-sm text-slate-600 hover:text-red-600 flex items-center gap-1 mb-6"
                >
                    <ArrowLeft className="w-4 h-4" />
                    Retour au groupe
                </Link>

                <div className="grid lg:grid-cols-3 gap-8">
                    {/* Profile */}
                    <Card className="lg:col-span-1">
                        <CardContent className="p-6">
                            <div className="text-center">
                                <div className="w-20 h-20 bg-slate-100 rounded-full flex items-center justify-center mx-auto mb-4">
                                    <User className="w-10 h-10 text-slate-400" />
                                </div>
                                <h2 className="text-xl font-bold text-slate-900">
                                    {stagiaire.prenom} {stagiaire.nom}
                                </h2>
                                <div className="flex items-center justify-center gap-2 text-slate-500 mt-2">
                                    <Mail className="w-4 h-4" />
                                    <span className="text-sm">{stagiaire.email}</span>
                                </div>
                                <div className="flex items-center justify-center gap-2 text-slate-500 mt-1">
                                    <Calendar className="w-4 h-4" />
                                    <span className="text-sm">
                                        Inscrit le {new Date(stagiaire.created_at).toLocaleDateString('fr-FR')}
                                    </span>
                                </div>
                                
                                <div className="mt-4 p-3 bg-slate-50 rounded-lg">
                                    <p className="text-sm text-slate-600">Groupe</p>
                                    <p className="font-semibold text-slate-900">{groupe?.nom}</p>
                                </div>
                            </div>
                        </CardContent>
                    </Card>

                    {/* Stats */}
                    <div className="lg:col-span-2 space-y-6">
                        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                            <Card>
                                <CardContent className="p-6">
                                    <div className="text-center">
                                        <p className="text-3xl font-bold text-slate-900">{Math.round(progressPct)}%</p>
                                        <p className="text-sm text-slate-500">Progression</p>
                                        <Progress value={progressPct} className="mt-2 h-2" />
                                    </div>
                                </CardContent>
                            </Card>
                            
                            <Card>
                                <CardContent className="p-6">
                                    <div className="text-center">
                                        <p className="text-3xl font-bold text-slate-900">{quiz_results?.length || 0}</p>
                                        <p className="text-sm text-slate-500">Quiz réalisés</p>
                                    </div>
                                </CardContent>
                            </Card>
                            
                            <Card>
                                <CardContent className="p-6">
                                    <div className="text-center">
                                        <p className={`text-3xl font-bold ${avgScore >= groupe?.seuil_reussite ? 'text-green-600' : 'text-red-600'}`}>
                                            {Math.round(avgScore)}%
                                        </p>
                                        <p className="text-sm text-slate-500">Score moyen</p>
                                    </div>
                                </CardContent>
                            </Card>
                        </div>

                        {/* Quiz History */}
                        <Card>
                            <CardHeader>
                                <CardTitle>Historique des quiz</CardTitle>
                            </CardHeader>
                            <CardContent>
                                {quiz_results?.length === 0 ? (
                                    <div className="empty-state py-8">
                                        <Star className="w-12 h-12 mx-auto text-slate-300 mb-3" />
                                        <p className="text-slate-500">Aucun quiz réalisé</p>
                                    </div>
                                ) : (
                                    <div className="space-y-3">
                                        {quiz_results.map((result) => (
                                            <div 
                                                key={result.id}
                                                className="flex items-center justify-between p-4 bg-slate-50 rounded-lg"
                                            >
                                                <div className="flex items-center gap-4">
                                                    <div className={`w-10 h-10 rounded-lg flex items-center justify-center ${getScoreColor(result.percentage, groupe?.seuil_reussite)}`}>
                                                        {result.percentage >= groupe?.seuil_reussite ? (
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
                                                                hour: '2-digit',
                                                                minute: '2-digit'
                                                            })}
                                                        </p>
                                                    </div>
                                                </div>
                                                <div className="text-right">
                                                    <p className={`text-lg font-bold ${
                                                        result.percentage >= groupe?.seuil_reussite ? 'text-green-600' : 'text-red-600'
                                                    }`}>
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
                </div>
            </div>
        </Layout>
    );
};

export default FormateurStagiaireDetail;
