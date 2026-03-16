import React, { useState, useEffect } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { 
    ArrowLeft, 
    ArrowRight, 
    BookOpen, 
    FileText,
    Play,
    CheckCircle2,
    ChevronRight
} from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../components/ui/tabs';
import { ScrollArea } from '../components/ui/scroll-area';
import Layout from '../components/Layout';
import { getChapter, getUser, getProgress } from '../lib/api';

const ChapterDetail = () => {
    const { chapterId } = useParams();
    const navigate = useNavigate();
    const user = getUser();
    const [chapter, setChapter] = useState(null);
    const [loading, setLoading] = useState(true);
    const [activeFiche, setActiveFiche] = useState(0);
    const [progress, setProgress] = useState(null);

    useEffect(() => {
        loadData();
    }, [chapterId]);

    const loadData = async () => {
        try {
            const chapterData = await getChapter(chapterId);
            setChapter(chapterData);
            
            if (user) {
                const progressData = await getProgress();
                setProgress(progressData);
            }
        } catch (error) {
            console.error('Erreur:', error);
        } finally {
            setLoading(false);
        }
    };

    const isCompleted = progress?.chapters_completed?.includes(chapterId) || false;

    const renderContent = (content) => {
        // Simple markdown-like rendering
        const lines = content.split('\n');
        return lines.map((line, index) => {
            // Headers
            if (line.startsWith('**') && line.endsWith('**')) {
                return (
                    <h3 key={index} className="font-semibold text-slate-900 mt-4 mb-2">
                        {line.replace(/\*\*/g, '')}
                    </h3>
                );
            }
            // Bold sections
            if (line.includes('**')) {
                const parts = line.split(/\*\*(.*?)\*\*/g);
                return (
                    <p key={index} className="mb-2">
                        {parts.map((part, i) => 
                            i % 2 === 1 ? <strong key={i} className="font-semibold text-slate-900">{part}</strong> : part
                        )}
                    </p>
                );
            }
            // List items
            if (line.startsWith('- ')) {
                return (
                    <li key={index} className="ml-4 mb-1 text-slate-700">
                        {line.substring(2)}
                    </li>
                );
            }
            // Numbered list
            if (/^\d+\./.test(line)) {
                return (
                    <li key={index} className="ml-4 mb-1 text-slate-700 list-decimal">
                        {line.replace(/^\d+\.\s*/, '')}
                    </li>
                );
            }
            // Empty line
            if (line.trim() === '') {
                return <br key={index} />;
            }
            // Regular paragraph
            return (
                <p key={index} className="mb-2 text-slate-700 leading-relaxed">
                    {line}
                </p>
            );
        });
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

    if (!chapter) {
        return (
            <Layout>
                <div className="max-w-7xl mx-auto px-4 py-8">
                    <p className="text-center text-slate-600">Chapitre non trouvé</p>
                    <Link to="/chapitres" className="block text-center mt-4">
                        <Button variant="outline">Retour aux chapitres</Button>
                    </Link>
                </div>
            </Layout>
        );
    }

    return (
        <Layout>
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8" data-testid="chapter-detail">
                {/* Breadcrumb */}
                <div className="flex items-center gap-2 text-sm text-slate-600 mb-6">
                    <Link to="/chapitres" className="hover:text-red-600 transition-colors">
                        Chapitres
                    </Link>
                    <ChevronRight className="w-4 h-4" />
                    <span className="text-slate-900 font-medium">Chapitre {chapter.numero}</span>
                </div>

                {/* Header */}
                <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-8">
                    <div>
                        <div className="flex items-center gap-3 mb-2">
                            <span className="px-3 py-1 bg-red-100 text-red-700 text-sm font-medium rounded-full">
                                Chapitre {chapter.numero}
                            </span>
                            {isCompleted && (
                                <span className="px-3 py-1 bg-green-100 text-green-700 text-sm font-medium rounded-full flex items-center gap-1">
                                    <CheckCircle2 className="w-4 h-4" />
                                    Complété
                                </span>
                            )}
                        </div>
                        <h1 className="text-3xl font-bold text-slate-900 mb-2">
                            {chapter.titre}
                        </h1>
                        <p className="text-slate-600">
                            {chapter.description}
                        </p>
                    </div>
                    
                    {user && (
                        <Link to={`/quiz/${chapterId}`}>
                            <Button className="bg-red-600 hover:bg-red-700" data-testid="start-quiz-btn">
                                <Play className="w-4 h-4 mr-2" />
                                Passer le quiz
                            </Button>
                        </Link>
                    )}
                </div>

                {/* Content */}
                <div className="grid lg:grid-cols-4 gap-8">
                    {/* Sidebar - Fiches List */}
                    <div className="lg:col-span-1">
                        <Card className="sticky top-24" data-testid="fiches-sidebar">
                            <CardHeader className="pb-3">
                                <CardTitle className="text-sm font-medium text-slate-600 flex items-center gap-2">
                                    <FileText className="w-4 h-4" />
                                    Fiches ({chapter.fiches.length})
                                </CardTitle>
                            </CardHeader>
                            <CardContent className="p-0">
                                <ScrollArea className="h-[400px]">
                                    <div className="px-4 pb-4 space-y-1">
                                        {chapter.fiches.map((fiche, index) => (
                                            <button
                                                key={fiche.id}
                                                onClick={() => setActiveFiche(index)}
                                                className={`w-full text-left px-3 py-2 rounded-lg text-sm transition-colors ${
                                                    activeFiche === index
                                                        ? 'bg-red-100 text-red-700 font-medium'
                                                        : 'text-slate-600 hover:bg-slate-100'
                                                }`}
                                                data-testid={`fiche-btn-${index}`}
                                            >
                                                {fiche.titre}
                                            </button>
                                        ))}
                                    </div>
                                </ScrollArea>
                            </CardContent>
                        </Card>
                    </div>

                    {/* Main Content */}
                    <div className="lg:col-span-3">
                        <Card data-testid="fiche-content">
                            <CardHeader className="border-b border-slate-100">
                                <CardTitle className="text-xl">
                                    {chapter.fiches[activeFiche]?.titre}
                                </CardTitle>
                            </CardHeader>
                            <CardContent className="p-6">
                                <div className="prose prose-slate max-w-none">
                                    {renderContent(chapter.fiches[activeFiche]?.contenu || '')}
                                </div>
                            </CardContent>
                        </Card>

                        {/* Navigation */}
                        <div className="flex items-center justify-between mt-6">
                            <Button
                                variant="outline"
                                onClick={() => setActiveFiche(Math.max(0, activeFiche - 1))}
                                disabled={activeFiche === 0}
                                data-testid="prev-fiche-btn"
                            >
                                <ArrowLeft className="w-4 h-4 mr-2" />
                                Précédent
                            </Button>
                            
                            <span className="text-sm text-slate-500">
                                Fiche {activeFiche + 1} sur {chapter.fiches.length}
                            </span>
                            
                            {activeFiche < chapter.fiches.length - 1 ? (
                                <Button
                                    variant="outline"
                                    onClick={() => setActiveFiche(activeFiche + 1)}
                                    data-testid="next-fiche-btn"
                                >
                                    Suivant
                                    <ArrowRight className="w-4 h-4 ml-2" />
                                </Button>
                            ) : user ? (
                                <Link to={`/quiz/${chapterId}`}>
                                    <Button className="bg-red-600 hover:bg-red-700" data-testid="go-to-quiz-btn">
                                        Passer le quiz
                                        <ArrowRight className="w-4 h-4 ml-2" />
                                    </Button>
                                </Link>
                            ) : (
                                <Link to="/login">
                                    <Button className="bg-red-600 hover:bg-red-700">
                                        Se connecter
                                        <ArrowRight className="w-4 h-4 ml-2" />
                                    </Button>
                                </Link>
                            )}
                        </div>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default ChapterDetail;
