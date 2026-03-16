import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { 
    BookOpen, 
    ArrowRight,
    Shield,
    ClipboardList,
    HardHat,
    Sparkles,
    Heart,
    Activity,
    AlertTriangle,
    Bone,
    Brain,
    Truck,
    Users,
    Search
} from 'lucide-react';
import { Button } from '../components/ui/button';
import { Input } from '../components/ui/input';
import Layout from '../components/Layout';
import { getChapters, getUser, getProgress } from '../lib/api';

// Icon mapping
const iconMap = {
    Shield: Shield,
    ClipboardList: ClipboardList,
    HardHat: HardHat,
    Sparkles: Sparkles,
    Heart: Heart,
    Activity: Activity,
    AlertTriangle: AlertTriangle,
    Bone: Bone,
    Brain: Brain,
    Truck: Truck,
    Users: Users,
    BookOpen: BookOpen
};

const Chapters = () => {
    const [chapters, setChapters] = useState([]);
    const [loading, setLoading] = useState(true);
    const [searchQuery, setSearchQuery] = useState('');
    const [progress, setProgress] = useState(null);
    const user = getUser();

    useEffect(() => {
        loadData();
    }, []);

    const loadData = async () => {
        try {
            const chaptersData = await getChapters();
            setChapters(chaptersData);
            
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

    const filteredChapters = chapters.filter(chapter =>
        chapter.titre.toLowerCase().includes(searchQuery.toLowerCase()) ||
        chapter.description.toLowerCase().includes(searchQuery.toLowerCase())
    );

    const isChapterCompleted = (chapterId) => {
        return progress?.chapters_completed?.includes(chapterId) || false;
    };

    const getIcon = (iconName) => {
        const Icon = iconMap[iconName] || BookOpen;
        return Icon;
    };

    return (
        <Layout>
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8" data-testid="chapters-page">
                {/* Header */}
                <div className="mb-8">
                    <h1 className="text-3xl md:text-4xl font-bold text-slate-900 mb-2">
                        Chapitres de formation
                    </h1>
                    <p className="text-slate-600">
                        Parcourez les 12 chapitres du programme PSE (Premiers Secours en Équipe)
                    </p>
                </div>

                {/* Search */}
                <div className="mb-8">
                    <div className="relative max-w-md">
                        <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-400" />
                        <Input
                            placeholder="Rechercher un chapitre..."
                            value={searchQuery}
                            onChange={(e) => setSearchQuery(e.target.value)}
                            className="pl-10"
                            data-testid="search-chapters"
                        />
                    </div>
                </div>

                {/* Chapters Grid */}
                {loading ? (
                    <div className="flex justify-center py-12">
                        <div className="spinner"></div>
                    </div>
                ) : filteredChapters.length === 0 ? (
                    <div className="empty-state py-12">
                        <BookOpen className="w-12 h-12 mx-auto text-slate-300 mb-3" />
                        <p className="text-slate-500">Aucun chapitre trouvé</p>
                    </div>
                ) : (
                    <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 stagger-children">
                        {filteredChapters.map((chapter) => {
                            const Icon = getIcon(chapter.icon);
                            const isCompleted = isChapterCompleted(chapter.id);
                            
                            return (
                                <Link 
                                    key={chapter.id} 
                                    to={`/chapitre/${chapter.id}`}
                                    className="group"
                                    data-testid={`chapter-card-${chapter.id}`}
                                >
                                    <div className={`bg-white border rounded-xl p-6 h-full transition-all duration-200 hover:shadow-lg hover:border-red-200 hover:-translate-y-1 ${isCompleted ? 'border-green-200 bg-green-50/30' : 'border-slate-200'}`}>
                                        <div className="flex items-start justify-between mb-4">
                                            <div className={`w-12 h-12 rounded-xl flex items-center justify-center transition-colors ${isCompleted ? 'bg-green-100 text-green-600' : 'bg-red-100 text-red-600 group-hover:bg-red-600 group-hover:text-white'}`}>
                                                <Icon className="w-6 h-6" />
                                            </div>
                                            {isCompleted && (
                                                <span className="px-2 py-1 bg-green-100 text-green-700 text-xs font-medium rounded-full">
                                                    Complété
                                                </span>
                                            )}
                                        </div>
                                        
                                        <div className="mb-2">
                                            <span className="text-xs font-medium text-slate-400 uppercase tracking-wider">
                                                Chapitre {chapter.numero}
                                            </span>
                                        </div>
                                        
                                        <h3 className="text-lg font-semibold text-slate-900 mb-2 group-hover:text-red-600 transition-colors">
                                            {chapter.titre}
                                        </h3>
                                        
                                        <p className="text-sm text-slate-600 mb-4 line-clamp-2">
                                            {chapter.description}
                                        </p>
                                        
                                        <div className="flex items-center justify-between pt-4 border-t border-slate-100">
                                            <div className="flex items-center gap-2 text-sm text-slate-500">
                                                <BookOpen className="w-4 h-4" />
                                                <span>{chapter.fiches?.length || 0} fiches</span>
                                            </div>
                                            <ArrowRight className="w-5 h-5 text-slate-400 group-hover:text-red-600 group-hover:translate-x-1 transition-all" />
                                        </div>
                                    </div>
                                </Link>
                            );
                        })}
                    </div>
                )}

                {/* Info Banner */}
                {!user && (
                    <div className="mt-12 bg-slate-900 rounded-2xl p-8 text-center" data-testid="cta-banner">
                        <h3 className="text-xl font-semibold text-white mb-2">
                            Créez un compte pour suivre votre progression
                        </h3>
                        <p className="text-slate-400 mb-6">
                            Accédez aux quiz et suivez votre avancement dans la formation
                        </p>
                        <Link to="/register">
                            <Button className="bg-red-600 hover:bg-red-700">
                                S'inscrire gratuitement
                                <ArrowRight className="w-4 h-4 ml-2" />
                            </Button>
                        </Link>
                    </div>
                )}
            </div>
        </Layout>
    );
};

export default Chapters;
