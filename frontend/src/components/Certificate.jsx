import React, { useState, useEffect, useRef } from 'react';
import { 
    Award,
    Download,
    PartyPopper,
    CheckCircle2,
    Calendar,
    BookOpen,
    TrendingUp,
    FileDown,
    Loader2
} from 'lucide-react';
import { Button } from '../components/ui/button';
import { Card, CardContent, CardHeader, CardTitle } from '../components/ui/card';
import { downloadCertificatePDF } from '../lib/api';
import { toast } from 'sonner';

const CertificatePDF = ({ certificateData, onClose }) => {
    const certificateRef = useRef(null);
    const [downloading, setDownloading] = useState(false);

    const handleDownloadPDF = async () => {
        setDownloading(true);
        try {
            const blob = await downloadCertificatePDF();
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = `certificat_FOAD_${certificateData.formation_type}_${certificateData.nom}_${certificateData.prenom}.pdf`;
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            document.body.removeChild(a);
            toast.success('Certificat téléchargé avec succès !');
        } catch (error) {
            console.error('Erreur téléchargement:', error);
            toast.error('Erreur lors du téléchargement du certificat');
            // Fallback to print version
            handlePrint();
        } finally {
            setDownloading(false);
        }
    };

    const handlePrint = () => {
        // Create a printable version as fallback
        const printWindow = window.open('', '_blank');
        printWindow.document.write(`
            <!DOCTYPE html>
            <html>
            <head>
                <title>${certificateData.certificate_title}</title>
                <style>
                    * { margin: 0; padding: 0; box-sizing: border-box; }
                    body { 
                        font-family: 'Georgia', serif; 
                        display: flex; 
                        justify-content: center; 
                        align-items: center; 
                        min-height: 100vh;
                        background: #f8f9fa;
                        padding: 20px;
                    }
                    .certificate {
                        width: 800px;
                        padding: 60px;
                        background: white;
                        border: 3px solid #dc2626;
                        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
                        text-align: center;
                        position: relative;
                    }
                    .certificate::before {
                        content: '';
                        position: absolute;
                        top: 15px;
                        left: 15px;
                        right: 15px;
                        bottom: 15px;
                        border: 1px solid #dc2626;
                        pointer-events: none;
                    }
                    .logo {
                        width: 120px;
                        height: auto;
                        margin-bottom: 20px;
                    }
                    .title {
                        font-size: 32px;
                        color: #dc2626;
                        margin-bottom: 10px;
                        font-weight: bold;
                        text-transform: uppercase;
                        letter-spacing: 2px;
                    }
                    .subtitle {
                        font-size: 18px;
                        color: #64748b;
                        margin-bottom: 40px;
                    }
                    .certifies {
                        font-size: 16px;
                        color: #475569;
                        margin-bottom: 10px;
                    }
                    .name {
                        font-size: 36px;
                        color: #1e293b;
                        font-weight: bold;
                        margin-bottom: 30px;
                        padding: 15px 0;
                        border-top: 2px solid #e2e8f0;
                        border-bottom: 2px solid #e2e8f0;
                    }
                    .achievement {
                        font-size: 16px;
                        color: #475569;
                        margin-bottom: 15px;
                        line-height: 1.6;
                    }
                    .highlight {
                        color: #dc2626;
                        font-weight: bold;
                    }
                    .score {
                        font-size: 24px;
                        color: #059669;
                        font-weight: bold;
                        margin: 20px 0;
                    }
                    .date {
                        font-size: 14px;
                        color: #64748b;
                        margin-top: 40px;
                    }
                    .footer {
                        margin-top: 50px;
                        font-size: 12px;
                        color: #94a3b8;
                    }
                    @media print {
                        body { background: white; }
                        .certificate { box-shadow: none; }
                    }
                </style>
            </head>
            <body>
                <div class="certificate">
                    <img src="/images/logo-secours73.png" alt="Logo" class="logo" />
                    <h1 class="title">Certificat de Validation</h1>
                    <p class="subtitle">Formation Ouverte à Distance - ${certificateData.formation_type} 1</p>
                    
                    <p class="certifies">Nous certifions que</p>
                    <h2 class="name">${certificateData.prenom} ${certificateData.nom}</h2>
                    
                    <p class="achievement">
                        a validé avec succès l'ensemble des modules de la<br/>
                        <span class="highlight">Formation Ouverte à Distance Premiers Secours en Équipe - ${certificateData.formation_type}</span>
                    </p>
                    
                    <p class="score">Score moyen: ${certificateData.average_score}%</p>
                    
                    <p class="achievement">
                        Groupe de formation: <strong>${certificateData.groupe_nom}</strong><br/>
                        ${certificateData.chapters_completed} chapitres complétés
                    </p>
                    
                    <p class="date">
                        Délivré le ${new Date(certificateData.completion_date).toLocaleDateString('fr-FR', {
                            day: 'numeric',
                            month: 'long',
                            year: 'numeric'
                        })}
                    </p>
                    
                    <p class="footer">
                        Secours Alpes 73 - Association agréée pour la formation aux premiers secours<br/>
                        Ce certificat atteste de la validation de la partie théorique de la formation
                    </p>
                </div>
                <script>
                    window.onload = function() { window.print(); }
                </script>
            </body>
            </html>
        `);
        printWindow.document.close();
    };

    return (
        <div className="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
            <div className="bg-white rounded-xl max-w-2xl w-full max-h-[90vh] overflow-auto">
                {/* Preview Header */}
                <div className="p-6 border-b border-slate-200 flex items-center justify-between">
                    <div className="flex items-center gap-3">
                        <Award className="w-8 h-8 text-yellow-500" />
                        <div>
                            <h2 className="text-xl font-bold text-slate-900">Votre Certificat</h2>
                            <p className="text-sm text-slate-500">Aperçu avant téléchargement</p>
                        </div>
                    </div>
                    <button 
                        onClick={onClose}
                        className="text-slate-400 hover:text-slate-600"
                    >
                        ✕
                    </button>
                </div>

                {/* Certificate Preview */}
                <div className="p-8" ref={certificateRef}>
                    <div className="border-2 border-red-600 p-8 text-center relative">
                        <div className="absolute top-3 left-3 right-3 bottom-3 border border-red-200 pointer-events-none"></div>
                        
                        <img 
                            src="/images/logo-secours73.png" 
                            alt="Logo Secours Alpes 73" 
                            className="h-20 mx-auto mb-4"
                        />
                        
                        <h1 className="text-2xl font-bold text-red-600 uppercase tracking-wide mb-2">
                            Certificat de Validation
                        </h1>
                        <p className="text-slate-500 mb-8">
                            Formation Ouverte à Distance - {certificateData.formation_type} 1
                        </p>
                        
                        <p className="text-slate-600 mb-2">Nous certifions que</p>
                        <h2 className="text-3xl font-bold text-slate-900 py-4 border-t border-b border-slate-200 mb-6">
                            {certificateData.prenom} {certificateData.nom}
                        </h2>
                        
                        <p className="text-slate-600 mb-4">
                            a validé avec succès l'ensemble des modules de la<br/>
                            <span className="text-red-600 font-semibold">
                                Formation Ouverte à Distance Premiers Secours en Équipe - {certificateData.formation_type}
                            </span>
                        </p>
                        
                        <p className="text-2xl font-bold text-green-600 my-4">
                            Score moyen: {certificateData.average_score}%
                        </p>
                        
                        <p className="text-slate-600 mb-6">
                            Groupe: <strong>{certificateData.groupe_nom}</strong><br/>
                            {certificateData.chapters_completed} chapitres complétés
                        </p>
                        
                        <p className="text-sm text-slate-500">
                            Délivré le {new Date(certificateData.completion_date).toLocaleDateString('fr-FR', {
                                day: 'numeric',
                                month: 'long',
                                year: 'numeric'
                            })}
                        </p>
                    </div>
                </div>

                {/* Actions */}
                <div className="p-6 border-t border-slate-200 flex gap-3">
                    <Button variant="outline" onClick={onClose} className="flex-1">
                        Fermer
                    </Button>
                    <Button 
                        onClick={handleDownloadPDF}
                        disabled={downloading}
                        className="flex-1 bg-red-600 hover:bg-red-700"
                    >
                        {downloading ? (
                            <>
                                <Loader2 className="w-4 h-4 mr-2 animate-spin" />
                                Génération...
                            </>
                        ) : (
                            <>
                                <FileDown className="w-4 h-4 mr-2" />
                                Télécharger PDF
                            </>
                        )}
                    </Button>
                </div>
            </div>
        </div>
    );
};

