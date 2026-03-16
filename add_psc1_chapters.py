#!/usr/bin/env python3
"""
Script pour ajouter les chapitres PSC1 à la base de données
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv
from pathlib import Path

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / 'backend' / '.env')

# MongoDB connection
mongo_url = os.environ['MONGO_URL']
client = AsyncIOMotorClient(mongo_url)
db = client[os.environ['DB_NAME']]

psc1_chapters = [
    {
        "id": "psc1-ch1",
        "numero": 1,
        "titre": "Obstruction des voies aériennes",
        "description": "Reconnaître et traiter un étouffement chez l'adulte, l'enfant et le nourrisson.",
        "icon": "Wind",
        "formation_type": "PSC",
        "image_url": "https://images.unsplash.com/photo-1622115297822-a3798fdbe1f6",
        "fiches": [
            {
                "id": "psc1-f1-1",
                "titre": "Reconnaître l'obstruction",
                "contenu": """**Définition:** Gêne ou empêchement brutal de l'air entre l'extérieur et les poumons.

**🔴 OBSTRUCTION COMPLÈTE (urgence vitale):**
- La victime ne peut plus parler, crier ou tousser
- Garde la bouche ouverte
- S'agite, devient bleue
- Ne peut émettre aucun son

**🟡 OBSTRUCTION PARTIELLE:**
- La victime peut encore parler et tousser
- Respire avec bruit
- Reste consciente

**Causes fréquentes:**
- Aliments (noix, cacahuètes, carottes)
- Petits objets chez l'enfant
- Survient souvent pendant un repas"""
            },
            {
                "id": "psc1-f1-2",
                "titre": "Gestes de secours",
                "contenu": """**SI OBSTRUCTION PARTIELLE:**
✓ Installer la victime dans la position où elle se sent le mieux
✓ L'encourager à tousser
✓ Appeler le 15 ou 112
✓ Surveiller attentivement

**SI OBSTRUCTION COMPLÈTE:**
1. **Claques dans le dos** (1 à 5 fois)
   - Se placer sur le côté, pencher la victime vers l'avant
   - Claques vigoureuses entre les omoplates

2. **Si inefficace: Compressions abdominales** (1 à 5 fois)
   - Se placer derrière la victime
   - Poing au-dessus du nombril
   - Tirer vers l'arrière et vers le haut

3. **Alterner** claques et compressions jusqu'à expulsion

**⚠️ Si la victime perd connaissance:**
- Appeler immédiatement le 15
- Débuter RCP (réanimation cardio-pulmonaire)"""
            }
        ]
    },
    {
        "id": "psc1-ch2",
        "numero": 2,
        "titre": "Hémorragies externes",
        "description": "Arrêter une hémorragie externe et éviter la détresse circulatoire.",
        "icon": "Droplet",
        "formation_type": "PSC",
        "image_url": "https://images.unsplash.com/photo-1609840534277-88833ef3ddeb",
        "fiches": [
            {
                "id": "psc1-f2-1",
                "titre": "Reconnaître une hémorragie",
                "contenu": """**Définition:** Perte de sang qui ne s'arrête pas spontanément et imbibe rapidement un mouchoir.

**Signes:**
- Saignement abondant et continu
- Le sang peut être rouge vif ou foncé
- Peut être masqué par un vêtement

**Risques:**
- Détresse circulatoire
- Arrêt cardiaque
- Infection pour le sauveteur (se protéger!)

**⚠️ NE PAS confondre avec:**
- Une écorchure qui s'arrête seule
- Un simple saignement de nez"""
            },
            {
                "id": "psc1-f2-2",
                "titre": "Arrêter le saignement",
                "contenu": """**CONDUITE À TENIR:**

1. **Compression directe** (méthode prioritaire)
   - Appuyer fortement sur la plaie
   - Utiliser un tissu propre si possible
   - Maintenir la compression jusqu'aux secours

2. **Allonger la victime** confortablement

3. **Alerter le 15 ou 112**

4. **Si compression inefficace:** GARROT
   - À 5-7 cm au-dessus de la plaie
   - Sur un membre uniquement
   - Serrer jusqu'à arrêt du saignement
   - ⚠️ Ne JAMAIS retirer sans avis médical

