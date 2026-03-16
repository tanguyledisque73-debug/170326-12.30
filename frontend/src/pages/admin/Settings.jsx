import React, { useState, useEffect } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { 
    ArrowLeft,
    Settings,
    Image,
    Link as LinkIcon,
    Plus,
    Trash2,
    Save,
    ExternalLink,
    Eye,
    Pencil
} from 'lucide-react';
import { Button } from '../../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/card';
import { Input } from '../../components/ui/input';
import { Label } from '../../components/ui/label';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../components/ui/select';
import { Switch } from '../../components/ui/switch';
import Layout from '../../components/Layout';
import { 
    getUser, 
    getSiteSettings, 
    updateSiteSettings, 
    getSiteImages, 
    createSiteImage, 
    updateSiteImage, 
    deleteSiteImage 
} from '../../lib/api';
import { toast } from 'sonner';

const AdminSettings = () => {
    const navigate = useNavigate();
    const user = getUser();
    const [loading, setLoading] = useState(true);
    const [saving, setSaving] = useState(false);
    
    // HelloAsso settings
    const [helloassoUrl, setHelloassoUrl] = useState('');
    const [helloassoEnabled, setHelloassoEnabled] = useState(false);
    
    // Images
    const [images, setImages] = useState([]);
    const [showAddImage, setShowAddImage] = useState(false);
    const [editingImage, setEditingImage] = useState(null);
    const [imageForm, setImageForm] = useState({
        name: '',
        url: '',
        alt_text: '',
        section: 'hero',
        order: 0
    });

    useEffect(() => {
        if (!user || user.role !== 'admin') {
            navigate('/login');
            return;
        }
        loadData();
    }, []);

    const loadData = async () => {
        try {
            const [settings, imagesData] = await Promise.all([
                getSiteSettings(),
                getSiteImages()
            ]);
            setHelloassoUrl(settings.helloasso_url || '');
            setHelloassoEnabled(settings.helloasso_enabled || false);
            setImages(imagesData || []);
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors du chargement');
        } finally {
            setLoading(false);
        }
    };

    const handleSaveSettings = async () => {
        setSaving(true);
        try {
            await updateSiteSettings({
                helloasso_url: helloassoUrl,
                helloasso_enabled: helloassoEnabled
            });
            toast.success('Paramètres enregistrés');
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors de l\'enregistrement');
        } finally {
            setSaving(false);
        }
    };

    const handleAddImage = async (e) => {
        e.preventDefault();
        try {
            await createSiteImage(imageForm);
            toast.success('Image ajoutée');
            setShowAddImage(false);
            setImageForm({ name: '', url: '', alt_text: '', section: 'hero', order: 0 });
            loadData();
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors de l\'ajout');
        }
    };

    const handleUpdateImage = async (e) => {
        e.preventDefault();
        try {
            await updateSiteImage(editingImage.id, imageForm);
            toast.success('Image mise à jour');
            setEditingImage(null);
            setImageForm({ name: '', url: '', alt_text: '', section: 'hero', order: 0 });
            loadData();
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors de la mise à jour');
        }
    };

    const handleDeleteImage = async (imageId) => {
        if (!confirm('Supprimer cette image ?')) return;
        try {
            await deleteSiteImage(imageId);
            toast.success('Image supprimée');
            loadData();
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors de la suppression');
        }
    };

    const startEditImage = (image) => {
        setEditingImage(image);
        setImageForm({
            name: image.name,
            url: image.url,
            alt_text: image.alt_text,
            section: image.section,
            order: image.order
        });
        setShowAddImage(false);
    };

    const sectionOptions = [
        { value: 'hero', label: 'Page d\'accueil (Hero)' },
        { value: 'pse', label: 'Page PSE' },
        { value: 'bnssa', label: 'Page BNSSA' },
        { value: 'psc', label: 'Page PSC' },
        { value: 'about', label: 'À propos' }
    ];

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
            <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8" data-testid="admin-settings">
                {/* Back */}
                <Link 
                    to="/admin"
                    className="text-sm text-slate-600 hover:text-red-600 flex items-center gap-1 mb-6"
                >
                    <ArrowLeft className="w-4 h-4" />
                    Retour au tableau de bord
                </Link>

                <h1 className="text-3xl font-bold text-slate-900 mb-8">
                    Paramètres du site
                </h1>

                {/* HelloAsso Settings */}
                <Card className="mb-8" data-testid="helloasso-settings">
                    <CardHeader>
                        <CardTitle className="flex items-center gap-2">
                            <LinkIcon className="w-5 h-5" />
                            Lien HelloAsso - Nous soutenir
                        </CardTitle>
                    </CardHeader>
                    <CardContent className="space-y-4">
                        <div className="flex items-center justify-between p-4 bg-slate-50 rounded-lg">
                            <div>
                                <Label htmlFor="helloasso-enabled" className="font-medium">
                                    Activer le bouton "Faire un don"
                                </Label>
                                <p className="text-sm text-slate-500">
                                    Affiche le bouton de don sur la page d'accueil
                                </p>
                            </div>
                            <Switch
                                id="helloasso-enabled"
                                checked={helloassoEnabled}
                                onCheckedChange={setHelloassoEnabled}
                            />
                        </div>
                        
                        <div className="space-y-2">
                            <Label htmlFor="helloasso-url">URL HelloAsso</Label>
                            <Input
                                id="helloasso-url"
                                placeholder="https://www.helloasso.com/associations/..."
                                value={helloassoUrl}
                                onChange={(e) => setHelloassoUrl(e.target.value)}
                            />
                            <p className="text-xs text-slate-500">
                                Collez ici le lien de votre page de collecte HelloAsso
                            </p>
                        </div>

                        {helloassoUrl && (
                            <a 
                                href={helloassoUrl} 
                                target="_blank" 
                                rel="noopener noreferrer"
                                className="text-sm text-red-600 hover:text-red-700 flex items-center gap-1"
                            >
                                <Eye className="w-4 h-4" />
                                Prévisualiser le lien
                                <ExternalLink className="w-3 h-3" />
                            </a>
                        )}

                        <Button 
                            onClick={handleSaveSettings} 
                            className="bg-red-600 hover:bg-red-700"
                            disabled={saving}
                        >
                            {saving ? (
                                <div className="spinner w-5 h-5 border-2 border-white/30 border-t-white"></div>
                            ) : (
                                <>
                                    <Save className="w-4 h-4 mr-2" />
                                    Enregistrer
                                </>
                            )}
                        </Button>
                    </CardContent>
                </Card>

                {/* Images Management */}
                <Card data-testid="images-settings">
                    <CardHeader className="flex flex-row items-center justify-between">
                        <CardTitle className="flex items-center gap-2">
                            <Image className="w-5 h-5" />
                            Images de présentation
                        </CardTitle>
                        <Button 
                            variant="outline" 
                            size="sm"
                            onClick={() => {
                                setShowAddImage(true);
                                setEditingImage(null);
                                setImageForm({ name: '', url: '', alt_text: '', section: 'hero', order: 0 });
                            }}
                        >
                            <Plus className="w-4 h-4 mr-2" />
                            Ajouter une image
                        </Button>
                    </CardHeader>
                    <CardContent>
                        {/* Add/Edit Form */}
                        {(showAddImage || editingImage) && (
                            <form 
                                onSubmit={editingImage ? handleUpdateImage : handleAddImage}
                                className="p-4 bg-slate-50 rounded-lg mb-6 space-y-4"
                            >
                                <h3 className="font-medium text-slate-900">
                                    {editingImage ? 'Modifier l\'image' : 'Ajouter une image'}
                                </h3>
                                
                                <div className="grid md:grid-cols-2 gap-4">
                                    <div className="space-y-2">
                                        <Label htmlFor="img-name">Nom</Label>
                                        <Input
                                            id="img-name"
                                            placeholder="Ex: Hero principal"
                                            value={imageForm.name}
                                            onChange={(e) => setImageForm({...imageForm, name: e.target.value})}
                                            required
                                        />
                                    </div>
                                    <div className="space-y-2">
                                        <Label htmlFor="img-section">Section</Label>
                                        <Select 
                                            value={imageForm.section}
                                            onValueChange={(value) => setImageForm({...imageForm, section: value})}
                                        >
                                            <SelectTrigger>
                                                <SelectValue />
                                            </SelectTrigger>
                                            <SelectContent>
                                                {sectionOptions.map(opt => (
                                                    <SelectItem key={opt.value} value={opt.value}>
                                                        {opt.label}
                                                    </SelectItem>
                                                ))}
                                            </SelectContent>
                                        </Select>
                                    </div>
                                </div>
                                
                                <div className="space-y-2">
                                    <Label htmlFor="img-url">URL de l'image</Label>
                                    <Input
                                        id="img-url"
                                        placeholder="https://..."
                                        value={imageForm.url}
                                        onChange={(e) => setImageForm({...imageForm, url: e.target.value})}
                                        required
                                    />
                                    <p className="text-xs text-slate-500">
                                        Utilisez un hébergeur d'images (Unsplash, Imgur, etc.) ou votre propre serveur
                                    </p>
                                </div>
                                
                                <div className="grid md:grid-cols-2 gap-4">
                                    <div className="space-y-2">
                                        <Label htmlFor="img-alt">Texte alternatif</Label>
                                        <Input
                                            id="img-alt"
                                            placeholder="Description de l'image"
                                            value={imageForm.alt_text}
                                            onChange={(e) => setImageForm({...imageForm, alt_text: e.target.value})}
                                            required
                                        />
                                    </div>
                                    <div className="space-y-2">
                                        <Label htmlFor="img-order">Ordre d'affichage</Label>
                                        <Input
                                            id="img-order"
                                            type="number"
                                            min="0"
                                            value={imageForm.order}
                                            onChange={(e) => setImageForm({...imageForm, order: parseInt(e.target.value)})}
                                        />
                                    </div>
                                </div>

                                {imageForm.url && (
                                    <div className="border rounded-lg p-2 bg-white">
                                        <p className="text-xs text-slate-500 mb-2">Aperçu:</p>
                                        <img 
                                            src={imageForm.url} 
                                            alt={imageForm.alt_text || 'Aperçu'}
                                            className="max-h-32 rounded object-cover"
                                            onError={(e) => e.target.style.display = 'none'}
                                        />
                                    </div>
                                )}

                                <div className="flex gap-2">
                                    <Button type="submit" className="bg-red-600 hover:bg-red-700">
                                        {editingImage ? 'Mettre à jour' : 'Ajouter'}
                                    </Button>
                                    <Button 
                                        type="button" 
                                        variant="outline"
                                        onClick={() => {
                                            setShowAddImage(false);
                                            setEditingImage(null);
                                        }}
                                    >
                                        Annuler
                                    </Button>
                                </div>
                            </form>
                        )}

                        {/* Images List */}
                        {images.length === 0 ? (
                            <div className="text-center py-8">
                                <Image className="w-12 h-12 mx-auto text-slate-300 mb-3" />
                                <p className="text-slate-500">Aucune image ajoutée</p>
                            </div>
                        ) : (
                            <div className="space-y-3">
                                {images.map((image) => (
                                    <div 
                                        key={image.id}
                                        className="flex items-center gap-4 p-3 bg-slate-50 rounded-lg"
                                    >
                                        <img 
                                            src={image.url} 
                                            alt={image.alt_text}
                                            className="w-16 h-16 rounded object-cover flex-shrink-0"
                                            onError={(e) => e.target.src = 'https://via.placeholder.com/64?text=Erreur'}
                                        />
                                        <div className="flex-1 min-w-0">
                                            <p className="font-medium text-slate-900 truncate">{image.name}</p>
                                            <p className="text-sm text-slate-500">
                                                Section: {sectionOptions.find(o => o.value === image.section)?.label || image.section}
                                            </p>
                                        </div>
                                        <div className="flex items-center gap-2">
                                            <Button 
                                                variant="ghost" 
                                                size="sm"
                                                onClick={() => startEditImage(image)}
                                            >
                                                <Pencil className="w-4 h-4" />
                                            </Button>
                                            <Button 
                                                variant="ghost" 
                                                size="sm"
                                                className="text-red-600 hover:text-red-700 hover:bg-red-50"
                                                onClick={() => handleDeleteImage(image.id)}
                                            >
                                                <Trash2 className="w-4 h-4" />
                                            </Button>
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

export default AdminSettings;
