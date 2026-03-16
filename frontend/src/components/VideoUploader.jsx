import React, { useState, useRef } from 'react';
import { 
    Upload, 
    Video, 
    X, 
    Check, 
    Loader2,
    Link as LinkIcon,
    Play
} from 'lucide-react';
import { Button } from './ui/button';
import { Input } from './ui/input';
import { Label } from './ui/label';
import { uploadVideo } from '../lib/api';
import { toast } from 'sonner';

const VideoUploader = ({ value, onChange, onVideoUploaded }) => {
    const [isUploading, setIsUploading] = useState(false);
    const [uploadProgress, setUploadProgress] = useState(0);
    const [mode, setMode] = useState('url'); // 'url' or 'upload'
    const fileInputRef = useRef(null);

    const handleFileSelect = async (e) => {
        const file = e.target.files?.[0];
        if (!file) return;

        // Validate file type
        const allowedTypes = ['video/mp4', 'video/webm', 'video/ogg', 'video/quicktime'];
        if (!allowedTypes.includes(file.type)) {
            toast.error('Format non supporté. Utilisez MP4, WebM, OGG ou MOV.');
            return;
        }

        // Validate file size (max 100MB)
        if (file.size > 100 * 1024 * 1024) {
            toast.error('Fichier trop volumineux. Maximum 100MB.');
            return;
        }

        setIsUploading(true);
        setUploadProgress(0);

        try {
            const result = await uploadVideo(file);
            const videoUrl = `${process.env.REACT_APP_BACKEND_URL}${result.url}`;
            onChange(videoUrl);
            if (onVideoUploaded) {
                onVideoUploaded(result);
            }
            toast.success('Vidéo uploadée avec succès !');
        } catch (error) {
            console.error('Upload error:', error);
            toast.error(error.response?.data?.detail || 'Erreur lors de l\'upload');
        } finally {
            setIsUploading(false);
            setUploadProgress(0);
        }
    };

    const getVideoPreview = () => {
        if (!value) return null;

        // YouTube
        if (value.includes('youtube.com') || value.includes('youtu.be')) {
            const videoId = value.match(/(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^"&?\/\s]{11})/)?.[1];
            if (videoId) {
                return (
                    <iframe
                        src={`https://www.youtube.com/embed/${videoId}`}
                        className="w-full h-full rounded"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowFullScreen
                        title="Aperçu vidéo"
                    />
                );
            }
        }

        // Vimeo
        if (value.includes('vimeo.com')) {
            const vimeoId = value.match(/vimeo\.com\/(\d+)/)?.[1];
            if (vimeoId) {
                return (
                    <iframe
                        src={`https://player.vimeo.com/video/${vimeoId}`}
                        className="w-full h-full rounded"
                        allow="autoplay; fullscreen; picture-in-picture"
                        allowFullScreen
                        title="Aperçu vidéo"
                    />
                );
            }
        }

        // Direct video URL (uploaded or external)
        return (
            <video
                src={value}
                controls
                className="w-full h-full rounded"
            >
                Votre navigateur ne supporte pas la lecture vidéo.
            </video>
        );
    };

    return (
        <div className="space-y-3">
            {/* Mode selector */}
            <div className="flex gap-2">
                <Button
                    type="button"
                    variant={mode === 'url' ? 'default' : 'outline'}
                    size="sm"
                    onClick={() => setMode('url')}
                    className={mode === 'url' ? 'bg-red-600 hover:bg-red-700' : ''}
                >
                    <LinkIcon className="w-4 h-4 mr-1" />
                    URL
                </Button>
                <Button
                    type="button"
                    variant={mode === 'upload' ? 'default' : 'outline'}
                    size="sm"
                    onClick={() => setMode('upload')}
                    className={mode === 'upload' ? 'bg-red-600 hover:bg-red-700' : ''}
                >
                    <Upload className="w-4 h-4 mr-1" />
                    Uploader
                </Button>
            </div>

            {/* URL Input */}
            {mode === 'url' && (
                <div>
                    <Input
                        value={value || ''}
                        onChange={(e) => onChange(e.target.value)}
                        placeholder="https://youtube.com/watch?v=... ou https://vimeo.com/..."
                    />
                    <p className="text-xs text-slate-500 mt-1">
                        Supporte YouTube, Vimeo ou URL directe de vidéo
                    </p>
                </div>
            )}

            {/* Upload Zone */}
            {mode === 'upload' && (
                <div
                    className={`border-2 border-dashed rounded-lg p-6 text-center transition-colors ${
                        isUploading ? 'border-red-300 bg-red-50' : 'border-slate-300 hover:border-red-400'
                    }`}
                    onClick={() => !isUploading && fileInputRef.current?.click()}
                >
                    <input
                        ref={fileInputRef}
                        type="file"
                        accept="video/mp4,video/webm,video/ogg,video/quicktime"
                        onChange={handleFileSelect}
                        className="hidden"
                    />

                    {isUploading ? (
                        <div className="flex flex-col items-center gap-2">
                            <Loader2 className="w-8 h-8 text-red-600 animate-spin" />
                            <p className="text-sm text-slate-600">Upload en cours...</p>
                        </div>
                    ) : (
                        <div className="flex flex-col items-center gap-2 cursor-pointer">
                            <div className="w-12 h-12 bg-slate-100 rounded-full flex items-center justify-center">
                                <Video className="w-6 h-6 text-slate-400" />
                            </div>
                            <p className="text-sm text-slate-600">
                                Cliquez pour sélectionner une vidéo
                            </p>
                            <p className="text-xs text-slate-400">
                                MP4, WebM, OGG, MOV • Max 100MB
                            </p>
                        </div>
                    )}
                </div>
            )}

            {/* Preview */}
            {value && (
                <div className="relative">
                    <div className="flex items-center justify-between mb-2">
                        <p className="text-xs text-slate-500 flex items-center gap-1">
                            <Play className="w-3 h-3" />
                            Aperçu vidéo
                        </p>
                        <Button
                            type="button"
                            variant="ghost"
                            size="sm"
                            onClick={() => onChange('')}
                            className="text-red-600 hover:text-red-700 h-6 px-2"
                        >
                            <X className="w-3 h-3 mr-1" />
                            Supprimer
                        </Button>
                    </div>
                    <div className="aspect-video bg-black rounded-lg overflow-hidden">
                        {getVideoPreview()}
                    </div>
                </div>
            )}
        </div>
    );
};

export default VideoUploader;
