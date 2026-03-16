import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Heart, Eye, EyeOff, ArrowRight, LogIn } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Input } from '../components/ui/input';
import { Label } from '../components/ui/label';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../components/ui/card';
import { login, setAuth } from '../lib/api';
import { toast } from 'sonner';

const Login = () => {
    const navigate = useNavigate();
    const [loading, setLoading] = useState(false);
    const [showPassword, setShowPassword] = useState(false);
    const [formData, setFormData] = useState({
        email: '',
        password: ''
    });

    const handleChange = (e) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);

        try {
            const response = await login(formData);
            setAuth(response.token, response.user);
            toast.success('Connexion réussie !');
            
            // Check if user needs to set password
            if (response.user.must_set_password) {
                navigate('/set-password');
                return;
            }
            
            // Redirect based on role
            switch (response.user.role) {
                case 'admin':
                    navigate('/admin');
                    break;
                case 'formateur':
                    navigate('/formateur');
                    break;
                case 'stagiaire':
                    navigate('/stagiaire');
                    break;
                case 'visiteur':
                    navigate('/visiteur');
                    break;
                default:
                    navigate('/');
            }
        } catch (error) {
            console.error('Erreur:', error);
            toast.error(error.response?.data?.detail || 'Email ou mot de passe incorrect');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-slate-50 flex flex-col" data-testid="login-page">
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
                            <LogIn className="w-7 h-7 text-red-600" />
                        </div>
                        <CardTitle className="text-2xl">Connexion</CardTitle>
                        <CardDescription>
                            Accédez à votre espace de formation
                        </CardDescription>
                    </CardHeader>
                    <CardContent>
                        <form onSubmit={handleSubmit} className="space-y-4">
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

                            <div className="text-center mt-4">
                                <Link to="/forgot-password" className="text-sm text-red-600 hover:text-red-700">
                                    Mot de passe oublié ?
                                </Link>
                            </div>

                            <Button 
                                type="submit" 
                                className="w-full bg-red-600 hover:bg-red-700"
                                disabled={loading}
                                data-testid="submit-login"
                            >
                                {loading ? (
                                    <div className="spinner w-5 h-5 border-2 border-white/30 border-t-white"></div>
                                ) : (
                                    <>
                                        Se connecter
                                        <ArrowRight className="w-4 h-4 ml-2" />
                                    </>
                                )}
                            </Button>
                        </form>

                        <div className="mt-6 space-y-4">
                            <div className="text-center text-sm text-slate-600">
                                Pas encore de compte ?
                            </div>
                            <div className="grid grid-cols-2 gap-3">
                                <Link to="/register">
                                    <Button variant="outline" className="w-full text-sm">
                                        Avec code groupe
                                    </Button>
                                </Link>
                                <Link to="/inscription-gratuite">
                                    <Button variant="outline" className="w-full text-sm">
                                        Compte gratuit
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

export default Login;
