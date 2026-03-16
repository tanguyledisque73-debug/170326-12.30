import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Heart, Eye, EyeOff, ArrowRight, Key } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Input } from '../components/ui/input';
import { Label } from '../components/ui/label';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '../components/ui/card';
import { setPassword, getUser, setAuth } from '../lib/api';
import { toast } from 'sonner';

const SetPassword = () => {
    const navigate = useNavigate();
    const user = getUser();
    const [loading, setLoading] = useState(false);
    const [showPassword, setShowPassword] = useState(false);
    const [password, setPasswordValue] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        if (password !== confirmPassword) {
            toast.error('Les mots de passe ne correspondent pas');
            return;
        }
        
        if (password.length < 6) {
            toast.error('Le mot de passe doit contenir au moins 6 caractères');
            return;
        }

        setLoading(true);

        try {
            await setPassword(password);
            
            // Update local user data
            const updatedUser = { ...user, must_set_password: false };
            setAuth(localStorage.getItem('secours73_token'), updatedUser);
            
            toast.success('Mot de passe défini avec succès !');
            
            // Redirect based on role
            switch (user.role) {
                case 'admin':
                    navigate('/admin');
                    break;
                case 'formateur':
                    navigate('/formateur');
                    break;
                default:
                    navigate('/');
            }
        } catch (error) {
            console.error('Erreur:', error);
            toast.error(error.response?.data?.detail || 'Erreur lors de la mise à jour');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="min-h-screen bg-slate-50 flex flex-col" data-testid="set-password-page">
            {/* Header */}
            <header className="bg-white border-b border-slate-200 py-4">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex items-center gap-2">
                        <div className="w-10 h-10 bg-red-600 rounded-lg flex items-center justify-center">
                            <Heart className="w-5 h-5 text-white" strokeWidth={2.5} />
                        </div>
                        <div>
                            <span className="font-bold text-lg text-slate-900">Secours</span>
                            <span className="font-bold text-lg text-red-600 ml-1">73</span>
                        </div>
                    </div>
                </div>
            </header>

            {/* Main */}
            <main className="flex-1 flex items-center justify-center py-12 px-4">
                <Card className="w-full max-w-md shadow-lg animate-fade-in">
                    <CardHeader className="text-center pb-2">
                        <div className="w-14 h-14 bg-yellow-100 rounded-xl flex items-center justify-center mx-auto mb-4">
                            <Key className="w-7 h-7 text-yellow-600" />
                        </div>
                        <CardTitle className="text-2xl">Définir votre mot de passe</CardTitle>
                        <CardDescription>
                            Bienvenue {user?.prenom} ! Veuillez définir votre mot de passe personnel.
                        </CardDescription>
                    </CardHeader>
                    <CardContent>
                        <form onSubmit={handleSubmit} className="space-y-4">
                            <div className="space-y-2">
                                <Label htmlFor="password">Nouveau mot de passe</Label>
                                <div className="relative">
                                    <Input
                                        id="password"
                                        type={showPassword ? 'text' : 'password'}
                                        placeholder="••••••••"
                                        value={password}
                                        onChange={(e) => setPasswordValue(e.target.value)}
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

                            <div className="space-y-2">
                                <Label htmlFor="confirmPassword">Confirmer le mot de passe</Label>
                                <Input
                                    id="confirmPassword"
                                    type={showPassword ? 'text' : 'password'}
                                    placeholder="••••••••"
                                    value={confirmPassword}
                                    onChange={(e) => setConfirmPassword(e.target.value)}
                                    required
                                    minLength={6}
                                    data-testid="input-confirm-password"
                                />
                            </div>

                            <Button 
                                type="submit" 
                                className="w-full bg-red-600 hover:bg-red-700"
                                disabled={loading}
                                data-testid="submit-password"
                            >
                                {loading ? (
                                    <div className="spinner w-5 h-5 border-2 border-white/30 border-t-white"></div>
                                ) : (
                                    <>
                                        Définir mon mot de passe
                                        <ArrowRight className="w-4 h-4 ml-2" />
                                    </>
                                )}
                            </Button>
                        </form>
                    </CardContent>
                </Card>
            </main>
        </div>
    );
};

export default SetPassword;
