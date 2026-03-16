#!/usr/bin/env python3
"""
Script de création des 12 chapitres PSE selon référentiel 2024
Respecte strictement l'ordre et le contenu du référentiel
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

# Images pour gestes techniques PSE
images = {
    "formation": "https://images.unsplash.com/photo-1622551546704-36926ae49878",
    "retournement": "https://pikwizard.com/photo/emergency-first-aid-cpr-being-performed-by-medical-professional/4793b84166515d790addf0c1ba9ea406/",
    "ecg": "https://images.unsplash.com/photo-1770836037704-44bd8c7b6978",
    "pls_2": "https://images.unsplash.com/photo-1630225757034-d49c20300b55",
    "echarpe": "https://pikwizard.com/photo/ambulance-team-assisting-injured-woman-on-stretcher/fb0ef18296b6eb2f19bd875ccee642f0/",
    "relevage_4": "https://images.unsplash.com/photo-1772140994531-20ba4efd9df2",
    "cpr": "https://images.unsplash.com/photo-1759872138841-c342bd6410ae",
    "secours": "https://images.unsplash.com/photo-1622115297822-a3798fdbe1f6"
}

pse_chapters = [
    # Chapitre 1 déjà créé - on le met à jour
    {
        "id": "ch1",
        "numero": 1,
        "titre": "Attitude et comportement",
        "description": "Rôle du citoyen de sécurité civile, principes d'intervention, abord relationnel et préservation du potentiel mental du secouriste. (PSE 1)",
        "icon": "Users",
        "formation_type": "PSE",
        "image_url": images["formation"],
        "fiches": []  # Déjà rempli, on ne touche pas
    },
    
    # Chapitre 2
    {
        "id": "ch2",
        "numero": 2,
        "titre": "Bilans",
        "description": "Évaluation de l'état de la victime par les 4 regards successifs, surveillance et transmission du bilan. (PSE 1)",
        "icon": "ClipboardList",
        "formation_type": "PSE",
        "image_url": images["retournement"],
        "fiches": [
            {
                "id": "ch2-resume",
                "titre": "Les 4 regards du bilan (PSE 1)",
                "contenu": """## Les Bilans - Évaluation de la victime

### 🎯 Objectif
Phase essentielle de recueil d'informations pour évaluer la situation et l'état de la victime.

### 📋 Les 4 Regards

**1️⃣ PREMIER REGARD - Vision globale**
- Nature de l'intervention
- Identifier les dangers
- Nombre de victimes
- Moyens complémentaires

**2️⃣ DEUXIÈME REGARD - Menaces vitales**
- Hémorragie externe
- Obstruction voies aériennes
- Absence de réaction/respiration

**3️⃣ TROISIÈME REGARD - Fonctions vitales**
- Évaluer : Respiration → Circulation → Neurologique
- Traiter ce qui tue en PREMIER
- Demander avis médical si détresse

**4️⃣ QUATRIÈME REGARD - Examen complet**
- Interrogatoire (mécanisme, plaintes, antécédents)
- Examen tête aux pieds
- Paramètres physiologiques

### 📊 Surveillance
- Toutes les 5 min si détresse vitale
- Toutes les 10-15 min sinon
- Suivre l'évolution et adapter les gestes

### 📡 Transmission du bilan
Compte-rendu **concis, complet, structuré, logique et chronologique**

### 🔧 Fiches Techniques principales
- Retournement à 1 et 2 secouristes
- Évaluation fonctions (respiratoire, circulatoire, neurologique)
- Mesures (PA, SpO2, glycémie, température, douleur)
- Électrocardiogramme""",
                "image_url": images["retournement"]
            }
        ]
    },
    
    # Chapitre 3
    {
        "id": "ch3",
        "numero": 3,
        "titre": "Protection et sécurité",
        "description": "Équipements de protection individuelle, sécurité sur intervention et dégagement d'urgence. (PSE 1 & 2)",
        "icon": "Shield",
        "formation_type": "PSE",
        "image_url": images["secours"],
        "fiches": [
            {
                "id": "ch3-resume",
                "titre": "Protection et sécurité (PSE 1 & 2)",
                "contenu": """## Protection et Sécurité

### 🦺 EPI - Équipement Protection Individuelle (PSE 1)
**Obligatoires :**
- Gants à usage unique
- Bandes réfléchissantes
- Blouson adapté
- Lampe de poche