**PROTECTION DU SAUVETEUR:**
🧤 Porter des gants ou sac plastique
🚫 Ne pas toucher bouche/yeux/nez
🧼 Se laver les mains après

**CAS PARTICULIERS:**
- Saignement de nez: assis, tête penchée en avant, comprimer 10 min
- Vomissement de sang: alerter le 15 immédiatement"""
            }
        ]
    },
    {
        "id": "psc1-ch3",
        "numero": 3,
        "titre": "Perte de connaissance",
        "description": "Reconnaître une perte de connaissance et mettre la victime en position latérale de sécurité (PLS).",
        "icon": "User",
        "formation_type": "PSC",
        "image_url": "https://images.unsplash.com/photo-1564732005956-20420ebdab60",
        "fiches": [
            {
                "id": "psc1-f3-1",
                "titre": "Reconnaître la perte de connaissance",
                "contenu": """**Définition:** Personne qui ne répond pas et ne réagit à aucune sollicitation, mais qui RESPIRE.

**Comment vérifier:**

1. **Vérifier la réponse:**
   - Poser des questions simples
   - Secouer doucement les épaules
   - Prendre la main et donner un ordre

2. **Vérifier la respiration:**
   - Basculer la tête en arrière
   - Regarder, écouter, sentir pendant 10 secondes
   - Observer le soulèvement de la poitrine

**⚠️ Risques:**
- Obstruction des voies aériennes par la langue
- Étouffement par vomissements
- Évolution vers l'arrêt cardiaque

**Causes possibles:**
- Malaise
- Traumatisme crânien
- Intoxication
- Maladie"""
            },
            {
                "id": "psc1-f3-2",
                "titre": "Position Latérale de Sécurité (PLS)",
                "contenu": """**SI LA VICTIME RESPIRE:**

**🎯 Objectif:** Maintenir les voies aériennes ouvertes et permettre l'écoulement des liquides.

**RÉALISATION (adulte/enfant):**

1. **Préparation:**
   - Retirer les lunettes
   - Placer le bras côté sauveteur à angle droit
   - Saisir l'autre main et l'amener sur l'oreille
   - Relever la jambe opposée

2. **Retournement:**
   - Tirer sur la jambe pour faire pivoter la victime
   - Dégager délicatement la main

3. **Stabilisation:**
   - Ajuster la jambe à angle droit
   - Ouvrir la bouche

**APRÈS LA PLS:**
✓ Alerter le 15 ou 112
✓ Couvrir la victime
✓ Surveiller la respiration en continu

