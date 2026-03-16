#!/usr/bin/env python3
"""
Script pour créer les chapitres PSC1 complets basés sur le référentiel 2024
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

psc1_chapters = [
    {
        "id": "psc1-ch1",
        "numero": 1,
        "titre": "Informations générales et Protection",
        "description": "Le citoyen de sécurité civile, alerte et protection des populations, principes de protection.",
        "icon": "Shield",
        "formation_type": "PSC",
        "image_url": "https://images.unsplash.com/photo-1622115297822-a3798fdbe1f6",
        "fiches": [
            {
                "id": "psc1-f1-1",
                "titre": "Le citoyen de Sécurité Civile",
                "contenu": """## Le citoyen de Sécurité Civile

### Protection juridique
Les citoyens qui portent assistance à une personne en situation de danger grave et imminent sont **protégés juridiquement** et considérés comme collaborateurs du service public.

---

### Messages clés

**Prévenir les accidents :**
- Éliminer les dangers ou réduire les risques
- Suivre les consignes de sécurité
- Vérifier régulièrement l'état des personnes vulnérables

**Entretenir ses compétences :**
- Mettre à jour régulièrement ses connaissances en premiers secours
- Envisager la formation PSC1 ou supérieure

**S'engager :**
- Devenir bénévole dans les associations de sécurité civile
- Utiliser les outils numériques d'alerte d'urgence

---

### Impact psychologique d'une intervention

**Réactions normales :**
- Stress pendant l'intervention
- Fatigue après l'intervention
- Besoin de parler