### 🚨 Sécurité sur intervention (PSE 1)

**Approche prudente :**
1. Repérer les dangers persistants
2. Délimiter la zone d'intervention
3. Mettre en place protections collectives
4. Supprimer les dangers si possible

### ⚡ Interventions particulières (PSE 2)

**Accident électrique :**
- Couper le courant
- Écarter les personnes
- Attendre équipes spécialisées

**Accident de la route :**
- Gilet haute visibilité
- Baliser la zone
- Garer en sécurité
- Interdire approche si danger
- NE PAS fumer

**Monoxyde de carbone / Incendie :**
- Ne pas pénétrer sans protection
- Attendre pompiers

### 🔧 Fiche Technique
- **Dégagement d'urgence** : Soustraire victime à danger réel, vital, immédiat et non contrôlable""",
                "image_url": ""
            }
        ]
    },
    
    # Chapitre 4
    {
        "id": "ch4",
        "numero": 4,
        "titre": "Hygiène et asepsie",
        "description": "Risques infectieux, précautions standards et particulières, accident d'exposition à un risque viral. (PSE 1)",
        "icon": "Activity",
        "formation_type": "PSE",
        "image_url": "",
        "fiches": [
            {
                "id": "ch4-resume",
                "titre": "Hygiène et asepsie (PSE 1)",
                "contenu": """## Hygiène et Asepsie

### 🦠 Risque infectieux

**Transmission des maladies :**
- Contact direct
- Gouttelettes
- Air
- Autres voies

### 🧤 Précautions STANDARDS (toujours)

**Hygiène quotidienne :**
- Se laver quotidiennement
- Ongles courts
- Désinfection mains régulière

**Sur intervention :**
- Porter gants à usage unique
- Masque si nécessaire
- Tenue adaptée
- Respecter gestion déchets (DASRI)

### 🔴 Accident Exposition Risque Viral (AEV)

**Si contact sang/liquide biologique :**

**Pour une plaie :**
1. ❌ NE PAS faire saigner
2. Nettoyer à l'eau et savon
3. Désinfecter (antiseptique)
4. Rendre compte IMMÉDIATEMENT

**Pour projection muqueuses :**
1. Rincer abondamment (10-15 min)
2. Rendre compte IMMÉDIATEMENT

**Risques :** VIH, Hépatites B et C

### 🔧 Fiches Techniques
- Friction des mains (gel hydroalcoolique)
- Lavage des mains
- Mise en place gants stériles
- Nettoyage véhicule/matériel
- Retrait gants
- Utilisation détergents/désinfectants
- Élimination déchets DASRI""",
                "image_url": ""
            }
        ]
    },
    
    # Chapitre 5 - URGENCES VITALES (le plus important)
    {
        "id": "ch5",
        "numero": 5,
        "titre": "Urgences vitales",
        "description": "Arrêt cardiaque, détresses (circulatoire, neurologique, respiratoire), hémorragies, obstruction voies aériennes, perte de connaissance. (PSE 1)",
        "icon": "Heart",
        "formation_type": "PSE",
        "image_url": images["cpr"],
        "fiches": [
            {
                "id": "ch5-arret-cardiaque",
                "titre": "Arrêt cardiaque (PSE 1)",
                "contenu": """## Arrêt Cardiaque

### 🚨 Définition
Cœur qui ne fonctionne plus ou de manière anarchique.

### 🔍 Reconnaître
- ❌ Absence de réponse
- ❌ Absence de respiration ou respiration agonique
- ❌ Absence de pouls

### ⚡ Conduite à tenir

**1. RECONNAÎTRE**
**2. ALERTER** (faire alerter le 15 + réclamer DAE)
**3. RCP immédiate**
**4. DÉFIBRILLATION dès que possible**

### 💪 RCP - Réanimation Cardio-Pulmonaire

**Adulte :**
- 30 compressions thoraciques
- 2 insufflations
- Rythme : 100-120 compressions/minute

**Enfant/Nourrisson :**
- 15 compressions
- 2 insufflations

**⚠️ NE JAMAIS arrêter avant :**
- Arrivée des secours
- Victime respire normalement
- Épuisement complet""",
                "image_url": images["cpr"]
            },
            {
                "id": "ch5-detresses",
                "titre": "Les détresses vitales (PSE 1)",
                "contenu": """## Détresses Vitales

### 🩸 DÉTRESSE CIRCULATOIRE
**Signes :**
- Pâleur intense
- Extrémités froides
- Pouls rapide/faible
- Marbrures cutanées
- TRC augmenté

**Action :** Arrêter cause, oxygénation, aide médicale

---

### 🧠 DÉTRESSE NEUROLOGIQUE
**Signes :**
- Somnolence ou perte connaissance
- Désorientation
- Trouble du langage
- Paralysie
- Convulsions

**Action :** Position adaptée, avis médical, surveillance

---

### 🫁 DÉTRESSE RESPIRATOIRE
**Signes :**
- Difficulté à respirer
- Agitation
- Sifflements, gargouillements
- Cyanose (bleu)
- SpO2 basse

**Action :** Arrêter cause, oxygénation, aide médicale""",
                "image_url": ""
            },
            {
                "id": "ch5-hemorragies",
                "titre": "Hémorragies (PSE 1)",
                "contenu": """## Hémorragies

### 🩸 HÉMORRAGIE EXTERNE
Saignement abondant et continu

**Conduite :**
1. **Compression manuelle** directe et forte
2. Allonger la victime
3. Alerter le 15
4. Si inefficace → **GARROT** (5-7 cm au-dessus)

**⚠️ Garrot : JAMAIS retirer sans avis médical**

---

### 💉 HÉMORRAGIES EXTÉRIORISÉES
Sang qui sort par orifice naturel

**Localisations :**
- Nez (épistaxis)
- Oreille
- Bouche
- Voies urinaires
- Anale, vaginale

**Action :** Adapter selon localisation, alerter le 15""",
                "image_url": ""
            },
            {
                "id": "ch5-obstruction",
                "titre": "Obstruction voies aériennes (PSE 1)",
                "contenu": """## Obstruction des Voies Aériennes

### 🟡 OBSTRUCTION PARTIELLE
Victime peut parler, crier, tousser

**Action :**
- ✅ Encourager à tousser
- Surveiller
- Alerter le 15

---

### 🔴 OBSTRUCTION COMPLÈTE
Victime ne peut plus parler, crier, tousser

**Action immédiate - Alterner :**

**5 CLAQUES dans le dos**
- Pencher victime en avant
- Entre les omoplates
- Vigoureuses

**5 COMPRESSIONS abdominales (Heimlich)**
- Derrière la victime
- Poing au-dessus du nombril
- Tirer vers arrière et haut

**⚠️ Si perte connaissance → RCP immédiate**""",
                "image_url": ""
            },
            {
                "id": "ch5-perte-connaissance",
                "titre": "Perte de connaissance (PSE 1)",
                "contenu": """## Perte de Connaissance

### 🔍 Reconnaître
- ❌ Absence de réponse
- ✅ MAIS respire normalement

### 🛡️ Risques
- Chute de la langue
- Régurgitations
- Obstruction voies aériennes

### 🔄 Conduite à tenir

**Si NON traumatique :**
1. Libérer voies aériennes
2. **PLS** (Position Latérale Sécurité)
3. Alerter le 15
4. Surveiller respiration EN CONTINU

**Si traumatisme suspecté :**
1. Maintenir tête dans l'axe
2. Libérer voies aériennes
3. Alerter le 15
4. NE PAS mobiliser

**⚠️ Si arrêt respiratoire → RCP**""",
                "image_url": images["pls_2"]
            }
        ]
    },
    
    # Chapitres 6 à 12 avec structure de base
    {
        "id": "ch6",
        "numero": 6,
        "titre": "Malaises et affections spécifiques",
        "description": "AVC, convulsions, asthme, douleur thoracique, malaise hypoglycémique, malaise général, réaction allergique grave. (PSE 1 & 2)",
        "icon": "AlertCircle",
        "formation_type": "PSE",
        "image_url": "",
        "fiches": [
            {
                "id": "ch6-resume",
                "titre": "Malaises et affections spécifiques",
                "contenu": """## Malaises et Affections Spécifiques

### 🧠 AVC - Accident Vasculaire Cérébral (PSE 2)
**Signes :** Faiblesse/paralysie bras, déformation visage, trouble parole, perte vision
**Action :** Position adaptée, alerter 15 URGENCE

### 🌀 Crise convulsive généralisée
**Signes :** Contractions musculaires, perte connaissance
**Action :** Protéger, ne pas immobiliser, PLS après, alerter 15

### 🫁 Crise d'asthme
**Signes :** Difficulté respirer, sifflements
**Action :** Position assise, aide médicaments, O2, alerter 15

### 💔 Douleur thoracique (PSE 2)
**Action :** Repos absolu, position confort, alerter 15 URGENCE

### 🍬 Malaise hypoglycémique (diabétique)
**Signes :** Sueurs, tremblements, confusion
**Action :** Sucre rapide si conscient, alerter 15

### 🤒 Malaise général (PSE 1)
**Action :** Repos, questionner, alerter 15, surveiller

### 🐝 Réaction allergique grave
**Signes :** Gonflement, difficulté respirer, urticaire
**Action :** Aide médicament (stylo auto-injecteur), alerter 15 URGENCE""",
                "image_url": ""
            }
        ]
    },
    {
        "id": "ch7",
        "numero": 7,
        "titre": "Atteintes circonstancielles",
        "description": "Accident électrique, plongée, accouchement inopiné, chaleur, compression membre, gelures, hypothermie, intoxications, noyade, pendaison, piqûres/morsures. (PSE 1 & 2)",
        "icon": "Zap",
        "formation_type": "PSE",
        "image_url": "",
        "fiches": [
            {
                "id": "ch7-resume",
                "titre": "Atteintes circonstancielles",
                "contenu": """## Atteintes Circonstancielles

Situations spécifiques nécessitant adaptations

### ⚡ Accident électrique (PSE 2)
- Couper courant, écarter, attendre spécialistes

### 🤿 Accidents plongée
- Oxygénation, position adaptée, caisson hyperbare

### 👶 Accouchement inopiné (PSE 2)
- Accompagner, prise en charge nouveau-né

### 🌡️ Affections chaleur (PSE 2)
- Refroidir, hydrater, repos

### 🧊 Gelures / Hypothermie (PSE 2)
- Réchauffer progressivement, couvrir

### ☠️ Intoxications (PSE 2)
- Identifier toxique, ventilation, alerter centre antipoison

### 💧 Noyade (PSE 1)
- Sortir de l'eau, RCP si nécessaire, réchauffer

### 🪢 Pendaison/Strangulation (PSE 2)
- Dégager, RCP, position adaptée

### 🐍 Piqûres/Morsures (PSE 2)
- Immobiliser, désinfecter, surveillance""",
                "image_url": ""
            }
        ]
    },
    {
        "id": "ch8",
        "numero": 8,
        "titre": "Traumatismes",
        "description": "Brûlures, plaies, traumatismes de l'abdomen, bassin, crâne, dos/cou, thorax, membres, face. Immobilisations. (PSE 1 & 2)",
        "icon": "Bandage",
        "formation_type": "PSE",
        "image_url": images["echarpe"],
        "fiches": [
            {
                "id": "ch8-brulures",
                "titre": "Brûlures (PSE 1)",
                "contenu": """## Brûlures

### 🌊 GESTE PRIORITAIRE : REFROIDIR

**TOUJOURS refroidir immédiatement :**
- Eau courante tempérée (15-25°C)
- Pendant AU MOINS 10-20 minutes
- Retirer vêtements et bijoux (sauf si collés)

### 🔴 Brûlure GRAVE
- Cloque > moitié paume main
- Destruction profonde
- Localisations : visage, cou, mains, articulations
- Origine chimique, électrique

**Action :** Refroidir, alerter 15, surveiller

### 🟢 Brûlure SIMPLE
**Action :** Refroidir, protéger, consulter si tétanos non à jour""",
                "image_url": ""
            },
            {
                "id": "ch8-plaies",
                "titre": "Plaies (PSE 1)",
                "contenu": """## Plaies

### 🔴 Plaie GRAVE
- Hémorragie associée
- Mécanisme pénétrant
- Localisations : thorax, abdomen, œil
- Objet enfoncé

**⚠️ NE JAMAIS retirer objet enfoncé**
**Action :** Arrêter hémorragie, alerter 15

### 🟢 Plaie SIMPLE
1. Laver mains
2. Nettoyer plaie (eau)
3. Désinfecter
4. Protéger (pansement)
5. Consulter si tétanos non à jour""",
                "image_url": ""
            },
            {
                "id": "ch8-traumatismes-graves",
                "titre": "Traumatismes graves (PSE 2)",
                "contenu": """## Traumatismes Graves

**RÈGLE D'OR : NE PAS MOBILISER**

### 🦴 Traumatisme DOS/COU (PSE 2)
- Maintenir tête en position neutre
- Collier cervical
- Plan dur ou matelas dépression
- Alerter 15

### 🧠 Traumatisme CRÂNE (PSE 2)
- Position adaptée
- Surveiller conscience
- Alerter 15

### 🫁 Traumatisme THORAX (PSE 2)
- Position demi-assise
- Oxygénation
- Alerter 15

### 🦴 Traumatisme MEMBRES (PSE 1)
- Immobiliser dans position trouvée
- Ne pas réaligner
- Attelles, écharpes

### 🔧 Fiches Techniques principales
- Immobilisation attelles (dépression, modulable, traction)
- Immobilisation écharpes (membre supérieur)
- Collier cervical
- Retrait casque protection
- Contention pelvienne""",
                "image_url": images["echarpe"]
            }
        ]
    },
    {
        "id": "ch9",
        "numero": 9,
        "titre": "Souffrance psychique et comportements inhabituels",
        "description": "Personnes en situation de crise psychologique, prise en charge adaptée. (PSE 2)",
        "icon": "Brain",
        "formation_type": "PSE",
        "image_url": "",
        "fiches": [
            {
                "id": "ch9-resume",
                "titre": "Souffrance psychique (PSE 2)",
                "contenu": """## Souffrance Psychique et Comportements Inhabituels

### 🧠 Personnes en situation de crise (PSE 2)

**Définition :**
Personne présentant comportements inhabituels suite à événement traumatisant ou trouble psychiatrique.

**Signes :**
- Agitation, agressivité
- Prostration, mutisme
- Confusion, désorientation
- Idées suicidaires

### 🤝 Prise en charge

**Principes :**
- Approche calme et empathique
- Établir le dialogue
- Rassurer et écouter
- Respecter distance sécurité
- Ne pas juger

**Actions :**
- Évaluer danger pour soi/victime/tiers
- Alerter le 15
- Rester avec la victime
- Faciliter intervention secours
- Protéger si comportement dangereux

**⚠️ Si danger immédiat :**
- Appeler forces de l'ordre
- Ne pas s'exposer
- Assurer sa propre sécurité""",
                "image_url": ""
            }
        ]
    },
    {
        "id": "ch10",
        "numero": 10,
        "titre": "Relevage et brancardage",
        "description": "Techniques de relevage à 3 et 4 secouristes, brancardage, installation dans vecteur de transport. (PSE 2)",
        "icon": "Move",
        "formation_type": "PSE",
        "image_url": images["relevage_4"],
        "fiches": [
            {
                "id": "ch10-resume",
                "titre": "Relevage et brancardage (PSE 2)",
                "contenu": """## Relevage et Brancardage

### 🎯 Objectif
Déplacer une victime en sécurité vers le brancard ou véhicule de transport.

### 👥 RELEVAGE À 4 SECOURISTES
**Technique de référence**
- 1 à la tête (commande)
- 1 au bassin
- 2 aux membres inférieurs
- Mouvement synchronisé

### 👥 RELEVAGE À 3 SECOURISTES
**Si pas assez d'équipiers**
- 1 à la tête (commande)
- 1 au niveau thorax/bassin
- 1 aux membres inférieurs

### 🛏️ BRANCARDAGE

**À 4 secouristes :**
- 2 à l'avant
- 2 à l'arrière
- Chef à la tête
- Déplacement synchronisé

**À 3 secouristes :**
- 2 à l'avant
- 1 à l'arrière

### 🔧 Fiches Techniques
- Relevage à 4 et 3 secouristes
- Brancard cuillère
- Brancardage à 4 et 3
- Chaise de transport
- Arrimage victime
- Installation dans vecteur
- Préparation dispositif portage""",
                "image_url": images["relevage_4"]
            }
        ]
    },
    {
        "id": "ch11",
        "numero": 11,
        "titre": "Situations particulières",
        "description": "Situations à nombreuses victimes, repérage et tri. (PSE 1)",
        "icon": "Users",
        "formation_type": "PSE",
        "image_url": "",
        "fiches": [
            {
                "id": "ch11-resume",
                "titre": "Situations à nombreuses victimes (PSE 1)",
                "contenu": """## Situations à Nombreuses Victimes

### 🚨 Définition
Événement provoquant plusieurs victimes simultanées où les moyens habituels sont insuffisants.

**Exemples :**
- Accident de la circulation
- Catastrophe naturelle
- Attentat
- Accident industriel

### 🎯 Principes d'action

**1. RECONNAÎTRE la situation**
- Évaluer nombre victimes
- Identifier dangers persistants

**2. ALERTER avec précision**
- Localisation exacte
- Nature événement
- Nombre victimes estimé
- Moyens nécessaires

**3. REPÉRAGE et TRI**
- Identifier urgences absolues
- Regrouper les victimes
- Établir priorités
- Marquer les victimes

### 🏷️ REPÉRAGE (PSE 1)

**Catégories de tri :**

**🔴 UA - Urgence Absolue**
- Détresse vitale immédiate
- Hémorragie, détresse respiratoire

**🟡 UR - Urgence Relative**
- Blessures sérieuses mais stables
- Peut attendre

**🟢 IMPLIQUÉ**
- Blessures légères
- Marche, parle normalement

**⚫ DCD - Décédé**
- Absence signes vitaux

### ⚠️ Sécurité
- Protéger la zone
- Éviter suraccident
- Coordonner avec secours""",
                "image_url": ""
            }
        ]
    },
    {
        "id": "ch12",
        "numero": 12,
        "titre": "Divers",
        "description": "Informations générales sur les recommandations PSE. (PSE 1 & 2)",
        "icon": "BookOpen",
        "formation_type": "PSE",
        "image_url": "",
        "fiches": [
            {
                "id": "ch12-resume",
                "titre": "Informations générales (PSE 1 & 2)",
                "contenu": """## Informations Générales

### 📚 Référentiel PSE 2024

Ce référentiel est l'ouvrage de référence pour la formation **Premiers Secours en Équipe**.

### 🎓 Formation

**PSE 1 - Premiers Secours en Équipe niveau 1**
- Formation initiale
- 28 heures minimum
- Acquisition compétences de base

**PSE 2 - Premiers Secours en Équipe niveau 2**
- Complément du PSE 1
- 28 heures minimum
- Techniques avancées

### 🔄 Formation continue

**Obligatoire pour maintenir compétences :**
- 6 heures/an minimum
- Révision techniques
- Actualisation connaissances

### 📋 Contenu référentiel

**Types de fiches :**
- **AC** : Apports de Connaissances
- **PR** : Procédures
- **FT** : Fiches Techniques

### 🎯 Principes généraux

**Ne jamais oublier :**
1. Assurer sa propre sécurité
2. Ne pas nuire à la victime
3. Appliquer les techniques apprises
4. Demander de l'aide si nécessaire
5. Surveiller en continu
6. Transmettre le bilan

### 📞 Numéros d'urgence

- **15** : SAMU
- **18** : Pompiers
- **112** : Numéro européen
- **114** : Urgence SMS (sourds/malentendants)""",
                "image_url": ""
            }
        ]
    }
]

