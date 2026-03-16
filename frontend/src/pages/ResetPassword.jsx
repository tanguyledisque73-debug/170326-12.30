import React, { useState, useEffect } from 'react';
import { useNavigate, useSearchParams, Link } from 'react-router-dom';
import { Lock, CheckCircle } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Input } from '../components/ui/input';
import { Label } from '../components/ui/label';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import Layout from '../components/Layout';
import { resetPassword } from '../lib/api';
import { toast } from 'sonner';

const ResetPassword = () => {
    const [searchParams] = useSearchParams();
    const navigate = useNavigate();
    const token = searchParams.get('token');
    
    const [newPassword, setNewPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [loading, setLoading] = useState(false);
    const [success, setSuccess] = useState(false);

    useEffect(() => {
        if (!token) {
            toast.error('Lien invalide');
            navigate('/login');
        }
    }, [token, navigate]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        if (newPassword.length < 6) {
            toast.error('Le mot de passe doit contenir au moins 6 caractères');
            return;
        }

        if (newPassword !== confirmPassword) {
            toast.error('Les mots de passe ne correspondent pas');
            return;
        }

        setLoading(true);
        try {
            await resetPassword(token, newPassword);
            setSuccess(true);
            toast.success('Mot de passe réinitialisé avec succès !');
            setTimeout(() => {
                navigate('/login');
            }, 3000);
        } catch (error) {
            console.error('Erreur:', error);
            toast.error(error.response?.data?.detail || 'Le lien est invalide ou a expiré');
        } finally {
            setLoading(false);
        }
    };

    return (
        <Layout>
            <div className="min-h-screen flex items-center justify-center px-4 py-12">
                <div className="max-w-md w-full">
                    <Card>
                        <CardHeader>
                            <CardTitle className="text-2xl text-center">
                                Nouveau mot de passe
                            </CardTitle>
                        </CardHeader>
                        <CardContent>
                            {!success ? (
                                <>
                                    <p className="text-slate-600 text-center mb-6">
                                        Choisissez un nouveau mot de passe sécurisé pour votre compte.
                                    </p>
                                    
                                    <form onSubmit={handleSubmit} className="space-y-4">
                                        <div>
                                            <Label htmlFor="newPassword">Nouveau mot de passe</Label>
                                            <div className="relative">
                                                <Lock className="absolute left-3 top-3 h-5 w-5 text-slate-400" />
                                                <Input
                                                    id="newPassword"
                                                    type="password"
                                                    value={newPassword}
                                                    onChange={(e) => setNewPassword(e.target.value)}
                                                    placeholder="••••••••"
                                                    className="pl-10"
                                                    required
                                                    minLength={6}
                                                />
                                            </div>
                                            <p className="text-xs text-slate-500 mt-1">
                                                Au moins 6 caractères
                                            </p>
                                        </div>

                                        <div>
                                            <Label htmlFor="confirmPassword">Confirmer le mot de passe</Label>
                                            <div className="relative">
                                                <Lock className="absolute left-3 top-3 h-5 w-5 text-slate-400" />
                                                <Input
                                                    id="confirmPassword"
                                                    type="password"
                                                    value={confirmPassword}
                                                    onChange={(e) => setConfirmPassword(e.target.value)}
                                                    placeholder="••••••••"
                                                    className="pl-10"
                                                    required
                                                    minLength={6}
                                                />
                                            </div>
                                        </div>

                                        <Button 
                                            type="submit" 
                                            className="w-full bg-red-600 hover:bg-red-700"
                                            disabled={loading}
                                        >
                                            {loading ? 'Réinitialisation...' : 'Réinitialiser le mot de passe'}
                                        </Button>
                                    </form>
                                </>
                            ) : (
                                <div className="text-center space-y-4">
                                    <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto">
                                        <CheckCircle className="w-8 h-8 text-green-600" />
                                    </div>
                                    <h3 className="font-semibold text-lg">Mot de passe réinitialisé !</h3>
                                    <p className="text-slate-600">
                                        Votre mot de passe a été modifié avec succès.
                                    </p>
                                    <p className="text-sm text-slate-500">
                                        Redirection vers la page de connexion...
                                    </p>
                                    <Link to="/login">
                                        <Button variant="outline" className="mt-4">
                                            Se connecter maintenant
                                        </Button>
                                    </Link>
                                </div>
                            )}
                        </CardContent>
                    </Card>
                </div>
            </div>
        </Layout>
    );
};

export default ResetPassword;