**⚠️ Si la respiration s'arrête:** Débuter immédiatement la RCP"""
            }
        ]
    },
    {
        "id": "psc1-ch4",
        "numero": 4,
        "titre": "Arrêt cardiaque",
        "description": "Reconnaître un arrêt cardiaque et pratiquer la réanimation cardio-pulmonaire (RCP) avec défibrillateur.",
        "icon": "Heart",
        "formation_type": "PSC",
        "image_url": "https://images.unsplash.com/photo-1622551546704-36926ae49878",
        "fiches": [
            {
                "id": "psc1-f4-1",
                "titre": "Reconnaître l'arrêt cardiaque",
                "contenu": """**Définition:** Le cœur ne fonctionne plus, n'assurant plus l'oxygénation du cerveau.

**Signes:**
- ❌ La victime ne répond pas
- ❌ Ne réagit à aucune stimulation
- ❌ Ne respire PAS ou respiration anormale (lente, bruyante, inefficace)

**⚠️ URGENCE ABSOLUE:**
Chaque minute compte ! Sans intervention, le cerveau subit des lésions irréversibles dès la 1ère minute.

**🔗 Chaîne de survie:**
1. Alerter (15 ou 112)
2. Masser (RCP)
3. Défibriller (DAE)
4. Secours médicalisés

**Causes fréquentes:**
- Infarctus du myocarde (adulte)
- Problème respiratoire (enfant)
- Noyade, électrocution, traumatisme"""
            },
            {
                "id": "psc1-f4-2",
                "titre": "Réanimation Cardio-Pulmonaire (RCP)",
                "contenu": """**CONDUITE À TENIR:**

1. **Faire alerter le 15 et réclamer un DAE**

2. **Débuter IMMÉDIATEMENT la RCP:**

**💪 COMPRESSIONS THORACIQUES**
- Au centre de la poitrine
- Bras tendus, verticalement
- Enfoncer de 5 cm
- Rythme: 100-120 compressions/minute
- 🎵 Tempo de "Stayin' Alive"

**💨 INSUFFLATIONS** (si vous savez faire)
- 2 insufflations après 30 compressions
- Basculer la tête, pincer le nez
- Souffler jusqu'à soulèvement de la poitrine

**Rythme: 30 compressions / 2 insufflations**

**⚡ DÈS L'ARRIVÉE DU DAE:**
- Mettre en marche
- Suivre les instructions vocales
- Appliquer les électrodes sur thorax nu
- Ne PAS toucher la victime pendant analyse
- Si choc indiqué: s'écarter et laisser faire
- Reprendre IMMÉDIATEMENT la RCP après le choc

**⚠️ Ne JAMAIS arrêter avant:**
- L'arrivée des secours
- La victime respire normalement
- Épuisement complet"""
            }
        ]
    },
    {
        "id": "psc1-ch5",
        "numero": 5,
        "titre": "Malaises",
        "description": "Reconnaître les signes d'un malaise et adopter la conduite appropriée.",
        "icon": "AlertCircle",
        "formation_type": "PSC",
        "image_url": "https://images.unsplash.com/photo-1659019479941-1fd644624339",
        "fiches": [
            {
                "id": "psc1-f5-1",
                "titre": "Reconnaître un malaise",
                "contenu": """**Définition:** Sensation pénible traduisant un trouble du fonctionnement de l'organisme.

**Signes variables:**
- Ne se sent pas bien
- Pâleur, sueurs
- Douleur thoracique
- Difficulté à respirer ou parler
- Faiblesse, vertiges
- Troubles de la parole
- Douleur abdominale

**🚨 SIGNES D'URGENCE ABSOLUE:**

**Accident cardiaque:**
- Douleur dans la poitrine

**AVC (Accident Vasculaire Cérébral):**
- Faiblesse ou paralysie d'un bras
- Déformation du visage
- Difficulté à parler
- Perte de vision
- Mal de tête sévère et brutal

**⏱️ Pour l'AVC, chaque minute compte!**"""
            },
            {
                "id": "psc1-f5-2",
                "titre": "Conduite à tenir",
                "contenu": """**ACTIONS IMMÉDIATES:**

1. **Mettre au repos**
   - Allonger confortablement
   - Ou assis si difficultés respiratoires
   - Position où la victime se sent le mieux

2. **Desserrer les vêtements**

3. **Questionner la victime:**
   - Âge
   - Que ressentez-vous?
   - Depuis combien de temps?
   - Antécédents médicaux
   - Traitements en cours

4. **Alerter le 15** et décrire les signes

5. **Rassurer et surveiller**

**SI SIGNES D'AVC OU DOULEUR THORACIQUE:**
🚨 Appeler immédiatement le 15

**Sur demande médicale:**
- Aider la victime à prendre son traitement
- Donner du sucre si malaise diabétique

**En cas d'aggravation:**
- Recontacter le 15
- Perte de connaissance → PLS
- Arrêt respiratoire → RCP

**Malaise par la chaleur:**
- Installer dans endroit frais
- Déshabiller/desserrer vêtements
- Rafraîchir (eau, ventilateur)
- Faire boire si consciente"""
            }
        ]
    },
    {
        "id": "psc1-ch6",
        "numero": 6,
        "titre": "Plaies",
        "description": "Différencier plaie simple et plaie grave, adopter la conduite appropriée.",
        "icon": "Bandage",
        "formation_type": "PSC",
        "image_url": "https://images.unsplash.com/photo-1624638760852-8ede1666ab07",
        "fiches": [
            {
                "id": "psc1-f6-1",
                "titre": "Types de plaies",
                "contenu": """**Définition:** Lésion de la peau avec atteinte des tissus en dessous.

**🟢 PLAIE SIMPLE:**
- Petite coupure superficielle
- Éraflure
- Saigne peu

**🔴 PLAIE GRAVE:**
- Hémorragie associée
- Mécanisme pénétrant (couteau, morsure, balle)
- Localisations à risque:
  * Thorax
  * Abdomen
  * Œil
  * Orifice naturel
- Aspect déchiqueté ou écrasé
- Objet enfoncé dans la plaie

**Risques:**
- Hémorragie
- Infection (tétanos)
- Atteinte d'organes vitaux"""
            },
            {
                "id": "psc1-f6-2",
                "titre": "Conduite à tenir",
                "contenu": """**FACE À UNE PLAIE GRAVE:**

⚠️ **NE JAMAIS retirer un objet enfoncé!**

1. **Si hémorragie:** Arrêter le saignement

2. **Installer la victime:**
   - Assise (plaie au thorax)
   - Allongée jambes fléchies (abdomen)
   - Allongée yeux fermés (œil)

3. **Alerter le 15 ou 112**

4. **Protéger et surveiller**

---

**FACE À UNE PLAIE SIMPLE:**

1. **Se laver les mains**

2. **Nettoyer la plaie:**
   - Eau courante (avec ou sans savon)
   - Du centre vers l'extérieur

3. **Désinfecter:**
   - Antiseptique

4. **Protéger:**
   - Pansement adhésif

5. **Conseiller de consulter si:**
   - Vaccination tétanos non à jour
   - Signes d'infection (rougeur, chaleur, gonflement, fièvre)

**💡 BON À SAVOIR:**
- Ne pas mettre de coton sur une plaie
- Ne pas souffler sur une plaie
- Changer le pansement régulièrement"""
            }
        ]
    },
    {
        "id": "psc1-ch7",
        "numero": 7,
        "titre": "Brûlures",
        "description": "Évaluer la gravité d'une brûlure et adopter la conduite appropriée.",
        "icon": "Flame",
        "formation_type": "PSC",
        "image_url": "https://images.unsplash.com/photo-1622115585848-1d5b6e8af4e4",
        "fiches": [
            {
                "id": "psc1-f7-1",
                "titre": "Types de brûlures",
                "contenu": """**Définition:** Lésion de la peau, voies aériennes ou digestives.

**🟢 BRÛLURE SIMPLE:**
- Rougeur
- Cloque de surface < la moitié de la paume de la main

**🔴 BRÛLURE GRAVE:**
- Cloque > la moitié de la paume de la main
- Destruction profonde (aspect blanchâtre ou noirâtre)
- Localisations à risque:
  * Visage, cou
  * Mains
  * Articulations
  * Près d'un orifice naturel
- Rougeur étendue chez l'enfant
- Origine chimique, électrique ou radiologique

**Causes:**
- Chaleur (flamme, liquide bouillant, objet chaud)
- Substances chimiques
- Électricité
- Rayonnements (soleil, laser)"""
            },
            {
                "id": "psc1-f7-2",
                "titre": "Conduite à tenir",
                "contenu": """**🌊 GESTE PRIORITAIRE: REFROIDIR**

**TOUJOURS refroidir IMMÉDIATEMENT:**
- Eau courante tempérée (15-25°C)
- Faible pression
- Pendant **AU MOINS 10 minutes** (idéalement 20 min)
- Retirer vêtements et bijoux (sauf si collés)

---

**BRÛLURE GRAVE:**

1. **Débuter le refroidissement**
2. **Faire alerter le 15**
3. **Poursuivre le refroidissement**
4. **Installer la victime:**
   - Allongée confortablement
   - Assise si gêne respiratoire
5. **Surveiller**
6. ⚠️ **Aucun produit sans avis médical**

---

**BRÛLURE SIMPLE:**

1. **Refroidir jusqu'à disparition de la douleur**
2. **Ne JAMAIS percer les cloques**
3. **Protéger par pansement stérile**
4. **Consulter un médecin si:**
   - Vaccination tétanos non à jour
   - Enfant ou nourrisson
   - Signes d'infection

---

**CAS PARTICULIERS:**

**Brûlure chimique:**
- Rincer abondamment à l'eau
- Retirer vêtements imbibés SOUS l'eau
- Conserver info sur le produit

**Brûlure électrique:**
- Couper le courant avant de toucher
- Alerter le 15 systématiquement

**💡 À RETENIR: Refroidir, refroidir, refroidir!**"""
            }
        ]
    },
    {
        "id": "psc1-ch8",
        "numero": 8,
        "titre": "Traumatismes",
        "description": "Reconnaître un traumatisme et éviter l'aggravation des lésions.",
        "icon": "Bone",
        "formation_type": "PSC",
        "image_url": "https://images.unsplash.com/photo-1759872138841-c342bd6410ae",
        "fiches": [
            {
                "id": "psc1-f8-1",
                "titre": "Reconnaître un traumatisme",
                "contenu": """**Définition:** Lésion des os (fractures), articulations (entorses, luxations) ou organes suite à un choc.

**Signes:**
- Douleur vive à la mobilisation
- Difficulté ou impossibilité de bouger
- Gonflement
- Déformation visible
- Ecchymose (bleu)

**Signes de gravité:**

**Après un choc à la tête:**
- Perte de connaissance
- Maux de tête intenses
- Vomissements
- Somnolence, confusion
- Saignement nez/oreilles

**Après un choc au thorax/abdomen:**
- Douleur intense
- Difficulté à respirer
- Vomissement de sang

**Traumatisme de la colonne:**
- Douleur au cou ou au dos
- Fourmillements
- Impossibilité de bouger un membre

**⚠️ ATTENTION:**
Un traumatisme peut cacher des lésions internes graves!"""
            },
            {
                "id": "psc1-f8-2",
                "titre": "Conduite à tenir",
                "contenu": """**RÈGLE D'OR: NE PAS MOBILISER LA VICTIME**

**SI LA VICTIME A PERDU CONNAISSANCE:**
→ Appliquer conduite "Perte de connaissance"

**SI LA VICTIME EST CONSCIENTE:**

1. **Conseiller de ne pas bouger**
   - Surtout la partie douloureuse

2. **Alerter le 15 ou 112**

3. **Protéger du froid, de la chaleur**

4. **Surveiller et parler régulièrement**

---

**CAS PARTICULIERS:**

**Douleur au cou (suspicion traumatisme cervical):**
- Maintenir la tête à deux mains
- De chaque côté, dans l'axe
- Ne pas bouger jusqu'aux secours
- Alerter le 15

**Fracture avec déformation:**
- NE PAS tenter de réaligner!
- Immobiliser dans la position trouvée
- Alerter le 15

**Choc à la tête:**
- Surveiller l'apparition de signes neurologiques
- Même si la victime semble aller bien
- Conseiller de consulter

**💡 EN CAS DE DOUTE sur la gravité:**
→ TOUJOURS alerter le 15

**⚠️ Ne jamais:**
- Mobiliser une victime de traumatisme
- Donner à boire ou à manger
- Retirer le casque d'un motard"""
            }
        ]
    }
]

