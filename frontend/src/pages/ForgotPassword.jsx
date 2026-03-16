import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import { ArrowLeft, Mail } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Input } from '../components/ui/input';
import { Label } from '../components/ui/label';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import Layout from '../components/Layout';
import { forgotPassword } from '../lib/api';
import { toast } from 'sonner';

const ForgotPassword = () => {
    const [email, setEmail] = useState('');
    const [loading, setLoading] = useState(false);
    const [emailSent, setEmailSent] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        
        if (!email) {
            toast.error('Veuillez entrer votre email');
            return;
        }

        setLoading(true);
        try {
            await forgotPassword(email);
            setEmailSent(true);
            toast.success('Email envoyé ! Vérifiez votre boîte de réception');
        } catch (error) {
            console.error('Erreur:', error);
            toast.success('Si cet email existe, un lien a été envoyé');
            setEmailSent(true);
        } finally {
            setLoading(false);
        }
    };

    return (
        <Layout>
            <div className="min-h-screen flex items-center justify-center px-4 py-12">
                <div className="max-w-md w-full">
                    <Link to="/login" className="inline-flex items-center text-sm text-slate-600 hover:text-slate-900 mb-6">
                        <ArrowLeft className="w-4 h-4 mr-2" />
                        Retour à la connexion
                    </Link>

                    <Card>
                        <CardHeader>
                            <CardTitle className="text-2xl text-center">
                                Mot de passe oublié
                            </CardTitle>
                        </CardHeader>
                        <CardContent>
                            {!emailSent ? (
                                <>
                                    <p className="text-slate-600 text-center mb-6">
                                        Entrez votre adresse email et nous vous enverrons un lien pour réinitialiser votre mot de passe.
                                    </p>
                                    
                                    <form onSubmit={handleSubmit} className="space-y-4">
                                        <div>
                                            <Label htmlFor="email">Adresse email</Label>
                                            <div className="relative">
                                                <Mail className="absolute left-3 top-3 h-5 w-5 text-slate-400" />
                                                <Input
                                                    id="email"
                                                    type="email"
                                                    value={email}
                                                    onChange={(e) => setEmail(e.target.value)}
                                                    placeholder="vous@exemple.com"
                                                    className="pl-10"
                                                    required
                                                />
                                            </div>
                                        </div>

                                        <Button 
                                            type="submit" 
                                            className="w-full bg-red-600 hover:bg-red-700"
                                            disabled={loading}
                                        >
                                            {loading ? 'Envoi en cours...' : 'Envoyer le lien de réinitialisation'}
                                        </Button>
                                    </form>
                                </>
                            ) : (
                                <div className="text-center space-y-4">
                                    <div className="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto">
                                        <Mail className="w-8 h-8 text-green-600" />
                                    </div>
                                    <h3 className="font-semibold text-lg">Email envoyé !</h3>
                                    <p className="text-slate-600">
                                        Si un compte existe avec l'adresse <strong>{email}</strong>, vous recevrez un email avec un lien pour réinitialiser votre mot de passe.
                                    </p>
                                    <p className="text-sm text-slate-500">
                                        Le lien est valable pendant 1 heure.
                                    </p>
                                    <Link to="/login">
                                        <Button variant="outline" className="mt-4">
                                            Retour à la connexion
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

export default ForgotPassword;
