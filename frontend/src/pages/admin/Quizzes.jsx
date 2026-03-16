import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { 
    Plus,
    Pencil,
    Trash2,
    Video,
    FileQuestion
} from 'lucide-react';
import { Button } from '../../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/card';
import Layout from '../../components/Layout';
import { getQuizzes, adminDeleteQuiz, getChapters, getUser } from '../../lib/api';
import { toast } from 'sonner';

const AdminQuizzes = () => {
    const navigate = useNavigate();
    const user = getUser();
    const [loading, setLoading] = useState(true);
    const [quizzes, setQuizzes] = useState([]);
    const [chapters, setChapters] = useState([]);
    const [deleteConfirm, setDeleteConfirm] = useState(null);

    useEffect(() => {
        if (!user || user.role !== 'admin') {
            navigate('/login');
            return;
        }
        loadData();
    }, []);

    const loadData = async () => {
        try {
            const [quizzesData, chaptersData] = await Promise.all([
                getQuizzes(),
                getChapters()
            ]);
            setQuizzes(quizzesData);
            setChapters(chaptersData);
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors du chargement');
        } finally {
            setLoading(false);
        }
    };

    const handleDelete = async (quizId) => {
        try {
            await adminDeleteQuiz(quizId);
            toast.success('Quiz supprimé');
            setDeleteConfirm(null);
            loadData();
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors de la suppression');
        }
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
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8" data-testid="admin-quizzes">
                {/* Header */}
                <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-8">
                    <div>
                        <h1 className="text-3xl font-bold text-slate-900 mb-2">
                            Gestion des Quiz
                        </h1>
                        <p className="text-slate-600">
                            Créez, modifiez ou supprimez des quiz. Ajoutez des vidéos de présentation.
                        </p>
                    </div>
                    <Link to="/admin/quiz">
                        <Button className="bg-red-600 hover:bg-red-700">
                            <Plus className="w-4 h-4 mr-2" />
                            Nouveau quiz
                        </Button>
                    </Link>
                </div>

                {/* Quizzes List */}
                <Card>
                    <CardHeader>
                        <CardTitle>Quiz existants ({quizzes.length})</CardTitle>
                    </CardHeader>
                    <CardContent>
                        {quizzes.length === 0 ? (
                            <div className="empty-state py-8">
                                <FileQuestion className="w-12 h-12 mx-auto text-slate-300 mb-3" />
                                <p className="text-slate-500 mb-4">Aucun quiz créé</p>
                                <Link to="/admin/quiz">
                                    <Button size="sm" className="bg-red-600 hover:bg-red-700">
                                        Créer un quiz
                                    </Button>
                                </Link>
                            </div>
                        ) : (
                            <div className="space-y-3">
                                {quizzes.map((quiz) => (
                                    <div 
                                        key={quiz.id}
                                        className="flex items-center justify-between p-4 bg-slate-50 rounded-lg"
                                    >
                                        <div className="flex-1">
                                            <div className="flex items-center gap-2 mb-1">
                                                <p className="font-medium text-slate-900">{quiz.titre}</p>
                                                {quiz.video_url && (
                                                    <span className="px-2 py-0.5 bg-purple-100 text-purple-700 text-xs rounded font-medium flex items-center gap-1">
                                                        <Video className="w-3 h-3" />
                                                        Vidéo
                                                    </span>
                                                )}
                                            </div>
                                            <p className="text-sm text-slate-500">
                                                Chapitre: {getChapterTitle(quiz.chapter_id)}
                                            </p>
                                            <p className="text-xs text-slate-400 mt-1">
                                                {quiz.questions?.length || 0} questions
                                            </p>
                                        </div>
                                        <div className="flex items-center gap-2">
                                            <Link to={`/admin/quiz/${quiz.id}`}>
                                                <Button variant="outline" size="sm">
                                                    <Pencil className="w-4 h-4 mr-1" />
                                                    Modifier
                                                </Button>
                                            </Link>
                                            
                                            {deleteConfirm === quiz.id ? (
                                                <div className="flex gap-2">
                                                    <Button 
                                                        size="sm" 
                                                        variant="destructive"
                                                        onClick={() => handleDelete(quiz.id)}
                                                    >
                                                        Confirmer
                                                    </Button>
                                                    <Button 
                                                        size="sm" 
                                                        variant="outline"
                                                        onClick={() => setDeleteConfirm(null)}
                                                    >
                                                        Annuler
                                                    </Button>
                                                </div>
                                            ) : (
                                                <Button 
                                                    size="sm" 
                                                    variant="ghost"
                                                    className="text-red-600 hover:text-red-700 hover:bg-red-50"
                                                    onClick={() => setDeleteConfirm(quiz.id)}
                                                >
                                                    <Trash2 className="w-4 h-4" />
                                                </Button>
                                            )}
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

export default AdminQuizzes;
