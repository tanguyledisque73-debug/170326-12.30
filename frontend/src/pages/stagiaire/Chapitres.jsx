import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { 
    BookOpen, 
    Lock,
    Unlock,
    CheckCircle2,
    ArrowRight
} from 'lucide-react';
import { Button } from '../../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/card';
import Layout from '../../components/Layout';
import { stagiaireGetChapitres, getUser } from '../../lib/api';
import { toast } from 'sonner';

const StagiaireChapitres = () => {
    const navigate = useNavigate();
    const user = getUser();
    const [loading, setLoading] = useState(true);
    const [chapitres, setChapitres] = useState([]);
    const [seuil, setSeuil] = useState(80);

    useEffect(() => {
        if (!user || user.role !== 'stagiaire') {
            navigate('/login');
            return;
        }
        loadData();
    }, []);

    const loadData = async () => {
        try {
            const data = await stagiaireGetChapitres();
            setChapitres(data.chapitres || []);
            setSeuil(data.seuil_reussite || 80);
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors du chargement');
        } finally {
            setLoading(false);
        }
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
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8" data-testid="stagiaire-chapitres">
                <div className="mb-8">
                    <h1 className="text-3xl font-bold text-slate-900 mb-2">
                        Chapitres de formation
                    </h1>
                    <p className="text-slate-600">
                        Validez chaque quiz avec un score d'au moins <strong>{seuil}%</strong> pour débloquer le chapitre suivant.
                    </p>
                </div>

                {chapitres.length === 0 ? (
                    <Card>
                        <CardContent className="py-12">
                            <div className="empty-state">
                                <BookOpen className="w-12 h-12 mx-auto text-slate-300 mb-3" />
                                <p className="text-slate-500">Aucun chapitre configuré pour votre groupe</p>
                            </div>
                        </CardContent>
                    </Card>
                ) : (
                    <div className="grid gap-4">
                        {chapitres.map((chapter, index) => (
                            <Card 
                                key={chapter.id}
                                className={`transition-all ${
                                    chapter.is_unlocked 
                                        ? 'hover:shadow-lg cursor-pointer' 
                                        : 'opacity-60'
                                } ${chapter.is_completed ? 'border-green-200 bg-green-50/50' : ''}`}
                                data-testid={`chapter-${chapter.id}`}
                            >
                                <CardContent className="p-6">
                                    <div className="flex items-center gap-6">
                                        {/* Status icon */}
                                        <div className={`w-14 h-14 rounded-xl flex items-center justify-center flex-shrink-0 ${
                                            chapter.is_completed 
                                                ? 'bg-green-100 text-green-600'
                                                : chapter.is_unlocked 
                                                    ? 'bg-red-100 text-red-600'
                                                    : 'bg-slate-200 text-slate-400'
                                        }`}>
                                            {chapter.is_completed ? (
                                                <CheckCircle2 className="w-7 h-7" />
                                            ) : chapter.is_unlocked ? (
                                                <Unlock className="w-7 h-7" />
                                            ) : (
                                                <Lock className="w-7 h-7" />
                                            )}
                                        </div>

                                        {/* Content */}
                                        <div className="flex-1">
                                            <div className="flex items-center gap-2 mb-1">
                                                <span className={`text-xs font-medium px-2 py-0.5 rounded ${
                                                    chapter.is_completed 
                                                        ? 'bg-green-100 text-green-700'
                                                        : chapter.is_unlocked 
                                                            ? 'bg-red-100 text-red-700'
                                                            : 'bg-slate-200 text-slate-500'
                                                }`}>
                                                    Étape {index + 1}
                                                </span>
                                                {chapter.is_completed && (
                                                    <span className="text-xs font-medium px-2 py-0.5 rounded bg-green-100 text-green-700">
                                                        Validé
                                                    </span>
                                                )}
                                            </div>
                                            <h3 className="text-lg font-semibold text-slate-900 mb-1">
                                                {chapter.titre}
                                            </h3>
                                            <p className="text-sm text-slate-600 line-clamp-1">
                                                {chapter.description}
                                            </p>
                                            <div className="flex items-center gap-4 mt-2 text-sm text-slate-500">
                                                <span className="flex items-center gap-1">
                                                    <BookOpen className="w-4 h-4" />
                                                    {chapter.fiches?.length || 0} fiches
                                                </span>
                                            </div>
                                        </div>

                                        {/* Action */}
                                        {chapter.is_unlocked && (
                                            <Link to={`/stagiaire/chapitre/${chapter.id}`}>
                                                <Button 
                                                    className={chapter.is_completed ? '' : 'bg-red-600 hover:bg-red-700'}
                                                    variant={chapter.is_completed ? 'outline' : 'default'}
                                                >
                                                    {chapter.is_completed ? 'Revoir' : 'Accéder'}
                                                    <ArrowRight className="w-4 h-4 ml-2" />
                                                </Button>
                                            </Link>
                                        )}
                                    </div>
                                </CardContent>
                            </Card>
                        ))}
                    </div>
                )}
            </div>
        </Layout>
    );
};

export default StagiaireChapitres;
