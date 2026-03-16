import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Heart, Eye, EyeOff, ArrowRight, UserPlus } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Input } from '../components/ui/input';
import { Label } from '../components/ui/label';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../components/ui/card';
import { registerVisiteur, setAuth } from '../lib/api';
import { toast } from 'sonner';

const RegisterVisiteur = () => {
    const navigate = useNavigate();
    const [loading, setLoading] = useState(false);
    const [showPassword, setShowPassword] = useState(false);
    const [formData, setFormData] = useState({
        email: '',
        password: '',
        nom: '',
        prenom: ''
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);

        try {
            const response = await registerVisiteur(formData);
            setAuth(response.token, response.user);
            toast.success('Compte créé ! Vous avez accès à un aperçu limité du contenu.');
            navigate('/visiteur');
        } catch (error) {
            console.error('Erreur:', error);
            toast.error(error.response?.data?.detail || 'Erreur lors de l\'inscription');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-slate-50 flex flex-col" data-testid="register-visiteur-page">
            {/* Header */}
            <header className="bg-white border-b border-slate-200 py-4">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <Link to="/" className="flex items-center gap-2 w-fit">
                        <div className="w-10 h-10 bg-red-600 rounded-lg flex items-center justify-center">
                            <Heart className="w-5 h-5 text-white" strokeWidth={2.5} />
                        </div>
                        <div>
                            <span className="font-bold text-lg text-slate-900">Secours</span>
                            <span className="font-bold text-lg text-red-600 ml-1">73</span>
                        </div>
                    </Link>
                </div>
            </header>

            {/* Main */}
            <main className="flex-1 flex items-center justify-center py-12 px-4">
                <Card className="w-full max-w-md shadow-lg animate-fade-in">
                    <CardHeader className="text-center pb-2">
                        <div className="w-14 h-14 bg-green-100 rounded-xl flex items-center justify-center mx-auto mb-4">
                            <UserPlus className="w-7 h-7 text-green-600" />
                        </div>
                        <CardTitle className="text-2xl">Compte Gratuit</CardTitle>
                        <CardDescription>
                            Accédez à un aperçu du contenu de formation
                        </CardDescription>
                    </CardHeader>
                    <CardContent>
                        {/* Info box */}
                        <div className="mb-6 p-4 bg-yellow-50 rounded-lg border border-yellow-200">
                            <p className="text-sm text-yellow-800">
                                <strong>Accès limité :</strong> Vous pourrez consulter un aperçu des chapitres PSE et accéder gratuitement au contenu PSC (Premiers Secours Citoyen).
                            </p>
                            <p className="text-sm text-yellow-700 mt-2">
                                Pour accéder aux quiz et à la formation complète, demandez un code groupe à votre formateur.
                            </p>
                        </div>

                        <form onSubmit={handleSubmit} className="space-y-4">
                            <div className="grid grid-cols-2 gap-4">
                                <div className="space-y-2">
                                    <Label htmlFor="prenom">Prénom</Label>
                                    <Input
                                        id="prenom"
                                        name="prenom"
                                        placeholder="Jean"
                                        value={formData.prenom}
                                        onChange={handleChange}
                                        required
                                        data-testid="input-prenom"
                                    />
                                </div>
                                <div className="space-y-2">
                                    <Label htmlFor="nom">Nom</Label>
                                    <Input
                                        id="nom"
                                        name="nom"
                                        placeholder="Dupont"
                                        value={formData.nom}
                                        onChange={handleChange}
                                        required
                                        data-testid="input-nom"
                                    />
                                </div>
                            </div>

                            <div className="space-y-2">
                                <Label htmlFor="email">Email</Label>
                                <Input
                                    id="email"
                                    name="email"
                                    type="email"
                                    placeholder="jean.dupont@example.com"
                                    value={formData.email}
                                    onChange={handleChange}
                                    required
                                    data-testid="input-email"
                                />
                            </div>

                            <div className="space-y-2">
                                <Label htmlFor="password">Mot de passe</Label>
                                <div className="relative">
                                    <Input
                                        id="password"
                                        name="password"
                                        type={showPassword ? 'text' : 'password'}
                                        placeholder="••••••••"
                                        value={formData.password}
                                        onChange={handleChange}
                                        required
                                        minLength={6}
                                        data-testid="input-password"
                                    />
                                    <button
                                        type="button"
                                        onClick={() => setShowPassword(!showPassword)}
                                        className="absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-slate-600"
                                    >
                                        {showPassword ? <EyeOff className="w-4 h-4" /> : <Eye className="w-4 h-4" />}
                                    </button>
                                </div>
                            </div>

                            <Button 
                                type="submit" 
                                className="w-full bg-green-600 hover:bg-green-700"
                                disabled={loading}
                                data-testid="submit-register"
                            >
                                {loading ? (
                                    <div className="spinner w-5 h-5 border-2 border-white/30 border-t-white"></div>
                                ) : (
                                    <>
                                        Créer mon compte gratuit
                                        <ArrowRight className="w-4 h-4 ml-2" />
                                    </>
                                )}
                            </Button>
                        </form>

                        <div className="mt-6 space-y-4">
                            <div className="text-center text-sm text-slate-600">
                                Déjà un compte ?{' '}
                                <Link to="/login" className="font-medium text-red-600 hover:text-red-700">
                                    Se connecter
                                </Link>
                            </div>
                            
                            <div className="border-t border-slate-200 pt-4">
                                <p className="text-center text-sm text-slate-500 mb-2">
                                    Vous avez un code groupe ?
                                </p>
                                <Link to="/register" className="block">
                                    <Button variant="outline" className="w-full">
                                        S'inscrire avec un code
                                    </Button>
                                </Link>
                            </div>
                        </div>
                    </CardContent>
                </Card>
            </main>
        </div>
    );
};

export default RegisterVisiteur;
