# FAOD-SECOURS73 - Plateforme de Formation aux Premiers Secours

## Original Problem Statement
Application de formation aux premiers secours pour le département de Savoie (73). Plateforme permettant la gestion de formations PSE, BNSSA et PSC.

## Architecture
- **Frontend**: React.js avec TailwindCSS
- **Backend**: FastAPI (Python)
- **Base de données**: MongoDB
- **PDF**: ReportLab
- **Email**: Resend API
- **Authentification**: JWT token-based avec multi-rôles

## User Personas
1. **Admin**: Gestion globale (formateurs, chapitres, quiz, certificats)
2. **Formateur**: Gestion de groupes, suivi des stagiaires, documents, configuration certificats
3. **Stagiaire**: Progression formation, quiz, certificat PDF
4. **Visiteur**: Accès gratuit PSC

## What's Been Implemented

### Sessions précédentes - Base + Enrichissement
- ✅ Système d'authentification multi-rôles
- ✅ Gestion des groupes de formation avec seuil personnalisable
- ✅ 12 chapitres PSE et 8 chapitres PSC complets (référentiel 2024)
- ✅ Quiz QCM et Vrai/Faux
- ✅ Progression des stagiaires avec déblocage séquentiel
- ✅ Logo de l'association intégré

### Fonctionnalités Certificats, Email, Vidéos
- ✅ **Génération PDF certificats** (ReportLab):
  - Endpoint `/api/stagiaire/certificate/pdf`
  - Logo, nom, prénom, score moyen, date
  - Format paysage A4 professionnel
- ✅ **Notifications email** (Resend):
  - Email au formateur quand un stagiaire obtient son certificat
  - "M. X a validé la FAOD PSE 1"
  - Configuration via `RESEND_API_KEY` dans .env
- ✅ **Upload vidéos direct**:
  - Endpoint `/api/upload/video` (max 100MB)
  - Formats: MP4, WebM, OGG, MOV
  - Streaming via `/api/videos/{id}`
  - Composant `VideoUploader.jsx` avec onglets URL/Upload
- ✅ **Bannière de félicitations** quand certificat débloqué
- ✅ **Bouton télécharger PDF** dans le modal certificat

### Vérification Déploiement (Janvier 2026)
- ✅ Health check API réussi
- ✅ Tous les services opérationnels
- ✅ Variables d'environnement correctes
- ✅ CORS configuré correctement
- ✅ Application prête pour le déploiement

## Comptes de test

| Rôle | Email | Mot de passe | Notes |
|------|-------|--------------|-------|
| Admin | ledisque.tanguy73@hotmail.com | NewAdmin123! | Accès complet |
| Formateur test | test@secours73.fr | test123 | Groupe Test (seuil 0%) |
| Stagiaire test | stagiaire.test@secours73.fr | test123 | Certificat débloqué |
| Code groupe | - | TEST0000 | Seuil 0% |

## API Endpoints

### Authentification
- `POST /api/auth/register` - Inscription stagiaire avec code groupe
- `POST /api/auth/register-visiteur` - Inscription visiteur gratuit
- `POST /api/auth/login` - Connexion
- `GET /api/auth/me` - Utilisateur courant

### Chapitres
- `GET /api/chapters?formation_type=PSE` - Chapitres PSE
- `GET /api/psc/chapters` - Chapitres PSC (gratuit)
- `GET /api/chapters/{id}` - Détail chapitre

### Certificats
- `GET /api/stagiaire/certificate/status` - Vérifier si certificat débloqué
- `GET /api/stagiaire/certificate/generate` - Données du certificat (JSON)
- `GET /api/stagiaire/certificate/pdf` - Télécharger le PDF
- `GET /api/certificates/config/{groupe_id}` - Config chapitres obligatoires
- `POST /api/certificates/config/{groupe_id}` - Définir chapitres obligatoires

### Vidéos
- `POST /api/upload/video` - Upload vidéo (100MB max)
- `GET /api/videos/{id}` - Streaming vidéo
- `DELETE /api/videos/{id}` - Supprimer vidéo

## Configuration Email (Resend)

```env
RESEND_API_KEY="re_PnhTe82d_..."
SENDER_EMAIL="onboarding@resend.dev"
```

⚠️ **Note**: Pour envoyer des emails à des destinataires externes, vérifier un domaine sur resend.com/domains et changer `SENDER_EMAIL`.

## État du Déploiement

**Status: PRÊT POUR LE DÉPLOIEMENT**

### Checks passés:
- ✅ Compilation OK
- ✅ Variables d'environnement OK
- ✅ URLs frontend dans .env uniquement
- ✅ Backend utilise MONGO_URL et DB_NAME depuis .env
- ✅ CORS autorise les origines de production
- ✅ Configuration Supervisor valide
- ✅ Pas de problèmes de dotenv override

### Avertissements (non-bloquants):
- Scripts utilitaires avec connexions MongoDB hardcodées (pas utilisés en runtime)
- Dépendances AI/ML dans requirements.txt non utilisées (peuvent être nettoyées)

## Prioritized Backlog

### P0 - Critical (FAIT)
- ✅ Toutes les fonctionnalités demandées implémentées
- ✅ Vérification déploiement complète

### P1 - High Priority
- [ ] Vérifier domaine Resend pour emails externes
- [ ] Statistiques avancées formateur
- [ ] Export données progression

### P2 - Medium Priority  
- [ ] Mode hors-ligne
- [ ] Rappels email pour stagiaires inactifs
- [ ] Nettoyer dépendances inutilisées

### P3 - Low Priority
- [ ] App mobile native
- [ ] Intégration HelloAsso

## Next Tasks
1. Déployer l'application via bouton "Deploy" sur Emergent
2. Vérifier domaine sur Resend pour envoyer aux vrais formateurs
3. Ajouter plus de vidéos pédagogiques
4. Statistiques avancées pour le dashboard formateur
