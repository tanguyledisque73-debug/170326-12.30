import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Heart, Eye, EyeOff, ArrowRight, UserPlus, Key } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Input } from '../components/ui/input';
import { Label } from '../components/ui/label';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../components/ui/card';
import { registerStagiaire, setAuth } from '../lib/api';
import { toast } from 'sonner';

const Register = () => {
    const navigate = useNavigate();
    const [loading, setLoading] = useState(false);
    const [showPassword, setShowPassword] = useState(false);
    const [formData, setFormData] = useState({
        email: '',
        password: '',
        nom: '',
        prenom: '',
        code_groupe: ''
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);

        try {
            const response = await registerStagiaire(formData);
            setAuth(response.token, response.user);
            toast.success('Inscription réussie ! Bienvenue dans votre groupe de formation.');
            navigate('/stagiaire');
        } catch (error) {
            console.error('Erreur:', error);
            toast.error(error.response?.data?.detail || 'Erreur lors de l\'inscription');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-slate-50 flex flex-col" data-testid="register-page">
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
                        <div className="w-14 h-14 bg-red-100 rounded-xl flex items-center justify-center mx-auto mb-4">
                            <UserPlus className="w-7 h-7 text-red-600" />
                        </div>
                        <CardTitle className="text-2xl">Inscription Stagiaire</CardTitle>
                        <CardDescription>
                            Rejoignez votre groupe de formation avec le code fourni par votre formateur
                        </CardDescription>
                    </CardHeader>
                    <CardContent>
                        <form onSubmit={handleSubmit} className="space-y-4">
                            {/* Code groupe en premier et mis en évidence */}
                            <div className="space-y-2 p-4 bg-red-50 rounded-lg border border-red-200">
                                <Label htmlFor="code_groupe" className="flex items-center gap-2 text-red-700">
                                    <Key className="w-4 h-4" />
                                    Code du groupe
                                </Label>
                                <Input
                                    id="code_groupe"
                                    name="code_groupe"
                                    placeholder="Ex: ABC12345"
                                    value={formData.code_groupe}
                                    onChange={handleChange}
                                    required
                                    className="uppercase font-mono text-lg tracking-wider"
                                    data-testid="input-code-groupe"
                                />
                                <p className="text-xs text-red-600">
                                    Code fourni par votre formateur
                                </p>
                            </div>

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
                                className="w-full bg-red-600 hover:bg-red-700"
                                disabled={loading}
                                data-testid="submit-register"
                            >
                                {loading ? (
                                    <div className="spinner w-5 h-5 border-2 border-white/30 border-t-white"></div>
                                ) : (
                                    <>
                                        S'inscrire
                                        <ArrowRight className="w-4 h-4 ml-2" />
                                    </>
                                )}
                            </Button>
                        </form>

                        <div className="mt-6 space-y-4">
                            <div className="text-center text-sm text-slate-600">
                                Déjà inscrit ?{' '}
                                <Link to="/login" className="font-medium text-red-600 hover:text-red-700">
                                    Se connecter
                                </Link>
                            </div>
                            
                            <div className="border-t border-slate-200 pt-4">
                                <p className="text-center text-sm text-slate-500 mb-2">
                                    Pas de code groupe ?
                                </p>
                                <Link to="/inscription-gratuite" className="block">
                                    <Button variant="outline" className="w-full">
                                        Créer un compte gratuit (accès limité)
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

export default Register;
