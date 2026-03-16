import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { 
    FolderPlus, 
    Users,
    Copy,
    Settings,
    Plus,
    GripVertical,
    ChevronUp,
    ChevronDown,
    Check,
    X
} from 'lucide-react';
import { Button } from '../../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/card';
import { Input } from '../../components/ui/input';
import { Label } from '../../components/ui/label';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../components/ui/select';
import { Checkbox } from '../../components/ui/checkbox';
import Layout from '../../components/Layout';
import { formateurGetGroupes, formateurCreateGroupe, getChapters, getUser } from '../../lib/api';
import { toast } from 'sonner';

const FormateurGroupes = () => {
    const navigate = useNavigate();
    const user = getUser();
    const [loading, setLoading] = useState(true);
    const [groupes, setGroupes] = useState([]);
    const [chapters, setChapters] = useState([]);
    const [showCreate, setShowCreate] = useState(false);
    const [creating, setCreating] = useState(false);
    const [formData, setFormData] = useState({
        nom: '',
        formation_type: 'PSE',
        seuil_reussite: 80,
        chapitres_ordre: []
    });
    const [selectedChapters, setSelectedChapters] = useState([]);

    useEffect(() => {
        if (!user || user.role !== 'formateur') {
            navigate('/login');
            return;
        }
        loadData();
    }, []);

    const loadData = async () => {
        try {
            const [groupesData, chaptersData] = await Promise.all([
                formateurGetGroupes(),
                getChapters('PSE')
            ]);
            setGroupes(groupesData);
            setChapters(chaptersData);
            // Set default: all chapters selected in order
            const defaultSelected = chaptersData.map(c => ({ ...c, selected: true }));
            setSelectedChapters(defaultSelected);
            setFormData(prev => ({
                ...prev,
                chapitres_ordre: chaptersData.map(c => c.id)
            }));
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors du chargement');
        } finally {
            setLoading(false);
        }
    };

    const loadChaptersForType = async (formationType) => {
        try {
            const chaptersData = await getChapters(formationType);
            setChapters(chaptersData);
            const defaultSelected = chaptersData.map(c => ({ ...c, selected: true }));
            setSelectedChapters(defaultSelected);
            setFormData(prev => ({
                ...prev,
                formation_type: formationType,
                chapitres_ordre: chaptersData.map(c => c.id)
            }));
        } catch (error) {
            console.error('Erreur:', error);
        }
    };

    const toggleChapterSelection = (chapterId) => {
        setSelectedChapters(prev => 
            prev.map(c => c.id === chapterId ? { ...c, selected: !c.selected } : c)
        );
    };

    const moveChapter = (index, direction) => {
        const newOrder = [...selectedChapters];
        const newIndex = direction === 'up' ? index - 1 : index + 1;
        if (newIndex < 0 || newIndex >= newOrder.length) return;
        [newOrder[index], newOrder[newIndex]] = [newOrder[newIndex], newOrder[index]];
        setSelectedChapters(newOrder);
    };

    const selectAllChapters = () => {
        setSelectedChapters(prev => prev.map(c => ({ ...c, selected: true })));
    };

    const deselectAllChapters = () => {
        setSelectedChapters(prev => prev.map(c => ({ ...c, selected: false })));
    };

    const handleCreate = async (e) => {
        e.preventDefault();
        
        const selectedIds = selectedChapters.filter(c => c.selected).map(c => c.id);
        if (selectedIds.length === 0) {
            toast.error('Sélectionnez au moins un chapitre');
            return;
        }
        
        setCreating(true);
        try {
            const result = await formateurCreateGroupe({
                ...formData,
                chapitres_ordre: selectedIds
            });
            toast.success(`Groupe créé ! Code: ${result.groupe.code_acces}`);
            setShowCreate(false);
            loadData();
            setFormData({
                nom: '',
                formation_type: 'PSE',
                seuil_reussite: 80,
                chapitres_ordre: chapters.map(c => c.id)
            });
        } catch (error) {
            console.error('Erreur:', error);
            toast.error(error.response?.data?.detail || 'Erreur lors de la création');
        } finally {
            setCreating(false);
        }
    };

    const copyCode = (code) => {
        navigator.clipboard.writeText(code);
        toast.success('Code copié !');
    };

    const selectedCount = selectedChapters.filter(c => c.selected).length;

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
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8" data-testid="formateur-groupes">
                {/* Header */}
                <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4 mb-8">
                    <div>
                        <h1 className="text-3xl font-bold text-slate-900 mb-2">
                            Groupes de formation
                        </h1>
                        <p className="text-slate-600">
                            Créez et gérez vos groupes de stagiaires.
                        </p>
                    </div>
                    <Button 
                        className="bg-red-600 hover:bg-red-700"
                        onClick={() => setShowCreate(true)}
                    >
                        <Plus className="w-4 h-4 mr-2" />
                        Nouveau groupe
                    </Button>
                </div>

                {/* Create Form */}
                {showCreate && (
                    <Card className="mb-8 animate-fade-in" data-testid="create-groupe-form">
                        <CardHeader>
                            <CardTitle>Créer un nouveau groupe</CardTitle>
                        </CardHeader>
                        <CardContent>
                            <form onSubmit={handleCreate} className="space-y-6">
                                <div className="grid md:grid-cols-2 gap-4">
                                    <div className="space-y-2">
                                        <Label htmlFor="nom">Nom du groupe</Label>
                                        <Input
                                            id="nom"
                                            placeholder="Ex: PSE1 - Session Janvier 2026"
                                            value={formData.nom}
                                            onChange={(e) => setFormData({...formData, nom: e.target.value})}
                                            required
                                        />
                                    </div>
                                    <div className="space-y-2">
                                        <Label htmlFor="formation_type">Type de formation</Label>
                                        <Select 
                                            value={formData.formation_type}
                                            onValueChange={(value) => loadChaptersForType(value)}
                                        >
                                            <SelectTrigger>
                                                <SelectValue />
                                            </SelectTrigger>
                                            <SelectContent>
                                                <SelectItem value="PSE">PSE - Premiers Secours en Équipe</SelectItem>
                                                <SelectItem value="BNSSA">BNSSA - Sauvetage Aquatique</SelectItem>
                                            </SelectContent>
                                        </Select>
                                    </div>
                                </div>
                                
                                <div className="space-y-2">
                                    <Label htmlFor="seuil">Seuil de réussite (minimum 80%)</Label>
                                    <Input
                                        id="seuil"
                                        type="number"
                                        min={80}
                                        max={100}
                                        value={formData.seuil_reussite}
                                        onChange={(e) => setFormData({...formData, seuil_reussite: parseInt(e.target.value)})}
                                        required
                                    />
                                    <p className="text-xs text-slate-500">
                                        Score minimum pour valider un chapitre et débloquer le suivant
                                    </p>
                                </div>

                                {/* Chapter Selection and Ordering */}
                                <div className="space-y-3">
                                    <div className="flex items-center justify-between">
                                        <Label>Chapitres et ordre de progression ({selectedCount} sélectionnés)</Label>
                                        <div className="flex gap-2">
                                            <Button type="button" variant="outline" size="sm" onClick={selectAllChapters}>
                                                <Check className="w-3 h-3 mr-1" />
                                                Tout
                                            </Button>
                                            <Button type="button" variant="outline" size="sm" onClick={deselectAllChapters}>
                                                <X className="w-3 h-3 mr-1" />
                                                Aucun
                                            </Button>
                                        </div>
                                    </div>
                                    <p className="text-xs text-slate-500">
                                        Sélectionnez les chapitres à inclure et réorganisez l'ordre avec les flèches
                                    </p>
                                    
                                    <div className="border rounded-lg divide-y max-h-80 overflow-y-auto">
                                        {selectedChapters.map((chapter, index) => (
                                            <div 
                                                key={chapter.id}
                                                className={`flex items-center gap-3 p-3 ${
                                                    chapter.selected ? 'bg-white' : 'bg-slate-50 opacity-60'
                                                }`}
                                            >
                                                <div className="flex flex-col gap-0.5">
                                                    <button
                                                        type="button"
                                                        onClick={() => moveChapter(index, 'up')}
                                                        disabled={index === 0}
                                                        className="p-0.5 hover:bg-slate-200 rounded disabled:opacity-30"
                                                    >
                                                        <ChevronUp className="w-4 h-4" />
                                                    </button>
                                                    <button
                                                        type="button"
                                                        onClick={() => moveChapter(index, 'down')}
                                                        disabled={index === selectedChapters.length - 1}
                                                        className="p-0.5 hover:bg-slate-200 rounded disabled:opacity-30"
                                                    >
                                                        <ChevronDown className="w-4 h-4" />
                                                    </button>
                                                </div>
                                                
                                                <Checkbox
                                                    checked={chapter.selected}
                                                    onCheckedChange={() => toggleChapterSelection(chapter.id)}
                                                />
                                                
                                                <div className="flex-1">
                                                    <span className={`inline-flex items-center justify-center w-6 h-6 rounded-full text-xs font-medium mr-2 ${
                                                        chapter.selected ? 'bg-red-100 text-red-700' : 'bg-slate-200 text-slate-500'
                                                    }`}>
                                                        {index + 1}
                                                    </span>
                                                    <span className={chapter.selected ? 'text-slate-900' : 'text-slate-500'}>
                                                        {chapter.titre}
                                                    </span>
                                                </div>
                                            </div>
                                        ))}
                                    </div>
                                </div>

                                <div className="flex gap-3 pt-4">
                                    <Button type="submit" className="bg-red-600 hover:bg-red-700" disabled={creating || selectedCount === 0}>
                                        {creating ? <div className="spinner w-5 h-5 border-2 border-white/30 border-t-white"></div> : 'Créer le groupe'}
                                    </Button>
                                    <Button type="button" variant="outline" onClick={() => setShowCreate(false)}>
                                        Annuler
                                    </Button>
                                </div>
                            </form>
                        </CardContent>
                    </Card>
                )}

                {/* Groupes List */}
                {groupes.length === 0 ? (
                    <Card>
                        <CardContent className="py-12">
                            <div className="empty-state">
                                <FolderPlus className="w-12 h-12 mx-auto text-slate-300 mb-3" />
                                <p className="text-slate-500 mb-4">Vous n'avez pas encore de groupe</p>
                                <Button 
                                    onClick={() => setShowCreate(true)}
                                    className="bg-red-600 hover:bg-red-700"
                                >
                                    Créer mon premier groupe
                                </Button>
                            </div>
                        </CardContent>
                    </Card>
                ) : (
                    <div className="grid md:grid-cols-2 gap-6">
                        {groupes.map((groupe) => (
                            <Card key={groupe.id} className="card-hover" data-testid={`groupe-card-${groupe.id}`}>
                                <CardContent className="p-6">
                                    <div className="flex items-start justify-between mb-4">
                                        <div>
                                            <div className="flex items-center gap-2 mb-1">
                                                <h3 className="font-semibold text-lg text-slate-900">{groupe.nom}</h3>
                                            </div>
                                            <div className="flex items-center gap-2">
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
                                                {!groupe.is_active && (
                                                    <span className="px-2 py-0.5 bg-slate-100 text-slate-500 rounded text-xs font-medium">
                                                        Inactif
                                                    </span>
                                                )}
                                            </div>
                                        </div>
                                    </div>
                                    
                                    <div className="space-y-3 mb-4">
                                        <div className="flex items-center justify-between p-3 bg-slate-50 rounded-lg">
                                            <span className="text-sm text-slate-600">Code d'accès</span>
                                            <button 
                                                onClick={() => copyCode(groupe.code_acces)}
                                                className="flex items-center gap-2 font-mono text-lg font-bold text-red-600 hover:text-red-700"
                                            >
                                                {groupe.code_acces}
                                                <Copy className="w-4 h-4" />
                                            </button>
                                        </div>
                                        
                                        <div className="grid grid-cols-2 gap-3">
                                            <div className="text-center p-3 bg-slate-50 rounded-lg">
                                                <p className="text-2xl font-bold text-slate-900">{groupe.nb_stagiaires || 0}</p>
                                                <p className="text-xs text-slate-500">/ {groupe.max_stagiaires} stagiaires</p>
                                            </div>
                                            <div className="text-center p-3 bg-slate-50 rounded-lg">
                                                <p className="text-2xl font-bold text-slate-900">{groupe.seuil_reussite}%</p>
                                                <p className="text-xs text-slate-500">Seuil requis</p>
                                            </div>
                                        </div>
                                    </div>
                                    
                                    <div className="flex gap-2">
                                        <Link to={`/formateur/groupe/${groupe.id}`} className="flex-1">
                                            <Button variant="outline" className="w-full">
                                                <Users className="w-4 h-4 mr-2" />
                                                Voir les stagiaires
                                            </Button>
                                        </Link>
                                        {groupe.formateur_id === user?.id && (
                                            <Link to={`/formateur/groupe/${groupe.id}`}>
                                                <Button variant="outline" size="icon">
                                                    <Settings className="w-4 h-4" />
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

export default FormateurGroupes;
