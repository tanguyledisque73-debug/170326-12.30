import React, { useState, useEffect } from 'react';
import { Mail, Send, Inbox, SendHorizontal, User } from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { Input } from '../components/ui/input';
import { Label } from '../components/ui/label';
import { Textarea } from '../components/ui/textarea';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '../components/ui/tabs';
import { Badge } from '../components/ui/badge';
import Layout from '../components/Layout';
import { getReceivedMessages, getSentMessages, sendMessage, markMessageAsRead, getUnreadCount, getUser } from '../lib/api';
import { toast } from 'sonner';

const Messages = () => {
    const user = getUser();
    const [activeTab, setActiveTab] = useState('received');
    const [receivedMessages, setReceivedMessages] = useState([]);
    const [sentMessages, setSentMessages] = useState([]);
    const [unreadCount, setUnreadCount] = useState(0);
    const [loading, setLoading] = useState(true);
    const [selectedMessage, setSelectedMessage] = useState(null);
    const [showCompose, setShowCompose] = useState(false);
    
    // Formulaire
    const [formData, setFormData] = useState({
        destinataire_id: '',
        sujet: '',
        contenu: ''
    });

    useEffect(() => {
        loadMessages();
        loadUnreadCount();
    }, []);

    const loadMessages = async () => {
        setLoading(true);
        try {
            const [received, sent] = await Promise.all([
                getReceivedMessages(),
                getSentMessages()
            ]);
            setReceivedMessages(received);
            setSentMessages(sent);
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors du chargement');
        } finally {
            setLoading(false);
        }
    };

    const loadUnreadCount = async () => {
        try {
            const { count } = await getUnreadCount();
            setUnreadCount(count);
        } catch (error) {
            console.error('Erreur:', error);
        }
    };

    const handleSelectMessage = async (message) => {
        setSelectedMessage(message);
        setShowCompose(false);
        
        if (!message.lu && message.destinataire_id === user.id) {
            try {
                await markMessageAsRead(message.id);
                loadMessages();
                loadUnreadCount();
            } catch (error) {
                console.error('Erreur:', error);
            }
        }
    };

    const handleSendMessage = async (e) => {
        e.preventDefault();
        
        if (!formData.destinataire_id || !formData.sujet || !formData.contenu) {
            toast.error('Veuillez remplir tous les champs');
            return;
        }

        try {
            await sendMessage(formData.destinataire_id, formData.sujet, formData.contenu);
            toast.success('Message envoyé !');
            setFormData({ destinataire_id: '', sujet: '', contenu: '' });
            setShowCompose(false);
            loadMessages();
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors de l\'envoi');
        }
    };

    const renderMessageList = (messages) => {
        if (messages.length === 0) {
            return (
                <div className="text-center py-8 text-slate-500">
                    <Mail className="w-12 h-12 mx-auto mb-2 text-slate-300" />
                    <p>Aucun message</p>
                </div>
            );
        }

        return (
            <div className="space-y-2">
                {messages.map((msg) => (
                    <div
                        key={msg.id}
                        onClick={() => handleSelectMessage(msg)}
                        className={`p-4 border rounded-lg cursor-pointer hover:bg-slate-50 transition-colors ${
                            selectedMessage?.id === msg.id ? 'bg-slate-50 border-red-200' : ''
                        } ${!msg.lu && msg.destinataire_id === user.id ? 'bg-blue-50' : ''}`}
                    >
                        <div className="flex items-start justify-between">
                            <div className="flex-1">
                                <div className="flex items-center gap-2 mb-1">
                                    <User className="w-4 h-4 text-slate-400" />
                                    <span className="font-medium text-slate-900">
                                        {activeTab === 'received' 
                                            ? `${msg.expediteur_prenom} ${msg.expediteur_nom}`
                                            : `${msg.destinataire_prenom} ${msg.destinataire_nom}`
                                        }
                                    </span>
                                    {!msg.lu && msg.destinataire_id === user.id && (
                                        <Badge variant="default" className="bg-blue-600">Nouveau</Badge>
                                    )}
                                </div>
                                <p className="font-medium text-slate-900 text-sm">{msg.sujet}</p>
                                <p className="text-sm text-slate-600 truncate">{msg.contenu}</p>
                            </div>
                            <span className="text-xs text-slate-500">
                                {new Date(msg.date_envoi).toLocaleDateString('fr-FR')}
                            </span>
                        </div>
                    </div>
                ))}
            </div>
        );
    };

    return (
        <Layout>
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
                <div className="flex items-center justify-between mb-6">
                    <h1 className="text-3xl font-bold text-slate-900">Messagerie</h1>
                    <Button 
                        onClick={() => { setShowCompose(true); setSelectedMessage(null); }}
                        className="bg-red-600 hover:bg-red-700"
                    >
                        <Send className="w-4 h-4 mr-2" />
                        Nouveau message
                    </Button>
                </div>

                <div className="grid lg:grid-cols-3 gap-6">
                    {/* Liste des messages */}
                    <div className="lg:col-span-1">
                        <Card>
                            <CardHeader className="pb-3">
                                <Tabs value={activeTab} onValueChange={setActiveTab}>
                                    <TabsList className="grid w-full grid-cols-2">
                                        <TabsTrigger value="received" className="flex items-center gap-2">
                                            <Inbox className="w-4 h-4" />
                                            Reçus
                                            {unreadCount > 0 && (
                                                <Badge variant="destructive" className="ml-1">{unreadCount}</Badge>
                                            )}
                                        </TabsTrigger>
                                        <TabsTrigger value="sent" className="flex items-center gap-2">
                                            <SendHorizontal className="w-4 h-4" />
                                            Envoyés
                                        </TabsTrigger>
                                    </TabsList>
                                </Tabs>
                            </CardHeader>
                            <CardContent>
                                {loading ? (
                                    <div className="text-center py-8">
                                        <div className="spinner mx-auto"></div>
                                    </div>
                                ) : (
                                    <>
                                        {activeTab === 'received' && renderMessageList(receivedMessages)}
                                        {activeTab === 'sent' && renderMessageList(sentMessages)}
                                    </>
                                )}
                            </CardContent>
                        </Card>
                    </div>

                    {/* Détail message ou composer */}
                    <div className="lg:col-span-2">
                        <Card>
                            <CardHeader>
                                <CardTitle>
                                    {showCompose ? 'Nouveau message' : selectedMessage ? 'Détail du message' : 'Sélectionnez un message'}
                                </CardTitle>
                            </CardHeader>
                            <CardContent>
                                {showCompose ? (
                                    <form onSubmit={handleSendMessage} className="space-y-4">
                                        <div>
                                            <Label htmlFor="destinataire_id">ID Destinataire</Label>
                                            <Input
                                                id="destinataire_id"
                                                value={formData.destinataire_id}
                                                onChange={(e) => setFormData({ ...formData, destinataire_id: e.target.value })}
                                                placeholder="ID du destinataire"
                                                required
                                            />
                                            <p className="text-xs text-slate-500 mt-1">Demandez l'ID à votre destinataire</p>
                                        </div>
                                        <div>
                                            <Label htmlFor="sujet">Sujet</Label>
                                            <Input
                                                id="sujet"
                                                value={formData.sujet}
                                                onChange={(e) => setFormData({ ...formData, sujet: e.target.value })}
                                                placeholder="Objet du message"
                                                required
                                            />
                                        </div>
                                        <div>
                                            <Label htmlFor="contenu">Message</Label>
                                            <Textarea
                                                id="contenu"
                                                value={formData.contenu}
                                                onChange={(e) => setFormData({ ...formData, contenu: e.target.value })}
                                                placeholder="Votre message..."
                                                rows={8}
                                                required
                                            />
                                        </div>
                                        <div className="flex gap-2">
                                            <Button type="submit" className="bg-red-600 hover:bg-red-700">
                                                <Send className="w-4 h-4 mr-2" />
                                                Envoyer
                                            </Button>
                                            <Button type="button" variant="outline" onClick={() => setShowCompose(false)}>
                                                Annuler
                                            </Button>
                                        </div>
                                    </form>
                                ) : selectedMessage ? (
                                    <div className="space-y-4">
                                        <div className="pb-4 border-b">
                                            <div className="flex items-center gap-2 mb-2">
                                                <User className="w-5 h-5 text-slate-400" />
                                                <div>
                                                    <p className="font-medium text-slate-900">
                                                        {activeTab === 'received' 
                                                            ? `De : ${selectedMessage.expediteur_prenom} ${selectedMessage.expediteur_nom}`
                                                            : `À : ${selectedMessage.destinataire_prenom} ${selectedMessage.destinataire_nom}`
                                                        }
                                                    </p>
                                                    <p className="text-xs text-slate-500">
                                                        {new Date(selectedMessage.date_envoi).toLocaleString('fr-FR')}
                                                    </p>
                                                </div>
                                            </div>
                                            <h3 className="font-semibold text-lg">{selectedMessage.sujet}</h3>
                                        </div>
                                        <div className="prose max-w-none">
                                            <p className="text-slate-700 whitespace-pre-wrap">{selectedMessage.contenu}</p>
                                        </div>
                                    </div>
                                ) : (
                                    <div className="text-center py-12 text-slate-500">
                                        <Mail className="w-16 h-16 mx-auto mb-4 text-slate-300" />
                                        <p>Sélectionnez un message pour le lire</p>
                                    </div>
                                )}
                            </CardContent>
                        </Card>
                    </div>
                </div>
            </div>
        </Layout>
    );
};

export default Messages;