**Gestion du stress :**
- Se préparer par une formation régulière
- Adopter une posture empathique avec les victimes
- Débriefing avec les services d'urgence"""
            },
            {
                "id": "psc1-f1-2",
                "titre": "Alerte et protection des populations",
                "contenu": """## Alerte et protection des populations

### Systèmes d'alerte

**Signal National d'Alerte (SNA) :**
- Sirènes pour confinement ou évacuation
- Signaux spécifiques selon les risques

**FR-ALERT :**
- Notifications sur téléphone mobile
- Danger imminent

**Autres moyens :**
- Radio, télévision, médias locaux
- Réseaux sociaux officiels (Ministère de l'Intérieur)

---

### Conduite à tenir

**Avant une crise :**
- S'informer sur les risques locaux
- Préparer un kit d'urgence

**Face à une alerte :**
- Rejoindre un bâtiment sûr
- **Ne pas aller chercher les enfants à l'école**
- Rester informé de la situation
- Éviter les appels non urgents
- Suivre les instructions officielles

**Mesures de confinement :**
- Fermer portes et fenêtres
- Colmater les ouvertures
- Couper la ventilation/climatisation

---

### En période d'épidémie

- Se laver les mains régulièrement
- Tousser/éternuer dans le coude
- Utiliser des mouchoirs jetables
- Éviter de se toucher le visage
- Maintenir une distance d'au moins 1 mètre
- Porter un masque si la distance ne peut être maintenue"""
            },
            {
                "id": "psc1-f1-3",
                "titre": "Protection et dégagement d'urgence",
                "contenu": """## Protection

### Protéger une personne exposée à un danger

- Supprimer ou éloigner le danger si possible **sans risquer sa propre sécurité**
- Délimiter clairement la zone de danger

---

### Dégagement d'urgence d'une victime

**Exceptionnellement**, si une victime ne peut échapper à un danger réel et immédiat :
- La déplacer vers un lieu sûr
- Utiliser le trajet le plus sûr et le plus rapide

⚠️ **Le dégagement d'urgence est un dernier recours en raison du danger potentiel**

---

### Face à une attaque terroriste ou violence

**Suivre les consignes nationales :**
1. **S'échapper** si c'est sécuritaire
2. Sinon **se cacher** et se barricader
3. **Alerter** les services d'urgence (qui, quoi, où)
4. Si la fuite/cachette est impossible et que la vie est en danger : **résister**

---

### En période épidémique (maladie respiratoire)

- Appliquer les gestes barrières
- Demander aux témoins de les respecter
- Faire isoler la victime si possible, lui faire porter un masque
- Maintenir ses distances des personnes malades
- Porter un masque si vous devez vous approcher
- Se laver les mains après l'intervention"""
            },
            {
                "id": "psc1-f1-4",
                "titre": "L'alerte aux secours",
                "contenu": """## L'alerte aux secours

### Objectif
Informer un service d'urgence de la situation d'une victime et de la nature de l'assistance requise.

---

### Numéros d'urgence

| Numéro | Service | Usage |
|--------|---------|-------|
| **18** | Pompiers | Secours à personne, accidents, incendies |
| **15** | SAMU | Urgences médicales, problèmes de santé |
| **112** | Européen | Numéro d'urgence universel |
| **114** | SMS/Visio | Personnes sourdes, malentendantes, violences domestiques |

---

### Comment passer l'appel

1. **Transmettre clairement les informations**
2. **Répondre aux questions** des services d'urgence
3. **Suivre les instructions**
4. **Ne raccrocher que quand on vous le demande**

---

### Informations minimales à transmettre

- 📞 Numéro de téléphone ou point d'appel
- ❓ Nature du problème (maladie, accident, agression)
- 👥 Nombre de victimes
- 📍 Localisation précise de l'événement

---

### En cas de maladie respiratoire (COVID-19, grippe)

- Si signes de maladie sans détresse vitale : demander à la victime d'appeler son médecin
- Respecter les gestes barrières
- Si difficulté respiratoire ou signes d'urgence vitale : appeler un numéro d'urgence"""
            }
        ]
    },
    {
        "id": "psc1-ch2",
        "numero": 2,
        "titre": "Obstruction des voies aériennes",
        "description": "Reconnaître et traiter un étouffement chez l'adulte, l'enfant et le nourrisson.",
        "icon": "Wind",
        "formation_type": "PSC",
        "image_url": "https://images.unsplash.com/photo-1622115585848-1d5b6e8af4e4",
        "fiches": [
            {
                "id": "psc1-f2-1",
                "titre": "Reconnaître l'obstruction",
                "contenu": """## Obstruction des voies aériennes

### Définition
Obstruction des voies aériennes où le mouvement de l'air est entravé.

---

### 🔴 OBSTRUCTION COMPLÈTE (urgence vitale)

**La victime :**
- ❌ Ne peut plus parler, crier ou tousser
- ❌ Ne peut émettre AUCUN son
- 😮 Garde la bouche ouverte
- 😰 S'agite, panique
- 🔵 Devient progressivement bleue (cyanose)
- 🤚 Porte souvent les mains à sa gorge

**⏱️ URGENCE ABSOLUE : Quelques minutes avant la perte de connaissance !**

---

### 🟡 OBSTRUCTION PARTIELLE

**La victime :**
- ✓ Peut encore parler (même difficilement)
- ✓ Peut tousser (même faiblement)
- ✓ Respire avec bruit (sifflement)
- ✓ Reste consciente
- ⚠️ Peut évoluer vers une obstruction complète

---

### Causes fréquentes

**Chez l'adulte et la personne âgée :**
- Aliments (noix, morceaux de viande)
- Bonbons durs
- Arêtes de poisson

**Chez l'enfant :**
- Aliments (carottes crues, raisins entiers)
- Petits jouets, billes, pièces
- Morceaux de ballons éclatés"""
            },
            {
                "id": "psc1-f2-2",
                "titre": "Conduite à tenir - Obstruction partielle",
                "contenu": """## Obstruction partielle

### 🟡 SI LA VICTIME TOUSSE ENCORE

1. **Installer la victime** confortablement
2. **Encourager à tousser** - la toux est le meilleur mécanisme d'expulsion
3. **Demander un avis médical**
4. **Surveiller** attentivement la victime

---

### ⚠️ SURVEILLANCE

Si la toux devient inefficace ou la victime montre des signes de fatigue :

➡️ **Traiter comme une obstruction COMPLÈTE**

---

### Points importants

- Ne jamais taper dans le dos si la victime tousse efficacement
- Rester près de la victime
- Observer l'évolution des symptômes"""
            },
            {
                "id": "psc1-f2-3",
                "titre": "Conduite à tenir - Obstruction complète",
                "contenu": """## Obstruction complète - Adulte/Enfant

### Étape 1 : Les claques dans le dos

1. Se placer sur le côté et légèrement en arrière de la victime
2. Soutenir le thorax d'une main
3. Pencher la victime en avant
4. Donner **1 à 5 claques vigoureuses** entre les omoplates avec le talon de la main ouverte

---

### Étape 2 : Compressions abdominales (Heimlich)

**Si les claques sont inefficaces :**

1. Se placer debout ou à genoux derrière la victime
2. Passer les bras sous les bras de la victime, autour du haut de l'abdomen
3. Placer le poing (dos de la main vers le haut) juste au-dessus du nombril
4. Placer l'autre main sur le poing
5. Tirer brusquement vers l'arrière et vers le haut
6. Effectuer **1 à 5 compressions**

---

### Cycle à répéter

**5 claques dans le dos** ➡️ **5 compressions abdominales** ➡️ Répéter

**ARRÊTER quand :**
- La victime tousse
- La victime respire
- L'objet est expulsé

---

### ⚠️ Si la victime perd connaissance

1. L'allonger au sol
2. Appeler les secours
3. Commencer la RCP
4. Vérifier la bouche à chaque cycle et retirer l'objet si visible"""
            },
            {
                "id": "psc1-f2-4",
                "titre": "Cas particuliers",
                "contenu": """## Cas particuliers

### 👶 Nourrisson

**Claques dans le dos :**
1. Placer le nourrisson face vers le bas sur l'avant-bras
2. Soutenir la tête avec les doigts
3. Tête plus basse que le tronc
4. Donner 1 à 5 claques entre les omoplates

**Compressions thoraciques :**
1. Retourner le nourrisson sur le dos
2. Placer la pulpe de deux doigts sur le sternum
3. Effectuer 1 à 5 compressions profondes

---

### 🤰 Femme enceinte / Personne obèse

**Si l'abdomen ne peut pas être encerclé :**
- Effectuer des **compressions thoraciques** au lieu des compressions abdominales
- Placer le poing au milieu du sternum
- Tirer brusquement vers l'arrière

---

### Victime allongée ou immobile

Effectuer des compressions thoraciques comme pour l'arrêt cardiaque"""
            }
        ]
    },
    {
        "id": "psc1-ch3",
        "numero": 3,
        "titre": "Hémorragies externes",
        "description": "Identifier et arrêter une hémorragie externe, compression directe et garrot.",
        "icon": "Droplet",
        "formation_type": "PSC",
        "image_url": "https://images.unsplash.com/photo-1579684385127-1ef15d508118",
        "fiches": [
            {
                "id": "psc1-f3-1",
                "titre": "Reconnaître une hémorragie",
                "contenu": """## Hémorragies externes

### Définition
Saignement prolongé d'une plaie ou d'un orifice naturel qui ne s'arrête pas spontanément.

---

### Signes
- Le sang **imbibe rapidement** un tissu
- Le saignement ne s'arrête pas seul
- ⚠️ Les écorchures mineures qui cessent de saigner ne sont PAS des hémorragies

---

### Causes
- Traumatismes (coupures, chutes, projectiles)
- Conditions médicales (rupture de varice)

---

### Risques

**Pour la victime :**
- Détresse circulatoire
- Arrêt cardiaque dû à la perte de sang

**Pour le sauveteur :**
- Infection par maladies transmissibles si exposé au sang

---

### Principe d'action
**Arrêter ou limiter la perte de sang** pour retarder l'apparition du choc"""
            },
            {
                "id": "psc1-f3-2",
                "titre": "Compression directe",
                "contenu": """## La compression directe

### Indication
Toute plaie avec saignement abondant

### Justification
Arrêter le saignement en comprimant les vaisseaux sanguins

---

### Réalisation

**Compression manuelle :**
1. Appuyer fermement directement sur le site du saignement
2. Utiliser une main, de préférence avec un tissu propre (mouchoir, torchon, vêtement)
3. Continuer jusqu'à l'arrivée des secours
4. Si pas de tissu disponible : utiliser les mains nues

---

### Pansement compressif

**Peut remplacer la compression manuelle si le saignement est arrêté :**
1. Couche de matériau absorbant
2. Recouverte d'une bande ou d'un lien large
3. Fixée fermement

⚠️ **Non adapté pour** : cou, tête, thorax ou abdomen

---

### Points clés
- La compression doit être **suffisante** pour arrêter le saignement
- La compression doit être **continue**"""
            },
            {
                "id": "psc1-f3-3",
                "titre": "Le garrot",
                "contenu": """## Le garrot

### Indication
Hémorragie de membre où la compression directe est :
- Inefficace
- Impossible (victimes multiples, plaie inaccessible)

### Justification
Arrêter l'hémorragie externe en interrompant complètement la circulation dans le membre

---

### Matériel

**Garrot improvisé :**
- Bande large et non élastique (3-5 cm, au moins 1,50 m)
- Barre rigide (10-20 cm) pour le serrage

**Garrot industriel :**
- Disponible dans le commerce
- Préférable si disponible

⚠️ **Ne PAS utiliser** les bandes élastiques destinées aux prises de sang

---

### Réalisation

1. Appliquer le garrot **5-7 cm au-dessus de la plaie** (entre le cœur et la plaie)
2. **Jamais sur une articulation**

**Avec garrot improvisé :**
1. Enrouler la bande deux fois autour du membre
2. Faire un nœud
3. Placer la barre au-dessus du nœud
4. Faire deux autres nœuds pour la fixer
5. Tourner la barre pour serrer jusqu'à arrêt du saignement
6. Sécuriser la barre

---

### ⚠️ Points critiques
- Le garrot ne doit **JAMAIS être retiré** sans avis médical
- **Noter l'heure** de pose du garrot"""
            },
            {
                "id": "psc1-f3-4",
                "titre": "Cas particuliers et protection",
                "contenu": """## Situations particulières

### Saignement de nez
1. S'asseoir, penché en avant
2. Se moucher vigoureusement
3. Pincer les narines pendant 10 minutes
4. Consulter si le saignement persiste, récidive, ou suite à un choc

### Vomissement / Crachement de sang
- Signe de maladie grave
- Position confortable si conscient
- Position sur le côté si inconscient
- Appeler les secours

### Saignement d'un orifice naturel
- Position allongée
- Appeler les secours

---

## Protection du sauveteur

### Mesures de protection

- Se protéger avec des **gants** ou un sac plastique
- **Éviter** de toucher bouche, nez ou yeux
- Se laver les mains et toute peau souillée
- Changer de vêtements souillés rapidement

### Quand consulter

- Si vous avez une plaie qui a été souillée
- Si du sang a éclaboussé votre visage"""
            }
        ]
    },
    {
        "id": "psc1-ch4",
        "numero": 4,
        "titre": "Perte de connaissance",
        "description": "Reconnaître et prendre en charge une victime inconsciente qui respire.",
        "icon": "User",
        "formation_type": "PSC",
        "image_url": "https://images.unsplash.com/photo-1630225757034-d49c20300b55",
        "fiches": [
            {
                "id": "psc1-f4-1",
                "titre": "Reconnaître la perte de connaissance",
                "contenu": """## Perte de connaissance

### Définition
Une personne qui **ne répond pas** et **ne réagit pas** aux stimuli verbaux ou physiques mais qui **respire**.

---

### Causes
- Origine traumatique
- Origine médicale
- Origine toxique

---

### Risques
Évolution vers l'arrêt respiratoire puis cardiaque par :
- Obstruction des voies aériennes (chute de la langue)
- Inhalation de liquides dans la gorge (vomissements)

---

### Principe d'action
**Assurer l'ouverture des voies aériennes** pour permettre le drainage et la respiration"""
            },
            {
                "id": "psc1-f4-2",
                "titre": "Évaluation de la victime",
                "contenu": """## Évaluation de la conscience et de la respiration

### Étape 1 : Évaluer la réactivité

**Poser des questions simples :**
- "Comment allez-vous ?"
- "Vous m'entendez ?"

**Stimuler doucement :**
- Secouer légèrement les épaules

**Demander une commande simple :**
- "Serrez-moi la main"

---

### Si la victime répond ou réagit
➡️ Suivre la procédure pour un malaise

### Si la victime ne répond pas et ne réagit pas

1. **Demander de l'aide** si vous êtes seul
2. **Allonger la victime** sur le dos
3. **Libérer les voies aériennes** (bascule de la tête en arrière + élévation du menton)
4. **Vérifier la respiration** pendant 10 secondes maximum

---

### Vérification de la respiration

**Regarder** : le thorax se soulève-t-il ?
**Écouter** : entend-on un souffle ?
**Sentir** : sent-on un souffle sur la joue ?

⏱️ **Maximum 10 secondes**"""
            },
            {
                "id": "psc1-f4-3",
                "titre": "Position Latérale de Sécurité (PLS)",
                "contenu": """## Position Latérale de Sécurité

### Indication
Victime inconsciente mais qui respire, d'origine **non traumatique**

### Justification
- Maintenir les voies aériennes ouvertes
- Permettre l'écoulement des liquides de la bouche
- Empêcher la langue de bloquer les voies aériennes

---

### Réalisation (Adulte/Enfant)

**Étape 1 - Préparer le retournement :**
1. Retirer les lunettes
2. Aligner les jambes
3. Placer le bras le plus proche à angle droit, coude plié, paume vers le haut
4. Se placer à côté de la victime
5. Amener l'autre bras de la victime contre son oreille, main sur votre joue
6. Saisir la jambe opposée derrière le genou, la plier en gardant le pied au sol

**Étape 2 - Retourner la victime :**
1. Tirer la jambe pliée pour faire pivoter la victime vers vous jusqu'à ce que le genou touche le sol
2. Retirer doucement la main de sous la tête tout en la maintenant

**Étape 3 - Stabiliser :**
1. Ajuster la jambe supérieure (hanche et genou à angle droit)
2. Ouvrir la bouche de la victime sans bouger la tête

---

### Pour les nourrissons
Placer sur le côté, généralement dans les bras du sauveteur, dos contre le sauveteur

---

### Points clés
- Position stable
- Minimiser les mouvements de la colonne
- Permettre une surveillance continue de la respiration
- Permettre le drainage des liquides"""
            },
            {
                "id": "psc1-f4-4",
                "titre": "Cas traumatique et surveillance",
                "contenu": """## Victime traumatisée ou origine inconnue

### Conduite à tenir

1. **Laisser la victime sur le dos**
2. **Maintenir les voies aériennes ouvertes**
3. **Appeler les secours**
4. **Surveiller la respiration** en continu
5. En cas de vomissement : **tourner prudemment sur le côté** en maintenant l'axe tête-cou-tronc

---

## Surveillance continue

### Dans tous les cas

- Protéger du froid/chaud
- Surveiller la respiration en permanence

### Si la respiration s'arrête ou devient anormale

➡️ **Traiter comme un arrêt cardiaque** et alerter les secours

---

## Libération des voies aériennes

### Technique

**Adulte/Enfant :**
1. Placer une main sur le front de la victime
2. Placer les doigts de l'autre main sous la pointe du menton
3. Basculer doucement la tête en arrière tout en soulevant le menton

**Nourrisson :**
1. Amener la tête en position neutre (dans l'axe du corps)
2. Soulever le menton
3. Éviter l'extension excessive de la colonne cervicale"""
            }
        ]
    },
    {
        "id": "psc1-ch5",
        "numero": 5,
        "titre": "Arrêt cardiaque",
        "description": "Reconnaître un arrêt cardiaque, réaliser la RCP et utiliser un défibrillateur.",
        "icon": "Heart",
        "formation_type": "PSC",
        "image_url": "https://images.unsplash.com/photo-1759872138841-c342bd6410ae",
        "fiches": [
            {
                "id": "psc1-f5-1",
                "titre": "Reconnaître l'arrêt cardiaque",
                "contenu": """## Arrêt cardiaque

### Définition
Le cœur ne fonctionne plus efficacement, empêchant l'oxygénation du cerveau.

---

### Signes

La victime ne répond pas, ne réagit pas ET :
- ❌ **Ne respire pas** (pas de mouvement thoracique, pas de son, pas de souffle)
- ❌ Ou a une **respiration anormale** (lente, bruyante, difficile, inefficace - gasps)

⚠️ **Les gasps** (respiration agonale) sont un signe d'arrêt cardiaque !

---

### Causes

**Chez l'adulte :**
- Problèmes cardiaques (infarctus, fibrillation ventriculaire)

**Chez l'enfant :**
- Origine respiratoire le plus souvent

**Autres causes :**
- Détresse circulatoire (hémorragie, brûlures graves)
- Obstruction des voies aériennes
- Intoxication
- Traumatisme
- Noyade

---

### Risques
- **Décès en quelques minutes** par manque d'oxygène au cerveau et au cœur
- Des lésions cérébrales peuvent survenir dès la première minute"""
            },
            {
                "id": "psc1-f5-2",
                "titre": "Réanimation Cardio-Pulmonaire (RCP)",
                "contenu": """## La chaîne de survie

**Alerter** → **RCP** → **Défibrillation** = Augmente les chances de survie

---

## Compressions thoraciques

### Position de la victime
- Horizontale, sur le dos
- Surface dure de préférence

### Position du sauveteur
À genoux près de la victime

### Localisation des compressions

| Âge | Localisation |
|-----|--------------|
| Adulte | Milieu du thorax, sur le sternum, moitié inférieure |
| Enfant | Sur le sternum, un doigt au-dessus du processus xiphoïde |
| Nourrisson | Sur le sternum, avec deux doigts |

---

### Réalisation

**Adulte/Enfant :**
- Placer le talon d'une main au centre du thorax
- Placer l'autre main dessus, doigts entrelacés
- Bras tendus, coudes verrouillés
- Comprimer verticalement

**Nourrisson :**
- Utiliser deux doigts au centre du thorax

---

### Paramètres

| | Adulte | Enfant | Nourrisson |
|--|--------|--------|------------|
| Profondeur | ~5 cm (max 6 cm) | ~5 cm (1/3 thorax) | ~4 cm (1/3 thorax) |
| Fréquence | **100-120/min** | **100-120/min** | **100-120/min** |

⚠️ **Relâcher complètement** le thorax entre les compressions"""
            },
            {
                "id": "psc1-f5-3",
                "titre": "Insufflations et cycle RCP",
                "contenu": """## Insufflations (bouche-à-bouche)

### Réalisation

**Adulte/Enfant :**
1. Ouvrir les voies aériennes (bascule tête/menton)
2. Pincer le nez de la victime
3. Ouvrir la bouche, soulever le menton
4. Prendre une respiration normale
5. Faire un joint étanche sur la bouche
6. Souffler pendant environ 1 seconde
7. Observer le soulèvement du thorax
8. Relâcher légèrement pour permettre l'expiration
9. Donner une seconde insufflation

**Nourrisson :**
- Tête en position neutre
- Couvrir la bouche ET le nez avec votre bouche

---

### Si le thorax ne se soulève pas
- Vérifier la position des voies aériennes
- Vérifier l'étanchéité
- Rechercher un corps étranger visible

---

## Cycle de RCP

### Adulte
**30 compressions : 2 insufflations**

### Enfant/Nourrisson
**5 insufflations initiales** puis **15 compressions : 2 insufflations**

---

### Si les insufflations sont impossibles
(répulsion, COVID-19, etc.)

➡️ Effectuer des **compressions thoraciques continues** à 100-120/min"""
            },
            {
                "id": "psc1-f5-4",
                "titre": "Défibrillation (DAE)",
                "contenu": """## Le Défibrillateur Automatisé Externe (DAE)

### Fonction
- Analyse l'activité électrique du cœur
- Reconnaît les rythmes anormaux causant l'arrêt cardiaque
- Délivre un choc électrique pour arrêter l'activité électrique chaotique

### Sécurité
Le DAE est **conçu pour être utilisé par le grand public** et est sûr

---

## Utilisation

### Étapes générales
1. **Allumer le DAE**
2. **Suivre les instructions** (vocales et visuelles)
3. **Continuer la RCP** jusqu'à ce que le DAE demande d'arrêter

### Application des électrodes

**Adulte :**
- Appliquer sur le thorax nu selon le schéma indiqué
- Généralement : une sous la clavicule droite, une sous l'aisselle gauche

**Enfant/Nourrisson :**
- Utiliser des électrodes pédiatriques si disponibles
- Si non disponibles : une sur le thorax, une dans le dos

---

### Pendant l'analyse
- **S'assurer que personne ne touche la victime**
- Le DAE analyse le rythme cardiaque

### Si choc conseillé
1. S'assurer que tout le monde s'écarte
2. Appuyer sur le bouton de choc (ou le DAE délivre automatiquement)
3. **Reprendre immédiatement** les compressions thoraciques

### Si pas de choc conseillé
➡️ **Reprendre immédiatement** les compressions thoraciques

---

## Précautions

| Situation | Action |
|-----------|--------|
| Thorax humide | Sécher avant d'appliquer les électrodes |
| Patch médicamenteux | Retirer avant d'appliquer les électrodes |
| Pacemaker | Placer l'électrode à ~1 main de distance |
| Poils excessifs | Raser si nécessaire |
| Sol mouillé | Déplacer la victime sur surface sèche |"""
            },
            {
                "id": "psc1-f5-5",
                "titre": "Conduite complète et cas particuliers",
                "contenu": """## Conduite à tenir complète

### Avec un témoin

1. **Demander** d'appeler les secours et d'apporter un DAE
2. **Commencer la RCP** (30:2)
3. **Utiliser le DAE** dès qu'il est disponible
4. **Suivre les instructions** du DAE
5. **Continuer** jusqu'à l'arrivée des secours

### Seul

1. **Appeler les secours** (haut-parleur si possible)
2. **Commencer la RCP**
3. Si un DAE est accessible en moins de 10 secondes, aller le chercher
4. **Continuer** jusqu'à l'arrivée des secours

---

## En période d'épidémie (COVID-19)

### Modifications

1. **Se protéger** avec un masque
2. **Évaluer la respiration** sans basculer la tête ni ouvrir la bouche
3. **Ne pas faire de bouche-à-bouche** sauf :
   - Si vous vivez avec la victime
   - Si c'est un enfant/nourrisson
4. Placer un **tissu sur le visage** de la victime pour les compressions et la défibrillation
5. **Se laver les mains** après l'intervention

---

## Quand arrêter la RCP

- Les secours prennent le relais
- La victime reprend une respiration normale
- Épuisement du sauveteur (relais toutes les 2 min si possible)

---

## Points clés

⏱️ **Agir vite** - chaque minute compte
🔄 **Ne pas interrompre** les compressions
⚡ **Défibriller** dès que possible
🤝 **Se relayer** toutes les 2 minutes"""
            }
        ]
    },
    {
        "id": "psc1-ch6",
        "numero": 6,
        "titre": "Malaises",
        "description": "Reconnaître et prendre en charge une personne victime d'un malaise.",
        "icon": "Activity",
        "formation_type": "PSC",
        "image_url": "https://images.unsplash.com/photo-1576091160550-2173dba999ef",
        "fiches": [
            {
                "id": "psc1-f6-1",
                "titre": "Reconnaître un malaise",
                "contenu": """## Malaises

### Définition
Sensation de mal-être indiquant un désordre corporel, sans cause clairement identifiée. La victime est **consciente** mais ne va pas bien.

---

### Causes
- Maladies diverses
- Intoxications
- Allergies

---

### Risques
Certains signes nécessitent des soins médicaux urgents pour éviter :
- Des séquelles permanentes
- Le décès

⚠️ Même des signes apparemment mineurs peuvent indiquer une situation grave

---

### Principe d'action
- Mettre la victime au repos
- L'écouter et l'observer
- Recueillir des informations pour l'avis médical"""
            },
            {
                "id": "psc1-f6-2",
                "titre": "Signes d'alerte",
                "contenu": """## Signes nécessitant une alerte immédiate

### 🫀 Accident cardiaque
- Douleur thoracique (oppressante, serrant, irradiant vers le bras ou la mâchoire)

### 🧠 AVC (Accident Vasculaire Cérébral)

**Signes FAST :**
- **F**ace : Asymétrie du visage (bouche de travers)
- **A**rm : Faiblesse ou paralysie d'un bras
- **S**peech : Difficulté à parler
- **T**ime : Noter l'heure de début des symptômes

**Autres signes d'AVC :**
- Perte de vision
- Maux de tête violents
- Perte d'équilibre
- Chute inexpliquée

---

### 🦠 Maladie infectieuse contagieuse
- Fièvre (>37,8°C)
- Frissons
- Sueurs abondantes
- Courbatures
- Fatigue intense

### Autres signes graves
- Douleur abdominale intense avec troubles digestifs
- Difficulté à respirer ou parler
- Sensation de froid avec sueurs ou pâleur intense"""
            },
            {
                "id": "psc1-f6-3",
                "titre": "Conduite à tenir",
                "contenu": """## Conduite à tenir face à un malaise

### 1. Position de repos

- **Allongée** confortablement (lit, canapé, sol)
- **Assise** si difficulté respiratoire
- **Toute position** que la victime trouve confortable

### 2. Mesures de protection

En période d'épidémie :
- Appliquer les gestes barrières
- Maintenir les distances
- Demander à la victime de porter un masque
- Desserrer les vêtements si gênants

### 3. Rassurer la victime

- Rester calme
- Protéger des éléments (froid, chaleur, pluie)

---

## Recueil d'informations

À noter pour les secours :
- Âge de la victime
- Durée du malaise
- Antécédents d'épisodes similaires
- État de santé actuel
- Médicaments en cours

---

## Appel aux secours

1. Contacter les services médicaux (15)
2. Transmettre toutes les informations recueillies
3. Suivre les instructions
4. Si demandé : donner le médicament habituel ou du sucre

---

## Si aggravation

- Recontacter les secours
- Pratiquer les premiers secours si perte de connaissance"""
            },
            {
                "id": "psc1-f6-4",
                "titre": "Cas particuliers",
                "contenu": """## Malaise vagal (pré-syncope)

### Manœuvres physiques préventives

Si la victime reconnaît les signes avant-coureurs d'une perte de connaissance :

**S'accroupir :**
- S'accroupir, tête entre les genoux

**Croiser les jambes :**
- Debout ou assis contre un mur
- Croiser les jambes
- Contracter les muscles des jambes et fessiers
- Contracter les muscles abdominaux

**Mains crochées :**
- Crocher les doigts ensemble
- Coudes écartés
- Tirer comme pour séparer les mains

➡️ Ces manœuvres sont à poursuivre après s'être allongé

---

## Malaise lié à la chaleur

### Conduite à tenir

1. **Déplacer** la victime dans un endroit frais et bien ventilé
2. **Mesurer** la température si possible
3. **Desserrer** ou retirer les vêtements
4. **Rafraîchir** la victime :
   - Pulvériser de l'eau froide
   - Envelopper dans des linges mouillés froids
   - Placer sous un ventilateur
   - Appliquer des poches de glace (enveloppées) aux aisselles, aines ou cou
5. Si consciente et capable d'avaler : **donner** de petites quantités d'eau fraîche

---

### Signes de gravité
- Température très élevée
- Confusion
- Perte de connaissance

➡️ **Appeler immédiatement les secours**"""
            }
        ]
    },
    {
        "id": "psc1-ch7",
        "numero": 7,
        "titre": "Plaies et Brûlures",
        "description": "Évaluer la gravité et prendre en charge les plaies et les brûlures.",
        "icon": "Bandage",
        "formation_type": "PSC",
        "image_url": "https://images.unsplash.com/photo-1612277795421-9bc7706a4a34",
        "fiches": [
            {
                "id": "psc1-f7-1",
                "titre": "Les plaies",
                "contenu": """## Les plaies

### Définition
Lésion de la peau et des tissus sous-jacents

---

### Types de plaies

**Plaie simple :**
- Petite coupure superficielle
- Écorchure avec peu de saignement

**Plaie grave :**
- Saignement important associé
- Mécanisme pénétrant (objet tranchant, morsure, projectile)
- Localisation critique (thorax, abdomen, œil, près d'un orifice naturel)
- Aspect déchiqueté ou écrasé

---

### Risques
- Hémorragie
- Insuffisance respiratoire (plaie thoracique)
- Infection secondaire (tétanos)

---

## Conduite à tenir - Plaie grave

1. **Ne jamais retirer** les corps étrangers fichés
2. **Arrêter le saignement** (voir Hémorragies)
3. **Position d'attente** :
   - Thorax : assis (facilite la respiration)
   - Abdomen : allongé, jambes fléchies
   - Œil : allongé, tête maintenue
   - Autres : allongé
4. **Protéger** des éléments
5. **Appeler les secours** et suivre les instructions
6. **Rassurer** et **surveiller** la victime"""
            },
            {
                "id": "psc1-f7-2",
                "titre": "Plaies simples et soins",
                "contenu": """## Plaie simple - Conduite à tenir

### Étapes

1. **Se laver les mains** à l'eau et au savon

2. **Nettoyer la plaie** :
   - À l'eau courante (avec ou sans savon)
   - Abondamment

3. **Désinfecter** :
   - Seulement si pas d'eau disponible

4. **Protéger** :
   - Couvrir avec un pansement adhésif

5. **Conseiller** de consulter un médecin :
   - Pour vérifier la validité de la vaccination antitétanique
   - Si des signes d'infection apparaissent

---

### Signes d'infection à surveiller
- Rougeur croissante
- Gonflement
- Douleur qui augmente
- Écoulement de pus
- Fièvre

---

### Rappel important

**Le tétanos** est une maladie grave !
➡️ Toujours vérifier la vaccination"""
            },
            {
                "id": "psc1-f7-3",
                "titre": "Les brûlures",
                "contenu": """## Les brûlures

### Définition
Lésion de la peau, des voies aériennes ou digestives causée par :
- Chaleur
- Produits chimiques
- Électricité
- Frottement
- Rayonnement

---

### Types de brûlures

**Brûlure simple :**
- Rougeur
- Cloque inférieure à la moitié de la paume de la victime

**Brûlure grave :**
- Cloques supérieures à la moitié de la paume
- Destruction profonde (blanc/noir, parfois indolore)
- Localisation : visage, cou, mains, articulations, orifices naturels
- Rougeur étendue chez l'enfant (coup de soleil généralisé)
- Brûlure chimique, électrique ou radiologique

---

### Risques
- Défaillance circulatoire ou respiratoire (brûlures étendues/inhalation)
- Douleur sévère
- Infection
- Séquelles fonctionnelles/esthétiques"""
            },
            {
                "id": "psc1-f7-4",
                "titre": "Conduite à tenir - Brûlures",
                "contenu": """## Conduite à tenir

### Étape 1 : REFROIDIR

**Immédiatement** refroidir la zone brûlée :
- Eau courante **tempérée** (pas glacée)
- Pendant **au moins 10 minutes** (idéalement 20)
- ⚠️ Au-delà de 30 minutes après la brûlure, le refroidissement est inefficace

### Étape 2 : RETIRER

Retirer vêtements et bijoux **s'ils ne sont pas adhérents** à la peau

---

## Brûlure grave

1. **Appeler les secours** immédiatement pendant le refroidissement
2. **Continuer** le refroidissement selon les instructions
3. **Positionner** la victime :
   - Allongée confortablement
   - Assise si difficulté respiratoire
4. **Laisser visible** la zone brûlée si possible
5. **Surveiller** et suivre les instructions
6. ❌ **Aucun produit** sans avis médical

---

## Brûlure simple

1. **Continuer** le refroidissement jusqu'à disparition de la douleur
2. ❌ **Ne jamais percer** les cloques
3. **Protéger** avec un pansement stérile ou film plastique
4. **Consulter** pour le rappel antitétanique et si signes d'infection

---

## Cas particuliers

### Brûlure chimique
- Se protéger du produit
- **Rincer abondamment** à l'eau courante (20-30 min)
- Retirer les vêtements souillés sous l'eau
- Pour les yeux : rincer sans atteindre l'autre œil
- ❌ **Ne pas faire vomir** si ingestion
- Appeler les secours

### Brûlure électrique
- ❌ **Ne pas toucher** la victime avant suppression du risque électrique
- Refroidir les zones brûlées visibles
- Appeler les secours

### Brûlure interne (vapeurs/caustiques)
- Position assise si difficulté respiratoire
- Appeler les secours"""
            }
        ]
    },
    {
        "id": "psc1-ch8",
        "numero": 8,
        "titre": "Traumatismes",
        "description": "Reconnaître et prendre en charge les traumatismes des os, articulations et organes.",
        "icon": "Bone",
        "formation_type": "PSC",
        "image_url": "https://images.unsplash.com/photo-1559757175-7cb057a7e65b",
        "fiches": [
            {
                "id": "psc1-f8-1",
                "titre": "Reconnaître un traumatisme",
                "contenu": """## Les traumatismes

### Définition
Lésions des :
- Os (fractures)
- Articulations (entorses, luxations)
- Organes
- Peau

---

### Signes
- Douleur intense
- Difficulté ou impossibilité de mouvement
- Gonflement
- Déformation de la zone touchée

### Signes secondaires (traumatisme crânien, thoracique, abdominal)
- Perte de connaissance
- Maux de tête persistants
- Vomissements
- Agitation ou somnolence
- Douleur abdominale

### Traumatisme du rachis
Peut affecter la moelle épinière ➡️ Risque de paralysie

---

### Causes
- Choc, coup, chute
- Mouvement forcé

---

### Risques
- Complications neurologiques (paralysie)
- Troubles de la conscience
- Détresse respiratoire
- Choc circulatoire"""
            },
            {
                "id": "psc1-f8-2",
                "titre": "Conduite à tenir",
                "contenu": """## Conduite à tenir

### Principe fondamental
❌ **NE PAS DÉPLACER LA VICTIME**

---

### Si perte de connaissance
➡️ Suivre la procédure pour perte de connaissance

### Si victime consciente et présentant des signes

1. **Demander fermement** à la victime de ne pas bouger la partie touchée
2. **Appeler les secours** et suivre les instructions
3. **Protéger** du froid, de la chaleur ou des intempéries
4. **Surveiller** la victime et lui parler régulièrement

---

## Suspicion de traumatisme du rachis (douleur au cou)

1. **Demander** à la victime de ne pas bouger la tête
2. **Appeler les secours**
3. Si possible : **stabiliser la colonne cervicale** en maintenant la tête avec les deux mains
4. **Surveiller** et parler à la victime

---

## Fracture déplacée d'un membre

1. ❌ **Ne pas tenter de réaligner**
2. **Appeler les secours**
3. **Surveiller** et parler à la victime"""
            },
            {
                "id": "psc1-f8-3",
                "titre": "Maintien de la tête",
                "contenu": """## Maintien de la tête

### Indication
- Victime avec douleur au cou après un traumatisme (suspicion de lésion de la colonne cervicale)
- Blessure à l'œil

### Justification
Stabiliser la tête et limiter les mouvements involontaires du cou

---

### Réalisation

1. **Informer** la victime de ne pas bouger la tête et de vos actions
2. S'installer **à genoux** de façon stable, dans l'axe de la tête
3. **Appuyer** les coudes sur le sol ou les genoux
4. **Placer** les mains de chaque côté de la tête de la victime
5. **Maintenir** la tête dans sa position actuelle

---

### Points clés

- Le sauveteur doit être en **position stable**
- Le maintien doit **limiter les mouvements**
- Maintenir jusqu'à l'arrivée des secours

---

### Rappel important

⚠️ **Tout traumatisme crânien peut être associé à un traumatisme du rachis**

En cas de doute : toujours considérer qu'il y a une lésion du rachis et agir en conséquence"""
            }
        ]
    }
]

async def create_psc1_chapters():
    print("🚀 Création des chapitres PSC1 complets...")
    
    # Supprimer les anciens chapitres PSC
    deleted = await db.chapters.delete_many({"formation_type": "PSC"})
    print(f"🗑️  Supprimé {deleted.deleted_count} anciens chapitres PSC")
    
    # Créer les nouveaux chapitres
    for chapter in psc1_chapters:
        await db.chapters.insert_one(chapter)
        print(f"✅ Créé: {chapter['titre']} ({len(chapter['fiches'])} fiches)")
    
    # Vérifier
    count = await db.chapters.count_documents({"formation_type": "PSC"})
    print(f"\n🎉 Total chapitres PSC1 créés: {count}")
    
    # Lister
    chapters = await db.chapters.find({"formation_type": "PSC"}, {"_id": 0, "id": 1, "numero": 1, "titre": 1}).sort("numero", 1).to_list(100)
    for ch in chapters:
        print(f"   Ch{ch['numero']:02d} - {ch['titre']}")

if __name__ == "__main__":
    asyncio.run(create_psc1_chapters())