# Quizzes pour chaque chapitre PSC1
psc1_quizzes = [
    {
        "id": "quiz-psc1-ch1",
        "chapter_id": "psc1-ch1",
        "titre": "Quiz - Obstruction des voies aériennes",
        "video_url": None,
        "questions": [
            {
                "id": "psc1-q1-1",
                "question": "Une victime s'étouffe, elle ne peut plus parler ni tousser mais elle reste consciente. Que faire en PREMIER?",
                "type": "qcm",
                "options": [
                    "Réaliser immédiatement des compressions abdominales",
                    "Donner 1 à 5 claques vigoureuses dans le dos",
                    "Appeler le 15 avant toute action",
                    "Donner à boire de l'eau"
                ],
                "correct_answer": 1,
                "explication": "Face à une obstruction complète, on commence TOUJOURS par donner 1 à 5 claques vigoureuses dans le dos entre les omoplates. Si inefficace, on passe aux compressions abdominales. L'alerte sera faite par un tiers ou après les premiers gestes."
            }
        ]
    },
    {
        "id": "quiz-psc1-ch2",
        "chapter_id": "psc1-ch2",
        "titre": "Quiz - Hémorragies externes",
        "video_url": None,
        "questions": [
            {
                "id": "psc1-q2-1",
                "question": "Une victime saigne abondamment de l'avant-bras. La compression directe est inefficace après plusieurs minutes. Que faire?",
                "type": "qcm",
                "options": [
                    "Continuer la compression directe jusqu'à l'arrivée des secours",
                    "Mettre en place un garrot entre le cœur et la plaie",
                    "Surélever le bras et attendre",
                    "Mettre de la glace sur la plaie"
                ],
                "correct_answer": 1,
                "explication": "Si la compression directe est inefficace ou impossible sur un membre, il faut mettre en place un garrot 5 à 7 cm au-dessus de la plaie (entre le cœur et la plaie). Le garrot ne doit jamais être retiré sans avis médical."
            }
        ]
    },
    {
        "id": "quiz-psc1-ch3",
        "chapter_id": "psc1-ch3",
        "titre": "Quiz - Perte de connaissance",
        "video_url": None,
        "questions": [
            {
                "id": "psc1-q3-1",
                "question": "Une personne est inconsciente mais respire normalement après un malaise. Quelle est la conduite à tenir?",
                "type": "qcm",
                "options": [
                    "La laisser allongée sur le dos et surveiller",
                    "La mettre en Position Latérale de Sécurité (PLS), alerter le 15 et surveiller la respiration",
                    "Lui donner à boire pour la réveiller",
                    "Lui donner des claques pour la réveiller"
                ],
                "correct_answer": 1,
                "explication": "Une victime inconsciente qui respire après un événement non traumatique doit être mise en PLS pour maintenir les voies aériennes libres et permettre l'écoulement des liquides. On alerte ensuite le 15 et on surveille en continu la respiration."
            }
        ]
    },
    {
        "id": "quiz-psc1-ch4",
        "chapter_id": "psc1-ch4",
        "titre": "Quiz - Arrêt cardiaque",
        "video_url": None,
        "questions": [
            {
                "id": "psc1-q4-1",
                "question": "Lors d'une RCP sur un adulte, quel est le rythme correct des compressions et insufflations?",
                "type": "qcm",
                "options": [
                    "15 compressions puis 2 insufflations",
                    "30 compressions puis 2 insufflations",
                    "20 compressions puis 1 insufflation",
                    "Uniquement des compressions sans insufflations"
                ],
                "correct_answer": 1,
                "explication": "Le rythme de RCP pour un adulte est de 30 compressions thoraciques suivies de 2 insufflations. Ce cycle doit être répété sans interruption jusqu'à l'arrivée des secours ou la reprise d'une respiration normale. La fréquence des compressions doit être de 100 à 120 par minute."
            }
        ]
    },
    {
        "id": "quiz-psc1-ch5",
        "chapter_id": "psc1-ch5",
        "titre": "Quiz - Malaises",
        "video_url": None,
        "questions": [
            {
                "id": "psc1-q5-1",
                "question": "Une personne présente brutalement une faiblesse d'un bras et une difficulté à parler. Que suspecter?",
                "type": "qcm",
                "options": [
                    "Un simple malaise vagal",
                    "Un Accident Vasculaire Cérébral (AVC) - alerter le 15 immédiatement",
                    "Une crise d'angoisse",
                    "Un problème digestif"
                ],
                "correct_answer": 1,
                "explication": "Ces signes (faiblesse/paralysie d'un bras, difficulté à parler) sont caractéristiques d'un AVC. C'est une urgence absolue où chaque minute compte. Il faut appeler immédiatement le 15. D'autres signes d'AVC: déformation du visage, perte de vision, mal de tête sévère."
            }
        ]
    },
    {
        "id": "quiz-psc1-ch6",
        "chapter_id": "psc1-ch6",
        "titre": "Quiz - Plaies",
        "video_url": None,
        "questions": [
            {
                "id": "psc1-q6-1",
                "question": "Une victime a un couteau planté dans le thorax. Que faire?",
                "type": "qcm",
                "options": [
                    "Retirer le couteau immédiatement pour limiter les dégâts",
                    "Ne JAMAIS retirer l'objet, installer la victime assise, alerter le 15",
                    "Retirer le couteau mais uniquement si la victime le demande",
                    "Pousser le couteau plus profondément pour arrêter le saignement"
                ],
                "correct_answer": 1,
                "explication": "Il ne faut JAMAIS retirer un objet enfoncé dans une plaie car il peut limiter le saignement. Pour une plaie au thorax, on installe la victime en position assise pour faciliter la respiration, et on alerte immédiatement le 15."
            }
        ]
    },
    {
        "id": "quiz-psc1-ch7",
        "chapter_id": "psc1-ch7",
        "titre": "Quiz - Brûlures",
        "video_url": None,
        "questions": [
            {
                "id": "psc1-q7-1",
                "question": "Quelle est la PREMIÈRE action à réaliser face à une brûlure?",
                "type": "qcm",
                "options": [
                    "Appliquer une crème ou du beurre",
                    "Percer les cloques pour éviter l'infection",
                    "Refroidir immédiatement à l'eau courante pendant au moins 10 minutes",
                    "Mettre un pansement sec"
                ],
                "correct_answer": 2,
                "explication": "Le geste prioritaire face à toute brûlure est de REFROIDIR immédiatement avec de l'eau courante tempérée (15-25°C) pendant au moins 10 minutes, idéalement 20 minutes. Cela limite l'extension de la brûlure et soulage la douleur. Ne jamais appliquer de corps gras ni percer les cloques."
            }
        ]
    },
    {
        "id": "quiz-psc1-ch8",
        "chapter_id": "psc1-ch8",
        "titre": "Quiz - Traumatismes",
        "video_url": None,
        "questions": [
            {
                "id": "psc1-q8-1",
                "question": "Une victime consciente se plaint d'une douleur au cou après une chute. Que faire?",
                "type": "qcm",
                "options": [
                    "L'aider à se relever doucement",
                    "Maintenir sa tête à deux mains dans l'axe, lui demander de ne pas bouger, alerter le 15",
                    "La mettre en Position Latérale de Sécurité",
                    "Lui donner un médicament contre la douleur"
                ],
                "correct_answer": 1,
                "explication": "Une douleur au cou après un traumatisme fait suspecter une atteinte de la colonne cervicale. Il faut maintenir la tête à deux mains dans l'axe pour stabiliser le rachis, demander à la victime de ne pas bouger, et alerter immédiatement le 15. Toute mobilisation pourrait aggraver les lésions."
            }
        ]
    }
]