const CertificateBanner = ({ onViewCertificate }) => {
    return (
        <div 
            className="bg-gradient-to-r from-green-500 to-emerald-600 text-white p-6 rounded-xl mb-6 animate-fade-in"
            data-testid="certificate-banner"
        >
            <div className="flex items-center gap-4">
                <div className="bg-white/20 p-3 rounded-full">
                    <PartyPopper className="w-8 h-8" />
                </div>
                <div className="flex-1">
                    <h2 className="text-2xl font-bold mb-1">
                        🎉 Félicitations !
                    </h2>
                    <p className="text-green-100">
                        Vous avez validé la FOAD PSE 1 ! Votre certificat est maintenant disponible.
                    </p>
                </div>
                <Button 
                    onClick={onViewCertificate}
                    className="bg-white text-green-600 hover:bg-green-50"
                >
                    <Award className="w-4 h-4 mr-2" />
                    Voir mon certificat
                </Button>
            </div>
        </div>
    );
};

const CertificateProgress = ({ status }) => {
    const completedCount = status.completed_chapters?.length || 0;
    const requiredCount = status.required_chapters?.length || 0;
    const progress = requiredCount > 0 ? (completedCount / requiredCount) * 100 : 0;

    return (
        <Card>
            <CardHeader>
                <CardTitle className="flex items-center gap-2">
                    <Award className="w-5 h-5 text-yellow-500" />
                    Progression vers le certificat
                </CardTitle>
            </CardHeader>
            <CardContent>
                {/* Progress Bar */}
                <div className="mb-4">
                    <div className="flex justify-between text-sm mb-2">
                        <span className="text-slate-600">{completedCount} / {requiredCount} chapitres validés</span>
                        <span className="font-semibold text-slate-900">{Math.round(progress)}%</span>
                    </div>
                    <div className="h-3 bg-slate-200 rounded-full overflow-hidden">
                        <div 
                            className="h-full bg-gradient-to-r from-red-500 to-red-600 rounded-full transition-all duration-500"
                            style={{ width: `${progress}%` }}
                        />
                    </div>
                </div>

                {/* Required Chapters List */}
                {status.remaining && status.remaining.length > 0 && (
                    <div>
                        <p className="text-sm font-medium text-slate-700 mb-2">
                            Chapitres restants à valider :
                        </p>
                        <ul className="space-y-1">
                            {status.remaining.map((chapterId) => (
                                <li key={chapterId} className="flex items-center gap-2 text-sm text-slate-600">
                                    <BookOpen className="w-4 h-4 text-slate-400" />
                                    {chapterId}
                                </li>
                            ))}
                        </ul>
                    </div>
                )}

                {progress === 100 && (
                    <div className="flex items-center gap-2 text-green-600 mt-4">
                        <CheckCircle2 className="w-5 h-5" />
                        <span className="font-medium">Tous les chapitres sont validés !</span>
                    </div>
                )}
            </CardContent>
        </Card>
    );
};

export { CertificatePDF, CertificateBanner, CertificateProgress };
