import React, { useState, useEffect } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { 
    ArrowLeft,
    Users,
    Copy,
    UserPlus,
    Eye,
    CheckCircle2,
    XCircle,
    TrendingUp,
    Settings
} from 'lucide-react';
import { Button } from '../../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/card';
import { Input } from '../../components/ui/input';
import { Label } from '../../components/ui/label';
import { Progress } from '../../components/ui/progress';
import Layout from '../../components/Layout';
import { formateurGetGroupeDetail, formateurInviteCollaborator, getUser } from '../../lib/api';
import { toast } from 'sonner';

const FormateurGroupeDetail = () => {
    const { groupeId } = useParams();
    const navigate = useNavigate();
    const user = getUser();
    const [loading, setLoading] = useState(true);
    const [groupe, setGroupe] = useState(null);
    const [stagiaires, setStagiaires] = useState([]);
    const [showInvite, setShowInvite] = useState(false);
    const [inviteEmail, setInviteEmail] = useState('');
    const [inviting, setInviting] = useState(false);

    useEffect(() => {
        if (!user || user.role !== 'formateur') {
            navigate('/login');
            return;
        }
        loadData();
    }, [groupeId]);

    const loadData = async () => {
        try {
            const data = await formateurGetGroupeDetail(groupeId);
            setGroupe(data.groupe);
            setStagiaires(data.stagiaires);
        } catch (error) {
            console.error('Erreur:', error);
            toast.error('Erreur lors du chargement');
            navigate('/formateur');
        } finally {
            setLoading(false);
        }
    };

    const copyCode = () => {
        navigator.clipboard.writeText(groupe.code_acces);
        toast.success('Code copié !');
    };

    const handleInvite = async (e) => {
        e.preventDefault();
        setInviting(true);
        try {
            await formateurInviteCollaborator(groupeId, inviteEmail);
            toast.success('Formateur invité avec succès !');
            setShowInvite(false);
            setInviteEmail('');
            loadData();
        } catch (error) {
            console.error('Erreur:', error);
            toast.error(error.response?.data?.detail || 'Erreur lors de l\'invitation');
        } finally {
            setInviting(false);
        }
    };

    const getScoreColor = (score) => {
        if (score >= 80) return 'text-green-600';
        if (score >= 60) return 'text-yellow-600';
        return 'text-red-600';
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
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8" data-testid="groupe-detail">
                {/* Back */}
                <Link 
                    to="/formateur"
                    className="text-sm text-slate-600 hover:text-red-600 flex items-center gap-1 mb-6"
                >
                    <ArrowLeft className="w-4 h-4" />
                    Retour au tableau de bord
                </Link>

                {/* Header */}
                <div className="flex flex-col md:flex-row md:items-start md:justify-between gap-4 mb-8">
                    <div>
                        <div className="flex items-center gap-2 mb-2">
                            <h1 className="text-3xl font-bold text-slate-900">{groupe.nom}</h1>
                            <span className={`px-2 py-0.5 rounded text-xs font-medium ${
                                groupe.formation_type === 'PSE' ? 'bg-red-100 text-red-700' :
                                groupe.formation_type === 'PSC' ? 'bg-green-100 text-green-700' :
                                'bg-blue-100 text-blue-700'
                            }`}>
                                {groupe.formation_type}
                            </span>
                        </div>
                        <p className="text-slate-600">
                            {groupe.nb_stagiaires || 0} / {groupe.max_stagiaires} stagiaires • Seuil de réussite: {groupe.seuil_reussite}%
                        </p>
                    </div>
                    
                    <div className="flex items-center gap-3">
                        <Link to={`/formateur/groupe/${groupeId}/settings`} data-testid="groupe-settings-btn">
                            <Button variant="outline" className="flex items-center gap-2">
                                <Settings className="w-4 h-4" />
                                Paramètres
                            </Button>
                        </Link>
                        <div className="p-4 bg-slate-100 rounded-lg">
                            <p className="text-xs text-slate-500 mb-1">Code d'accès</p>
                            <button 
                                onClick={copyCode}
                                className="flex items-center gap-2 font-mono text-xl font-bold text-red-600 hover:text-red-700"
                            >
                                {groupe.code_acces}
                                <Copy className="w-4 h-4" />
                            </button>
                        </div>
                    </div>
                </div>

                {/* Invite Collaborator */}
                {groupe.formateur_id === user?.id && (
                    <Card className="mb-6">
                        <CardContent className="p-4">
                            {showInvite ? (
                                <form onSubmit={handleInvite} className="flex items-end gap-3">
                                    <div className="flex-1">
                                        <Label htmlFor="email" className="text-sm">Email du formateur à inviter</Label>
                                        <Input
                                            id="email"
                                            type="email"
                                            placeholder="formateur@example.com"
                                            value={inviteEmail}
                                            onChange={(e) => setInviteEmail(e.target.value)}
                                            required
                                        />
                                    </div>
                                    <Button type="submit" disabled={inviting}>
                                        {inviting ? <div className="spinner w-5 h-5 border-2"></div> : 'Inviter'}
                                    </Button>
                                    <Button type="button" variant="outline" onClick={() => setShowInvite(false)}>
                                        Annuler
                                    </Button>
                                </form>
                            ) : (
                                <div className="flex items-center justify-between">
                                    <p className="text-sm text-slate-600">
                                        {groupe.collaborateurs?.length > 0 
                                            ? `${groupe.collaborateurs.length} collaborateur(s)` 
                                            : 'Invitez d\'autres formateurs à collaborer'}
                                    </p>
                                    <Button variant="outline" size="sm" onClick={() => setShowInvite(true)}>
                                        <UserPlus className="w-4 h-4 mr-2" />
                                        Inviter un formateur
                                    </Button>
                                </div>
                            )}
                        </CardContent>
                    </Card>
                )}

                {/* Stagiaires List */}
                <Card data-testid="stagiaires-list">
                    <CardHeader>
                        <CardTitle className="flex items-center gap-2">
                            <Users className="w-5 h-5" />
                            Stagiaires ({stagiaires.length})
                        </CardTitle>
                    </CardHeader>
                    <CardContent>
                        {stagiaires.length === 0 ? (
                            <div className="empty-state py-8">
                                <Users className="w-12 h-12 mx-auto text-slate-300 mb-3" />
                                <p className="text-slate-500 mb-2">Aucun stagiaire inscrit</p>
                                <p className="text-sm text-slate-400">
                                    Partagez le code <strong className="font-mono text-red-600">{groupe.code_acces}</strong> avec vos stagiaires
                                </p>
                            </div>
                        ) : (
                            <div className="overflow-x-auto">
                                <table className="data-table">
                                    <thead>
                                        <tr>
                                            <th>Stagiaire</th>
                                            <th>Progression</th>
                                            <th>Quiz réalisés</th>
                                            <th>Score moyen</th>
                                            <th></th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {stagiaires.map((stagiaire) => {
                                            const progressPct = groupe.chapitres_ordre?.length > 0 
                                                ? (stagiaire.chapitres_completes / groupe.chapitres_ordre.length) * 100 
                                                : 0;
                                            return (
                                                <tr key={stagiaire.id}>
                                                    <td>
                                                        <div>
                                                            <p className="font-medium text-slate-900">
                                                                {stagiaire.prenom} {stagiaire.nom}
                                                            </p>
                                                            <p className="text-xs text-slate-500">
                                                                {stagiaire.email}
                                                            </p>
                                                        </div>
                                                    </td>
                                                    <td>
                                                        <div className="w-32">
                                                            <div className="flex items-center justify-between text-xs mb-1">
                                                                <span className="text-slate-500">
                                                                    {stagiaire.chapitres_completes}/{groupe.chapitres_ordre?.length || 0}
                                                                </span>
                                                                <span className="font-medium">{Math.round(progressPct)}%</span>
                                                            </div>
                                                            <Progress value={progressPct} className="h-2" />
                                                        </div>
                                                    </td>
                                                    <td>
                                                        <span className="font-medium">{stagiaire.quizzes_completed}</span>
                                                    </td>
                                                    <td>
                                                        <span className={`font-semibold ${getScoreColor(stagiaire.average_score)}`}>
                                                            {Math.round(stagiaire.average_score)}%
                                                        </span>
                                                    </td>
                                                    <td>
                                                        <Link to={`/formateur/stagiaire/${stagiaire.id}`}>
                                                            <Button variant="ghost" size="sm">
                                                                <Eye className="w-4 h-4" />
                                                            </Button>
                                                        </Link>
                                                    </td>
                                                </tr>
                                            );
                                        })}
                                    </tbody>
                                </table>
                            </div>
                        )}
                    </CardContent>
                </Card>
            </div>
        </Layout>
    );
};

export default FormateurGroupeDetail;
