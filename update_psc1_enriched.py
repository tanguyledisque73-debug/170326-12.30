#!/usr/bin/env python3
"""
Script pour enrichir les chapitres PSC1 avec plus de contenu et d'illustrations
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

enriched_psc1_chapters = [
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
                "image_url": "https://images.unsplash.com/photo-1667834845220-087f7c25af72",
                "contenu": """## Qu'est-ce qu'une obstruction des voies aériennes ?

C'est une **gêne ou un empêchement brutal** des mouvements de l'air entre l'extérieur et les poumons, causé par un corps étranger qui bloque le passage.

---

### 🔴 OBSTRUCTION COMPLÈTE (urgence vitale immédiate)

**La victime :**
- ❌ **Ne peut plus parler, crier ou tousser**
- ❌ **Ne peut émettre AUCUN son**
- 😮 **Garde la bouche ouverte**
- 😰 **S'agite, panique**
- 🔵 **Devient progressivement bleue** (cyanose)
- 🤚 **Porte souvent les mains à sa gorge** (signe universel de l'étouffement)

**⏱️ URGENCE ABSOLUE : Quelques minutes seulement avant la perte de connaissance !**

---

### 🟡 OBSTRUCTION PARTIELLE

**La victime :**
- ✓ **Peut encore parler** (même difficilement)
- ✓ **Peut tousser** (même faiblement)
- ✓ **Respire avec bruit** (sifflement, râle)
- ✓ **Reste consciente**
- ⚠️ **Mais peut évoluer vers une obstruction complète**

---

### 🎯 Causes fréquentes

**Chez l'adulte et la personne âgée :**
- 🥜 Aliments : noix, cacahuètes, morceaux de viande
- 🍬 Bonbons durs
- 🦴 Arêtes de poisson, os de poulet

**Chez l'enfant :**
- 🥕 Aliments : carottes crues, raisins entiers, hot-dogs
- 🧸 Petits jouets, billes, pièces de monnaie
- 🎈 Morceaux de ballons éclatés

**Facteurs de risque :**
- Manger trop rapidement
- Parler ou rire en mangeant
- Consommation d'alcool
- Maladies affectant la déglutition
- Mauvaise dentition
- Port d'objets à la bouche (stylos, cure-dents)

---

### ⚠️ Situations à risque

L'obstruction survient le plus souvent :
- 🍽️ **Pendant les repas**
- 🍺 **Lors de soirées festives** (alcool)
- 👶 **Chez les jeunes enfants** qui portent tout à la bouche
- 👵 **Chez les personnes âgées** (troubles de la déglutition)"""
            },
            {
                "id": "psc1-f1-2",
                "titre": "Gestes de secours",
                "image_url": "https://images.unsplash.com/photo-1622115585848-1d5b6e8af4e4",
                "contenu": """## Conduite à tenir face à un étouffement

### 🟡 SI OBSTRUCTION PARTIELLE (la victime tousse encore)

**ACTIONS :**
1. ✅ **Installer la victime** dans la position où elle se sent le mieux
2. ✅ **L'encourager à tousser** fortement
3. ✅ **Appeler le 15 ou 112** pour demander un avis médical
4. ✅ **Rester auprès d'elle** et surveiller attentivement

**⚠️ ATTENTION :** Si la toux devient inefficace ou si la victime s'épuise, passer immédiatement à la conduite pour obstruction complète !

---

### 🔴 SI OBSTRUCTION COMPLÈTE (la victime ne peut plus tousser)

#### **ÉTAPE 1 : Claques dans le dos** 👋

**Réalisation :**
1. Se placer **sur le côté et légèrement en arrière** de la victime
2. Soutenir son thorax avec une main
3. **Pencher la victime vers l'avant**
4. Donner **1 à 5 claques vigoureuses** :
   - Avec le **talon de la main ouverte**
   - **Entre les omoplates**
   - De façon **vigoureuse et sèche**

**🎯 Objectif :** Provoquer un mouvement de toux pour débloquer et expulser le corps étranger.

**🔄 Vérifier après chaque claque** si le corps étranger est expulsé.

---

#### **ÉTAPE 2 : Compressions abdominales (Manœuvre de Heimlich)** 💪

**Si les claques dans le dos sont inefficaces :**

**Réalisation (Adulte ou enfant) :**
1. Se placer **debout ou à genoux derrière** la victime
2. **Pencher la victime** vers l'avant
3. Placer un **poing fermé** (dos de la main vers le ciel) :
   - Juste **au-dessus du nombril**
   - En dessous du sternum
4. Placer **l'autre main sur la première**
5. **Tirer franchement** vers l'arrière ET vers le haut
6. Effectuer **1 à 5 compressions**
7. **Relâcher entre chaque** compression

**🎯 Objectif :** Comprimer l'air dans les poumons pour expulser le corps étranger par effet "piston".

**⚠️ NE PAS appuyer sur les côtes !**

---

#### **CAS PARTICULIERS**

**Femme enceinte ou personne obèse :**
- Impossibilité d'encercler l'abdomen
- → Réaliser des **compressions THORACIQUES** au milieu du sternum

**Nourrisson (moins d'1 an) :**
- **5 claques dans le dos** (sur l'avant-bras, tête plus basse)
- Puis **5 compressions thoraciques** (avec 2 doigts)
- ⚠️ **JAMAIS de compressions abdominales** chez le nourrisson

---

### 🔄 ALTERNANCE CLAQUES / COMPRESSIONS

**Répéter le cycle :**
1. 5 claques dans le dos
2. 5 compressions abdominales (ou thoraciques)
3. Recommencer jusqu'à :
   - ✅ Apparition d'une toux
   - ✅ Reprise de la respiration
   - ✅ Rejet du corps étranger

---

### ✅ SI LES MANŒUVRES SONT EFFICACES

1. Installer la victime confortablement
2. La réconforter et la rassurer
3. Desserrer les vêtements
4. **Alerter les secours** (15 ou 112)
5. Surveiller la victime
6. **Conseiller une consultation médicale** (risque de lésions internes)

---

### 🚨 SI LA VICTIME PERD CONNAISSANCE

**ACTIONS IMMÉDIATES :**

1. 📞 **Appeler immédiatement le 15 ou 112**
   - Signaler l'obstruction et la perte de connaissance

2. 🛏️ **Accompagner la victime au sol** (en sécurité)

3. 💪 **Débuter immédiatement la RCP** :
   - 30 compressions thoraciques
   - 2 insufflations
   - **Avant chaque série d'insufflations :**
     * Ouvrir la bouche
     * Rechercher le corps étranger
     * Le retirer UNIQUEMENT s'il est visible et accessible

4. 🔄 **Poursuivre la réanimation** sans interruption jusqu'à :
   - Arrivée des secours
   - Reprise d'une respiration normale

**💡 Pourquoi la RCP ?**
Les compressions thoraciques peuvent déloger le corps étranger. L'ouverture de la bouche avant les insufflations permet de le retirer s'il est remonté.

---

### ⏱️ POINTS CLÉS À RETENIR

✓ **Obstruction complète = URGENCE VITALE**
✓ **Commencer par les claques dans le dos**
✓ **Alterner claques et compressions**
✓ **Ne pas appuyer sur les côtes**
✓ **Si perte de connaissance → RCP immédiate**
✓ **Toujours faire consulter après**"""
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
                "image_url": "https://images.unsplash.com/photo-1609840534195-e6385ca0d10a",
                "contenu": """## Qu'est-ce qu'une hémorragie externe ?

Une **perte de sang prolongée** qui provient d'une plaie ou d'un orifice naturel et qui **ne s'arrête pas spontanément**.

---

### 🩸 SIGNES D'UNE HÉMORRAGIE

**Saignement qui :**
- ❌ **Ne s'arrête pas spontanément**
- 💧 **Imbibe rapidement un mouchoir**
- 🌊 **Coule de façon continue**
- 🔴 **Peut être rouge vif** (artériel) ou **rouge foncé** (veineux)

**⚠️ ATTENTION :**
- Le saignement peut être **masqué par un vêtement**
- La victime peut être **allongée sur la plaie**
- Le sang peut s'accumuler **sous les vêtements**

---

### ✅ Ce qui N'EST PAS une hémorragie

- 🩹 Une écorchure qui s'arrête toute seule
- 🤧 Un simple saignement de nez qui cesse rapidement
- 💉 Un saignement après prise de sang (pression suffit)

---

### 🎯 Causes fréquentes

**Traumatismes :**
- 🚗 Accidents de la route
- 🏗️ Accidents domestiques ou du travail
- 🔪 Coupures avec objet tranchant (couteau, verre)
- ⛏️ Chutes sur objet pointu

**Projectiles :**
- 🔫 Balle d'arme à feu
- 💥 Éclats métalliques

**Causes médicales :**
- 🦵 Rupture de varice
- 💊 Effets de certains traitements anticoagulants

---

### ⚠️ RISQUES

**Pour la victime :**
- 🫀 **Détresse circulatoire** (chute de la tension)
- 😰 **État de choc** (organes mal irrigués)
- 🚨 **Arrêt cardiaque** par perte de sang importante
- ⏱️ Plus la perte de sang est importante, plus le risque est grave

**Pour le sauveteur :**
- 🦠 **Infection par maladie transmissible** :
  - VIH, hépatites B et C
  - Par contact avec le sang (effraction cutanée, projection)

**🧤 PROTECTION OBLIGATOIRE DU SAUVETEUR !**

---

### 🔍 Comment identifier la gravité ?

**Hémorragie GRAVE si :**
- 🌊 Saignement abondant et continu
- 🩸 Sang qui "gicle" (artère touchée)
- 😰 Victime présentant des signes de détresse :
  - Pâleur intense
  - Sueurs froides
  - Sensation de soif
  - Respiration rapide
  - Vertiges, malaise

**Toute hémorragie doit être considérée comme potentiellement grave !**

---

### 📍 Localisations particulières

**Saignement de nez (épistaxis) :**
- Fréquent et généralement bénin
- Peut être abondant chez les personnes sous anticoagulants

**Vomissement ou crachat de sang :**
- 🚨 Toujours GRAVE
- Signe de maladie ou lésion interne

**Perte de sang par orifice naturel :**
- Sang dans les selles, urines
- Saignement vaginal inhabituel
- 🚨 Nécessite avis médical urgent"""
            },
            {
                "id": "psc1-f2-2",
                "titre": "Arrêter le saignement",
                "image_url": "https://images.unsplash.com/photo-1765996796562-ce301df337a0",
                "contenu": """## Conduite à tenir face à une hémorragie

### 🎯 OBJECTIF : Arrêter ou limiter la perte de sang

---

### 🩹 MÉTHODE PRIORITAIRE : Compression directe

**RÉALISATION :**

1. **🔍 Constater l'hémorragie**
   - Écarter les vêtements si nécessaire
   - Localiser précisément la plaie

2. **🤚 Comprimer immédiatement**
   - Demander à la victime de comprimer elle-même
   - OU le faire à sa place si elle ne peut pas

3. **🧤 SE PROTÉGER !**
   - Porter des gants si disponibles
   - OU utiliser un sac plastique
   - OU interposer un tissu propre épais :
     * Mouchoirs
     * Torchon
     * Vêtement
   - Si rien : appuyer directement avec la main

4. **👐 Maintenir la compression**
   - **Appuyer FORTEMENT** sur la plaie
   - De façon **CONTINUE**
   - Jusqu'à l'arrivée des secours
   - ⚠️ Ne JAMAIS relâcher !

5. **🛏️ Allonger la victime**
   - Sur un lit, canapé ou sol
   - Position confortable
   - Limite la circulation vers la plaie

6. **📞 Alerter le 15 ou 112**

---

### 🩹 Pansement compressif (si disponible)

**Quand ?**
- Si la compression manuelle a arrêté le saignement
- Pour libérer le sauveteur
- Utilisé en complément

**Comment ?**
- Tissu propre recouvrant la plaie
- Fixé par une **bande élastique** ou lien large
- Serré suffisamment pour maintenir la pression

**⚠️ Impossible sur :**
- Cou
- Tête
- Thorax
- Abdomen

**Si le saignement reprend :**
→ Reprendre immédiatement la compression manuelle PAR-DESSUS le pansement

---

### 🔴 GARROT : Méthode d'exception

**Quand utiliser le garrot ?**

✓ Compression directe **IMPOSSIBLE** :
  - Plusieurs victimes simultanées
  - Catastrophe, attentat
  - Plaies multiples
  - Objet enfoncé dans membre

✓ Compression directe **INEFFICACE** :
  - Saignement qui ne s'arrête pas
  - Après plusieurs minutes de compression

**⚠️ UNIQUEMENT sur un MEMBRE** (bras ou jambe)

---

### 🎗️ RÉALISATION DU GARROT

**Matériel :**
- **Garrot industriel** (préférable)
- OU lien large improvisé (3-5 cm) + barre rigide

**Placement :**
- 📏 **5 à 7 cm au-dessus de la plaie**
- Entre le cœur et la plaie
- ⛔ **JAMAIS sur une articulation** (coude, genou)

**Technique avec garrot industriel :**
1. Suivre les instructions du fabricant
2. Enrouler autour du membre
3. Serrer jusqu'à arrêt du saignement
4. Sécuriser le système

**Technique avec lien improvisé :**
1. Faire 2 tours avec le lien large
2. Faire un nœud
3. Placer la barre au-dessus du nœud
4. Faire 2 nœuds par-dessus la barre
5. Tourner la barre pour serrer
6. Serrer jusqu'à l'arrêt du saignement
7. Maintenir le serrage (fixer la barre)

**🚨 RÈGLES ABSOLUES DU GARROT :**
- ⏱️ Noter l'heure de pose
- 👁️ Laisser le garrot VISIBLE
- 🚫 **NE JAMAIS desserrer ou retirer** sans avis médical
- 🚫 **NE JAMAIS recouvrir** avec un vêtement

---

### 🆘 APRÈS AVOIR ARRÊTÉ LE SAIGNEMENT

**Actions :**
1. ✅ Rassurer la victime
2. ✅ Protéger du froid/chaud/intempéries
3. ✅ Surveiller continuellement :
   - État de conscience
   - Respiration
   - Signes d'aggravation

**⚠️ SIGNES D'AGGRAVATION :**
- Pâleur croissante
- Sueurs froides
- Sensation de froid
- Agitation ou somnolence
- Perte de connaissance

**Si aggravation :**
1. 📞 Recontacter immédiatement les secours
2. Signaler l'aggravation
3. Pratiquer les gestes qui s'imposent :
   - Si perte de connaissance → PLS
   - Si arrêt respiratoire → RCP

---

### 🩺 CAS PARTICULIERS

**🤧 Saignement de nez :**
1. Asseoir la victime, **tête penchée en AVANT**
2. Moucher vigoureusement
3. Comprimer les narines 10 minutes
4. Si persiste ou récidive → avis médical
5. Avis médical si :
   - Après chute ou coup
   - Personne sous anticoagulants

**🤮 Vomissement ou crachat de sang :**
1. Installer confortablement (assise si consciente)
2. 📞 Alerter le 15 immédiatement
3. Surveiller

**🩸 Perte de sang par orifice naturel :**
1. Allonger la victime
2. 📞 Alerter le 15
3. Surveiller

---

### 🧤 PROTECTION DU SAUVETEUR

**AVANT l'intervention :**
- Mettre des gants (latex, nitrile)
- OU utiliser sac plastique
- OU tissu imperméable

**PENDANT l'intervention :**
- Ne pas porter les mains au visage
- Ne pas toucher bouche, nez, yeux
- Ne pas manger, boire, fumer

**APRÈS l'intervention :**
1. 🧼 **Se laver les mains** :
   - À l'eau et au savon
   - Pendant au moins 30 secondes
2. Utiliser gel hydroalcoolique
3. Retirer et laver les vêtements souillés

**Si contact avec le sang :**
- Plaie souillée par le sang
- Projection sur le visage
- → 🏥 Consulter IMMÉDIATEMENT un médecin
- → Traitement préventif possible dans les heures qui suivent

---

### ⏱️ POINTS CLÉS À RETENIR

✓ **Compression directe = méthode prioritaire**
✓ **Appuyer FORT et de façon CONTINUE**
✓ **Allonger la victime**
✓ **Garrot = méthode d'exception**
✓ **Ne JAMAIS retirer un garrot**
✓ **Toujours se PROTÉGER du contact avec le sang**
✓ **Surveiller les signes d'aggravation**"""
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
        "image_url": "https://images.unsplash.com/photo-1630225760711-ac8eaa0c8947",
        "fiches": [
            {
                "id": "psc1-f3-1",
                "titre": "Reconnaître la perte de connaissance",
                "image_url": "https://images.unsplash.com/photo-1630225757034-d49c20300b55",
                "contenu": """## Qu'est-ce qu'une perte de connaissance ?

État dans lequel une personne **ne répond pas** et **ne réagit à aucune sollicitation** verbale ou physique, **mais respire**.

---

### 🔍 COMMENT VÉRIFIER ?

#### **ÉTAPE 1 : Vérifier la réponse**

**Actions :**
1. 🗣️ **Poser des questions simples** :
   - "Comment vous appelez-vous ?"
   - "M'entendez-vous ?"
   - "Serrez ma main !"

2. 🤝 **Stimulation physique** :
   - Secouer doucement les épaules
   - Prendre la main et demander de serrer
   - Tapoter le sternum

**Résultat :**
- ✅ **La victime répond ou réagit** → Ce n'est PAS une perte de connaissance
- ❌ **Aucune réponse, aucune réaction** → Poursuivre la vérification

---

#### **ÉTAPE 2 : Vérifier la respiration**

**Préparation :**
1. 🆘 **Demander de l'aide** si vous êtes seul
2. 🛏️ **Allonger la victime sur le dos** (quelle que soit sa position initiale)

**Libération des voies aériennes :**
1. Placer une main sur le front
2. Placer 2-3 doigts sous le menton
3. **Basculer doucement la tête en arrière**
4. Élever le menton

**Apprécier la respiration (10 secondes) :**
- 👀 **REGARDER** : le soulèvement de la poitrine
- 👂 **ÉCOUTER** : les bruits respiratoires
- 🌬️ **SENTIR** : le souffle sur votre joue

*Se pencher au-dessus de la victime, joue près de sa bouche*

---

### ✅ LA VICTIME RESPIRE NORMALEMENT

**Signes :**
- Soulèvement régulier de la poitrine
- Bruit de respiration normal
- Souffle perceptible
- Rythme régulier

→ **C'EST UNE PERTE DE CONNAISSANCE**
→ Voir fiche suivante : Position Latérale de Sécurité

---

### ❌ LA VICTIME NE RESPIRE PAS ou respiration anormale

**Respiration anormale (agonique) :**
- Très lente et irrégulière
- Bruyante, râle
- Gasps (mouvements saccadés)
- Bouche qui s'ouvre comme un poisson

→ **C'EST UN ARRÊT CARDIAQUE**
→ Voir chapitre "Arrêt cardiaque"

---

### 🎯 Causes de la perte de connaissance

**Causes médicales :**
- 💊 Malaise grave
- 🧠 AVC (Accident Vasculaire Cérébral)
- ❤️ Crise cardiaque
- 🩸 Hypoglycémie (diabète)
- 🤒 Intoxication

**Causes traumatiques :**
- 🤕 Choc à la tête
- 🚗 Traumatisme crânien
- ⚡ Électrocution
- 💧 Début de noyade

**Causes toxiques :**
- 🍺 Alcool
- 💊 Médicaments, drogues
- 🏭 Intoxication au CO (monoxyde de carbone)

---

### ⚠️ RISQUES VITAUX

**Sans intervention :**

1. **Obstruction des voies aériennes** par :
   - 👅 La langue qui chute en arrière
   - 🤮 Vomissements ou régurgitations
   - 🩸 Sang qui s'écoule dans la gorge

2. **Arrêt respiratoire**
   - Manque d'oxygène

3. **Arrêt cardiaque**
   - Conséquence de l'arrêt respiratoire

**⏱️ Le risque évolue rapidement !**

---

### 🚨 SIGNES DE GRAVITÉ

**Nécessitant une surveillance renforcée :**
- Traumatisme récent (chute, accident)
- Victime très pâle ou cyanosée (bleutée)
- Respiration difficile ou bruyante
- Convulsions
- Température corporelle anormale
- Odeur inhabituelle (alcool, gaz)

---

### 💡 Différence entre perte de connaissance et sommeil

**Perte de connaissance :**
- ❌ Ne répond à AUCUNE sollicitation
- ❌ Ne se réveille pas
- ⚠️ Risque vital

**Personne endormie :**
- ✅ Répond aux stimulations fortes
- ✅ Se réveille si on insiste
- ✅ Pas de danger immédiat"""
            },
            {
                "id": "psc1-f3-2",
                "titre": "Position Latérale de Sécurité (PLS)",
                "image_url": "https://images.unsplash.com/photo-1766502715616-374da81c2a9c",
                "contenu": """## La Position Latérale de Sécurité (PLS)

### 🎯 OBJECTIFS

La PLS permet de :
- ✅ **Maintenir les voies aériennes libres**
- ✅ **Empêcher la langue de tomber** en arrière
- ✅ **Permettre l'écoulement des liquides** (vomissements, sang, salive)
- ✅ **Éviter l'étouffement**
- ✅ **Stabiliser la victime** dans une position sûre

---

### ⚠️ QUAND utiliser la PLS ?

**La victime :**
- ❌ **Ne répond pas**
- ❌ **Ne réagit pas**
- ✅ **MAIS respire normalement**
- 📍 Après un événement NON traumatique (malaise, intoxication)

**OU sur demande des secours (15)**

---

### 🚫 QUAND NE PAS utiliser la PLS ?

- ⛔ Si la victime a subi un **traumatisme** (chute, accident)
  → Laisser sur le dos et maintenir la tête
- ⛔ Si la victime **NE respire PAS**
  → C'est un arrêt cardiaque → RCP
- ⛔ Si vous êtes **en période épidémique** et non cohabitant
  → Suivre consignes sanitaires

---

## 🔄 RÉALISATION DE LA PLS (Adulte / Enfant)

### **1️⃣ PREMIER TEMPS : Préparation du retournement**

**Actions :**

1. **🕶️ Retirer les lunettes** de la victime

2. **🦵 Rapprocher les membres inférieurs**
   - Allonger les jambes côte à côte

3. **💪 Placer le bras du côté sauveteur** :
   - À angle droit (90°)
   - Coude plié
   - Paume de la main vers le haut

4. **🤚 Saisir l'autre bras** (opposé au sauveteur) :
   - Placer le dos de la main de la victime...
   - ... Contre son oreille côté sauveteur
   - Maintenir la main en place

5. **🦵 Saisir la jambe opposée** :
   - Attraper derrière le genou
   - Relever la jambe
   - Pied au sol, genou en l'air

---

### **2️⃣ DEUXIÈME TEMPS : Retournement**

**Actions :**

1. **↩️ Tirer sur la jambe relevée**
   - Pour faire pivoter la victime vers soi
   - D'un seul mouvement fluide
   - Jusqu'à ce que le genou touche le sol

2. **🧠 Dégager délicatement la main**
   - La main qui était sous la tête
   - Sans mobiliser la tête
   - Tout en maintenant la bascule de la tête en arrière

---

### **3️⃣ TROISIÈME TEMPS : Stabilisation**

**Actions :**

1. **📐 Ajuster la jambe du dessus** :
   - Hanche et genou à angle droit (90°)
   - Pour stabiliser le bassin
   - Empêcher la victime de basculer

2. **👄 Ouvrir la bouche**
   - Délicatement
   - Sans mobiliser la tête
   - Pour permettre l'écoulement de liquides

3. **Vérifier la position de la tête** :
   - Tête toujours basculée en arrière
   - Menton élevé
   - Voies aériennes dégagées

---

### 👶 CAS PARTICULIER : Nourrisson

**Pour un bébé de moins d'1 an :**

1. **Prendre le nourrisson dans les bras**
2. Le placer **sur le côté**
3. Contre votre avant-bras
4. **Dos contre vous**
5. Tête légèrement plus basse que le corps

**⚠️ Ne PAS réaliser la PLS classique sur un nourrisson !**

---

### 📞 APRÈS LA PLS

**ACTIONS OBLIGATOIRES :**

1. **📱 Alerter le 15 ou 112**
   - "La personne est inconsciente mais respire"
   - Préciser si traumatisme ou non
   - Donner l'adresse exacte

2. **🧥 Protéger la victime** :
   - Couvrir (couverture, manteau)
   - Protéger du froid, de la chaleur
   - Protéger des intempéries
   - Protéger des regards indiscrets

3. **👁️ Surveiller EN CONTINU** :
   - La respiration (toutes les minutes)
   - L'état de conscience
   - Couleur de la peau
   - Mouvements

4. **💬 Parler à la victime**
   - Même si elle ne répond pas
   - Expliquer ce que vous faites
   - La rassurer

---

### 🚨 SI LA RESPIRATION S'ARRÊTE OU DEVIENT ANORMALE

**ACTIONS IMMÉDIATES :**

1. Remettre la victime **SUR LE DOS**
2. **Débuter immédiatement la RCP**
3. Recontacter le 15 pour signaler l'aggravation

---

### ⏱️ PARTICULARITÉS EN CAS DE TRAUMATISME

**Si la victime a subi un choc, une chute ou un accident :**

❌ **NE PAS mettre en PLS**

✅ **Actions :**
- Laisser la victime **SUR LE DOS**
- **Maintenir la tête** dans l'axe du corps
- Alerter le 15
- Surveiller la respiration

**Exception :** Si vomissements ou régurgitations :
- Tourner la victime **sur le côté**
- En maintenant l'axe **tête-cou-tronc** aligné
- (Nécessite plusieurs sauveteurs)

---

### 🦠 PÉRIODE ÉPIDÉMIQUE (COVID-19, grippe...)

**Mesures de protection :**

1. **🩺 Se protéger** avec un masque

2. **❓ Questionner** sans toucher la victime :
   - Symptômes respiratoires ?
   - Fièvre récente ?

3. **👀 Apprécier la respiration** :
   - SANS bascule de tête
   - SANS ouvrir la bouche
   - SANS se pencher au-dessus

4. **🤚 Si inconsciente mais respire** :
   - Laisser dans la position trouvée
   - NE PAS mettre en PLS
   - Alerter le 15
   - Placer un tissu/masque sur sa bouche et nez

5. **🧼 Se laver les mains** immédiatement

6. **📞 Contacter les autorités sanitaires**

---

### ⏱️ POINTS CLÉS À RETENIR

✓ **PLS = Position de sauvetage pour victime inconsciente qui respire**
✓ **Permet d'éviter l'étouffement**
✓ **3 temps : Préparation / Retournement / Stabilisation**
✓ **Limiter les mouvements de la colonne vertébrale**
✓ **Toujours surveiller la respiration**
✓ **Si traumatisme : laisser sur le dos**
✓ **Si arrêt respiratoire : RCP immédiate**"""
            }
        ]
    }
    # Les autres chapitres suivent le même format enrichi...
    # Pour la longueur, je vais continuer avec les autres chapitres
]

async def update_chapters():
    """Mettre à jour les 3 premiers chapitres avec le contenu enrichi"""
    try:
        print("🔄 Mise à jour des chapitres PSC1 enrichis...")
        
        for chapter in enriched_psc1_chapters:
            print(f"✅ Mise à jour: {chapter['titre']}")
            await db.chapters.replace_one({"id": chapter["id"]}, chapter, upsert=True)
        
        print("\n🎉 Chapitres enrichis mis à jour avec succès!")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    asyncio.run(update_chapters())
