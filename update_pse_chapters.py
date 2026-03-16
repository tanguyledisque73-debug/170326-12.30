#!/usr/bin/env python3
"""
Script pour enrichir les chapitres PSE avec distinction PSE 1 / PSE 2
Basé sur le référentiel national PSE 2024
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from pathlib import Path

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / 'backend' / '.env')

mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

pse_chapters = [
    {
        "id": "ch1",
        "numero": 1,
        "titre": "Attitude et comportement du secouriste",
        "description": "Le rôle du citoyen secouriste, attitude professionnelle, abord relationnel de la victime, gestion du stress.",
        "icon": "Shield",
        "formation_type": "PSE",
        "image_url": "https://images.unsplash.com/photo-1612277795421-9bc7706a4a34",
        "fiches": [
            {
                "id": "ch1-f1",
                "titre": "Le secouriste : rôle et mission",
                "contenu": """## Le secouriste : rôle et mission

### 🎯 PSE 1 - Notions fondamentales

Le secouriste est un maillon essentiel de la chaîne des secours. Il intervient en premier sur les lieux d'un accident ou d'un malaise.

**Missions principales :**
- **Protéger** la victime et les témoins
- **Alerter** les secours adaptés
- **Secourir** en attendant les renforts

**Cadre juridique :**
- L'article 223-6 du Code pénal impose l'obligation de porter assistance
- Protection juridique pour les actes de secours de bonne foi
- Respect du secret professionnel

---

### 🎯 PSE 2 - Notions complémentaires

**Responsabilités élargies :**
- Coordination d'une équipe de secouristes
- Prise de décision en situation complexe
- Interface avec les services de secours professionnels
- Transmission du bilan aux équipes médicales

**Chef d'équipe PSE 2 :**
- Répartition des tâches
- Supervision des gestes techniques
- Gestion des ressources matérielles"""
            },
            {
                "id": "ch1-f2",
                "titre": "Communication et relation avec la victime",
                "contenu": """## Communication et relation avec la victime

### 🎯 PSE 1 - L'abord relationnel

**Principes de base :**
- Se présenter clairement (nom, qualité)
- Se mettre à hauteur de la victime
- Utiliser un ton calme et rassurant
- Expliquer chaque geste avant de l'effectuer

**Communication verbale :**
- Questions simples et fermées
- Reformulation pour vérifier la compréhension
- Éviter le jargon médical

**Communication non verbale :**
- Contact visuel
- Posture ouverte et rassurante
- Gestes doux et prévenants

---

### 🎯 PSE 2 - Situations particulières

**Victimes en état de choc émotionnel :**
- Laisser la victime s'exprimer
- Ne pas minimiser ses émotions
- Proposer une présence silencieuse si besoin

**Communication avec les proches :**
- Information factuelle sans pronostic
- Orientation vers les professionnels de santé
- Gestion des réactions émotionnelles

**Annonce d'un décès :**
- Formation spécifique requise
- Accompagnement des proches
- Respect des protocoles établis"""
            },
            {
                "id": "ch1-f3",
                "titre": "Gestion du stress opérationnel",
                "contenu": """## Gestion du stress opérationnel

### 🎯 PSE 1 - Reconnaître et gérer son stress

**Réactions normales face à l'urgence :**
- Accélération du rythme cardiaque
- Transpiration
- Sensation de tension
- Difficultés de concentration

**Techniques de gestion immédiate :**
- Respiration abdominale profonde
- Ancrage au sol (sentir ses pieds)
- Se concentrer sur les gestes appris
- Verbaliser ses actions

---

### 🎯 PSE 2 - Prévention et récupération

**Préparation mentale :**
- Visualisation des procédures
- Entraînement régulier
- Connaissance de ses limites

**Après l'intervention :**
- Débriefing technique et émotionnel
- Verbalisation avec les pairs
- Repos adapté

**Signes d'alerte (stress post-traumatique) :**
- Flashbacks récurrents
- Troubles du sommeil persistants
- Évitement des situations similaires
- Irritabilité inhabituelle

➡️ **Consulter un professionnel si les symptômes persistent au-delà de 4 semaines**"""
            }
        ]
    },
    {
        "id": "ch2",
        "numero": 2,
        "titre": "Bilan et surveillance",
        "description": "Réalisation du bilan d'urgence vitale, bilan complémentaire, surveillance et transmission.",
        "icon": "ClipboardList",
        "formation_type": "PSE",
        "image_url": "https://images.unsplash.com/photo-1579684385127-1ef15d508118",
        "fiches": [
            {
                "id": "ch2-f1",
                "titre": "Le bilan d'urgence vitale",
                "contenu": """## Le bilan d'urgence vitale

### 🎯 PSE 1 - Bilan immédiat

**Ordre d'évaluation (ABCDE) :**

| Lettre | Signification | Évaluation |
|--------|---------------|------------|
| **A** | Airway (Voies aériennes) | Libres ? Obstruées ? |
| **B** | Breathing (Respiration) | Présente ? Efficace ? |
| **C** | Circulation | Pouls ? Hémorragie ? |
| **D** | Disability (Neurologique) | Conscience ? Réactivité ? |
| **E** | Exposure (Exposition) | Lésions visibles ? |

**Évaluation de la conscience :**
- Poser une question simple
- Donner un ordre simple
- Stimulation douloureuse si pas de réponse

**Évaluation de la respiration :**
- Regarder le thorax se soulever
- Écouter le souffle
- Sentir l'air sur sa joue
- ⏱️ **10 secondes maximum**

---

### 🎯 PSE 2 - Bilan approfondi

**Paramètres vitaux à mesurer :**
- Fréquence respiratoire (FR)
- Fréquence cardiaque (FC)
- Pression artérielle (PA)
- Saturation en oxygène (SpO2)
- Température
- Glycémie capillaire (si indication)

**Échelle de Glasgow (GCS) :**

| Réponse | Score |
|---------|-------|
| **Ouverture des yeux** | 1-4 |
| **Réponse verbale** | 1-5 |
| **Réponse motrice** | 1-6 |
| **Total** | 3-15 |

⚠️ GCS ≤ 8 = Coma = Protection des voies aériennes"""
            },
            {
                "id": "ch2-f2",
                "titre": "Le bilan complémentaire",
                "contenu": """## Le bilan complémentaire

### 🎯 PSE 1 - Interrogatoire SAMPLE

| Lettre | Question |
|--------|----------|
| **S** | Signes et symptômes ? |
| **A** | Allergies connues ? |
| **M** | Médicaments en cours ? |
| **P** | Passé médical / chirurgical ? |
| **L** | Last meal (dernier repas) ? |
| **E** | Événement déclencheur ? |

