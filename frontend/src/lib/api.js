import axios from 'axios';

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API_BASE = `${BACKEND_URL}/api`;

// Create axios instance
const api = axios.create({
    baseURL: API_BASE,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Auth helpers
export const getToken = () => localStorage.getItem('secours73_token');
export const getUser = () => {
    const user = localStorage.getItem('secours73_user');
    return user ? JSON.parse(user) : null;
};

export const setAuth = (token, user) => {
    localStorage.setItem('secours73_token', token);
    localStorage.setItem('secours73_user', JSON.stringify(user));
};

export const clearAuth = () => {
    localStorage.removeItem('secours73_token');
    localStorage.removeItem('secours73_user');
};

// API Functions

// Auth - Stagiaire with group code
export const registerStagiaire = async (userData) => {
    const response = await api.post('/auth/register', userData);
    return response.data;
};

// Auth - Free visitor
export const registerVisiteur = async (userData) => {
    const response = await api.post('/auth/register-visiteur', userData);
    return response.data;
};

export const login = async (credentials) => {
    const response = await api.post('/auth/login', credentials);
    return response.data;
};

export const logout = async () => {
    const token = getToken();
    if (token) {
        await api.post(`/auth/logout?token=${token}`);
    }
    clearAuth();
};

export const setPassword = async (newPassword) => {
    const token = getToken();
    const response = await api.post(`/auth/set-password?token=${token}&new_password=${newPassword}`);
    return response.data;
};

export const getMe = async () => {
    const token = getToken();
    const response = await api.get(`/auth/me?token=${token}`);
    return response.data;
};

// Admin APIs
export const adminCreateFormateur = async (data) => {
    const token = getToken();
    const response = await api.post(`/admin/formateur?token=${token}`, data);
    return response.data;
};

export const adminDeleteFormateur = async (formateurId) => {
    const token = getToken();
    const response = await api.delete(`/admin/formateur/${formateurId}?token=${token}`);
    return response.data;
};

export const adminGetFormateurs = async () => {
    const token = getToken();
    const response = await api.get(`/admin/formateurs?token=${token}`);
    return response.data;
};

export const adminGetStats = async () => {
    const token = getToken();
    const response = await api.get(`/admin/stats?token=${token}`);
    return response.data;
};

export const adminCreateQuiz = async (data) => {
    const token = getToken();
    const response = await api.post(`/admin/quiz?token=${token}`, data);
    return response.data;
};

export const adminUpdateQuiz = async (quizId, data) => {
    const token = getToken();
    const response = await api.put(`/admin/quiz/${quizId}?token=${token}`, data);
    return response.data;
};

export const adminDeleteQuiz = async (quizId) => {
    const token = getToken();
    const response = await api.delete(`/admin/quiz/${quizId}?token=${token}`);
    return response.data;
};

// Formateur APIs
export const formateurCreateGroupe = async (data) => {
    const token = getToken();
    const response = await api.post(`/formateur/groupe?token=${token}`, data);
    return response.data;
};

export const formateurGetGroupes = async () => {
    const token = getToken();
    const response = await api.get(`/formateur/groupes?token=${token}`);
    return response.data;
};

export const formateurGetGroupeDetail = async (groupeId) => {
    const token = getToken();
    const response = await api.get(`/formateur/groupe/${groupeId}?token=${token}`);
    return response.data;
};

export const formateurUpdateGroupe = async (groupeId, data) => {
    const token = getToken();
    const response = await api.put(`/formateur/groupe/${groupeId}?token=${token}`, data);
    return response.data;
};

export const formateurInviteCollaborator = async (groupeId, formateurEmail) => {
    const token = getToken();
    const response = await api.post(`/formateur/groupe/${groupeId}/invite?token=${token}`, { 
        formateur_email: formateurEmail,
        groupe_id: groupeId 
    });
    return response.data;
};

export const formateurRemoveCollaborator = async (groupeId, collaborateurId) => {
    const token = getToken();
    const response = await api.delete(`/formateur/groupe/${groupeId}/collaborateur/${collaborateurId}?token=${token}`);
    return response.data;
};

export const formateurGetStagiaireDetail = async (stagiaireId) => {
    const token = getToken();
    const response = await api.get(`/formateur/stagiaire/${stagiaireId}?token=${token}`);
    return response.data;
};

// Stagiaire APIs
export const stagiaireGetProgress = async () => {
    const token = getToken();
    const response = await api.get(`/stagiaire/progress?token=${token}`);
    return response.data;
};

export const stagiaireGetChapitres = async () => {
    const token = getToken();
    const response = await api.get(`/stagiaire/chapitres?token=${token}`);
    return response.data;
};

// Chapters
export const getChapters = async (formationType = 'PSE') => {
    const response = await api.get(`/chapters?formation_type=${formationType}`);
    return response.data;
};

export const getChaptersPreview = async () => {
    const response = await api.get('/chapters/preview');
    return response.data;
};

export const getChapter = async (chapterId) => {
    const token = getToken();
    const url = token ? `/chapters/${chapterId}?token=${token}` : `/chapters/${chapterId}`;
    const response = await api.get(url);
    return response.data;
};

// PSC Chapters (free access)
export const getPSCChapters = async () => {
    const response = await api.get('/psc/chapters');
    return response.data;
};

// BNSSA Chapters (restricted)
export const getBNSSAChapters = async () => {
    const token = getToken();
    const response = await api.get(`/bnssa/chapters?token=${token}`);
    return response.data;
};

// Quizzes
export const getQuizzes = async () => {
    const response = await api.get('/quizzes');
    return response.data;
};

export const getQuizById = async (quizId) => {
    const response = await api.get(`/quizzes/${quizId}`);
    return response.data;
};

export const getQuizByChapter = async (chapterId) => {
    const response = await api.get(`/quizzes/chapter/${chapterId}`);
    return response.data;
};

export const submitQuiz = async (submission) => {
    const token = getToken();
    const response = await api.post(`/quizzes/submit?token=${token}`, submission);
    return response.data;
};

export const getQuizResults = async () => {
    const token = getToken();
    const response = await api.get(`/quiz-results?token=${token}`);
    return response.data;
};

// Seed database
export const seedDatabase = async () => {
    const response = await api.post('/seed');
    return response.data;
};

// Site Settings
export const getSiteSettings = async () => {
    const response = await api.get('/settings');
    return response.data;
};

export const updateSiteSettings = async (settings) => {
    const token = getToken();
    const response = await api.put(`/admin/settings?token=${token}`, settings);
    return response.data;
};

export const getSiteImages = async () => {
    const token = getToken();
    const response = await api.get(`/admin/images?token=${token}`);
    return response.data;
};

export const createSiteImage = async (image) => {
    const token = getToken();
    const response = await api.post(`/admin/images?token=${token}`, image);
    return response.data;
};

export const updateSiteImage = async (imageId, image) => {
    const token = getToken();
    const response = await api.put(`/admin/images/${imageId}?token=${token}`, image);
    return response.data;
};

export const deleteSiteImage = async (imageId) => {
    const token = getToken();
    const response = await api.delete(`/admin/images/${imageId}?token=${token}`);
    return response.data;
};

// ============== ADMIN CHAPTER MANAGEMENT ==============

export const adminCreateChapter = async (chapterData) => {
    const token = getToken();
    const response = await api.post(`/admin/chapter?token=${token}`, chapterData);
    return response.data;
};

export const adminUpdateChapter = async (chapterId, chapterData) => {
    const token = getToken();
    const response = await api.put(`/admin/chapter/${chapterId}?token=${token}`, chapterData);
    return response.data;
};

export const adminDeleteChapter = async (chapterId) => {
    const token = getToken();
    const response = await api.delete(`/admin/chapter/${chapterId}?token=${token}`);
    return response.data;
};

// ============== PASSWORD RESET ==============

export const forgotPassword = async (email) => {
    const response = await api.post('/auth/forgot-password', { email });
    return response.data;
};

export const resetPassword = async (token, new_password) => {
    const response = await api.post('/auth/reset-password', { token, new_password });
    return response.data;
};

// ============== MESSAGERIE ==============

export const sendMessage = async (destinataire_id, sujet, contenu) => {
    const token = getToken();
    const response = await api.post(`/messages?token=${token}`, { destinataire_id, sujet, contenu });
    return response.data;
};

export const getReceivedMessages = async () => {
    const token = getToken();
    const response = await api.get(`/messages/received?token=${token}`);
    return response.data;
};

export const getSentMessages = async () => {
    const token = getToken();
    const response = await api.get(`/messages/sent?token=${token}`);
    return response.data;
};

export const markMessageAsRead = async (messageId) => {
    const token = getToken();
    const response = await api.put(`/messages/${messageId}/read?token=${token}`);
    return response.data;
};

export const getUnreadCount = async () => {
    const token = getToken();
    const response = await api.get(`/messages/unread-count?token=${token}`);
    return response.data;
};

// ============== EMAILS ==============

export const formateurSendEmail = async (to_email, subject, message) => {
    const token = getToken();
    const response = await api.post(`/formateur/send-email?token=${token}&to_email=${to_email}&subject=${encodeURIComponent(subject)}&message=${encodeURIComponent(message)}`);
    return response.data;
};

export const sendWelcomeEmail = async (stagiaire_email) => {
    const token = getToken();
    const response = await api.post(`/admin/send-welcome-email?token=${token}&stagiaire_email=${stagiaire_email}`);
    return response.data;
};

// ============== DOCUMENTS ==============

export const uploadDocument = async (formData) => {
    const token = getToken();
    const response = await api.post(`/formateur/document/upload?token=${token}`, formData, {
        headers: {
            'Content-Type': 'multipart/form-data',
        },
    });
    return response.data;
};

export const getStagiaireDocuments = async () => {
    const token = getToken();
    const response = await api.get(`/stagiaire/documents?token=${token}`);
    return response.data;
};

export const getFormateurDocuments = async () => {
    const token = getToken();
    const response = await api.get(`/formateur/documents?token=${token}`);
    return response.data;
};

export const downloadDocument = async (docId) => {
    const token = getToken();
    const response = await api.get(`/documents/${docId}/download?token=${token}`, {
        responseType: 'blob',
    });
    return response.data;
};

export const deleteDocument = async (docId) => {
    const token = getToken();
    const response = await api.delete(`/formateur/document/${docId}?token=${token}`);
    return response.data;
};

// Certificate APIs
export const getCertificateStatus = async () => {
    const token = getToken();
    const response = await api.get(`/stagiaire/certificate/status?token=${token}`);
    return response.data;
};

export const generateCertificate = async () => {
    const token = getToken();
    const response = await api.get(`/stagiaire/certificate/generate?token=${token}`);
    return response.data;
};

export const downloadCertificatePDF = async () => {
    const token = getToken();
    const response = await api.get(`/stagiaire/certificate/pdf?token=${token}`, {
        responseType: 'blob'
    });
    return response.data;
};

export const getCertificateConfig = async (groupeId) => {
    const token = getToken();
    const response = await api.get(`/certificates/config/${groupeId}?token=${token}`);
    return response.data;
};

export const setCertificateConfig = async (groupeId, chapitresObligatoires) => {
    const token = getToken();
    const response = await api.post(`/certificates/config/${groupeId}?token=${token}`, {
        chapitres_obligatoires: chapitresObligatoires
    });
    return response.data;
};

// Video Upload APIs
export const uploadVideo = async (file) => {
    const token = getToken();
    const formData = new FormData();
    formData.append('file', file);
    
    const response = await api.post(`/upload/video?token=${token}`, formData, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    });
    return response.data;
};

export const deleteVideo = async (videoId) => {
    const token = getToken();
    const response = await api.delete(`/videos/${videoId}?token=${token}`);
    return response.data;
};

export default api;
