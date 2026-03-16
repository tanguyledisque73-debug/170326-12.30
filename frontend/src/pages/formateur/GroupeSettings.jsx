import React, { useState, useEffect } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import { 
    ArrowLeft,
    Save,
    GripVertical,
    CheckCircle2,
    Settings,
    BookOpen,
    Percent,
    ListOrdered,
    Info,
    Award
} from 'lucide-react';
import { Button } from '../../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from '../../components/ui/card';
import { Input } from '../../components/ui/input';
import { Label } from '../../components/ui/label';
import { Switch } from '../../components/ui/switch';
import Layout from '../../components/Layout';
import { formateurGetGroupeDetail, formateurUpdateGroupe, getChapters, getUser, getCertificateConfig, setCertificateConfig } from '../../lib/api';
import { toast } from 'sonner';

const FormateurGroupeSettings = () => {
    const { groupeId } = useParams();
    const navigate = useNavigate();
    const user = getUser();
    
    const [loading, setLoading] = useState(true);
    const [saving, setSaving] = useState(false);
    const [groupe, setGroupe] = useState(null);
    const [availableChapters, setAvailableChapters] = useState([]);
    
    // Form state
    const [nom, setNom] = useState('');
    const [seuilReussite, setSeuilReussite] = useState(80);
    const [chapitresOrdre, setChapitresOrdre] = useState([]);
    const [isActive, setIsActive] = useState(true);
    const [chapitresObligatoires, setChapitresObligatoires] = useState([]);
    
    // Drag and drop
    const [draggedItem, setDraggedItem] = useState(null);

    useEffect(() => {
        if (!user || user.role !== 'formateur') {
            navigate('/login');
            return;
        }
        loadData();
    }, [groupeId]);

    const loadData = async () => {
        try {
            const [groupeData, chaptersData] = await Promise.all([
                formateurGetGroupeDetail(groupeId),
                getChapters(groupeData?.groupe?.formation_type || 'PSE')
            ]);
            
            setGroupe(groupeData.groupe);
            setNom(groupeData.groupe.nom);
            setSeuilReussite(groupeData.groupe.seuil_reussite);
            setChapitresOrdre(groupeData.groupe.chapitres_ordre || []);
            setIsActive(groupeData.groupe.is_active);
            
            // Fetch chapters for the formation type
            const chapters = await getChapters(groupeData.groupe.formation_type);
            setAvailableChapters(chapters);
            
            // Fetch certificate config
            try {
                const certConfig = await getCertificateConfig(groupeId);
                setChapitresObligatoires(certConfig.chapitres_obligatoires || groupeData.groupe.chapitres_ordre || []);
            } catch {
                setChapitresObligatoires(groupeData.groupe.chapitres_ordre || []);
            }
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors du chargement');
            navigate('/formateur');
        } finally {
            setLoading(false);
        }
    };

    const handleSave = async () => {
        if (seuilReussite < 80 || seuilReussite > 100) {
            toast.error('Le seuil de réussite doit être entre 80% et 100%');
            return;
        }

        setSaving(true);
        try {
            await Promise.all([
                formateurUpdateGroupe(groupeId, {
                    nom,
                    seuil_reussite: seuilReussite,
                    chapitres_ordre: chapitresOrdre,
                    is_active: isActive
                }),
                setCertificateConfig(groupeId, chapitresObligatoires)
            ]);
            toast.success('Paramètres enregistrés avec succès !');
            navigate(`/formateur/groupe/${groupeId}`);
        } catch (error) {
            console.error('Erreur:', error);
            toast.error(error.response?.data?.detail || 'Erreur lors de la sauvegarde');
        } finally {
            setSaving(false);
        }
    };

    const toggleChapter = (chapterId) => {
        if (chapitresOrdre.includes(chapterId)) {
            setChapitresOrdre(chapitresOrdre.filter(id => id !== chapterId));
            // Also remove from obligatoires if removed from ordre
            setChapitresObligatoires(chapitresObligatoires.filter(id => id !== chapterId));
        } else {
            setChapitresOrdre([...chapitresOrdre, chapterId]);
        }
    };

    const toggleObligatoire = (chapterId) => {
        if (chapitresObligatoires.includes(chapterId)) {
            setChapitresObligatoires(chapitresObligatoires.filter(id => id !== chapterId));
        } else {
            setChapitresObligatoires([...chapitresObligatoires, chapterId]);
        }
    };

    const handleDragStart = (e, index) => {
        setDraggedItem(index);
        e.dataTransfer.effectAllowed = 'move';
    };

    const handleDragOver = (e, index) => {
        e.preventDefault();
        if (draggedItem === null || draggedItem === index) return;
        
        const newOrder = [...chapitresOrdre];
        const item = newOrder[draggedItem];
        newOrder.splice(draggedItem, 1);
        newOrder.splice(index, 0, item);
        
        setChapitresOrdre(newOrder);
        setDraggedItem(index);
    };

    const handleDragEnd = () => {
        setDraggedItem(null);
    };

    const getChapterInfo = (chapterId) => {
        return availableChapters.find(ch => ch.id === chapterId);
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

    if (!groupe) {
        return (
            <Layout>
                <div className="max-w-7xl mx-auto px-4 py-8 text-center">
                    <p className="text-slate-600">Groupe non trouvé</p>
                    <Link to="/formateur" className="mt-4 inline-block">
                        <Button variant="outline">Retour</Button>
                    </Link>
                </div>
            </Layout>
        );
    }

    return (
        <Layout>
            <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8" data-testid="groupe-settings">
                {/* Back */}
                <Link 
                    to={`/formateur/groupe/${groupeId}`}
                    className="text-sm text-slate-600 hover:text-red-600 flex items-center gap-1 mb-6"
                >
                    <ArrowLeft className="w-4 h-4" />
                    Retour au groupe
                </Link>

                {/* Header */}
                <div className="mb-8">
                    <h1 className="text-3xl font-bold text-slate-900 flex items-center gap-3">
                        <Settings className="w-8 h-8 text-red-600" />
                        Paramètres du groupe
                    </h1>
                    <p className="text-slate-600 mt-2">
                        Configurez le taux de réussite et l'ordre de déblocage des chapitres pour <strong>{groupe.nom}</strong>
                    </p>
                </div>

                {/* Info Banner */}
                <Card className="mb-6 bg-blue-50 border-blue-200">
                    <CardContent className="p-4 flex items-start gap-3">
                        <Info className="w-5 h-5 text-blue-600 flex-shrink-0 mt-0.5" />
                        <div className="text-sm text-blue-800">
                            <p className="font-medium mb-1">Comment fonctionne la progression ?</p>
                            <ul className="space-y-1 text-blue-700">
                                <li>• Le stagiaire doit obtenir au moins le <strong>seuil de réussite</strong> au quiz pour débloquer le chapitre suivant</li>
                                <li>• L'ordre des chapitres ci-dessous détermine la progression du stagiaire</li>
                                <li>• Vous pouvez réorganiser les chapitres par glisser-déposer</li>
                            </ul>
                        </div>
                    </CardContent>
                </Card>

                {/* General Settings */}
                <Card className="mb-6">
                    <CardHeader>
                        <CardTitle className="flex items-center gap-2">
                            <BookOpen className="w-5 h-5" />
                            Informations générales
                        </CardTitle>
                    </CardHeader>
                    <CardContent className="space-y-4">
                        <div className="grid md:grid-cols-2 gap-4">
                            <div className="space-y-2">
                                <Label htmlFor="nom">Nom du groupe</Label>
                                <Input
                                    id="nom"
                                    value={nom}
                                    onChange={(e) => setNom(e.target.value)}
                                    placeholder="Ex: Formation PSE Janvier 2025"
                                />
                            </div>
                            <div className="space-y-2">
                                <Label>Type de formation</Label>
                                <Input 
                                    value={groupe.formation_type} 
                                    disabled 
                                    className="bg-slate-100"
                                />
                            </div>
                        </div>
                        
                        <div className="flex items-center justify-between p-4 bg-slate-50 rounded-lg">
                            <div>
                                <p className="font-medium text-slate-900">Groupe actif</p>
                                <p className="text-sm text-slate-500">
                                    Un groupe inactif n'accepte plus de nouvelles inscriptions
                                </p>
                            </div>
                            <Switch
                                checked={isActive}
                                onCheckedChange={setIsActive}
                            />
                        </div>
                    </CardContent>
                </Card>

                {/* Seuil de réussite */}
                <Card className="mb-6">
                    <CardHeader>
                        <CardTitle className="flex items-center gap-2">
                            <Percent className="w-5 h-5" />
                            Seuil de réussite
                        </CardTitle>
                        <CardDescription>
                            Score minimum requis pour valider un chapitre et débloquer le suivant
                        </CardDescription>
                    </CardHeader>
                    <CardContent>
                        <div className="flex items-center gap-4">
                            <Input
                                type="number"
                                min="80"
                                max="100"
                                value={seuilReussite}
                                onChange={(e) => setSeuilReussite(parseInt(e.target.value) || 80)}
                                className="w-24 text-center text-lg font-bold"
                            />
                            <span className="text-2xl font-bold text-slate-600">%</span>
                            <div className="flex-1">
                                <input
                                    type="range"
                                    min="80"
                                    max="100"
                                    value={seuilReussite}
                                    onChange={(e) => setSeuilReussite(parseInt(e.target.value))}
                                    className="w-full h-2 bg-slate-200 rounded-lg appearance-none cursor-pointer accent-red-600"
                                />
                                <div className="flex justify-between text-xs text-slate-500 mt-1">
                                    <span>80% (minimum)</span>
                                    <span>100%</span>
                                </div>
                            </div>
                        </div>
                    </CardContent>
                </Card>

                {/* Ordre des chapitres */}
                <Card className="mb-6">
                    <CardHeader>
                        <CardTitle className="flex items-center gap-2">
                            <ListOrdered className="w-5 h-5" />
                            Ordre des chapitres ({chapitresOrdre.length} sélectionnés)
                        </CardTitle>
                        <CardDescription>
                            Sélectionnez et ordonnez les chapitres de la formation. Glissez-déposez pour réorganiser.
                        </CardDescription>
                    </CardHeader>
                    <CardContent>
                        {/* Selected chapters (draggable) */}
                        {chapitresOrdre.length > 0 && (
                            <div className="mb-6">
                                <p className="text-sm font-medium text-slate-700 mb-3">Chapitres sélectionnés (dans l'ordre)</p>
                                <div className="space-y-2">
                                    {chapitresOrdre.map((chapterId, index) => {
                                        const chapter = getChapterInfo(chapterId);
                                        if (!chapter) return null;
                                        
                                        return (
                                            <div
                                                key={chapterId}
                                                draggable
                                                onDragStart={(e) => handleDragStart(e, index)}
                                                onDragOver={(e) => handleDragOver(e, index)}
                                                onDragEnd={handleDragEnd}
                                                className={`flex items-center gap-3 p-3 bg-green-50 border border-green-200 rounded-lg cursor-move transition-all ${
                                                    draggedItem === index ? 'opacity-50 scale-95' : ''
                                                }`}
                                            >
                                                <GripVertical className="w-5 h-5 text-slate-400" />
                                                <span className="w-8 h-8 bg-red-600 text-white rounded-full flex items-center justify-center text-sm font-bold">
                                                    {index + 1}
                                                </span>
                                                <div className="flex-1">
                                                    <p className="font-medium text-slate-900">{chapter.titre}</p>
                                                    <p className="text-xs text-slate-500">Chapitre {chapter.numero}</p>
                                                </div>
                                                <Button
                                                    type="button"
                                                    variant="ghost"
                                                    size="sm"
                                                    onClick={() => toggleChapter(chapterId)}
                                                    className="text-red-600 hover:text-red-700"
                                                >
                                                    Retirer
                                                </Button>
                                            </div>
                                        );
                                    })}
                                </div>
                            </div>
                        )}

                        {/* Available chapters */}
                        <div>
                            <p className="text-sm font-medium text-slate-700 mb-3">Chapitres disponibles</p>
                            <div className="space-y-2">
                                {availableChapters
                                    .filter(ch => !chapitresOrdre.includes(ch.id))
                                    .map((chapter) => (
                                        <div
                                            key={chapter.id}
                                            className="flex items-center gap-3 p-3 bg-slate-50 border border-slate-200 rounded-lg hover:bg-slate-100 transition-colors"
                                        >
                                            <span className="w-8 h-8 bg-slate-300 text-slate-700 rounded-full flex items-center justify-center text-sm font-bold">
                                                {chapter.numero}
                                            </span>
                                            <div className="flex-1">
                                                <p className="font-medium text-slate-900">{chapter.titre}</p>
                                                <p className="text-xs text-slate-500">{chapter.fiches?.length || 0} fiches</p>
                                            </div>
                                            <Button
                                                type="button"
                                                variant="outline"
                                                size="sm"
                                                onClick={() => toggleChapter(chapter.id)}
                                                className="text-green-600 hover:text-green-700 hover:border-green-600"
                                            >
                                                <CheckCircle2 className="w-4 h-4 mr-1" />
                                                Ajouter
                                            </Button>
                                        </div>
                                    ))
                                }
                                {availableChapters.filter(ch => !chapitresOrdre.includes(ch.id)).length === 0 && (
                                    <p className="text-sm text-slate-500 text-center py-4">
                                        Tous les chapitres sont sélectionnés
                                    </p>
                                )}
                            </div>
                        </div>
                    </CardContent>
                </Card>

                {/* Chapitres obligatoires pour le certificat */}
                <Card className="mb-6">
                    <CardHeader>
                        <CardTitle className="flex items-center gap-2">
                            <Award className="w-5 h-5 text-yellow-500" />
                            Chapitres obligatoires pour le certificat ({chapitresObligatoires.length} sélectionnés)
                        </CardTitle>
                        <CardDescription>
                            Sélectionnez les chapitres que les stagiaires doivent valider pour obtenir leur certificat FOAD {groupe?.formation_type} 1.
                        </CardDescription>
                    </CardHeader>
                    <CardContent>
                        {chapitresOrdre.length === 0 ? (
                            <p className="text-sm text-slate-500 text-center py-4">
                                Sélectionnez d'abord des chapitres ci-dessus
                            </p>
                        ) : (
                            <div className="space-y-2">
                                {chapitresOrdre.map((chapterId) => {
                                    const chapter = getChapterInfo(chapterId);
                                    if (!chapter) return null;
                                    const isObligatoire = chapitresObligatoires.includes(chapterId);
                                    
                                    return (
                                        <div
                                            key={chapterId}
                                            className={`flex items-center justify-between p-3 rounded-lg border transition-colors cursor-pointer ${
                                                isObligatoire 
                                                    ? 'bg-yellow-50 border-yellow-300' 
                                                    : 'bg-slate-50 border-slate-200 hover:bg-slate-100'
                                            }`}
                                            onClick={() => toggleObligatoire(chapterId)}
                                        >
                                            <div className="flex items-center gap-3">
                                                <div className={`w-6 h-6 rounded-full flex items-center justify-center ${
                                                    isObligatoire 
                                                        ? 'bg-yellow-500 text-white' 
                                                        : 'bg-slate-200 text-slate-400'
                                                }`}>
                                                    {isObligatoire && <CheckCircle2 className="w-4 h-4" />}
                                                </div>
                                                <div>
                                                    <p className="font-medium text-slate-900">{chapter.titre}</p>
                                                    <p className="text-xs text-slate-500">Chapitre {chapter.numero}</p>
                                                </div>
                                            </div>
                                            <span className={`text-xs font-medium px-2 py-1 rounded ${
                                                isObligatoire 
                                                    ? 'bg-yellow-200 text-yellow-800' 
                                                    : 'bg-slate-200 text-slate-600'
                                            }`}>
                                                {isObligatoire ? 'Obligatoire' : 'Optionnel'}
                                            </span>
                                        </div>
                                    );
                                })}
                            </div>
                        )}
                        
                        {chapitresObligatoires.length > 0 && (
                            <div className="mt-4 p-3 bg-green-50 rounded-lg border border-green-200">
                                <p className="text-sm text-green-800">
                                    <strong>Info:</strong> Les stagiaires devront valider {chapitresObligatoires.length} chapitre(s) pour obtenir leur "Certificat de validation de la FOAD {groupe?.formation_type} 1".
                                </p>
                            </div>
                        )}
                    </CardContent>
                </Card>

                {/* Actions */}
                <div className="flex items-center justify-between">
                    <Link to={`/formateur/groupe/${groupeId}`}>
                        <Button variant="outline">Annuler</Button>
                    </Link>
                    <Button 
                        onClick={handleSave}
                        disabled={saving || chapitresOrdre.length === 0}
                        className="bg-red-600 hover:bg-red-700"
                    >
                        {saving ? (
                            <div className="spinner w-5 h-5 border-2 border-white/30 border-t-white"></div>
                        ) : (
                            <>
                                <Save className="w-4 h-4 mr-2" />
                                Enregistrer les paramètres
                            </>
                        )}
                    </Button>
                </div>
            </div>
        </Layout>
    );
};

export default FormateurGroupeSettings;