**Examen de la tête aux pieds :**
- Recherche de déformations
- Recherche de plaies
- Recherche de douleurs
- Recherche de saignements

---

### 🎯 PSE 2 - Bilan circonstanciel et lésionnel

**Analyse de la scène :**
- Mécanisme de l'accident
- Énergie cinétique impliquée
- Position de la victime à l'arrivée
- Témoignages recueillis

**Examen segmentaire détaillé :**

| Segment | Rechercher |
|---------|------------|
| Crâne | Plaie, hématome, écoulement |
| Rachis cervical | Douleur, déformation |
| Thorax | Asymétrie, volet costal |
| Abdomen | Défense, rigidité |
| Bassin | Instabilité (1 seule fois) |
| Membres | Déformation, pouls distaux |

**Critères de gravité (critères de Vittel) :**
- Éjection du véhicule
- Décès d'un autre passager
- Chute > 6 mètres
- Victime projetée ou écrasée"""
            },
            {
                "id": "ch2-f3",
                "titre": "Transmission et surveillance",
                "contenu": """## Transmission et surveillance

### 🎯 PSE 1 - Alerte et transmission de base

**Contenu du message d'alerte :**
1. Qui appelle (identité, qualité)
2. Où (adresse précise, point de repère)
3. Quoi (nature du problème)
4. Combien de victimes
5. Premières mesures prises
6. Besoin de renforts ?

**Surveillance continue :**
- État de conscience
- Respiration
- Coloration de la peau
- Évolution des plaintes

---

### 🎯 PSE 2 - Bilan transmis au médecin

**Structure du bilan (méthode SBAR) :**

| Étape | Contenu |
|-------|---------|
| **S**ituation | Identité, motif d'intervention |
| **B**ackground | Circonstances, antécédents |
| **A**ssessment | Constantes, lésions, évolution |
| **R**ecommandation | Actions réalisées, besoins |

**Feuille de bilan :**
- Horaires précis des événements
- Constantes répétées (toutes les 5-10 min)
- Gestes effectués
- Évolution de l'état

**Transmission au SAMU :**
- Appel au 15
- Bilan structuré
- Réponse aux questions du médecin régulateur
- Application des consignes médicales"""
            }
        ]
    },
    {
        "id": "ch3",
        "numero": 3,
        "titre": "Protection et sécurité",
        "description": "Protection individuelle et collective, sécurisation de zone, dégagement d'urgence.",
        "icon": "ShieldAlert",
        "formation_type": "PSE",
        "image_url": "https://images.unsplash.com/photo-1582139329536-e7284fece509",
        "fiches": [
            {
                "id": "ch3-f1",
                "titre": "Protection individuelle et collective",
                "contenu": """## Protection individuelle et collective

### 🎯 PSE 1 - Principes de base

**Protection individuelle :**
- Équipements de protection individuelle (EPI)
- Gants à usage unique (obligatoires)
- Masque de protection respiratoire
- Lunettes de protection si risque de projection

**Les dangers :**
- Dangers visibles (feu, fumée, eau)
- Dangers invisibles (gaz, électricité)
- Dangers potentiels (sur-accident)

**Actions de protection :**
1. Identifier le(s) danger(s)
2. Supprimer le danger si possible
3. Éloigner la victime du danger
4. Isoler le danger (baliser la zone)

---

### 🎯 PSE 2 - Sécurisation avancée

**Zonage d'intervention :**

| Zone | Couleur | Accès |
|------|---------|-------|
| Exclusion | Rouge | Secouristes équipés |
| Contrôlée | Orange | Secouristes |
| Soutien | Verte | Public, logistique |

**Balisage réglementaire :**
- Triangles de signalisation
- Cônes et rubalise
- Signaleur si nécessaire
- Coordination avec les forces de l'ordre

**Risques NRBC :**
- Nucléaire
- Radiologique
- Biologique
- Chimique
➡️ Ne pas intervenir sans équipement adapté"""
            },
            {
                "id": "ch3-f2",
                "titre": "Dégagement d'urgence",
                "contenu": """## Dégagement d'urgence

### 🎯 PSE 1 - Techniques de base

**Indication :**
Le dégagement d'urgence est **EXCEPTIONNEL** et justifié uniquement si :
- La victime est exposée à un danger vital immédiat
- Il est impossible de supprimer le danger
- Le sauveteur ne se met pas en danger

**Techniques pour victime au sol :**

**Traction par les chevilles :**
- Victime sur le dos
- Saisir les chevilles
- Tirer dans l'axe du corps
- Terrain plat uniquement

**Traction par les poignets :**
- Saisir les deux poignets
- Tirer dans l'axe
- Surveiller la tête

**Traction par les vêtements :**
- Saisir les vêtements au niveau des épaules
- Caler la tête entre ses avant-bras
- Tirer en reculant

---

### 🎯 PSE 2 - Dégagements complexes

**Dégagement d'un véhicule :**
- Évaluation rapide de l'accès
- Stabilisation du véhicule
- Protection de la victime (couverture)
- Maintien de l'axe tête-cou-tronc
- Extraction sur plan dur si disponible

**Sauvetage en équipe :**
- Un secouriste maintient la tête
- Un secouriste aux épaules
- Un secouriste au bassin
- Commandements clairs
- Mouvements synchronisés"""
            }
        ]
    },
    {
        "id": "ch4",
        "numero": 4,
        "titre": "Hygiène et asepsie",
        "description": "Règles d'hygiène, prévention des infections, nettoyage et désinfection du matériel.",
        "icon": "Sparkles",
        "formation_type": "PSE",
        "image_url": "https://images.unsplash.com/photo-1584515933487-779824d29309",
        "fiches": [
            {
                "id": "ch4-f1",
                "titre": "Hygiène des mains et EPI",
                "contenu": """## Hygiène des mains et équipements de protection

### 🎯 PSE 1 - Règles fondamentales

**Hygiène des mains :**
La transmission manuportée est la principale voie de contamination.

**Lavage des mains (eau + savon) :**
1. Mouiller les mains
2. Savonner 30 secondes minimum
3. Frotter toutes les surfaces (paumes, dos, entre les doigts, ongles)
4. Rincer abondamment
5. Sécher avec un essuie-mains à usage unique

**Friction hydro-alcoolique (SHA) :**
- Sur mains visuellement propres
- 3 ml de solution
- Frotter jusqu'à séchage complet (30 sec)

**Quand se laver les mains :**
- Avant et après chaque contact avec une victime
- Après avoir retiré les gants
- Après contact avec des liquides biologiques

---

### 🎯 PSE 2 - Équipements de protection

**Gants :**
- Usage unique obligatoire
- Changer entre chaque victime
- Retrait sans se contaminer

**Masque chirurgical :**
- Protection contre les projections
- À porter si risque de contact avec sécrétions