async def add_psc1_data():
    """Ajouter les chapitres et quiz PSC1 à la base de données"""
    try:
        print("🔄 Ajout des chapitres PSC1...")
        
        # Ajouter les chapitres
        for chapter in psc1_chapters:
            # Vérifier si le chapitre existe déjà
            existing = await db.chapters.find_one({"id": chapter["id"]})
            if existing:
                print(f"⚠️  Chapitre {chapter['titre']} existe déjà, mise à jour...")
                await db.chapters.replace_one({"id": chapter["id"]}, chapter)
            else:
                print(f"✅ Ajout du chapitre: {chapter['titre']}")
                await db.chapters.insert_one(chapter)
        
        print("\n🔄 Ajout des quiz PSC1...")
        
        # Ajouter les quiz
        for quiz in psc1_quizzes:
            # Vérifier si le quiz existe déjà
            existing = await db.quizzes.find_one({"id": quiz["id"]})
            if existing:
                print(f"⚠️  Quiz {quiz['titre']} existe déjà, mise à jour...")
                await db.quizzes.replace_one({"id": quiz["id"]}, quiz)
            else:
                print(f"✅ Ajout du quiz: {quiz['titre']}")
                await db.quizzes.insert_one(quiz)
        
        print("\n🎉 Tous les chapitres et quiz PSC1 ont été ajoutés avec succès!")
        
    except Exception as e:
        print(f"❌ Erreur lors de l'ajout des données: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(add_psc1_data())
