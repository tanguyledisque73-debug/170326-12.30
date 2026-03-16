import React, { useState, useEffect } from 'react';
import { Mail, Send } from 'lucide-react';
import { Button } from '../../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/card';
import { Input } from '../../components/ui/input';
import { Label } from '../../components/ui/label';
import { Textarea } from '../../components/ui/textarea';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../../components/ui/select';
import Layout from '../../components/Layout';
import { formateurSendEmail, formateurGetGroupes } from '../../lib/api';
import { toast } from 'sonner';

const SendEmail = () => {
    const [groupes, setGroupes] = useState([]);
    const [selectedGroupe, setSelectedGroupe] = useState('');
    const [stagiaires, setStagiaires] = useState([]);
    const [sending, setSending] = useState(false);
    
    const [formData, setFormData] = useState({
        to_email: '',
        subject: '',
        message: ''
    });

    useEffect(() => {
        loadGroupes();
    }, []);

    const loadGroupes = async () => {
        try {
            const grps = await formateurGetGroupes();
            setGroupes(grps);
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors du chargement des groupes');
        }
    };

    const handleGroupeChange = (groupeId) => {
        setSelectedGroupe(groupeId);
        const groupe = groupes.find(g => g.id === groupeId);
        if (groupe && groupe.stagiaires) {
            setStagiaires(groupe.stagiaires);
        } else {
            setStagiaires([]);
        }
        setFormData({ ...formData, to_email: '' });
    };

    const handleSend = async (e) => {
        e.preventDefault();
        
        if (!formData.to_email || !formData.subject || !formData.message) {
            toast.error('Veuillez remplir tous les champs');
            return;
        }

        setSending(true);
        try {
            await formateurSendEmail(formData.to_email, formData.subject, formData.message);
            toast.success('Email envoyé avec succès !');
            setFormData({
                to_email: '',
                subject: '',
                message: ''
            });
            setSelectedGroupe('');
        } catch (error) {
            console.error('Erreur:', error);
            toast.error(error.response?.data?.detail || 'Erreur lors de l\'envoi');
        } finally {
            setSending(false);
        }
    };

    return (
        <Layout>
            <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                <div className="flex items-center gap-3 mb-6">
                    <Mail className="w-8 h-8 text-red-600" />
                    <h1 className="text-3xl font-bold text-slate-900">Envoyer un email</h1>
                </div>

                <Card>
                    <CardHeader>
                        <CardTitle>Composer un message</CardTitle>
                        <p className="text-sm text-slate-600 mt-1">
                            Envoyez un email à vos stagiaires
                        </p>
                    </CardHeader>
                    <CardContent>
                        <form onSubmit={handleSend} className="space-y-6">
                            <div>
                                <Label htmlFor="groupe">Groupe (optionnel - pour aide à la sélection)</Label>
                                <Select 
                                    value={selectedGroupe}
                                    onValueChange={handleGroupeChange}
                                >
                                    <SelectTrigger>
                                        <SelectValue placeholder="Sélectionner un groupe" />
                                    </SelectTrigger>
                                    <SelectContent>
                                        {groupes.map(groupe => (
                                            <SelectItem key={groupe.id} value={groupe.id}>
                                                {groupe.nom}
                                            </SelectItem>
                                        ))}
                                    </SelectContent>
                                </Select>
                            </div>

                            {selectedGroupe && stagiaires.length > 0 && (
                                <div>
                                    <Label htmlFor="stagiaire">Stagiaire du groupe</Label>
                                    <Select 
                                        value={formData.to_email}
                                        onValueChange={(value) => setFormData({ ...formData, to_email: value })}
                                    >
                                        <SelectTrigger>
                                            <SelectValue placeholder="Sélectionner un stagiaire" />
                                        </SelectTrigger>
                                        <SelectContent>
                                            {stagiaires.map((stagiaire, idx) => (
                                                <SelectItem key={idx} value={stagiaire.email}>
                                                    {stagiaire.prenom} {stagiaire.nom} ({stagiaire.email})
                                                </SelectItem>
                                            ))}
                                        </SelectContent>
                                    </Select>
                                </div>
                            )}

                            <div>
                                <Label htmlFor="to_email">Email du destinataire *</Label>
                                <Input
                                    id="to_email"
                                    type="email"
                                    value={formData.to_email}
                                    onChange={(e) => setFormData({ ...formData, to_email: e.target.value })}
                                    placeholder="exemple@email.com"
                                    required
                                />
                                <p className="text-xs text-slate-500 mt-1">
                                    Vous pouvez aussi entrer l'email directement
                                </p>
                            </div>

                            <div>
                                <Label htmlFor="subject">Objet *</Label>
                                <Input
                                    id="subject"
                                    value={formData.subject}
                                    onChange={(e) => setFormData({ ...formData, subject: e.target.value })}
                                    placeholder="Objet de l'email"
                                    required
                                />
                            </div>

                            <div>
                                <Label htmlFor="message">Message *</Label>
                                <Textarea
                                    id="message"
                                    value={formData.message}
                                    onChange={(e) => setFormData({ ...formData, message: e.target.value })}
                                    placeholder="Votre message..."
                                    rows={10}
                                    required
                                />
                            </div>

                            <Button 
                                type="submit" 
                                className="w-full bg-red-600 hover:bg-red-700"
                                disabled={sending}
                            >
                                <Send className="w-4 h-4 mr-2" />
                                {sending ? 'Envoi en cours...' : 'Envoyer l\'email'}
                            </Button>
                        </form>
                    </CardContent>
                </Card>

                <div className="mt-6 p-4 bg-blue-50 border border-blue-200 rounded-lg">
                    <h3 className="font-medium text-blue-900 mb-2">💡 Conseils</h3>
                    <ul className="text-sm text-blue-800 space-y-1">
                        <li>• L'email sera envoyé depuis la plateforme Secours 73</li>
                        <li>• Le destinataire pourra vous répondre directement à votre email</li>
                        <li>• Vérifiez bien l'adresse email avant d'envoyer</li>
                    </ul>
                </div>
            </div>
        </Layout>
    );
};

export default SendEmail;