**Masque FFP2 :**
- Maladies à transmission aérienne
- Tuberculose, COVID-19, grippe

**Surblouse :**
- Risque de projection importante
- Aide au relevage de victime souillée"""
            },
            {
                "id": "ch4-f2",
                "titre": "Accidents d'exposition au sang (AES)",
                "contenu": """## Accidents d'exposition au sang

### 🎯 PSE 1 - Conduite à tenir immédiate

**Définition :**
Contact avec du sang ou liquide biologique lors d'une effraction cutanée ou projection sur muqueuse.

**Conduite immédiate :**

**En cas de piqûre ou coupure :**
1. Ne pas faire saigner
2. Nettoyer à l'eau et au savon
3. Rincer abondamment
4. Tremper 5 min dans Dakin ou eau de Javel diluée
5. Rincer et sécher

**En cas de projection oculaire :**
1. Rincer abondamment à l'eau claire
2. Pendant 5 minutes minimum
3. Du coin interne vers l'externe

---

### 🎯 PSE 2 - Démarches administratives

**Déclaration obligatoire :**
- Dans les 24 heures
- Certificat médical initial
- Déclaration d'accident de travail

**Consultation médicale urgente :**
- Aux urgences ou médecin référent
- Évaluation du risque de contamination
- Décision de traitement post-exposition (TPE)
- Suivi sérologique

**Risques infectieux :**
- VIH (risque 0.3% si piqûre)
- Hépatite B (risque 30%)
- Hépatite C (risque 3%)