async def create_all_pse_chapters():
    """Créer tous les chapitres PSE 2-12"""
    
    print("🚀 Création des chapitres PSE 2 à 12...\n")
    
    for chapter in pse_chapters:
        chapter_id = chapter["id"]
        
        # Skip ch1 déjà créé
        if chapter_id == "ch1":
            print(f"⏭️  Chapitre 1 déjà créé, ignoré")
            continue
        
        # Vérifier si existe
        existing = await db.chapters.find_one({"id": chapter_id, "formation_type": "PSE"})
        
        if existing:
            print(f"⚠️  Chapitre {chapter['numero']} - {chapter['titre']} existe, mise à jour...")
            await db.chapters.replace_one({"id": chapter_id, "formation_type": "PSE"}, chapter)
        else:
            print(f"✅ Création Chapitre {chapter['numero']} - {chapter['titre']}")
            await db.chapters.insert_one(chapter)
    
    # Vérifier le résultat
    count = await db.chapters.count_documents({"formation_type": "PSE"})
    print(f"\n🎉 Total chapitres PSE dans la base : {count}/12")
    
    # Lister tous les chapitres PSE
    chapters = await db.chapters.find(
        {"formation_type": "PSE"}, 
        {"numero": 1, "titre": 1}
    ).sort("numero", 1).to_list(20)
    
    print("\n📚 Liste des chapitres PSE créés :")
    for ch in chapters:
        print(f"   Ch{ch['numero']:02d} - {ch['titre']}")
    
    client.close()

if __name__ == "__main__":
    asyncio.run(create_all_pse_chapters())