➡️ **La vaccination contre l'hépatite B est obligatoire pour les secouristes**"""
            }
        ]
    },
    {
        "id": "ch5",
        "numero": 5,
        "titre": "Urgences vitales",
        "description": "Obstruction des voies aériennes, hémorragies, arrêt cardiaque, détresses vitales.",
        "icon": "HeartPulse",
        "formation_type": "PSE",
        "image_url": "https://images.unsplash.com/photo-1631815589968-fdb09a223b1e",
        "fiches": [
            {
                "id": "ch5-f1",
                "titre": "Obstruction des voies aériennes",
                "contenu": """## Obstruction des voies aériennes

### 🎯 PSE 1 - Reconnaissance et gestes de base

**Obstruction PARTIELLE :**
- La victime tousse, parle ou pleure
- Respiration sifflante possible
- ➡️ Encourager à tousser, ne rien faire d'autre
- ➡️ Surveiller l'évolution

**Obstruction TOTALE :**
- Impossibilité de parler, tousser, respirer
- Agitation, mains à la gorge
- Cyanose progressive

**Conduite à tenir - Adulte/Enfant :**

**1. Claques dans le dos (1 à 5) :**
- Pencher la victime en avant
- Claques entre les omoplates
- Avec le talon de la main

**2. Compressions abdominales - Heimlich (1 à 5) :**
- Se placer derrière la victime
- Poing au-dessus du nombril
- Compressions vers l'arrière et le haut

**Alterner jusqu'à désobstruction ou perte de connaissance**

---

### 🎯 PSE 2 - Cas particuliers et matériel

**Nourrisson :**
- Claques dans le dos (tête en bas)
- Compressions thoraciques (pas abdominales)

**Femme enceinte / Obèse :**
- Compressions thoraciques

**Victime inconsciente :**
- Allonger, appeler les secours
- Débuter la RCP
- Vérifier la bouche à chaque cycle

**Matériel PSE 2 :**
- Pince de Magill (extraction sous laryngoscopie)
- Aspirateur de mucosités
- Canule oropharyngée (Guedel)"""
            },
            {
                "id": "ch5-f2",
                "titre": "Hémorragies externes",
                "contenu": """## Hémorragies externes

### 🎯 PSE 1 - Compression et garrot

**Définition :**
Saignement abondant qui ne s'arrête pas spontanément et imbibe un mouchoir en quelques secondes.

**Compression directe :**
1. Appuyer fortement sur la plaie
2. Avec la main (gantée) ou un tissu propre
3. Maintenir la pression jusqu'à l'arrivée des secours

**Pansement compressif :**
- Si la compression manuelle contrôle le saignement
- Coussin hémostatique + bande large
- Ne pas desserrer

**Garrot :**
Indications :
- Compression directe impossible ou inefficace
- Multiples victimes (situation de catastrophe)
- Amputation traumatique

Réalisation :
- 5-7 cm au-dessus de la plaie
- Jamais sur une articulation
- Serrer jusqu'à arrêt du saignement
- Noter l'heure de pose
- ⚠️ **Ne jamais desserrer sans avis médical**

---

### 🎯 PSE 2 - Pansements hémostatiques

**Pansement compressif d'urgence (type israelien) :**
- Compresse intégrée
- Système de serrage
- Application rapide

**Agents hémostatiques :**
- QuikClot, Celox
- À plaquer dans la plaie
- Compression maintenue 3 minutes
- Réservé aux plaies jonctionnelles

**Points de compression à distance :**
- Artère fémorale (pli de l'aine)
- Artère humérale (face interne du bras)
- En dernier recours si garrot impossible"""
            },
            {
                "id": "ch5-f3",
                "titre": "Arrêt cardiaque et RCP",
                "contenu": """## Arrêt cardiaque et RCP

### 🎯 PSE 1 - Réanimation de base

**Reconnaissance :**
- Victime inconsciente
- Ne respire pas ou gasps (respiration agonale)
- ➡️ C'est un arrêt cardiaque

**Chaîne de survie :**
1. Reconnaissance et alerte précoce
2. RCP précoce
3. Défibrillation précoce
4. Soins médicalisés

**RCP adulte :**
- 30 compressions / 2 insufflations
- Fréquence : 100-120/min
- Profondeur : 5-6 cm
- Relâchement complet entre les compressions

**RCP enfant/nourrisson :**
- 15 compressions / 2 insufflations
- 5 insufflations initiales si origine asphyxique
- Profondeur : 1/3 du thorax

**Utilisation du DAE :**
- Mettre en marche dès disponible
- Suivre les instructions vocales
- Ne pas toucher la victime pendant l'analyse
- Choc si conseillé, reprendre RCP immédiatement après

---

### 🎯 PSE 2 - RCP médicalisée

**Matériel complémentaire :**
- BAVU (Ballon Auto-remplisseur à Valve Unidirectionnelle)
- Canule de Guedel
- Oxygène (15 L/min)
- Aspirateur de mucosités

**Ventilation au BAVU :**
- Canule de Guedel en place
- Tête en hyperextension
- Masque étanche
- Volume : soulèvement thoracique visible
- 1 insufflation par seconde

**Massage cardiaque mécanique :**
- Planche de massage
- Relais toutes les 2 minutes
- Compression/décompression active

**Administration d'adrénaline :**
- Sur prescription médicale uniquement
- 1 mg IV toutes les 3-5 min
- Voie intra-osseuse si IV impossible"""
            },
            {
                "id": "ch5-f4",
                "titre": "Détresses vitales",
                "contenu": """## Détresses vitales

### 🎯 PSE 1 - Reconnaissance des détresses

**Détresse respiratoire :**
- Difficulté à respirer, à parler
- Fréquence respiratoire anormale (< 10 ou > 30/min)
- Cyanose (lèvres, ongles bleutés)
- Tirage (muscles du cou contractés)
- Sueurs, agitation

**Détresse circulatoire (choc) :**
- Pâleur, marbrures
- Pouls rapide et faible
- Temps de recoloration cutanée > 3 sec
- Soif, angoisse
- Troubles de la conscience

**Détresse neurologique :**
- Troubles de la conscience (GCS < 15)
- Asymétrie pupillaire
- Déficit moteur ou sensitif
- Convulsions

---

### 🎯 PSE 2 - Prise en charge spécifique

**Détresse respiratoire :**
- Position demi-assise
- Oxygénothérapie (15 L/min au masque HC)
- Surveillance SpO2
- Préparer matériel d'aspiration

**Détresse circulatoire :**
- Position allongée, jambes surélevées
- Lutter contre l'hypothermie
- Oxygénothérapie
- Voie veineuse (si formé)

**Détresse neurologique :**
- PLS si inconscience
- Protection des voies aériennes
- Surveillance GCS toutes les 5 min
- Glycémie capillaire

**Critères de gravité extrême :**
- SpO2 < 90%
- PA systolique < 90 mmHg
- GCS ≤ 8
➡️ **Médicalisation urgente**"""
            }
        ]
    },
    {
        "id": "ch6",
        "numero": 6,
        "titre": "Malaises et affections spécifiques",
        "description": "Malaises, AVC, douleur thoracique, diabète, convulsions, allergies.",
        "icon": "Activity",
        "formation_type": "PSE",
        "image_url": "https://images.unsplash.com/photo-1576091160550-2173dba999ef",
        "fiches": [
            {
                "id": "ch6-f1",
                "titre": "Malaise et prise en charge générale",
                "contenu": """## Malaise : prise en charge générale

### 🎯 PSE 1 - Conduite à tenir

**Définition :**
Sensation pénible traduisant un trouble du fonctionnement de l'organisme, sans cause immédiatement identifiable.

**Signes d'alerte :**
- Douleur thoracique
- Difficulté à respirer
- Paralysie, trouble de la parole
- Perte de connaissance brève

**Conduite à tenir :**
1. Mettre la victime au repos (position de confort)
2. Questionner (SAMPLE)
3. Desserrer les vêtements
4. Rassurer
5. Alerter le 15 si signes de gravité
6. Surveiller

**Position adaptée :**
- Allongée si malaise vagal
- Demi-assise si gêne respiratoire
- Position choisie par la victime sinon

---

### 🎯 PSE 2 - Bilan et surveillance

**Constantes à relever :**
- Fréquence cardiaque
- Pression artérielle
- SpO2
- Glycémie si indication
- Température

**Transmission au 15 :**
- Circonstances de survenue
- Antécédents et traitement
- Signes présentés
- Évolution depuis le début
- Gestes effectués"""
            },
            {
                "id": "ch6-f2",
                "titre": "AVC et douleur thoracique",
                "contenu": """## AVC et douleur thoracique

### 🎯 PSE 1 - Reconnaissance et alerte

**AVC - Signes FAST :**
- **F**ace : Asymétrie du visage
- **A**rm : Faiblesse d'un bras
- **S**peech : Troubles de la parole
- **T**ime : Noter l'heure de début

⏱️ **URGENCE ABSOLUE - Appeler le 15 immédiatement**

**Douleur thoracique suspecte :**
- Douleur en étau, oppressante
- Irradiation bras gauche, mâchoire, dos
- Sueurs, nausées
- Angoisse intense

➡️ Position demi-assise
➡️ Ne pas mobiliser
➡️ Appeler le 15

---

### 🎯 PSE 2 - Prise en charge

**AVC :**
- Position adaptée (demi-assise si conscient)
- Oxygénothérapie si SpO2 < 94%
- Glycémie capillaire
- Surveillance neurologique (GCS)
- Ne rien donner à boire ni à manger

**Syndrome coronarien aigu :**
- Position demi-assise stricte
- Oxygénothérapie si SpO2 < 94%
- Défibrillateur à proximité
- Préparation TNT sublinguale si prescrit
- ECG si disponible et formé"""
            },
            {
                "id": "ch6-f3",
                "titre": "Diabète, convulsions, allergies",
                "contenu": """## Situations spécifiques

### 🎯 PSE 1 - Reconnaissance

**Hypoglycémie :**
- Sueurs, pâleur, tremblements
- Faim, fatigue intense
- Troubles du comportement
- Confusion, agressivité
➡️ Si conscient : resucrage (15g de sucre)
➡️ Si inconscient : PLS, appeler le 15

**Convulsions :**
- Mouvements anormaux involontaires
- Perte de connaissance
- Phase de récupération (confusion)
➡️ Protéger des traumatismes
➡️ Ne rien mettre dans la bouche
➡️ PLS après la crise

**Réaction allergique grave :**
- Urticaire, œdème du visage
- Gêne respiratoire
- Malaise, chute de tension
➡️ Position adaptée
➡️ Appeler le 15
➡️ Stylo d'adrénaline si disponible (Anapen)

---

### 🎯 PSE 2 - Prise en charge avancée

**Hypoglycémie sévère :**
- Glycémie < 0.6 g/L avec troubles de conscience
- Glucagon IM si prescrit (1 mg)
- Voie veineuse + G30% si formé

**État de mal épileptique :**
- Crise > 5 min ou crises répétées
- Protection des voies aériennes
- Oxygénothérapie
- Benzodiazépine sur prescription

**Choc anaphylactique :**
- Adrénaline IM (0.3-0.5 mg adulte)
- Voie veineuse, remplissage
- Oxygénothérapie haut débit
- Corticoïdes sur prescription"""
            }
        ]
    },
    {
        "id": "ch7",
        "numero": 7,
        "titre": "Atteintes traumatiques",
        "description": "Traumatismes des os et articulations, du crâne, du rachis, du thorax et de l'abdomen.",
        "icon": "Bone",
        "formation_type": "PSE",
        "image_url": "https://images.unsplash.com/photo-1559757175-7cb057a7e65b",
        "fiches": [
            {
                "id": "ch7-f1",
                "titre": "Traumatismes des membres",
                "contenu": """## Traumatismes des membres

### 🎯 PSE 1 - Reconnaissance et immobilisation de base

**Signes de fracture/luxation :**
- Douleur vive
- Impotence fonctionnelle
- Déformation visible
- Gonflement, hématome
- Craquement ressenti

**Principes d'immobilisation :**
- Ne pas mobiliser le membre atteint
- Immobiliser dans la position trouvée
- Contrôler le pouls distal avant et après
- Lutter contre la douleur (froid)

**Matériel PSE 1 :**
- Écharpe triangulaire
- Attelle souple (Sam Splint)
- Coussin d'immobilisation

---

### 🎯 PSE 2 - Immobilisation avancée

**Attelles à dépression :**
- Moulables, rigides une fois mises en dépression
- Adaptées aux déformations
- Contrôle du pouls distal obligatoire

**Attelle de traction (fémur) :**
- Fracture du fémur uniquement
- Mise en traction douce
- Soulagement de la douleur
- Formation spécifique requise

**Réalignement :**
- Uniquement si absence de pouls distal
- Traction douce dans l'axe
- Sous contrôle médical si possible
- Arrêter si résistance ou douleur intense"""
            },
            {
                "id": "ch7-f2",
                "titre": "Traumatisme du rachis",
                "contenu": """## Traumatisme du rachis

### 🎯 PSE 1 - Suspicion et immobilisation de base

**Quand suspecter un traumatisme du rachis :**
- Chute de hauteur
- Accident de la route
- Plongeon en eau peu profonde
- Traumatisme violent au-dessus des épaules
- Douleur du cou ou du dos
- Fourmillements, paralysie

**Principes fondamentaux :**
- Maintenir l'axe tête-cou-tronc
- Ne pas mobiliser la victime sauf urgence vitale
- Rassurer et expliquer

**Maintien tête :**
- Se placer dans l'axe de la victime
- Maintenir la tête en position neutre
- Coudes appuyés au sol ou sur les genoux
- Ne pas relâcher jusqu'à immobilisation complète

---

### 🎯 PSE 2 - Immobilisation complète

**Collier cervical :**
- Taille adaptée (menton-épaule)
- Mise en place à deux
- Un maintient la tête, l'autre pose le collier
- ⚠️ Ne dispense pas du maintien tête

**Matelas immobilisateur à dépression (MID) :**
- Installation par roulement prudent
- Moulage au corps
- Mise en dépression
- Sangles de maintien

**Plan dur :**
- Pour extraction ou relevage
- Immobilisation provisoire
- Transfert sur MID dès que possible

**Cas particulier - Casque intégral :**
- Retrait à deux secouristes
- Un maintient la tête et le cou
- L'autre retire le casque progressivement"""
            },
            {
                "id": "ch7-f3",
                "titre": "Traumatismes crânien, thoracique et abdominal",
                "contenu": """## Traumatismes crânien, thoracique et abdominal

### 🎯 PSE 1 - Reconnaissance

**Traumatisme crânien :**
- Perte de connaissance (même brève)
- Confusion, amnésie
- Maux de tête, vomissements
- Saignement oreille/nez (liquide clair)
- Pupilles asymétriques

**Traumatisme thoracique :**
- Douleur thoracique à la respiration
- Difficulté respiratoire
- Asymétrie des mouvements du thorax
- Plaie thoracique (succion)

**Traumatisme abdominal :**
- Douleur abdominale
- Ventre dur, ballonné
- Signes de choc sans hémorragie visible

---

### 🎯 PSE 2 - Prise en charge spécifique

**Traumatisme crânien :**
- Surveillance GCS toutes les 5 min
- Position adaptée (30° si conscient)
- Oxygénothérapie si besoin
- Préparer l'aspiration

**Plaie thoracique soufflante :**
- Pansement 3 côtés (valve improvisée)
- OU pansement occlusif spécifique
- Position demi-assise
- Oxygénothérapie haut débit

**Traumatisme abdominal :**
- Position allongée, jambes fléchies
- Ne rien donner à boire
- Couverture (lutter contre hypothermie)
- Éviscération : ne pas réintégrer, couvrir d'un champ humide"""
            }
        ]
    },
    {
        "id": "ch8",
        "numero": 8,
        "titre": "Souffrance psychique et comportements inhabituels",
        "description": "États de stress, crise d'angoisse, agitation, agressivité, risque suicidaire.",
        "icon": "Brain",
        "formation_type": "PSE",
        "image_url": "https://images.unsplash.com/photo-1620147461831-a97b99ade1d3",
        "fiches": [
            {
                "id": "ch8-f1",
                "titre": "Réactions de stress et crise d'angoisse",
                "contenu": """## Réactions de stress et crise d'angoisse

### 🎯 PSE 1 - Reconnaissance et premiers gestes

**Réaction de stress aigu :**
- Suite à un événement traumatisant
- Sidération (immobile, absent)
- Agitation désordonnée
- Pleurs, cris
- Fuite panique

**Conduite à tenir :**
- Isoler du tumulte si possible
- Parler calmement
- Proposer une présence silencieuse
- Ne pas forcer la parole
- Protéger des dangers

**Crise d'angoisse / Attaque de panique :**
- Sensation de mort imminente
- Oppression thoracique
- Palpitations, tremblements
- Hyperventilation
- Fourmillements des extrémités

**Conduite à tenir :**
- Rassurer (ce n'est pas grave, ça va passer)
- Isoler dans un endroit calme
- Faire respirer lentement (inspiration nasale, expiration buccale)
- Ne pas mettre de sac sur le visage

---

### 🎯 PSE 2 - Accompagnement et orientation

**Évaluation :**
- Antécédents de crises similaires
- Facteur déclenchant identifié
- Traitement en cours

**Orientation :**
- Premiers épisodes : avis médical
- Crises connues : traitement habituel si disponible
- Signes physiques associés : bilan complet

**Débriefing collectif (CUMP) :**
- Cellule d'Urgence Médico-Psychologique
- Intervention sur les événements majeurs
- Orientation vers suivi si besoin"""
            },
            {
                "id": "ch8-f2",
                "titre": "Agitation et agressivité",
                "contenu": """## Agitation et agressivité

### 🎯 PSE 1 - Approche sécurisée

**Causes possibles :**
- Origine psychiatrique
- Intoxication (alcool, drogues)
- Hypoglycémie
- Traumatisme crânien
- Hypoxie

**Principes de sécurité :**
- Ne jamais rester seul
- Garder une distance de sécurité
- Avoir une issue de repli
- Ne pas tourner le dos
- Alerter les forces de l'ordre si danger

**Approche relationnelle :**
- Voix calme et posée
- Phrases courtes et simples
- Éviter le contact physique non consenti
- Ne pas contredire frontalement
- Proposer plutôt qu'imposer

---

### 🎯 PSE 2 - Contention et sédation

**Contention physique :**
- En dernier recours
- Sur prescription médicale si possible
- Technique à plusieurs (4 minimum)
- Respecter la dignité
- Surveillance rapprochée

**Sédation médicamenteuse :**
- Sur prescription médicale uniquement
- Voie IM le plus souvent
- Surveillance des constantes
- Matériel de réanimation à proximité

**Causes à éliminer avant diagnostic psychiatrique :**
- Glycémie
- SpO2
- Température
- Traumatisme crânien
- Intoxication"""
            },
            {
                "id": "ch8-f3",
                "titre": "Risque suicidaire",
                "contenu": """## Risque suicidaire

### 🎯 PSE 1 - Reconnaissance et attitude

**Signes d'alerte :**
- Verbalisation d'idées suicidaires
- Don d'objets personnels
- Isolement brutal
- Calme soudain après période de détresse
- Comportements à risque inhabituels

**Attitude à adopter :**
- Prendre au sérieux toute verbalisation
- Écouter sans juger
- Ne pas banaliser ni dramatiser
- Ne pas laisser seul
- Alerter les secours

**Questions à poser (si approprié) :**
- "Avez-vous des idées de vous faire du mal ?"
- "Avez-vous pensé à comment ?"
- Questions factuelles, sans suggestion

---

### 🎯 PSE 2 - Évaluation et orientation

**Niveau de risque :**

| Niveau | Caractéristiques |
|--------|------------------|
| Faible | Idées passagères, pas de plan |
| Moyen | Idées fréquentes, ébauche de plan |
| Élevé | Plan précis, moyens disponibles, date fixée |

**Conduite à tenir :**
- Risque faible : orientation médecin traitant
- Risque moyen : avis psychiatrique urgent
- Risque élevé : hospitalisation, ne pas laisser seul

**Moyens létaux :**
- Sécuriser l'environnement
- Éloigner médicaments, armes, objets dangereux
- Ne pas laisser seul même un instant

**Numéros utiles :**
- 3114 : Numéro national de prévention du suicide
- 15 : SAMU
- 112 : Numéro d'urgence européen"""
            }
        ]
    },
    {
        "id": "ch9",
        "numero": 9,
        "titre": "Atteintes liées aux circonstances",
        "description": "Noyade, accidents électriques, intoxications, morsures, piqûres, gelures, hyperthermie.",
        "icon": "Thermometer",
        "formation_type": "PSE",
        "image_url": "https://images.unsplash.com/photo-1527066236128-2ff79f7b9705",
        "fiches": [
            {
                "id": "ch9-f1",
                "titre": "Noyade et accidents de plongée",
                "contenu": """## Noyade et accidents de plongée

### 🎯 PSE 1 - Noyade

**Définition :**
Détresse respiratoire suite à une immersion ou submersion dans un liquide.

**Stades de la noyade :**
1. Aquastress : angoisse, pas d'inhalation
2. Petit hypoxique : toux, gêne respiratoire
3. Grand hypoxique : troubles de conscience
4. Anoxique : arrêt respiratoire puis cardiaque

**Conduite à tenir :**
- Sortir de l'eau en sécurité
- Alerter les secours (15 ou 18)
- Si conscient : position adaptée, réchauffer
- Si inconscient qui respire : PLS
- Si arrêt respiratoire : 5 insufflations puis RCP

⚠️ **Toujours suspecter un traumatisme du rachis en cas de plongeon**

---

### 🎯 PSE 2 - Prise en charge avancée

**Oxygénothérapie :**
- Systématique même si SpO2 normale
- 15 L/min au masque haute concentration
- Surveillance prolongée (OAP secondaire)

**Accidents de plongée :**
- Barotraumatismes (oreilles, poumons)
- Accident de décompression
- Symptômes retardés possibles

**Conduite spécifique :**
- Oxygénothérapie normobare 15 L/min
- Position allongée
- Hydratation
- Évacuation vers centre hyperbare
- Ne pas reprendre l'avion"""
            },
            {
                "id": "ch9-f2",
                "titre": "Accidents électriques et intoxications",
                "contenu": """## Accidents électriques et intoxications

### 🎯 PSE 1 - Électrisation

**Dangers :**
- Brûlures (points d'entrée et sortie)
- Troubles du rythme cardiaque
- Tétanisation musculaire
- Traumatismes secondaires (chute)

**Conduite à tenir :**
1. Couper le courant AVANT d'approcher
2. Ou éloigner la victime avec un objet isolant (bois sec)
3. Si arrêt cardiaque : RCP + DAE
4. Rechercher les brûlures
5. Bilan et surveillance prolongée

⚠️ **Haute tension (> 1000V) : attendre les spécialistes**

---

**Intoxications :**

**Par inhalation (CO, fumées) :**
- Soustraire du milieu toxique
- Oxygénothérapie 15 L/min
- Surveillance

**Par ingestion :**
- Ne pas faire vomir
- Conserver l'emballage du produit
- Appeler le centre antipoison

---

### 🎯 PSE 2 - Prise en charge avancée

**Électrisation :**
- ECG si disponible (troubles du rythme)
- Voie veineuse
- Remplissage si brûlures étendues
- Surveillance continue (24h recommandées)

**Intoxication au CO :**
- SpO2 peut être faussement normale
- Signes : céphalées, vertiges, nausées
- Oxygénothérapie prolongée
- Orientation centre hyperbare si gravité"""
            },
            {
                "id": "ch9-f3",
                "titre": "Gelures, hypothermie et coup de chaleur",
                "contenu": """## Gelures, hypothermie et coup de chaleur

### 🎯 PSE 1 - Reconnaissance

**Gelures :**
- Exposition prolongée au froid
- Peau blanche, cireuse, insensible
- Puis rougeur, douleur, cloques au réchauffement

**Hypothermie :**
| Stade | Température | Signes |
|-------|-------------|--------|
| Légère | 35-32°C | Frissons, confusion |
| Modérée | 32-28°C | Somnolence, arrêt des frissons |
| Sévère | < 28°C | Coma, risque d'arrêt cardiaque |

**Coup de chaleur :**
- Température > 40°C
- Peau chaude, sèche, rouge
- Troubles de la conscience
- Urgence vitale

---

### 🎯 PSE 2 - Prise en charge

**Gelures :**
- Ne pas frotter
- Réchauffement progressif (bain 37-39°C)
- Antalgiques
- Avis chirurgical si stade avancé

**Hypothermie :**
- Mobilisation douce (risque de fibrillation)
- Réchauffement passif (couvertures)
- Réchauffement actif (couverture chauffante)
- RCP prolongée si arrêt (hypothermie protectrice)
- "Personne n'est morte tant qu'elle n'est pas réchauffée et morte"

**Coup de chaleur :**
- Refroidissement immédiat (déshabiller, eau fraîche)
- Ventilation
- Glaçons aux plis (aisselles, aines)
- Oxygénothérapie
- Voie veineuse, remplissage prudent"""
            }
        ]
    },
    {
        "id": "ch10",
        "numero": 10,
        "titre": "Relevage et brancardage",
        "description": "Techniques de relevage, brancardage, installation dans un véhicule de transport.",
        "icon": "Truck",
        "formation_type": "PSE",
        "image_url": "https://images.unsplash.com/photo-1587745416684-47953f16f02f",
        "fiches": [
            {
                "id": "ch10-f1",
                "titre": "Principes du relevage",
                "contenu": """## Principes du relevage

### 🎯 PSE 1 - Techniques de base

**Définition :**
Ensemble des techniques permettant de placer une victime sur un brancard.

**Principes fondamentaux :**
- Maintien de l'axe tête-cou-tronc
- Mouvements synchronisés
- Commandements clairs
- Effort réparti

**Relevage à 3 secouristes (pont simple) :**
1. Un secouriste maintient la tête
2. Un au niveau du tronc
3. Un au niveau des membres inférieurs
4. Le brancard est glissé sous la victime

**Relevage avec cuillère :**
- Victime allongée sur le dos
- Assemblage sous la victime
- Transfert sur brancard

---

### 🎯 PSE 2 - Techniques avancées

**Pont amélioré (4-5 secouristes) :**
- Meilleure stabilité
- Un secouriste dédié au brancard
- Coordination par le chef d'équipe

**Plan dur :**
- Retournement en bloc
- Maintien strict de l'axe
- Transfert rapide sur MID

**Relevage en terrain difficile :**
- Brancard cuillère
- Barquette de sauvetage
- Techniques de levage à la sangle

**Véhicule accidenté :**
- Coordination avec les pompiers
- Désincarcération si nécessaire
- Extraction sur plan dur"""
            },
            {
                "id": "ch10-f2",
                "titre": "Brancardage et transport",
                "contenu": """## Brancardage et transport

### 🎯 PSE 1 - Techniques de base

**Principes du brancardage :**
- Chef de brancard aux pieds (vision dégagée)
- Marche synchronisée (partir du même pied)
- Brancard horizontal
- Victime tête vers l'avant

**Commandements :**
- "Prêts ? Attention pour lever... Levez !"
- "En avant... Marche !"
- "Halte... Posez !"

**Franchissement d'obstacles :**
- Marches : élever côté obstacle
- Porte étroite : passage en biais
- Virage : petit pas côté intérieur

---

### 🎯 PSE 2 - Situations particulières

**Brancardage en pente :**
- Montée : victime tête en avant
- Descente : victime pieds en avant
- Maintien de l'horizontalité

**Brancardage en escalier :**
- 4 porteurs minimum
- Porteurs supplémentaires en relais
- Sangles de portage

**Installation en VSAV/ambulance :**
- Arrimage du brancard
- Surveillance pendant le transport
- Accès aux voies aériennes

**Aéronef (hélicoptère) :**
- Approche par l'avant
- Sous la supervision de l'équipage
- Brancard adapté
- Pas de brancard cuillère en vol"""
            }
        ]
    },
    {
        "id": "ch11",
        "numero": 11,
        "titre": "Situations particulières",
        "description": "Accouchement inopiné, nouveau-né à la naissance, personnes âgées, situations multivictimes.",
        "icon": "Baby",
        "formation_type": "PSE",
        "image_url": "https://images.unsplash.com/photo-1555252333-9f8e92e65df9",
        "fiches": [
            {
                "id": "ch11-f1",
                "titre": "Accouchement inopiné",
                "contenu": """## Accouchement inopiné

### 🎯 PSE 1 - Évaluation et premiers gestes

**Signes d'accouchement imminent :**
- Contractions rapprochées (< 5 min)
- Envie de pousser irrépressible
- Visualisation de la tête du bébé

**Matériel minimal :**
- Champ propre
- Clamp ou liens stériles
- Bonnet, couverture pour le bébé
- Serviettes propres

**Conduite à tenir :**
1. Alerter les secours (SAMU)
2. Installer la mère (demi-assise ou allongée)
3. La rassurer, la guider
4. Ne pas tirer sur le bébé
5. Accompagner la sortie

---

### 🎯 PSE 2 - Prise en charge complète

**Accueil du nouveau-né :**
1. Réceptionner le bébé
2. Sécher vigoureusement
3. Stimuler si besoin (friction du dos)
4. Évaluer : cri, tonus, coloration
5. Clamper le cordon à 15 cm du bébé
6. Peau à peau avec la mère

**Complications :**
- Circulaire du cordon : glisser par-dessus la tête
- Procidence du cordon : urgence absolue
- Siège : ne pas intervenir, attendre les secours
- Hémorragie du post-partum : massage utérin

**Réanimation du nouveau-né :**
- Aspiration douce si sécrétions
- 5 insufflations si pas de respiration
- RCP si FC < 60/min (3:1)"""
            },
            {
                "id": "ch11-f2",
                "titre": "Prise en charge de l'enfant et du nourrisson",
                "contenu": """## Prise en charge de l'enfant et du nourrisson

### 🎯 PSE 1 - Spécificités pédiatriques

**Définitions :**
- Nouveau-né : 0 à 1 mois
- Nourrisson : 1 mois à 1 an
- Enfant : 1 an à puberté

**Différences anatomiques :**
- Tête proportionnellement plus grosse
- Voies aériennes plus étroites
- Cage thoracique plus souple
- Fréquences cardiaques et respiratoires plus élevées

**Fréquences normales :**

| Âge | FR | FC |
|-----|----|----|
| Nourrisson | 30-40 | 120-160 |
| 1-5 ans | 20-30 | 100-140 |
| 5-12 ans | 15-25 | 80-120 |

---

### 🎯 PSE 2 - Situations d'urgence

**RCP pédiatrique :**
- 5 insufflations initiales
- 15:2 (2 secouristes) ou 30:2 (1 secouriste)
- Compression : 1/3 du thorax

**Obstruction des voies aériennes :**
- Claques dans le dos + compressions thoraciques (nourrisson)
- Claques dans le dos + Heimlich (enfant > 1 an)

**Détresse respiratoire :**
- Position adaptée
- Respect de la position de confort
- Humidification si laryngite
- Jamais d'examen de gorge si suspicion d'épiglottite

**Déshydratation :**
- Fontanelle déprimée (nourrisson)
- Yeux creux, pli cutané persistant
- Réhydratation orale si conscient"""
            },
            {
                "id": "ch11-f3",
                "titre": "Personnes âgées et situations multivictimes",
                "contenu": """## Situations particulières

### 🎯 PSE 1 - Personnes âgées

**Spécificités :**
- Fragilité osseuse (fractures faciles)
- Thermorégulation altérée
- Polymédication fréquente
- Communication parfois difficile

**Attention particulière :**
- Hypothermie même en été
- Déshydratation rapide
- Chutes fréquentes et graves
- Isolement social

**Maltraitance :**
- Signes physiques (ecchymoses, brûlures)
- Signes psychologiques (peur, repli)
- Négligence (hygiène, alimentation)
- ➡️ Signalement obligatoire

---

### 🎯 PSE 2 - Situations multivictimes

**Plan ORSEC Nombreuses Victimes (NOVI) :**
- Organisation spécifique
- Triage des victimes
- Chaîne médicale de l'avant

**Triage START :**

| Catégorie | Description | Action |
|-----------|-------------|--------|
| T1 (Rouge) | Urgence absolue | Prioritaire |
| T2 (Jaune) | Urgence relative | Attente possible |
| T3 (Vert) | Impliqués, valides | Regroupement |
| T4 (Noir) | Décédés | Mortelle |

**Rôle du secouriste :**
- Application du triage
- Gestes de sauvetage rapides
- Aide à l'évacuation
- Soutien psychologique

**PRV (Point de Regroupement des Victimes) :**
- Zone sécurisée
- Identification des victimes
- Orientation vers les PMA"""
            }
        ]
    },
    {
        "id": "ch12",
        "numero": 12,
        "titre": "Synthèse et mises en situation",
        "description": "Récapitulatif des compétences, cas pratiques, préparation à la certification.",
        "icon": "GraduationCap",
        "formation_type": "PSE",
        "image_url": "https://images.unsplash.com/photo-1434030216411-0b793f4b4173",
        "fiches": [
            {
                "id": "ch12-f1",
                "titre": "Récapitulatif des compétences PSE 1",
                "contenu": """## Récapitulatif des compétences PSE 1

### Compétences à maîtriser

**1. Protection et alerte**
- ✅ Identifier les dangers
- ✅ Supprimer ou isoler un danger
- ✅ Réaliser un dégagement d'urgence
- ✅ Transmettre une alerte adaptée

**2. Bilan**
- ✅ Réaliser un bilan d'urgence vitale
- ✅ Effectuer un bilan complémentaire
- ✅ Surveiller une victime

**3. Gestes de premiers secours**
- ✅ Libérer les voies aériennes
- ✅ Arrêter une hémorragie externe
- ✅ Traiter une obstruction des voies aériennes
- ✅ Réaliser une RCP avec DAE
- ✅ Mettre en PLS

**4. Situations spécifiques**
- ✅ Prendre en charge un malaise
- ✅ Immobiliser un membre traumatisé
- ✅ Protéger une victime d'un traumatisme du rachis
- ✅ Assister à un accouchement inopiné

**5. Travail en équipe**
- ✅ Communiquer efficacement
- ✅ Appliquer les procédures
- ✅ Utiliser le matériel de base"""
            },
            {
                "id": "ch12-f2",
                "titre": "Compétences complémentaires PSE 2",
                "contenu": """## Compétences complémentaires PSE 2

### Compétences supplémentaires

**1. Bilan avancé**
- ✅ Mesurer les constantes vitales
- ✅ Utiliser l'échelle de Glasgow
- ✅ Transmettre un bilan structuré

**2. Matériel spécifique**
- ✅ Utiliser le BAVU et l'oxygénothérapie
- ✅ Poser un collier cervical
- ✅ Utiliser le matelas immobilisateur
- ✅ Maîtriser les attelles à dépression

**3. Techniques de relevage**
- ✅ Réaliser un pont amélioré
- ✅ Utiliser le brancard cuillère
- ✅ Effectuer un brancardage sécurisé

**4. Situations complexes**
- ✅ Prendre en charge une détresse vitale
- ✅ Gérer une situation multivictimes
- ✅ Administrer des traitements prescrits
- ✅ Coordonner une équipe de secouristes

**5. Chef d'équipe**
- ✅ Organiser l'intervention
- ✅ Superviser les gestes techniques
- ✅ Assurer la liaison avec les services médicaux"""
            },
            {
                "id": "ch12-f3",
                "titre": "Préparation à la certification",
                "contenu": """## Préparation à la certification

### Évaluation PSE 1

**Épreuves :**
- QCM de connaissances théoriques
- Mise en situation pratique
- Évaluation continue pendant la formation

**Critères de réussite :**
- Maîtrise des gestes techniques
- Respect des protocoles
- Communication adaptée
- Travail en équipe

---

### Évaluation PSE 2

**Épreuves :**
- QCM approfondi
- Mise en situation avec utilisation du matériel
- Épreuve de chef d'équipe
- Évaluation continue

**Points d'attention :**
- Pertinence des décisions
- Qualité du bilan transmis
- Coordination de l'équipe
- Utilisation correcte du matériel

---

### Conseils pour réussir

**Préparation théorique :**
- Relire régulièrement les fiches
- S'auto-évaluer avec les quiz
- Comprendre plutôt que mémoriser

**Préparation pratique :**
- S'entraîner régulièrement
- Participer aux mises en situation
- Demander des feedbacks

**Le jour de l'évaluation :**
- Rester calme
- Verbaliser ses actions
- Demander de l'aide si besoin
- Appliquer les protocoles appris

**Après la certification :**
- Formation continue obligatoire
- Recyclages réguliers
- Maintien des compétences"""
            }
        ]
    }
]

async def update_pse_chapters():
    print("🚀 Mise à jour des chapitres PSE avec distinction PSE 1 / PSE 2...")
    
    for chapter in pse_chapters:
        result = await db.chapters.update_one(
            {"id": chapter["id"], "formation_type": "PSE"},
            {"$set": chapter},
            upsert=True
        )
        if result.modified_count > 0:
            print(f"✅ Mis à jour: {chapter['titre']} ({len(chapter['fiches'])} fiches)")
        elif result.upserted_id:
            print(f"➕ Créé: {chapter['titre']} ({len(chapter['fiches'])} fiches)")
        else:
            print(f"⏭️  Inchangé: {chapter['titre']}")
    
    # Vérifier le total
    count = await db.chapters.count_documents({"formation_type": "PSE"})
    total_fiches = 0
    async for ch in db.chapters.find({"formation_type": "PSE"}):
        total_fiches += len(ch.get("fiches", []))
    
    print(f"\n🎉 Total: {count} chapitres PSE avec {total_fiches} fiches")
    print("   Chaque fiche distingue clairement les notions PSE 1 et PSE 2")

if __name__ == "__main__":
    asyncio.run(update_pse_chapters())
