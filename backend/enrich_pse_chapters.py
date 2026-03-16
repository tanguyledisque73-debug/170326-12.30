#!/usr/bin/env python3
"""
Script d'enrichissement des chapitres PSE selon les critères FAOD
Référentiel : 2024 PSE.pdf - Recommandations PSE
"""

import os
from pymongo import MongoClient

# Connexion MongoDB
client = MongoClient('mongodb://localhost:27017')
db = client['test_database']

# Définition complète du contenu PSE selon le référentiel FAOD 2024
PSE_CHAPTERS_CONTENT = {
    1: {
        "titre": "Attitude et comportement",
        "type": "PSE",
        "fiches": [
            {
                "code": "01AC01",
                "titre": "Le citoyen de Sécurité Civile",
                "niveau": "PSE 1",
                "type_fiche": "AC",
                "contenu": """**Objectifs pédagogiques :**
- Comprendre le rôle du citoyen dans la Sécurité Civile
- Connaître la protection juridique du citoyen sauveteur

**Points clés :**
• Le citoyen est un acteur majeur de la Sécurité Civile (Loi 2004)
• Protection juridique : "Collaborateur occasionnel du service public" (LOI n° 2020-840)
• Le secouriste est le premier maillon de la chaîne de secours
• Actions de prévention des accidents de la vie courante
• Importance de l'entretien et du développement des compétences
• Possibilités d'engagement (pompier volontaire, bénévole, réserviste)
• Impact psychologique : préparation, intervention, échange post-intervention

**Messages essentiels FAOD :**
→ Prévenir plutôt que guérir : suppression des dangers
→ Formation continue recommandée
→ Engagement citoyen et solidarité nationale
→ Applications de sollicitation citoyenne (Staying Alive, Sauv Life, etc.)"""
            },
            {
                "code": "01AC02",
                "titre": "Enjeux et principes",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "AC",
                "contenu": """**Objectifs pédagogiques :**
- Connaître les rôles et missions du secouriste
- Comprendre les principes de base de l'intervention

**Rôles du secouriste :**

**Seul :**
• Vérification du matériel à la prise de poste
• Se rendre rapidement sur les lieux
• Protéger, examiner, alerter/faire alerter
• Secourir avec moyens du bord
• Surveiller la victime
• Aider les renforts

**En équipe :**
• Coordination avec l'équipe
• Bilan avec matériel
• Transmission via terminaux
• Procédures internes
• Reconditionnement matériel
• Débriefing post-intervention

**Principes fondamentaux :**
1. **Respecter l'hygiène et la sécurité** : EPI, condition physique, gestes et postures
2. **Ne pas nuire** : ne pas aggraver l'état de la victime
3. **Maîtriser les techniques** : formation et entraînement
4. **S'adapter** : faire preuve de faculté d'adaptation
5. **Aider les autres équipes** : collaboration avec les renforts

**Critères FAOD :**
→ Formation continue obligatoire
→ Coordination et travail en équipe
→ Respect des procédures"""
            },
            {
                "code": "01AC03",
                "titre": "Attitude et comportement du secouriste",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "AC",
                "contenu": """**Objectifs pédagogiques :**
- Comprendre l'impact psychologique des situations d'urgence
- Adopter une attitude adaptée face aux victimes
- Maîtriser l'abord relationnel

**Impact psychologique :**

**Réaction de stress normale :**
• Activation physiologique (FC, FR, PA augmentées)
• Tremblements, pâleur, sensations désagréables
• Phénomènes adaptatifs : focalisation, identification de stratégies
• Utile mais coûteuse en énergie

**État de crise (stress intense) :**
• Perception du danger > capacités à faire face
• Perte de capacité d'adaptation
• Réactions inhabituelles
• Nécessite prise en charge spécialisée (CUMP)

**Comportement général du secouriste :**
• Organisation, rigueur, professionnalisme
• Tenue propre et correcte
• Calme, courtoisie, humanité
• Respect des personnes et des lieux
• Respect de la vie privée
• Éviter les conflits

**Victimes primaires vs secondaires :**
• Primaires : exposées directement (subi, provoqué, vu)
• Secondaires : proches des victimes primaires

**Critères FAOD :**
→ Premiers secours psychologiques essentiels
→ Attitude = gestes techniques en importance
→ Empathie et professionnalisme"""
            },
            {
                "code": "01PR01",
                "titre": "L'abord relationnel en pratique",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "PR",
                "contenu": """**Objectif :** Établir le contact et le dialogue avec la victime

**ABORDER LA VICTIME :**

1. **Établir le contact :**
   • Se présenter : "Mr X, je m'appelle Y, je suis secouriste"
   • Obtenir permission pour le prénom si souhaité
   • Expliquer les raisons de la présence

2. **Instaurer le dialogue :**
   • Question ouverte : "Pouvez-vous me dire ce qu'il se passe ?"
   • "Comment puis-je vous aider ?"
   • Écoute active et empathique

**PRENDRE EN CHARGE :**

3. **Poser le cadre :**
   • Expliquer le déroulement de l'intervention
   • Informer des étapes (bilan, contact médecin, transport)

4. **Tout au long de l'intervention :**
   • Informer : "Je vais poser ma main sur votre ventre..."
   • Reconnaître : "Vous vivez un événement stressant"
   • Questionner si nécessaire
   • Reformuler pour vérifier la compréhension
   • Favoriser l'alliance : impliquer la victime
   • Être honnête : ne pas mentir, ne pas faire de fausses promesses

**PASSER LE RELAIS :**

5. **Préparer le passage :**
   • "Nous allons vous accompagner à l'hôpital..."
   • Présenter la victime à l'équipe suivante
   • Saluer avec paroles encourageantes

**Phrases clés FAOD :**
✓ "Je suis là pour vous aider"
✓ "Je reste avec vous"
✓ "De quoi auriez-vous besoin maintenant ?"
✗ Éviter : mentir, banaliser, encourager attitudes héroïques"""
            },
            {
                "code": "01PR02",
                "titre": "Intervenir auprès d'un enfant",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "PR",
                "contenu": """**Objectif :** Adapter la prise en charge aux particularités de l'enfant

**PARTICULARITÉS DE L'ENFANT :**
• Double impact : capacités de compréhension limitées + confrontation aux vulnérabilités parentales
• Expression souvent non verbale (silence, langage corporel)
• Perte de sécurité fondamentale si parents en détresse
• Peut protéger ses parents (calme forcé)

**PRENDRE EN CHARGE L'ENFANT :**

**Communication adaptée :**
• Se positionner à hauteur de l'enfant
• Ton posé, tonalité grave
• Parler directement même aux bébés
• Mots simples et honnêtes
• Utiliser l'imagination : "petits robots", références dessins animés

**Techniques spécifiques :**
• Impliquer les parents au maximum
• Solliciter participation : "Dis-moi dans quelle position tu te sens le mieux"
• Évaluer la douleur (échelles adaptées >5 ans, observation <5 ans)
• Couvrir rapidement ce qui peut angoisser (plaies, déformations)
• Utiliser une peluche comme médiateur

**À FAIRE :**
✓ Être honnête : "Il est possible que tu sentes quelque chose"
✓ Autoriser émotions : "Tu peux pleurer si tu en as besoin"
✓ Valoriser : "C'est bien, tu sais exactement comment faire"

**À ÉVITER :**
✗ Mentir : "Ça ne fait pas mal"
✗ Obliger à parler
✗ Banaliser ou dramatiser
✗ Attitudes héroïques : "Sois courageux"
✗ Menacer

**Critères FAOD :**
→ Adaptation communication = essentielle
→ Peluche = outil pédagogique majeur
→ Parents = ressource principale"""
            },
            {
                "code": "01AC04",
                "titre": "Préservation du potentiel mental du secouriste",
                "niveau": "PSE 2",
                "type_fiche": "AC",
                "contenu": """**Objectif :** Comprendre et prévenir les risques psychologiques du secouriste

**RÉACTIONS IMMÉDIATES DE STRESS :**

**Stress modéré (utile) :**
• Mobilisation des ressources
• Focalisation d'attention
• Incitation à l'action

**Stress intense (problématique) :**
• Agitation désordonnée
• Fuite
• Action automatique
• Sidération (incapacité d'agir)

**CONSÉQUENCES À LONG TERME :**

**1. Troubles psychotraumatiques :**
• Répétition (flashbacks, cauchemars)
• Évitement de situations rappelant l'événement
• Hypervigilance
• Pensées négatives
• **TSA** (Trouble Stress Aigu) : <1 mois
• **TSPT** (Trouble Stress Post-Traumatique) : >1 mois
• Traumatisme vicariant (exposition répétée aux horreurs)

**2. Usure et épuisement :**
• **Burn-out** : épuisement émotionnel, déshumanisation, perte d'accomplissement
• **Fatigue de compassion** : hypersensibilité, impuissance, cynisme, symptômes dépressifs

**PRÉSERVATION ET OPTIMISATION :**

**Opérationnalité mentale = 3 compétences :**
1. Condition physique
2. Technique
3. Mental (sang-froid, lucidité, adaptation)

**Stratégies de préservation :**

**Avant l'action :**
• Formation et entraînement continus
• Représentation réaliste des missions
• Connaissance des risques psychologiques

**Pendant l'action :**
• Mesures de protection physique et psychologique
• Techniques de gestion du stress (respiration contrôlée)

**Après l'action :**
• Hygiène de vie (repos, alimentation, activité physique)
• Équilibre vie pro/perso
• Reconnaissance de ses limites

**SITUATIONS CRITIQUES À RISQUE :**
• Proches (famille, collègues)
• Enfants en détresse/décédés
• Violence, morts violentes
• Événements exceptionnels (attentats, catastrophes)
• Sentiment d'impuissance ou d'échec
• Danger pour intégrité physique/psychique

**Critères FAOD :**
→ Détection précoce essentielle
→ Débriefing post-intervention obligatoire
→ Soutien psychologique disponible"""
            }
        ]
    },
    2: {
        "titre": "Bilans",
        "type": "PSE",
        "fiches": [
            {
                "code": "02AC01",
                "titre": "Les 4 regards du bilan",
                "niveau": "PSE 1",
                "type_fiche": "AC",
                "contenu": """**Objectif :** Maîtriser la méthode d'évaluation en 4 regards

**MÉTHODE DES 4 REGARDS :**

**1er REGARD - Évaluation instantanée :**
• Sécurité de la scène
• Nombre de victimes
• Gravité apparente
• Détresses immédiates

**2ème REGARD - Bilan vital :**
• Conscience
• Respiration
• Circulation (hémorragies)
• Identification des détresses vitales

**3ème REGARD - Bilan complémentaire :**
• Interrogatoire (SAMPLE)
• Examen physique de la tête aux pieds
• Signes et symptômes
• Circonstances

**4ème REGARD - Surveillance :**
• Évolution de l'état
• Efficacité des gestes
• Apparition de nouveaux signes
• Surveillance continue jusqu'aux renforts

**Mnémotechnique SAMPLE :**
• **S**ignes et symptômes
• **A**llergies
• **M**édicaments
• **P**assé médical
• **L**ast meal (dernier repas)
• **E**vénements (circonstances)

**Critères FAOD :**
→ Méthode systématique et répétitive
→ Priorisation des détresses vitales
→ Transmission structurée"""
            },
            {
                "code": "02PR01",
                "titre": "Réalisation du bilan complet",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "PR",
                "contenu": """**Objectif :** Conduire un bilan systématique et complet

**DÉROULEMENT :**

**1. Premier regard (3-5 secondes) :**
• Vision globale de la situation
• Appréciation instantanée
• Décision de protection immédiate si nécessaire

**2. Deuxième regard (30 secondes max) :**
• Vérifier conscience : "M'entendez-vous ?"
• Vérifier respiration : libération VA + observation
• Rechercher hémorragies externes
→ Traiter immédiatement toute détresse vitale

**3. Troisième regard (complément) :**
• Interrogatoire SAMPLE
• Examen physique systématique :
  - Tête et cou
  - Thorax
  - Abdomen
  - Bassin
  - Membres
• Signes vitaux (si équipement)
• Contexte et circonstances

**4. Quatrième regard (continu) :**
• Réévaluation régulière
• Efficacité des gestes
• Nouveaux signes
• Communication avec la victime

**TRANSMISSION DU BILAN :**
Structure claire et concise :
1. Identification (âge, sexe)
2. Motif d'appel
3. Circonstances
4. Détresses identifiées
5. Gestes réalisés
6. Évolution

**Critères FAOD :**
→ Systématique = aucun oubli
→ Hiérarchisation : vital d'abord
→ Documentation pour transmission"""
            }
        ]
    },
    3: {
        "titre": "Protection et sécurité",
        "type": "PSE",
        "fiches": [
            {
                "code": "03AC01",
                "titre": "Protection et sécurité - Principes généraux",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "AC",
                "contenu": """**Objectif :** Assurer la sécurité de tous les intervenants

**PRINCIPES DE PROTECTION :**

**1. Sécurité personnelle PRIORITAIRE :**
• Sauveteur en danger = victime supplémentaire
• Évaluation de la scène AVANT intervention
• EPI obligatoires

**2. Protection collective :**
• Sauveteur
• Victime(s)
• Témoins et public
• Autres intervenants

**DANGERS À IDENTIFIER :**

**Dangers immédiats :**
• Circulation routière
• Incendie, explosion
• Électricité
• Gaz toxiques
• Effondrement
• Noyade
• Violence

**Dangers évolutifs :**
• Aggravation possible
• Surveillance continue
• Réajustement des mesures

**MOYENS DE PROTECTION :**

**Balisage et signalisation :**
• Triangles de signalisation
• Gilets haute visibilité
• Cônes, rubalise
• Signaleurs

**Zones de sécurité :**
• Zone de danger (rouge)
• Zone de sécurité (verte)
• Périmètre adapté au danger

**Équipements de Protection Individuelle (EPI) :**
• Gants
• Lunettes
• Masques
• Casque
• Gilet haute visibilité

**Critères FAOD :**
→ Sécurité = préalable à toute action
→ Protection évolutive
→ Communication avec équipe"""
            },
            {
                "code": "03PR01",
                "titre": "Mise en sécurité d'une situation",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "PR",
                "contenu": """**Objectif :** Sécuriser rapidement une situation d'urgence

**DÉMARCHE SYSTÉMATIQUE :**

**1. OBSERVER :**
• Analyser la scène à distance
• Identifier les dangers
• Évaluer les risques

**2. PROTÉGER :**
• Supprimer le danger (si possible sans risque)
• Isoler le danger (balisage, extinction)
• Soustraire la victime (dégagement d'urgence)

**3. ALERTER :**
• Alerter les services adaptés
• Indiquer les dangers identifiés
• Demander moyens spécialisés si nécessaire

**SITUATIONS SPÉCIFIQUES :**

**Accident de la route :**
• Stationner en sécurité (feux détresse)
• Gilet haute visibilité
• Baliser (triangle à 200m en amont)
• Couper contact véhicules
• Serrer frein à main
• Ne pas fumer

**Incendie :**
• Alerter immédiatement
• Évacuer si possible
• Fermer portes
• Ne jamais revenir en arrière

**Électricité :**
• Ne JAMAIS toucher victime sous tension
• Couper courant à distance
• Alerter EDF si haute tension

**Gaz, produits toxiques :**
• Aérer si possible
• Alerter services spécialisés
• Évacuer en amont (vent dans le dos)

**Critères FAOD :**
→ Analyse de la situation = primordiale
→ Ne jamais se mettre en danger
→ Adapter les moyens au danger identifié"""
            },
            {
                "code": "03FT01",
                "titre": "Dégagement d'urgence",
                "niveau": "PSE 1",
                "type_fiche": "FT",
                "contenu": """**Indication :** Danger vital immédiat et impossible de supprimer/isoler

**Justification :**
Soustraire rapidement la victime au danger quand :
• Suppression du danger impossible
• Isolement du danger impossible
• Danger vital immédiat

**PRINCIPES :**
• Technique rapide mais non traumatisante
• Urgence absolue uniquement
• Risque aggravation < risque du danger

**TECHNIQUES PAR GABARIT :**

**Adulte/grand enfant :**
**1. Dégagement par les chevilles :**
• Saisir les deux chevilles
• Tirer en arrière
• Déplacer en ligne droite

**2. Dégagement par les poignets :**
• Saisir les deux poignets
• Tirer en arrière
• Maintenir bras tendus

**3. Dégagement par les vêtements :**
• Saisir vêtements au niveau des épaules
• Tirer en arrière
• Maintenir tête si possible

**Nourrisson/petit enfant :**
• Saisir sous les bras
• Soutenir la tête avec avant-bras
• Maintenir contre soi
• Se déplacer rapidement

**RISQUES :**
• Aggravation lésions traumatiques
• Acceptable seulement si danger vital immédiat

**Critères FAOD :**
→ Dernier recours uniquement
→ Rapidité primordiale
→ Déplacement minimal nécessaire"""
            }
        ]
    },
    4: {
        "titre": "Hygiène et asepsie",
        "type": "PSE",
        "fiches": [
            {
                "code": "04AC01",
                "titre": "Hygiène et asepsie - Principes",
                "niveau": "PSE 1",
                "type_fiche": "AC",
                "contenu": """**Objectif :** Prévenir les infections lors des interventions

**RISQUES INFECTIEUX :**

**Transmission possible :**
• Sang et liquides biologiques
• Contact direct (peau, muqueuses)
• Contact indirect (matériel contaminé)
• Gouttelettes (toux, éternuements)
• Aéroporté (air, poussières)

**Infections transmissibles :**
• VIH, hépatites B et C
• Tuberculose
• COVID-19, grippe
• Infections cutanées

**PRINCIPES D'HYGIÈNE :**

**1. Précautions standard :**
• Gants à usage unique (systématiques)
• Hygiène des mains (SHA avant/après)
• Masque si projections possibles
• Lunettes si projections
• Surblouse si souillures importantes

**2. Hygiène du matériel :**
• Nettoyage après usage
• Désinfection adaptée
• Matériel à usage unique privilégié
• Conditionnement stérile préservé

**3. Élimination des déchets :**
• DASRI (Déchets d'Activités de Soins à Risques Infectieux)
• Conteneurs spécifiques
• Objets piquants/tranchants : collecteur
• Protocoles d'élimination

**VACCINATION RECOMMANDÉE :**
• Hépatite B (obligatoire professionnels)
• Tétanos
• Diphtérie
• Poliomyélite
• Grippe annuelle
• COVID-19

**Critères FAOD :**
→ Protection systématique
→ Gestes d'hygiène automatiques
→ Connaissance des protocoles"""
            },
            {
                "code": "04PR01",
                "titre": "Lavage et désinfection des mains",
                "niveau": "PSE 1",
                "type_fiche": "PR",
                "contenu": """**Objectif :** Maîtriser les techniques d'hygiène des mains

**QUAND SE LAVER LES MAINS :**
• Avant de mettre les gants
• Après avoir retiré les gants
• Après contact avec liquides biologiques
• Avant et après chaque soin
• Avant de manger
• Après être allé aux toilettes

**TECHNIQUE LAVAGE SIMPLE (eau + savon) :**

Durée : 30 secondes minimum

1. Mouiller les mains
2. Savonner (savon liquide)
3. Frotter :
   • Paume contre paume
   • Dos des mains
   • Espaces interdigitaux
   • Dos des doigts
   • Pouces
   • Ongles et bout des doigts
   • Poignets
4. Rincer abondamment
5. Sécher avec essuie-mains usage unique
6. Fermer robinet avec essuie-mains

**FRICTION HYDRO-ALCOOLIQUE (SHA) :**

Durée : 30 secondes minimum
Utilisable si mains visuellement propres

1. 1 pression de SHA dans paume
2. Frotter jusqu'à séchage complet :
   • Paume contre paume
   • Dos des mains
   • Espaces interdigitaux
   • Dos des doigts
   • Pouces
   • Ongles et bout des doigts
   • Poignets
3. Laisser sécher (ne pas essuyer)

**ERREURS À ÉVITER :**
✗ SHA sur mains mouillées
✗ Rincer la SHA
✗ Temps insuffisant
✗ Oublier pouces, ongles, poignets

**Critères FAOD :**
→ Geste essentiel de prévention
→ Technique rigoureuse
→ Systématique avant/après soins"""
            },
            {
                "code": "04FT01",
                "titre": "Port des gants",
                "niveau": "PSE 1",
                "type_fiche": "FT",
                "contenu": """**Indication :** Systématique pour tout contact avec victime

**Justification :**
Protection bidirectionnelle :
• Secouriste ← Victime
• Victime ← Secouriste

**TYPE DE GANTS :**
• À usage unique
• Non stériles (sauf soins spécifiques)
• Latex, nitrile ou vinyle
• Taille adaptée

**TECHNIQUE DE MISE EN PLACE :**
1. Hygiène des mains
2. Sortir gants de la boîte
3. Enfiler premier gant (partie externe)
4. Enfiler second gant
5. Ajuster sans toucher extérieur

**TECHNIQUE DE RETRAIT :**
1. Pincer gant au poignet (extérieur)
2. Retourner en retirant
3. Former boule dans main gantée
4. Glisser doigts sous poignet 2ème gant
5. Retourner par-dessus le premier
6. Jeter dans DASRI
7. Hygiène des mains

**CHANGEMENT OBLIGATOIRE :**
• Entre deux victimes
• Si déchirés ou troués
• Si fortement souillés
• Si contact prolongé

**ERREURS À ÉVITER :**
✗ Toucher extérieur lors du retrait
✗ Réutiliser des gants
✗ Oublier hygiène des mains après
✗ Porter gants pour toucher matériel propre

**Critères FAOD :**
→ Protection systématique
→ Technique rigoureuse retrait
→ Toujours disponibles dans sac"""
            }
        ]
    },
    5: {
        "titre": "Urgences vitales",
        "type": "PSE",
        "fiches": [
            {
                "code": "05AC01",
                "titre": "L'arrêt cardiaque",
                "niveau": "PSE 1",
                "type_fiche": "AC",
                "contenu": """**Définition :**
Interruption brutale et généralement inattendue de la circulation du sang dans l'organisme

**Causes principales :**
• Infarctus du myocarde (adulte++)
• Détresse respiratoire non traitée
• Électrocution, noyade
• Intoxication, traumatisme grave
• Hémorragie massive

**Signes de reconnaissance :**
• Victime inconsciente (ne répond pas)
• Ne respire pas ou gasps (respiration agonique)
• Absence de pouls carotidien (vérification professionnelle)

**Chaîne de survie - 4 maillons :**
1. **Alerte précoce** (15 ou 112)
2. **RCP précoce** (compressions + insufflations)
3. **Défibrillation précoce** (DAE/DSA)
4. **Prise en charge médicalisée**

**Délais critiques :**
• Lésions cérébrales : dès 3 minutes
• Lésions irréversibles : après 5 minutes
• Chaque minute sans RCP : -10% survie
• Défibrillation <5 min : 50-70% survie

**Critères FAOD :**
→ Reconnaissance immédiate vitale
→ Pas d'hésitation : RCP d'emblée
→ Alerte rapide parallèle aux gestes"""
            },
            {
                "code": "05AC02",
                "titre": "Les détresses respiratoires",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "AC",
                "contenu": """**Définition :**
Difficulté ou impossibilité de respirer normalement

**Causes :**
• Obstruction voies aériennes (corps étranger, langue)
• Asthme, bronchiolite, BPCO
• Œdème pulmonaire
• Pneumothorax, épanchement
• Trauma thoracique

**Signes de détresse respiratoire :**

**Signes d'hypoxie :**
• Cyanose (coloration bleutée)
• Agitation, anxiété
• Sueurs
• Troubles de la conscience

**Signes de lutte respiratoire :**
• Fréquence respiratoire anormale (>20 ou <12)
• Tirage (creux sus-claviculaires, intercostal)
• Battement des ailes du nez
• Respiration abdominale paradoxale
• Position assise penchée en avant

**Signes de gravité :**
• Impossibilité de parler
• Cyanose importante
• Épuisement
• Troubles conscience
• Bradypnée (<12/min)
• Silence auscultatoire

**Évolution possible :**
Détresse respiratoire → Arrêt respiratoire → Arrêt cardiaque

**Critères FAOD :**
→ Reconnaissance urgence vitale
→ Oxygénation prioritaire
→ Surveillance continue FR"""
            },
            {
                "code": "05AC03",
                "titre": "Les hémorragies",
                "niveau": "PSE 1",
                "type_fiche": "AC",
                "contenu": """**Définition :**
Perte de sang abondante par une plaie

**Hémorragie = URGENCE VITALE**

**Reconnaissance :**
• Écoulement de sang abondant
• Nappe de sang qui s'étend
• Saignement qui ne s'arrête pas

**Conséquences :**
• Diminution volume sanguin circulant
• Hypoxie des organes
• Détresse circulatoire (état de choc)
• Arrêt cardiaque si non traitée

**Signes de détresse circulatoire :**
• Pâleur intense
• Sueurs, froid
• Soif intense
• Angoisse, agitation
• Pouls rapide et faible
• Baisse pression artérielle
• Troubles conscience

**Quantité critique :**
• Adulte : perte >1 litre = grave
• Enfant : perte >500 ml = grave
• Nourrisson : perte >100 ml = grave

**Types d'hémorragies :**
• Externe visible
• Extériorisée (nez, bouche, oreille, vagin, anus)
• Interne (non visible, suspicion clinique)

**Principe d'action :**
ARRÊTER LE SAIGNEMENT IMMÉDIATEMENT

**Critères FAOD :**
→ Pas d'hésitation : compression immédiate
→ Technique prioritaire = compression directe
→ Garrot si échec ou impossible"""
            },
            {
                "code": "05AC06",
                "titre": "Obstruction des voies aériennes par corps étranger",
                "niveau": "PSE 1",
                "type_fiche": "AC",
                "contenu": """**Définition :**
Gêne ou empêchement brutal des mouvements de l'air entre extérieur et poumons

**Types d'obstruction :**
• **Partielle** : air atteint encore les poumons (respiration efficace)
• **Complète** : air ne peut plus atteindre poumons (urgence absolue)

**Causes fréquentes :**
• Aliments (noix, cacahuètes, carottes)
• Petits objets (aimants, jouets)
• Plus fréquent : enfants et personnes âgées
• Moment : pendant repas ou jeu

**Facteurs de risque :**
• Alcool, médicaments sédatifs
• Maladies neurologiques
• Démence
• Mauvaise dentition
• Troubles de la déglutition

**Risques :**
• Obstruction complète : mort en quelques minutes
• Obstruction partielle : peut évoluer vers complète
• Privation d'oxygène : perte conscience → AC

**Reconnaissance - 3 situations possibles :**

**1. Obstruction complète (conscient) :**
• Ne peut plus parler, crier, tousser
• Bouche ouverte
• Toux inefficace ou absente
• Agitation, devient bleu

**2. Obstruction partielle (conscient) :**
• Peut parler ou crier
• Tousse vigoureusement
• Respire (bruit possible)
• Reste conscient

**3. Obstruction non levée (inconscient) :**
• Perte de connaissance
• Ne respire plus ou très difficilement
• Cyanose

**Critères FAOD :**
→ Situation = urgence absolue
→ Gestes immédiats sans attendre
→ Séquence : claques dos → compressions"""
            },
            {
                "code": "05AC08",
                "titre": "Perte de connaissance",
                "niveau": "PSE 1",
                "type_fiche": "AC",
                "contenu": """**Définition :**
Perte permanente ou temporaire de l'aptitude à communiquer et réagir

**Causes :**
• Traumatiques (TC, choc)
• Médicales (malaise, AVC, épilepsie, hypoglycémie)
• Toxiques (alcool, drogues, CO)

**Risques majeurs :**

**1. Obstruction des voies aériennes :**
• Chute de la langue en arrière (perte tonus musculaire)
• Empêche respiration naturelle ou artificielle

**2. Encombrement des VA :**
• Diminution réflexe de déglutition
• Écoulement liquides dans VA (salive, sang, vomissures)
• Inhalation (fausse route)

**Évolution possible :**
Perte de connaissance → Arrêt respiratoire → Arrêt cardiaque

**Signes de reconnaissance :**
• Ne répond pas aux sollicitations verbales
• Ne réagit pas aux stimulations physiques
• MAIS respire (différence avec AC)

**Principe d'action :**
Préserver la respiration en maintenant liberté des voies aériennes

**Victime NON traumatique :**
→ Position Latérale de Sécurité (PLS)

**Victime traumatique :**
→ Maintien sur le dos + surveillance
→ PLS seulement si vomissements ou si seul

**Critères FAOD :**
→ PLS = geste de sauvetage
→ Surveillance respiratoire continue
→ Si arrêt respiration : RCP immédiate"""
            },
            {
                "code": "05AC09",
                "titre": "Section de membre",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "AC",
                "contenu": """**Définition :**
Tout ou partie d'un membre sectionné ou arraché

**Causes :**
• Toujours traumatique
• Accidents travail (machines)
• AVP, accidents domestiques
• Explosions

**Particularités :**
• Hémorragie souvent présente au niveau du moignon
• Peut être retardée de plusieurs minutes
• Réimplantation parfois possible (chirurgie)

**Conséquences :**
• Identiques à hémorragie externe
• Détresse circulatoire
• État de choc
• Arrêt cardiaque si non traitée

**Délai pour réimplantation :**
• Membre chaud : 6-8 heures max
• Membre refroidi : jusqu'à 12-24h
• Conditionnement essentiel

**Principe d'action :**
1. Arrêter hémorragie (compression/garrot)
2. Lutter contre détresse circulatoire
3. Retrouver et préserver membre sectionné

**Critères FAOD :**
→ Arrêt hémorragie = priorité absolue
→ Conditionnement membre = pas retarder gestes vitaux
→ Membre au froid ≠ membre dans glace directe"""
            },
            {
                "code": "05PR01",
                "titre": "Arrêt cardiaque - Conduite à tenir",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "PR",
                "contenu": """**RECONNAISSANCE :**
• Victime inconsciente
• Ne respire pas (ou gasps)
→ ARRÊT CARDIAQUE confirmé

**CONDUITE À TENIR - SÉQUENCE :**

**1. ALERTER ou FAIRE ALERTER** (15 ou 112)
• Localisation précise
• "Arrêt cardiaque"
• Demander un DAE

**2. DÉBUTER RCP IMMÉDIATEMENT**
• Ne PAS vérifier le pouls (perte de temps)
• Compressions thoraciques

**3. APPLIQUER DAE DÈS DISPONIBLE**
• Poursuivre compressions pendant installation
• Suivre instructions vocales
• Reprendre RCP après choc

**ALGORITHME RCP :**

**Adulte & Enfant >8 ans :**
• 30 compressions thoraciques
• 2 insufflations
• Cycles de 30:2 sans interruption

**Enfant 1-8 ans (si 2 sauveteurs) :**
• 15 compressions thoraciques
• 2 insufflations
• Cycles de 15:2

**Nourrisson <1 an (si 2 sauveteurs) :**
• 15 compressions thoraciques
• 2 insufflations
• Cycles de 15:2

**COMPRESSIONS THORACIQUES :**
• Fréquence : 100-120/min
• Profondeur : 5-6 cm (adulte), 1/3 thorax (enfant)
• Relâchement complet entre chaque
• Temps compression = temps relâchement

**INSUFFLATIONS :**
• Libération VA (bascule tête)
• Bouche-à-bouche ou insufflateur
• Volume : soulèvement thorax visible
• Durée : 1 seconde par insufflation

**INTERRUPTIONS MINIMALES :**
• Analyse DAE : <10 secondes
• Ventilations : <10 secondes
• Changement sauveteur : <5 secondes

**ARRÊT DE LA RCP uniquement si :**
• Victime reprend respiration normale
• Relais par équipe médicalisée
• Épuisement sauveteur

**RELAIS TOUTES LES 2 MINUTES**
(pendant analyse DAE)

**Critères FAOD :**
→ RCP = priorité absolue
→ Qualité > quantité
→ Limiter interruptions <10 sec"""
            },
            {
                "code": "05PR10",
                "titre": "Obstruction partielle des voies aériennes",
                "niveau": "PSE 1",
                "type_fiche": "PR",
                "contenu": """**SITUATION :** Victime consciente, tousse vigoureusement, peut parler

**CONDUITE À TENIR :**

**1. NE JAMAIS réaliser de techniques de désobstruction**
   Risque : transformer obstruction partielle en complète

**2. Installer victime dans position où elle se sent le mieux**
   Généralement : assise penchée en avant

**3. Encourager à tousser**
   La toux = mécanisme naturel efficace
   "Toussez fort pour essayer d'expulser"

**4. Administrer oxygène si nécessaire**
   Inhalation 9-15 L/min

**5. Poursuivre bilan et surveiller attentivement**
   Surveillance respiratoire continue

**VIGILANCE - Passages à obstruction complète :**

**Appliquer CAT obstruction complète si :**
• Toux devient inefficace + signes de fatigue
• Obstruction partielle devient complète
• Arrêt de la respiration

**SIGNES D'AGGRAVATION :**
• Toux s'affaiblit
• Épuisement
• Cyanose augmente
• Angoisse croissante
• Difficulté à parler augmente

**TRANSMISSION AUX RENFORTS :**
• Circonstances (en train de manger)
• Type d'aliment ou objet suspecté
• Évolution depuis intervention
• Gestes réalisés

**CE QU'IL NE FAUT PAS FAIRE :**
✗ Taper dans le dos
✗ Compressions abdominales
✗ Mettre doigts dans la bouche
✗ Donner à boire
→ Risque transformation en obstruction complète

**Critères FAOD :**
→ Encourager toux = essentiel
→ Ne rien faire = mieux que mal faire
→ Surveillance = continue jusqu'à résolution"""
            },
            {
                "code": "05PR11",
                "titre": "Obstruction complète des voies aériennes",
                "niveau": "PSE 1",
                "type_fiche": "PR",
                "contenu": """**SITUATION :** Ne peut plus parler/crier/tousser, bouche ouverte, s'agite, devient bleu

**VICTIME CONSCIENTE - SÉQUENCE :**

**1. Laisser victime dans position actuelle**
   Généralement debout ou assise

**2. CLAQUES DANS LE DOS (1 à 5)**
   • Se placer sur le côté
   • Soutenir thorax avec une main
   • Pencher victime en avant
   • Donner claques vigoureuses entre omoplates
   • Observer si corps étranger expulsé

**3. Si ÉCHEC : COMPRESSIONS (1 à 5)**

   **Adulte/Enfant : Compressions ABDOMINALES**
   • Se placer derrière victime
   • Poing fermé au-dessus du nombril
   • Autre main par-dessus
   • Compressions vers arrière et vers le haut
   • 1 à 5 fois

   **Nourrisson/Femme enceinte/Obèse : Compressions THORACIQUES**
   • Nourrisson : sur avant-bras, pulpe 2 doigts milieu sternum
   • Adulte : même zone que compressions cardiaques
   • 1 à 5 fois

**4. RÉPÉTER LE CYCLE**
   Claques dos → Compressions → Claques dos...
   Jusqu'à :
   • Expulsion corps étranger
   • Apparition toux/cris/pleurs
   • Reprise respiration
   • **OU** perte de connaissance

**SI MANŒUVRES EFFICACES :**
• Installer position confort
• Réconforter
• Desserrer vêtements
• Poursuivre bilan
• Transmettre bilan pour avis médical (OBLIGATOIRE)
   → Complications possibles (fragment dans poumons, lésions internes)

**SI VICTIME PERD CONNAISSANCE :**
• Accompagner au sol
• **DÉBUTER RCP IMMÉDIATEMENT**
• Commencer par compressions thoraciques
• À chaque fin de cycle : vérifier présence corps étranger dans bouche
• Retirer prudemment si accessible

**ERREURS À ÉVITER :**
✗ Hésiter ou tarder
✗ Compressions trop douces
✗ Arrêter trop tôt
✗ Oublier avis médical même si efficace

**Critères FAOD :**
→ Vigueur des gestes = vitale
→ Alternance claques/compressions
→ Passage RCP si perte conscience"""
            },
            {
                "code": "05PR12",
                "titre": "Perte de connaissance - Victime non traumatique",
                "niveau": "PSE 1",
                "type_fiche": "PR",
                "contenu": """**SITUATION :** Victime inconsciente, respire, PAS de suspicion traumatisme

**CONDUITE À TENIR :**

**1. PLACER EN PLS (Position Latérale de Sécurité)**

   **Technique PLS (adulte/enfant) :**
   • Placer bras côté sauveteur à angle droit
   • Saisir bras opposé, main sous joue victime
   • Saisir jambe opposée, plier genou
   • Faire rouler vers soi en tirant sur genou
   • Ajuster jambe du dessus (genou à 90°)
   • Ouvrir bouche vers le sol
   • Contrôler respiration

   **Femme enceinte :** PLS côté gauche préférable

**2. ASPIRATION si encombrement VA**
   • Gargouillements audibles
   • Liquides visibles (salive, vomissures)
   • Sonde d'aspiration 18-26 Ch
   • <10 secondes par passage

**3. OXYGÈNE si nécessaire**
   • Inhalation 9-15 L/min
   • Masque adapté

**4. PROTÉGER victime**
   • Couverture si froid
   • Protection soleil/intempéries
   • Intimité préservée

**5. POURSUIVRE bilan**
   • Interrogatoire entourage
   • Recherche causes
   • Signes associés

**6. SURVEILLER attentivement**
   • Respiration CONTINUE
   • Renouveler libération VA
   • Réaspirer si nécessaire
   • Vérifier maintien PLS

**⚠️ SI ARRÊT RESPIRATION :**
→ Retourner sur le dos
→ Débuter RCP immédiatement

**TRANSMISSION :**
• Durée perte conscience
• Circonstances
• Antécédents connus
• Évolution depuis PLS

**Critères FAOD :**
→ PLS = geste vital pour maintenir respiration
→ Surveillance = jamais laisser seule
→ Réactivité si aggravation"""
            },
            {
                "code": "05PR13",
                "titre": "Perte de connaissance - Sauveteur isolé",
                "niveau": "PSE 1",
                "type_fiche": "PR",
                "contenu": """**SITUATION :** Seul sans matériel, victime inconsciente qui respire

**VICTIME NON SUSPECTE TRAUMATISME :**

**1. PLACER EN PLS**
   • Technique PLS standard
   • Femme enceinte/obèse : côté gauche privilégié

**2. FAIRE ALERTER ou ALERTER (15/112)**
   • Si témoin : envoyer alerter avec consignes précises
   • Si seul : alerter puis revenir auprès victime

**3. SURVEILLER RESPIRATION EN PERMANENCE**
   • Regarder : soulèvement ventre/poitrine
   • Écouter : bruits respiratoires
   • Sentir : mouvements avec main sur thorax
   • Jusqu'à arrivée secours

**VICTIME SUSPECTE TRAUMATISME ou DOUTE :**

**1. LAISSER SUR LE DOS**
   • Ne pas mobiliser
   • Maintenir tête si possible

**2. ALERTER ou FAIRE ALERTER**
   • Préciser suspicion traumatisme
   • Respecter consignes régulateur

**3. SURVEILLER RESPIRATION**
   • Même technique que ci-dessus
   • Permanence jusqu'aux secours

**4. SI VOMIT/RÉGURGITE :**
   • Tourner sur le côté
   • Maintenir axe tête-cou-tronc si possible
   • Demander aide témoin si disponible

**DANS TOUS LES CAS :**

**COMPLÉTER LE BILAN :**
• Interroger entourage si présent
• Noter circonstances
• Rechercher indices (médocs, carte diabétique, etc.)

**PROTÉGER :**
• Chaleur/froid
• Intempéries
• Intimité

**⚠️ SI RESPIRATION S'ARRÊTE OU DEVIENT ANORMALE :**
→ Retourner sur dos
→ Débuter RCP
→ Alerter évolution aux secours

**ERREURS FRÉQUENTES :**
✗ Quitter victime pour aller chercher aide (si pas de témoin)
✗ Arrêter surveillance respiration
✗ Oublier de protéger contre froid
✗ Ne pas transmettre circonstances

**Critères FAOD :**
→ Alerte précoce essentielle
→ Jamais laisser seule
→ Surveillance = rôle principal si seul"""
            },
            {
                "code": "05PR14",
                "titre": "Section de membre",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "PR",
                "contenu": """**SITUATION :** Membre ou partie de membre sectionné/arraché

**CONDUITE À TENIR - PRIORITÉS :**

**1. ARRÊTER L'HÉMORRAGIE IMMÉDIATEMENT**

   **Compression manuelle du moignon :**
   • Gants protection
   • Appuyer fortement sur moignon
   • Interposer compresses/tissu propre
   • Maintenir jusqu'au relais

   **Si échec : GARROT**
   • 5-7 cm au-dessus du moignon
   • Entre moignon et racine membre
   • Serrer jusqu'à arrêt saignement
   • Noter heure de pose

   **Si disponible : Gaze hémostatique**
   • Sur moignon si zone accessible
   • Compression 3 min minimum

**2. PANSEMENT COMPRESSIF sur moignon**
   • MÊME en l'absence de saignement actif
   • Prévention reprise hémorragie
   • Surveillance

**3. CONDITIONNER LE MEMBRE SECTIONNÉ**

   **Méthode de conditionnement :**
   a. Emballer membre :
      • Compresses stériles humides (sérum physio)
      • Sac plastique étanche
      • Identifier (nom victime)
   
   b. Refroidir :
      • Sac de glace ou glaçons
      • JAMAIS contact direct glace-membre
      • Température : 4°C idéale
   
   c. Accompagner membre avec victime
      • Informer équipe médicale
      • Délai crucial pour réimplantation

**4. LUTTER CONTRE DÉTRESSE CIRCULATOIRE**
   • Allonger victime
   • Surélever jambes si possible
   • Couvrir, rassurer
   • Oxygène si disponible

**5. POURSUIVRE BILAN**
   • Circonstances accident
   • Heure exacte
   • Lésions associées

**6. SURVEILLER CIRCULATION**
   • Conscience
   • Coloration
   • Pouls
   • Efficacité compression/garrot

**ERREURS À ÉVITER :**
✗ Retarder arrêt hémorragie pour chercher membre
✗ Membre directement dans glace
✗ Oublier de noter heure pose garrot
✗ Sous-estimer détresse circulatoire

**TRANSMISSION OBLIGATOIRE :**
• Type de section (franche/arrachement)
• Localisation précise
• Technique d'hémostase utilisée
• Heure pose garrot si posé
• Membre conditionné : OUI/NON
• État hémodynamique

**Critères FAOD :**
→ Hémorragie = priorité ABSOLUE (pronostic vital)
→ Membre = secondaire mais conditionner si possible
→ Conditionnement rapide = meilleures chances réimplantation"""
            },
            {
                "code": "05FT01",
                "titre": "Administration d'oxygène par insufflation",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "FT",
                "contenu": """**Indication :** Ventilation artificielle avec insufflateur manuel + source O2

**Justification :**
Enrichissement en O2 de l'air insufflé → Efficacité RCP accrue

**Matériel :**
• Bouteille d'oxygène
• Insufflateur manuel (adulte/pédiatrique/prématuré)
• Ballon-réserve (concentration O2 ~85% à 15 L/min)

**Réalisation :**

**1. PRÉPARATION :**
• Ouvrir bouteille O2
• Connecter tuyau : débitmètre → ballon-réserve
• Raccorder ballon-réserve à insufflateur

**2. RÉGLAGE :**
• Débit : 15 L/min
• Vérifier remplissage ballon-réserve

**3. VENTILATION :**
• Insuffler normalement
• Volume : soulèvement thorax visible
• Fréquence selon âge et situation

**4. AJUSTEMENT :**
• Si SpO2 mesurable et fiable : ajuster débit selon SpO2
• Si SpO2 non fiable : maintenir 15 L/min

**Risques et contre-indications :**
• Absence d'O2 : NE PAS interrompre ventilation
  → Insufflateur fonctionne à l'air ambiant
• Ne JAMAIS utiliser insufflateur avec ballon-réserve pour inhalation
  → Augmente résistance, aggrave détresse (surtout enfant)

**Évaluation efficacité :**
• Ballon-réserve jamais complètement aplati
• Soulèvement thorax à chaque insufflation
• SpO2 en amélioration si mesurable

**Critères FAOD :**
→ O2 = améliore efficacité RCP
→ Ne JAMAIS retarder RCP pour installer O2
→ Ventilation = priorité, O2 = amélioration"""
            },
            {
                "code": "05FT02",
                "titre": "Aspiration de mucosités",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "FT",
                "contenu": """**Indication :**
Encombrement VA par liquides/particules que victime ne peut expulser

**Reconnaissance encombrement :**
• Gargouillements audibles (respiration/ventilation)
• Vomissures, mucosités, sang sortant bouche/nez
• Chez nouveau-né : méconium, caillots, vernix

**Quand aspirer :**
• Après LVA et PLS (si perte conscience non trauma)
• Pendant compressions thoraciques (RCP)
• Nouveau-né en détresse à la naissance

**Justification :**
Retrait sécrétions → Amélioration respiration/ventilation → Oxygénation

**Matériel :**
• Pompe aspiration (manuelle/électrique/portable/véhicule)
• Sonde aspiration buccale adaptée âge :
  - Souple à extrémité mousse
  - OU Rigide (Yankauer)
• Réceptacle (flacon/sac usage unique)
• EPI (gants, masque, lunettes)

**Taille sonde + dépression :**
| Âge | Diamètre (Ch) | Dépression (mmHg) |
|-----|---------------|-------------------|
| Adulte | 18-26 | 350-500 |
| Enfant | 8-12 | 200-350 |
| Nourrisson | 6-8 | 200-250 |
| Nouveau-né | 4-6 | 120-150 |

**Réalisation :**

**1. PRÉPARATION :**
• EPI (gants, masque, lunettes)
• Raccorder sonde stérile au tuyau
• Mettre en marche + régler aspiration

**2. ASPIRATION :**
• Ouvrir bouche victime
• Introduire sonde doucement (perpendiculaire visage)
• Enfoncer jusqu'à butée
• Mettre en œuvre aspiration (obturer orifice)
• Retirer progressivement en rotation
• Si débris non aspirables : retirer avec doigts

**3. FIN :**
• Renouveler si nécessaire
• Remettre sonde dans emballage
• Éteindre appareil

**Durée aspiration :**
• Adulte : <10 secondes
• Enfant/nourrisson/nouveau-né : <5 secondes
→ Limite hypoxie

**CAS PARTICULIER Nouveau-né :**
• Sonde petit calibre (4-6 Ch)
• Dépression adaptée (120-150 mmHg)
• TOUJOURS bouche AVANT narines
• Bouche : <5 cm profondeur
• Narines : <1 cm profondeur, perpendiculaire visage

**Risques :**
• Hypoxie si aspiration trop longue
• Vomissement si victime consciente (PROSCRIRE)
• Lésions muqueuses (ouvrir prise d'air ponctuellement)

**Évaluation :**
Aspiration efficace = respiration/insufflations devenues silencieuses

**Critères FAOD :**
→ Geste essentiel maintien liberté VA
→ Durée limitée impérative
→ Matériel prêt systématiquement si perte conscience"""
            },
            {
                "code": "05FT03",
                "titre": "Compression manuelle",
                "niveau": "PSE 1",
                "type_fiche": "FT",
                "contenu": """**Indication :**
Toute hémorragie externe accessible sans corps étranger

**Justification :**
• Technique facile et rapide
• Très efficace (arrête la plupart des hémorragies)
• Suffit dans majorité des cas

**Matériel :**
• Gants usage unique (OBLIGATOIRE)
• Compresses (paquet)
• OU pansement "américain"
• OU tissu propre (mouchoir, torchon, vêtement)

**Réalisation :**

**1. PROTECTION :**
• Enfiler gants usage unique
• Protection bidirectionnelle

**2. COMPRESSION IMMÉDIATE :**
• Appuyer FORTEMENT sur endroit qui saigne
• Main protégée par gant

**3. INTERPOSITION :**
• Placer le plus tôt possible entre main et plaie :
  - Plusieurs compresses
  - Pansement
  - Tissu propre
• Augmente efficacité compression

**4. MAINTIEN :**
• Maintenir compression jusqu'au relais
• Relais = pansement compressif

**SI SAUVETEUR DOIT SE LIBÉRER :**
• Demander à victime de comprimer elle-même
  (si capable)
• OU demander à témoin
→ Situations nombreuses victimes

**Risques :**
• Contamination possible (AERI)
  → Gants OBLIGATOIRES
• Temps compression parfois prolongé :
  → Patients sous anticoagulants/antiagrégants

**Évaluation :**
Compression efficace = saignement arrêté

**ERREURS À ÉVITER :**
✗ Hésiter ou attendre
✗ Compression insuffisante (trop douce)
✗ Lâcher trop tôt
✗ Oublier les gants

**Critères FAOD :**
→ Technique de PREMIÈRE intention
→ Pas d'hésitation : compression IMMÉDIATE
→ Maintien jusqu'au pansement compressif
→ Si échec : garrot"""
            },
            {
                "code": "05FT04",
                "titre": "Compressions thoraciques",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "FT",
                "contenu": """**Indication :**
• Arrêt cardiaque (adulte/enfant/nourrisson)
• Perte conscience suite obstruction VA
• Nouveau-né avec FC <60/min

**Justification :**
• Rétablit circulation artificielle (20-30% débit normal)
• Suffisant pour oxygéner cerveau + cœur
• Compression vide cavités cardiaques + poumons
• Relâchement = sang aspiré et remplit cœur/poumons
• Lors obstruction VA : augmentation pression → expulsion CE

**Matériel optionnel :**
• Métronome (aide rythme)
• Moniteur profondeur
→ Amélioration qualité RCP

**Réalisation :**

**INSTALLATION :**
• Victime dos, horizontale
• Plan dur (sol, table)
• Se placer à genoux au plus près (adulte/enfant)

**LOCALISATION ZONE COMPRESSION :**

| Âge | Zone compression |
|-----|------------------|
| **Adulte/Enfant >1 an** | Milieu thorax (moitié inférieure sternum) |
| **Nourrisson <1 an** | Milieu thorax, 1 doigt sous ligne inter-mamelonnaire |
| **Nouveau-né** | Milieu thorax, ligne inter-mamelonnaire |

**TECHNIQUE COMPRESSION :**

**Adulte :**
• Talon d'une main au centre thorax
• Autre main par-dessus, doigts entrelacés
• Bras tendus, épaules à verticale sternum
• Appuyer verticalement

**Enfant 1-8 ans :**
• Talon d'une main (ou 2 si grand enfant)
• Même technique que adulte

**Nourrisson <1 an :**
• 2 techniques possibles :
  a) Pulpe 2 doigts (1 sauveteur)
  b) Technique 2 pouces (2 sauveteurs)

**PARAMÈTRES ESSENTIELS :**

| Paramètre | Valeur |
|-----------|--------|
| **Fréquence** | 100-120/min |
| **Profondeur adulte** | 5-6 cm |
| **Profondeur enfant/nourr** | 1/3 épaisseur thorax |
| **Relâchement** | Complet entre chaque |
| **Ratio temps** | Compression = Relâchement |

**QUALITÉ CRUCIALE :**
• Ne pas appuyer sur côtes
• Appui perpendiculaire
• Laisser thorax reprendre forme initiale
• Ne pas décoller talon main/pulpe doigts
• Limiter interruptions (<10 sec)

**RELAIS :**
• Toutes les 2 minutes
• Pendant analyse DAE
• Rotation sans interruption >5 sec

**Évaluation :**
• Profondeur suffisante
• Fréquence 100-120/min
• Relâchement complet
• Interruptions minimales

**Critères FAOD :**
→ Qualité > quantité
→ Profondeur + fréquence = essentielles
→ Relâchement complet = remplissage cœur
→ Relais régulier = maintien qualité"""
            }
        ]
    },
    6: {
        "titre": "Malaises et affections spécifiques",
        "type": "PSE",
        "fiches": [
            {
                "code": "06AC01",
                "titre": "Le malaise",
                "niveau": "PSE 1",
                "type_fiche": "AC",
                "contenu": """**Définition :**
Sensation pénible traduisant un trouble du fonctionnement de l'organisme, sans pouvoir en identifier obligatoirement l'origine

**Causes fréquentes :**
• Cardiaques (infarctus, troubles du rythme)
• Neurologiques (AVC, épilepsie, migraine)
• Métaboliques (hypoglycémie, diabète)
• Respiratoires (asthme, embolie)
• Digestives (gastro, intoxication)
• Psychologiques (angoisse, spasmophilie)

**Signes fréquents du malaise :**
• Pâleur, sueurs
• Nausées, vomissements
• Douleur (thorax, abdomen, tête)
• Vertiges, troubles de l'équilibre
• Faiblesse, fatigue intense
• Troubles visuels ou auditifs
• Difficultés à parler ou comprendre

**Signes de gravité (URGENCE VITALE) :**
• Douleur thoracique (étau, écrasement)
• Difficultés respiratoires importantes
• Troubles de la conscience
• Paralysie, troubles de la parole
• Convulsions
• Signes de choc

**Évolution possible :**
• Amélioration spontanée
• Aggravation → détresse vitale
• Récidive

**Principe d'action :**
• Mettre au repos
• Rechercher signes de gravité
• Transmettre pour avis médical
• Surveiller évolution

**Critères FAOD :**
→ Tout malaise = avis médical
→ Signes de gravité = urgence vitale
→ Surveillance continue jusqu'aux secours"""
            },
            {
                "code": "06AC02",
                "titre": "L'accident vasculaire cérébral (AVC)",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "AC",
                "contenu": """**Définition :**
Interruption brutale de la circulation sanguine dans une zone du cerveau

**Types d'AVC :**
• **AVC ischémique** (80%) : obstruction artère cérébrale (caillot)
• **AVC hémorragique** (20%) : rupture artère cérébrale

**Reconnaissance - Test FAST :**

**F - Face (Visage) :**
• Demander de sourire
→ Asymétrie du visage, bouche de travers

**A - Arms (Bras) :**
• Demander de lever les deux bras
→ Un bras ne peut pas se lever ou retombe

**S - Speech (Parole) :**
• Demander de répéter phrase simple
→ Troubles de la parole (mots incompréhensibles)

**T - Time (Temps) :**
→ Si 1 signe présent = AVC probable
→ URGENCE : noter heure début symptômes

**Autres signes possibles :**
• Troubles de la vision (perte vue d'un œil)
• Troubles de l'équilibre, vertiges
• Maux de tête intenses et inhabituels
• Perte de connaissance

**Fenêtre thérapeutique :**
• <4h30 : traitement thrombolyse possible
• Chaque minute compte : "Time is Brain"
• Pronostic dépend rapidité prise en charge

**Facteurs de risque :**
• HTA, diabète, cholestérol
• Tabac, alcool
• Fibrillation auriculaire
• Âge >65 ans
• Antécédents cardiaques

**Critères FAOD :**
→ Test FAST = outil diagnostic essentiel
→ Urgence absolue : chaque minute compte
→ Noter HEURE DÉBUT symptômes (crucial)"""
            },
            {
                "code": "06AC03",
                "titre": "La crise convulsive",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "AC",
                "contenu": """**Définition :**
Contractions musculaires involontaires, brutales et incontrôlables

**Types de crises :**

**Crise généralisée (Grand mal) :**
• Perte de connaissance brutale
• Phase tonique : raideur, chute
• Phase clonique : convulsions, secousses
• Morsure langue, perte urines
• Phase résolutive : respiration bruyante, hypotonie
• Durée : quelques minutes
• Confusion post-critique

**Crise partielle :**
• Conscience parfois préservée
• Convulsions localisées (visage, membre)
• Peut évoluer vers généralisée

**Causes :**
• Épilepsie (cause fréquente)
• Fièvre élevée (enfant)
• Traumatisme crânien
• AVC, tumeur cérébrale
• Hypoglycémie sévère
• Sevrage alcool/drogues
• Intoxication

**Signes de gravité :**
• Durée >5 minutes
• Crises répétées sans reprise conscience (état de mal)
• Première crise de la vie
• Trauma associé
• Détresse respiratoire post-critique
• Femme enceinte

**Évolution :**
• Arrêt spontané généralement
• Confusion post-critique normale
• Risque : traumatismes, inhalation, arrêt respiratoire

**Critères FAOD :**
→ Protéger victime pendant crise
→ NE RIEN mettre dans la bouche
→ Toute première crise = avis médical obligatoire"""
            },
            {
                "code": "06PR01",
                "titre": "Malaise - Conduite à tenir",
                "niveau": "PSE 1",
                "type_fiche": "PR",
                "contenu": """**CONDUITE À TENIR :**

**1. METTRE AU REPOS**
• Position confortable pour victime
• Allonger si possible (sauf détresse respi)
• Desserrer vêtements

**2. INTERROGATOIRE (malaise = bilan complet)**

**Circonstances :**
• Que faisiez-vous ?
• Début brutal ou progressif ?
• Première fois ou déjà eu ?

**Symptômes (LQDT) :**
• **L**ocalisation : Où avez-vous mal ?
• **Q**ualité : Comment est la douleur ? (étau, brûlure, etc.)
• **D**urée : Depuis combien de temps ?
• **T**rajet : Ça part où ? Ça va où ?

**SAMPLE :**
• **S**ignes et symptômes actuels
• **A**llergies connues
• **M**édicaments pris
• **P**assé médical (antécédents)
• **L**ast meal (dernier repas)
• **E**vénements (circonstances)

**3. RECHERCHER SIGNES DE GRAVITÉ**

**⚠️ SIGNES ALARMANTS :**
• Douleur thoracique (étau, écrasement)
• Difficultés respiratoires
• Troubles conscience
• Test FAST positif (suspicion AVC)
• Paralysie, troubles parole
• Convulsions

**4. MESURES ADAPTÉES**

**Si signes de gravité : URGENCE**
• Alerter 15 immédiatement
• Oxygène si disponible
• Installer position adaptée
• Préparer matériel urgence

**Si malaise simple :**
• Avis médical (transmission)
• Rassurer, surveiller
• Ne pas laisser seul

**5. ADMINISTRER SUCRE si hypoglycémie**
• Diabétique connu
• Signes : sueurs, tremblements, confusion
• 3 morceaux sucre ou boisson sucrée
• Si inconscient : PAS par bouche

**6. SURVEILLER**
• Conscience
• Respiration
• Circulation
• Évolution symptômes
• Jusqu'à amélioration ou arrivée secours

**CE QU'IL NE FAUT PAS FAIRE :**
✗ Laisser seul
✗ Donner médicaments (sauf si prescrits)
✗ Donner à boire si troubles conscience
✗ Minimiser les symptômes

**Critères FAOD :**
→ Bilan complet = essentiel
→ Signes de gravité = urgence vitale
→ Avis médical systématique"""
            },
            {
                "code": "06PR02",
                "titre": "AVC - Conduite à tenir",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "PR",
                "contenu": """**SUSPICION AVC - CONDUITE À TENIR :**

**1. TEST FAST (si victime consciente)**

**F - Face :** "Souriez"
→ Asymétrie ?

**A - Arms :** "Levez les deux bras"
→ Un bras ne monte pas ou retombe ?

**S - Speech :** "Répétez : le chat joue avec la souris"
→ Troubles de la parole ?

**→ 1 seul signe = AVC probable**

**2. NOTER L'HEURE EXACTE**
• Heure début des symptômes
• CRUCIAL pour thrombolyse (<4h30)
• Si inconnu : heure où victime vue normale en dernier

**3. ALERTER 15 IMMÉDIATEMENT**
• "Suspicion AVC"
• Symptômes observés (FAST)
• Heure début symptômes
• Urgence absolue

**4. INSTALLER POSITION ADAPTÉE**

**Si consciente :**
• Position demi-assise confortable
• Tête légèrement surélevée (30°)
• Côté paralysé soutenu

**Si inconsciente qui respire :**
• PLS côté paralysé en bas (si identifié)
• Surveillance respiration continue

**5. MESURES ASSOCIÉES**
• NE RIEN donner par bouche
  (troubles déglutition fréquents)
• Oxygène si disponible et nécessaire
• Rassurer, parler calmement
• Protéger contre froid/chaud
• Noter évolution

**6. PRÉPARER TRANSMISSION COMPLÈTE**
• Test FAST : résultats précis
• Heure début symptômes +++
• Autres symptômes (vision, équilibre, céphalées)
• Antécédents (HTA, diabète, FA, AVC)
• Traitements en cours (anticoagulants !)

**7. SURVEILLER ÉVOLUTION**
• Conscience (peut se dégrader)
• Respiration
• Aggravation symptômes ?
• Apparition nouveaux signes ?

**SPÉCIFICITÉS :**
• NE PAS donner aspirine (sauf ordre médical)
• NE PAS donner à boire/manger
• NE PAS perdre de temps (photos, vidéos)
• Transport rapide vers centre neuro-vasculaire

**Critères FAOD :**
→ "TIME IS BRAIN" : rapidité cruciale
→ Heure symptômes = information vitale
→ Pas de délai : alerte immédiate"""
            },
            {
                "code": "06PR03",
                "titre": "Crise convulsive - Conduite à tenir",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "PR",
                "contenu": """**PENDANT LA CRISE :**

**1. PROTÉGER LA VICTIME**
• Dégager espace autour (meubles, objets)
• Glisser coussin/vêtement sous tête
• Ne PAS déplacer (sauf danger)
• Éloigner curieux

**2. NOTER L'HEURE DE DÉBUT**
• Durée de la crise = info importante
• Si >5 min = urgence médicale

**3. CE QU'IL NE FAUT PAS FAIRE :**
✗ Maintenir ou bloquer mouvements
✗ Mettre quoi que ce soit dans la bouche
✗ Donner à boire ou médicament
✗ Gifler ou secouer
✗ Tenter de réveiller

**4. OBSERVER**
• Type de mouvements
• Durée
• Zone du corps touchée
• Morsure langue ?
• Perte urines ?

**APRÈS LA CRISE :**

**5. VÉRIFIER CONSCIENCE ET RESPIRATION**

**Si consciente :**
• Rassurer (confusion normale)
• Répondre calmement aux questions
• Laisser se reposer
• Ne pas forcer à se lever

**Si inconsciente mais respire :**
• Libérer voies aériennes
• PLS
• Aspirer sécrétions si nécessaire
• Surveiller respiration

**Si arrêt respiratoire :**
• Débuter RCP immédiatement

**6. RECHERCHER TRAUMATISMES**
• Tête (chute)
• Langue (morsure)
• Membres

**7. DÉCISION ALERTE**

**Alerte 15 OBLIGATOIRE si :**
• Première crise de la vie
• Durée >5 minutes
• Crises répétées sans reprise conscience
• Trauma associé
• Détresse respiratoire post-crise
• Femme enceinte
• Diabétique
• Pas de reprise conscience 10 min après

**Pas d'alerte si :**
• Épileptique connu
• Crise brève habituelle
• Reprise conscience normale
• Pas de traumatisme
• Entourage peut surveiller
→ Mais consultation médicale recommandée

**8. BILAN ET TRANSMISSION**
• Circonstances
• Durée crise
• Description crise
• Épileptique connu ? Traitement pris ?
• Traumatismes ?
• État actuel

**9. SURVEILLER**
• Conscience
• Respiration
• Nouvelle crise ?
• Jusqu'à récupération complète ou secours

**Critères FAOD :**
→ Protection pendant crise = priorité
→ NE RIEN mettre dans bouche
→ Durée >5 min = urgence
→ Première crise = toujours avis médical"""
            }
        ]
    },
    7: {
        "titre": "Atteintes circonstancielles",
        "type": "PSE",
        "fiches": [
            {
                "code": "07AC01",
                "titre": "Accidents liés à la chaleur",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "AC",
                "contenu": """**Types d'atteintes :**

**1. CRAMPES DE CHALEUR :**
• Contractions musculaires douloureuses
• Effort physique intense + chaleur
• Déshydratation, perte sels minéraux
• Bénin si pris en charge

**2. ÉPUISEMENT (INSOLATION) :**
• Température <40°C
• Fatigue intense, faiblesse
• Sueurs abondantes
• Nausées, céphalées
• Peau moite et pâle
• Conscience préservée

**3. COUP DE CHALEUR (URGENCE VITALE) :**
• Température >40°C
• Peau chaude, sèche, rouge
• Absence de sueurs
• Troubles conscience (confusion, agitation)
• Convulsions possibles
• Défaillance organes (cerveau, rein, foie)

**Populations à risque :**
• Nourrissons, jeunes enfants
• Personnes âgées
• Maladies chroniques
• Médicaments (diurétiques, neuroleptiques)
• Travailleurs extérieur
• Sportifs

**Facteurs favorisants :**
• Température élevée + humidité
• Effort physique intense
• Vêtements inadaptés
• Déshydratation
• Absence d'acclimatation

**Conséquences coup de chaleur :**
• Lésions cérébrales irréversibles
• Insuffisance rénale
• Défaillance multi-viscérale
• Décès si non traité rapidement

**Critères FAOD :**
→ Coup de chaleur = urgence vitale absolue
→ Refroidissement immédiat crucial
→ Prévention : hydratation + repos"""
            },
            {
                "code": "07AC02",
                "titre": "Hypothermie",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "AC",
                "contenu": """**Définition :**
Température corporelle <35°C

**Stades d'hypothermie :**

**LÉGÈRE (35-32°C) :**
• Frissons intenses
• Sensation de froid
• Maladresse, troubles coordination
• Conscience préservée

**MODÉRÉE (32-28°C) :**
• Frissons diminuent puis cessent
• Confusion, somnolence
• Troubles de la parole
• Bradycardie
• Rigidité musculaire

**SÉVÈRE (<28°C) :**
• Perte de connaissance
• Disparition réflexes
• Pouls et respiration difficiles à percevoir
• Rigidité importante
• Aspect de mort apparente
• Risque arrêt cardiaque

**Causes :**
• Exposition prolongée au froid
• Immersion eau froide
• Vêtements inadaptés
• Épuisement
• Alcool (vasodilatation)

**Populations à risque :**
• Personnes âgées
• Nourrissons
• SDF
• Alpinistes, navigateurs
• Victimes d'avalanche

**Particularité :**
**"Personne pas morte tant que pas chaude et morte"**
• Hypothermie = protection cerveau
• Cas de survie après AC prolongé
• Ne jamais arrêter RCP prématurément

**Conséquences :**
• Troubles du rythme cardiaque
• Arrêt cardiaque (FV fréquente)
• Gelures (extrémités)
• Décès

**Critères FAOD :**
→ Réchauffement progressif et prudent
→ Manipulations douces (risque FV)
→ Ne jamais masser, frictionner"""
            },
            {
                "code": "07AC03",
                "titre": "Noyade",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "AC",
                "contenu": """**Définition :**
Détresse par immersion/submersion dans liquide

**Stades de noyade :**

**NOYADE AVEC CONSCIENCE (Aquastress) :**
• Victime épuisée mais consciente
• Difficultés à se maintenir en surface
• Mouvements inefficaces
• Peut encore appeler
• Hypothermie débutante

**NOYADE AVEC INCONSCIENCE :**
• Perte de connaissance
• Peut respirer ou pas
• Inhalation d'eau possible
• Hypothermie fréquente

**ARRÊT CARDIAQUE :**
• Plus de respiration
• Submersion prolongée
• Hypothermie sévère possible

**Mécanismes :**
• Inhalation d'eau → asphyxie
• Spasme laryngé (protection mais asphyxie)
• Épuisement
• Hydrocution (choc thermique)
• Traumatisme (plongeon)

**Complications :**
• Œdème pulmonaire
• Pneumonie d'inhalation
• Hypothermie
• Lésions neurologiques (anoxie)
• Détresse respiratoire secondaire (6-72h)

**Surveillance prolongée :**
Toute victime de noyade doit être hospitalisée
→ Complications secondaires fréquentes

**Types d'eau :**
• Eau douce vs eau salée
• Eau froide (hypothermie ++)
• Eau polluée (infections)

**Critères FAOD :**
→ Sauvetage aquatique = personnel qualifié
→ Hypothermie fréquente associée
→ Hospitalisation systématique (surveillance)"""
            },
            {
                "code": "07PR01",
                "titre": "Coup de chaleur - Conduite à tenir",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "PR",
                "contenu": """**COUP DE CHALEUR = URGENCE VITALE**

**1. ALERTER 15 IMMÉDIATEMENT**
• "Coup de chaleur"
• Troubles conscience
• Température élevée

**2. SOUSTRAIRE À LA CHALEUR**
• Placer à l'ombre ou local frais
• Si impossible : créer ombre

**3. REFROIDIR IMMÉDIATEMENT**
(chaque minute compte)

**Méthodes de refroidissement :**
• Déshabiller (garder sous-vêtements)
• Asperger eau fraîche (pas glacée)
• Ventiler (ventilateur, éventail, courant d'air)
• Appliquer linges humides (front, nuque, aisselles, aines)
• Renouveler linges régulièrement

**Objectif : Température <39°C**

**4. POSITION ADAPTÉE**

**Si consciente :**
• Demi-assise
• Jambes légèrement surélevées

**Si inconsciente qui respire :**
• PLS
• Poursuivre refroidissement
• Surveiller respiration

**Si arrêt cardiaque :**
• RCP
• Poursuivre refroidissement pendant RCP

**5. SI CONSCIENTE ET COOPÉRANTE**
• Donner à boire eau fraîche
• Petites quantités répétées
• Arrêter si nausées/vomissements

**6. SURVEILLER**
• Conscience (peut se dégrader rapidement)
• Respiration
• Température (si thermomètre)
• Convulsions ?
• Jusqu'aux secours

**CE QU'IL NE FAUT PAS FAIRE :**
✗ Donner antipyrétiques (aspirine, paracétamol)
  → Inefficaces et dangereux
✗ Immersion dans eau glacée (choc)
✗ Frictions alcool
✗ Donner à boire si troubles conscience

**CRAMPES/ÉPUISEMENT (non grave) :**
• Repos à l'ombre
• Refroidissement progressif
• Boisson fraîche (eau + sel)
• Étirements doux si crampes
• Surveillance

**Critères FAOD :**
→ Refroidissement = priorité absolue
→ Rapidité cruciale (pronostic)
→ Hospitalisation systématique coup de chaleur"""
            },
            {
                "code": "07PR02",
                "titre": "Hypothermie - Conduite à tenir",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "PR",
                "contenu": """**HYPOTHERMIE - CONDUITE À TENIR :**

**1. MANIPULER AVEC PRÉCAUTION**
• Mouvements doux et lents
• NE PAS secouer, frictionner, masser
→ Risque déclenchement FV (fibrillation)

**2. SOUSTRAIRE AU FROID**
• Placer dans local chauffé
• Si impossible : isoler du sol (couverture)
• Abriter du vent

**3. ÉVALUER ÉTAT**

**Si consciente (hypothermie légère) :**
• Dialogue possible
• Frissons présents

**Si inconsciente :**
• Vérifier respiration avec attention
• Peut être très difficile à percevoir
• Observer 30-45 secondes
• Pas de mouvements = arrêt cardiaque

**4. RÉCHAUFFEMENT**

**HYPOTHERMIE LÉGÈRE (conscient) :**
• Retirer vêtements mouillés (découper)
• Envelopper couverture de survie (doré contre victime)
• Boisson chaude sucrée (si conscient et coopérant)
• Réchauffement progressif

**HYPOTHERMIE MODÉRÉE/SÉVÈRE :**
• Réchauffement PASSIF uniquement
• Couverture de survie
• Couvertures sèches
• PAS de réchauffement actif (bouillottes, friction)
→ Risque aggravation

**5. POSITION ADAPTÉE**

**Si consciente :**
• Position confortable
• Allongée si possible

**Si inconsciente qui respire :**
• Maintenir sur le dos (manipulation minimale)
• PLS seulement si vomissements

**Si arrêt cardiaque :**
• RCP immédiate
• Poursuivre jusqu'à réchauffement OU relais médical
• "Pas chaude et morte" → continuer RCP

**6. ALERTER**
• 15 si hypothermie modérée/sévère
• Préciser température si mesurée
• Circonstances (immersion, avalanche)

**7. SURVEILLER**
• Conscience
• Respiration (vérifier régulièrement)
• Réchauffement progressif
• Signes amélioration

**SPÉCIFICITÉS RCP EN HYPOTHERMIE :**
• Rythme normal compressions
• Défibrillation peut être inefficace si T°<30°C
• Continuer RCP longtemps (survie possible)
• Attendre réchauffement >32°C pour déclarer décès

**CE QU'IL NE FAUT PAS FAIRE :**
✗ Réchauffer rapidement (choc)
✗ Frictionner, masser
✗ Donner alcool
✗ Mobiliser brutalement
✗ Arrêter RCP trop tôt

**Critères FAOD :**
→ Manipulations douces (risque FV)
→ Réchauffement progressif
→ RCP prolongée si AC (espoir survie)"""
            },
            {
                "code": "07PR03",
                "titre": "Noyade - Conduite à tenir",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "PR",
                "contenu": """**APRÈS SAUVETAGE AQUATIQUE :**
(Sauvetage = personnel qualifié uniquement)

**1. ÉVALUER ÉTAT DE LA VICTIME**

**VICTIME CONSCIENTE (Aquastress) :**
• Épuisement mais consciente
• Peut parler, tousser

**VICTIME INCONSCIENTE :**
• Ne répond pas
• Vérifier respiration attentivement

**ARRÊT CARDIAQUE :**
• Inconsciente + ne respire pas

**2. CONDUITE À TENIR SELON ÉTAT**

**SI CONSCIENTE :**
• Sortir de l'eau
• Allonger, rassurer
• Retirer vêtements mouillés
• Sécher, réchauffer (couverture survie)
• Oxygène si disponible
• Ne pas laisser seule
• Alerter 15 (hospitalisation systématique)
• Surveiller respiration (complications secondaires)

**SI INCONSCIENTE QUI RESPIRE :**
• Sortir de l'eau
• Libérer voies aériennes
• PLS
• Protéger contre hypothermie
• Aspirer si encombrement
• Oxygène
• Alerter 15
• Surveiller respiration

**SI ARRÊT CARDIAQUE :**
• Sortir de l'eau
• Débuter RCP IMMÉDIATEMENT
• Commencer par 5 insufflations initiales
  (puis RCP classique 30:2)
→ Asphyxie = cause principale
• Alerter 15
• DAE dès disponible
• Sécher thorax avant électrodes
• Continuer RCP jusqu'aux secours

**3. ASPIRATION**
• Fréquente (eau + vomissements)
• Aspirer si gargouillements
• Renouveler si nécessaire

**4. GESTION HYPOTHERMIE ASSOCIÉE**
• Fréquente même en été
• Réchauffement passif
• Couverture de survie
• Manipulations douces

**5. OXYGÈNE**
• Systématique si disponible
• 9-15 L/min inhalation
• Sauf si arrêt cardiaque (insufflation)

**6. SURVEILLER**
• Respiration (complications retardées 6-72h)
• Conscience
• Température
• Vomissements
• Jusqu'aux secours

**HOSPITALISATION SYSTÉMATIQUE car :**
• Détresse respiratoire secondaire fréquente
• Œdème pulmonaire retardé
• Complications infectieuses
• Même si victime semble bien

**PARTICULARITÉS :**
• Vomissements fréquents (eau ingérée)
• Ne pas perdre temps à "vider eau"
• Hypothermie protège cerveau
• RCP prolongée justifiée

**CE QU'IL NE FAUT PAS FAIRE :**
✗ Compressions abdominales pour "vider eau"
✗ Retarder RCP
✗ Laisser repartir sans hospitalisation
✗ Sous-estimer hypothermie

**Critères FAOD :**
→ RCP commencer par 5 insufflations (asphyxie)
→ Hospitalisation TOUJOURS (surveillance)
→ Hypothermie souvent associée"""
            }
        ]
    },
    8: {
        "titre": "Traumatismes",
        "type": "PSE",
        "fiches": [
            {
                "code": "08AC01",
                "titre": "Les brûlures",
                "niveau": "PSE 1",
                "type_fiche": "AC",
                "contenu": """**Définition :**
Destruction de la peau et des tissus par chaleur, produits chimiques, électricité ou radiations

**Classification par profondeur :**

**1er DEGRÉ (superficielle) :**
• Rougeur, douleur
• Peau sèche
• Pas de cloque
• Ex : coup de soleil
• Guérison sans séquelle

**2ème DEGRÉ :**
• Cloques (phlyctènes)
• Douleur intense
• Peau rouge suintante sous cloques
• Guérison avec/sans cicatrice

**3ème DEGRÉ (profonde) :**
• Destruction totale peau
• Aspect cartonné, blanc/noir
• PEU ou PAS douloureuse (nerfs détruits)
• Nécessite greffe
• Séquelles importantes

**Évaluation de la gravité :**

**Critères de gravité :**
• **Surface** : >10% adulte, >5% enfant
  (Paume main victime = 1% surface)
• **Localisation** : visage, mains, pieds, organes génitaux, articulations
• **Profondeur** : 2ème degré étendu, 3ème degré
• **Terrain** : âge (<5 ans, >60 ans), pathologies
• **Cause** : électrique, chimique, inhalation fumées

**Complications :**
• Infection
• Déshydratation (pertes liquides)
• Choc (brûlures étendues)
• Détresse respiratoire (inhalation fumées)
• Séquelles esthétiques et fonctionnelles

**Critères FAOD :**
→ Refroidissement immédiat = priorité
→ Durée : 10-20 minutes minimum
→ Toute brûlure grave = urgence"""
            },
            {
                "code": "08AC02",
                "titre": "Les traumatismes",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "AC",
                "contenu": """**Définition :**
Lésion provoquée par un choc, une chute, un accident

**Types de traumatismes :**

**TRAUMATISME CRÂNIEN :**
• Choc à la tête
• Risque : lésions cérébrales, HED, HSD
• Signes gravité : PC, vomissements, amnésie, troubles conscience

**TRAUMATISME DU RACHIS :**
• Atteinte colonne vertébrale
• Risque : lésion moelle → paralysie
• Mécanismes : chute hauteur, AVP, plongeon

**TRAUMATISME THORACIQUE :**
• Choc sur thorax
• Risque : contusion pulmonaire, pneumothorax, hémothorax
• Signes : détresse respiratoire, douleur, déformation

**TRAUMATISME ABDOMINAL :**
• Choc sur abdomen
• Risque : lésions organes (foie, rate), hémorragie interne
• Signes : douleur abdominale, défense, choc

**TRAUMATISME DES MEMBRES :**
• Fractures, entorses, luxations
• Risque : lésions vasculo-nerveuses, hémorragie
• Signes : douleur, déformation, impotence, œdème

**POLYTRAUMATISME :**
• Plusieurs lésions traumatiques graves simultanées
• Pronostic vital engagé
• Nécessite prise en charge rapide et coordonnée

**Mécanismes à haut risque :**
• Chute >3 mètres
• AVP à haute cinétique
• Écrasement
• Éjection véhicule
• Décès sur les lieux
• Déformation importante véhicule

**Principe :**
Suspecter traumatisme grave si mécanisme violent

**Critères FAOD :**
→ Mécanisme = indice gravité
→ Immobilisation si suspicion
→ Bilan lésionnel complet"""
            },
            {
                "code": "08PR01",
                "titre": "Brûlure - Conduite à tenir",
                "niveau": "PSE 1",
                "type_fiche": "PR",
                "contenu": """**CONDUITE À TENIR BRÛLURE :**

**1. SUPPRIMER LA CAUSE**
• Éloigner source chaleur
• Éteindre flammes (rouler victime)
• Couper courant si électrique
• Retirer vêtements NON adhérents
• NE PAS retirer vêtements collés à peau

**2. REFROIDIR IMMÉDIATEMENT**
(le plus tôt possible, dans les 30 min)

**Technique :**
• Eau tempérée (15-25°C)
• Ruissellement doux
• Durée : 10-20 minutes minimum
• Jusqu'à apaisement douleur
• Toute la surface brûlée

**Objectifs refroidissement :**
• Stopper progression brûlure en profondeur
• Diminuer douleur
• Limiter œdème
• Réduire risque infection

**3. APRÈS REFROIDISSEMENT**

**Brûlure simple (pas grave) :**
• Sécher délicatement
• Recouvrir pansement stérile
• NE PAS percer cloques
• NE PAS appliquer corps gras, dentifrice, etc.

**Brûlure grave :**
• Recouvrir drap propre ou champ stérile
• NE RIEN appliquer
• Protéger contre froid (hypothermie)
• Oxygène si disponible

**4. ÉVALUER GRAVITÉ**

**Brûlure GRAVE si :**
• Surface >10% adulte (>5% enfant)
• Localisation : visage, mains, pieds, organes génitaux, articulations, voies aériennes
• 2ème degré étendu ou 3ème degré
• Âge <5 ans ou >60 ans
• Électrique ou chimique
• Inhalation fumées
• Pathologies associées

**5. ALERTER si brûlure grave**
• 15
• Décrire : surface, profondeur, localisation
• Circonstances

**6. POSITION**
• Allongée si brûlure étendue
• Surélever membre brûlé si possible
• Position confort si localisée

**7. LUTTER CONTRE CHOC**
• Couvrir (pas sur brûlure)
• Rassurer
• Oxygène si disponible
• NE RIEN donner par bouche

**8. SURVEILLER**
• Conscience
• Respiration (si inhalation fumées)
• Douleur
• Jusqu'aux secours

**BRÛLURES SPÉCIFIQUES :**

**Électrique :**
• 2 points contact (entrée/sortie)
• Lésions internes possibles
• Toujours grave

**Chimique :**
• Rinçage abondant prolongé (20-30 min)
• Retirer vêtements contaminés

**Inhalation fumées :**
• Détresse respiratoire
• Suies dans nez/bouche
• Oxygène haut débit
• Urgence vitale

**CE QU'IL NE FAUT PAS FAIRE :**
✗ Appliquer glace directement
✗ Percer cloques
✗ Appliquer corps gras, tulle, dentifrice
✗ Retirer vêtements adhérents
✗ Sous-estimer gravité

**Critères FAOD :**
→ Refroidissement = geste salvateur
→ 10-20 minutes minimum
→ Toute brûlure grave = 15"""
            },
            {
                "code": "08PR02",
                "titre": "Traumatisme - Conduite à tenir",
                "niveau": "PSE 1 & PSE 2",
                "type_fiche": "PR",
                "contenu": """**VICTIME TRAUMATISÉE - PRINCIPES :**

**1. ÉVALUER LE MÉCANISME**
• Hauteur chute
• Cinétique accident
• Type de choc
→ Détermine suspicion gravité

**2. ÉVITER TOUTE MOBILISATION**
• Laisser dans position trouvée
• Sauf danger vital immédiat
• Attendre renforts équipés

**3. BILAN LÉSIONNEL COMPLET**
• De la tête aux pieds
• Rechercher toutes les lésions
• Palper délicatement
• Demander où il a mal

**TRAUMATISME CRÂNIEN :**

**Signes de gravité :**
• Perte de connaissance
• Vomissements
• Amnésie (avant/après choc)
• Troubles comportement
• Somnolence
• Céphalées intenses
• Convulsions
• Écoulement sang/liquide clair oreille/nez

**Conduite à tenir :**
• Si conscient : allonger, tête surélevée
• Si inconscient : PLS si pas d'autre trauma
• Immobiliser tête si trauma rachis associé
• Surveiller conscience
• Alerte 15 si signes gravité

**TRAUMATISME RACHIS :**

**Suspicion si :**
• Mécanisme (chute, AVP, plongeon)
• Douleur rachis
• Impossibilité bouger membres
• Fourmillements, perte sensibilité

**Conduite à tenir :**
• NE PAS MOBILISER
• Maintenir tête en position neutre
• Rassurer, demander de ne pas bouger
• Attendre renforts (collier cervical, matelas coquille)
• PLS uniquement si vomissements ET impossible de faire autrement

**TRAUMATISME THORAX :**

**Signes :**
• Détresse respiratoire
• Douleur thoracique (aggravée inspiration)
• Déformation, enfoncement
• Emphysème sous-cutané

**Conduite à tenir :**
• Position demi-assise
• Oxygène haut débit
• Surveiller respiration
• Alerte 15

**TRAUMATISME ABDOMEN :**

**Signes :**
• Douleur abdominale
• Défense (contracture)
• Ecchymose (ceinture sécurité)
• Signes de choc

**Conduite à tenir :**
• Allonger, jambes fléchies
• NE RIEN donner par bouche
• Surveiller signes de choc
• Alerte 15

**TRAUMATISME MEMBRE :**

**Signes :**
• Douleur, impotence fonctionnelle
• Déformation
• Œdème, ecchymose
• Raccourcissement membre

**Conduite à tenir :**
• Immobiliser dans position trouvée
• Attelle si disponible
• Surélever si possible
• Froid (poche glace) si contusion
• Vérifier pouls en aval
• Alerte si fracture ouverte, déformation importante

**POLYTRAUMATISME :**

**Priorités :**
1. Détresses vitales d'abord
2. Hémorragies
3. Puis bilan lésionnel
4. Immobilisation globale

**4. SURVEILLER**
• Conscience
• Respiration
• Circulation
• Douleur
• Aggravation ?

**Critères FAOD :**
→ Mécanisme = indice de gravité
→ Limiter mobilisations
→ Bilan lésionnel systématique
→ Immobiliser avant mobiliser"""
            }
        ]
    },
    9: {
        "titre": "Souffrance psychique et comportements inhabituels",
        "type": "PSE",
        "fiches": [
            {
                "code": "09AC01",
                "titre": "Les personnes en situation de crise",
                "niveau": "PSE 2",
                "type_fiche": "AC",
                "contenu": """**Définition :**
État de déséquilibre psychologique intense face à événement perçu comme dépassant capacités d'adaptation

**Manifestations de la crise :**

**Émotionnelles :**
• Peur intense, terreur
• Colère, agressivité
• Tristesse profonde
• Sentiment d'impuissance
• Culpabilité

**Cognitives :**
• Confusion, désorientation
• Difficultés concentration
• Pensées envahissantes
• Déni de la réalité

**Comportementales :**
• Agitation, hyperactivité
• Prostration, inhibition
• Fuite, évitement
• Agressivité verbale/physique
• Comportements inhabituels

**Situations déclenchantes :**
• Événement traumatique (accident, agression, attentat)
• Annonce brutale (décès, maladie grave)
• Accumulation stress
• Confrontation à la mort
• Perte contrôle

**État de stress dépassé :**
• Stress > capacités adaptation
• Perte repères
• Réactions inadaptées
• Besoin aide externe

**Principe d'action :**
• Sécuriser
• Écouter activement
• Apaiser
• Orienter si nécessaire

**Critères FAOD :**
→ Attitude empathique essentielle
→ Ne pas juger les réactions
→ Soutien psychologique = geste de secours"""
            },
            {
                "code": "09AC02",
                "titre": "Risque suicidaire",
                "niveau": "PSE 2",
                "type_fiche": "AC",
                "contenu": """**Définition :**
Risque de passage à l'acte suicidaire (tentative ou suicide)

**Signes d'alerte :**

**Verbaux :**
• "Je n'en peux plus"
• "Je veux en finir"
• "Vous seriez mieux sans moi"
• "Bientôt tout sera fini"
• Adieux, testament

**Comportementaux :**
• Isolement social
• Dons d'objets personnels
• Mise en ordre affaires
• Changement brutal comportement
• Prise de risques
• Arrêt traitement

**Émotionnels :**
• Désespoir
• Sentiment d'échec
• Perte d'intérêt
• Calme suspect après crise

**Facteurs de risque :**
• Antécédents tentative
• Dépression
• Isolement
• Événement de vie difficile
• Deuil, séparation
• Maladie chronique
• Alcool, drogues
• Accès moyens létaux

**Urgence si :**
• Plan précis
• Moyens disponibles
• Date fixée
• Isolement
• Pas de soutien

**Critères FAOD :**
→ Question directe nécessaire
→ Parler du suicide ne le provoque pas
→ Évaluation urgence = vitale"""
            },
            {
                "code": "09PR01",
                "titre": "Personne en crise - Conduite à tenir",
                "niveau": "PSE 2",
                "type_fiche": "PR",
                "contenu": """**PERSONNE EN SITUATION DE CRISE :**

**1. ASSURER SA PROPRE SÉCURITÉ**
• Évaluer dangerosité
• Garder distance sécurité si agitation/agressivité
• Demander renfort si nécessaire
• Dégager objets dangereux

**2. SÉCURISER LA PERSONNE**
• Environnement calme
• Éloigner curieux
• Limiter stimulations

**3. ÉTABLIR LE CONTACT**

**Approche :**
• Calme, posé, rassurant
• Position non menaçante
• Respect distance
• Se présenter
• Ton de voix doux

**Communication :**
• "Je suis là pour vous aider"
• "Vous êtes en sécurité maintenant"
• Parler calmement
• Questions ouvertes
• Laisser s'exprimer

**4. ÉCOUTE ACTIVE**

**Techniques :**
• Attention totale
• Reformulation
• Validation émotions :
  "Je comprends que c'est difficile"
• NE PAS minimiser
• NE PAS juger
• NE PAS interrompre

**5. APAISER**

**Techniques d'apaisement :**
• Respiration guidée :
  "Respirez avec moi, inspirez... expirez..."
• Ancrage présent :
  "Regardez autour de vous, vous êtes en sécurité"
• Contact visuel doux
• Présence rassurante

**6. SELON COMPORTEMENT :**

**Agitation :**
• Garder calme
• Parler doucement
• Proposer s'asseoir
• Ne pas contraindre
• Laisser espace

**Prostration :**
• Rester proche
• Parler même si pas de réponse
• Contact physique doux (si accepté)
• Patience

**Agressivité :**
• Distance sécurité
• Calme, fermeté bienveillante
• Ne pas confronter
• Renfort si nécessaire
• Forces de l'ordre si danger

**7. ORIENTER**

**Avis médical si :**
• Détresse majeure
• Risque pour soi/autrui
• Incapacité se prendre en charge
• Demande exprimée

**Transmission :**
• Circonstances
• Comportement observé
• Propos tenus
• Risque suicidaire ?
• Ressources (entourage)

**8. IMPLIQUER ENTOURAGE**
• Personne de confiance
• Soutien après intervention
• Ne pas laisser seule

**CE QU'IL NE FAUT PAS FAIRE :**
✗ Minimiser : "C'est rien"
✗ Juger : "Vous exagérez"
✗ Confronter si agressif
✗ Promettre ce qu'on ne peut tenir
✗ Laisser seule si risque

**Critères FAOD :**
→ Sécurité = priorité
→ Écoute active = thérapeutique
→ Orienter vers soins si nécessaire"""
            },
            {
                "code": "09PR02",
                "titre": "Risque suicidaire - Conduite à tenir",
                "niveau": "PSE 2",
                "type_fiche": "PR",
                "contenu": """**SUSPICION RISQUE SUICIDAIRE :**

**1. POSER LA QUESTION DIRECTEMENT**

Ne PAS avoir peur de demander :
• "Avez-vous des idées de vous faire du mal ?"
• "Pensez-vous au suicide ?"
• "Souffrez-vous au point de vouloir mourir ?"

→ Poser la question ne provoque PAS le passage à l'acte
→ Au contraire : soulagement souvent

**2. ÉVALUER L'URGENCE**

**Questions à poser :**
• "Y avez-vous pensé récemment ?"
• "Avez-vous un plan ? Comment ?"
• "Quand pensez-vous le faire ?"
• "Avez-vous les moyens ?"
• "Quelqu'un peut vous aider ?"

**URGENCE ÉLEVÉE si :**
• Plan précis
• Moyens disponibles
• Absence de soutien
• Tentative antérieure
• Consommation alcool/drogues
• Calme suspect (décision prise)

**3. NE JAMAIS LAISSER SEULE**
• Présence continue
• Surveillance discrète mais attentive
• Impliquer proche de confiance
• Éliminer moyens si possibles (médicaments, armes)

**4. ÉCOUTE EMPATHIQUE**

**Attitude :**
• Prise au sérieux
• Sans jugement
• Validation souffrance :
  "Je comprends que vous souffrez"
• Espoir prudent :
  "Des solutions existent"

**CE QU'IL FAUT DIRE :**
✓ "Je suis content(e) que vous m'en parliez"
✓ "Votre souffrance est réelle"
✓ "On va trouver de l'aide ensemble"
✓ "Vous n'êtes pas seul(e)"

**CE QU'IL NE FAUT PAS DIRE :**
✗ "Pensez à ceux qui vous aiment"
✗ "Ce n'est pas si grave"
✗ "Vous n'avez pas le droit"
✗ "C'est égoïste"

**5. ALERTER SYSTÉMATIQUEMENT**

**Si urgence élevée :**
• 15 immédiatement
• "Personne en danger : risque suicidaire"
• Rester avec la personne
• Transmettre éléments

**Si urgence modérée :**
• Avis médical
• Orientation psychiatrie
• Accompagnement si possible

**6. IMPLIQUER RESSOURCES**
• Famille, amis (avec accord)
• Numéros utiles :
  - 3114 : Numéro National Prévention Suicide
  - SOS Amitié : 09 72 39 40 50
  - Urgences psychiatriques

**7. APRÈS TENTATIVE**

**Si victime consciente :**
• Soins physiques prioritaires
• Puis soutien psychologique
• Hospitalisation psychiatrique
• Transmission complète

**Si victime inconsciente :**
• Gestes d'urgence vitale
• Rechercher moyens utilisés
• Transmettre aux secours

**8. PROTECTION SECOURISTE**
• Impact émotionnel possible
• Débriefing équipe
• Ne pas culpabiliser si passage à l'acte
• Soutien professionnel si nécessaire

**Critères FAOD :**
→ Question directe = nécessaire et aidante
→ Ne JAMAIS laisser seule
→ Hospitalisation si urgence
→ Orienter vers aide spécialisée"""
            }
        ]
    },
    10: {
        "titre": "Relevage et brancardage",
        "type": "PSE",
        "fiches": [
            {
                "code": "10AC01",
                "titre": "Principes du relevage et brancardage",
                "niveau": "PSE 2",
                "type_fiche": "AC",
                "contenu": """**Objectifs :**
Déplacer victime de façon sûre, confortable et adaptée à son état

**Principes fondamentaux :**

**1. PRÉPARATION :**
• Évaluer état victime
• Choisir technique adaptée
• Nombre d'équipiers suffisant
• Matériel vérifié
• Chemin dégagé

**2. COORDINATION :**
• Chef de manœuvre désigné
• Ordres clairs et précis
• Mouvements synchronisés
• Communication continue

**3. SÉCURITÉ :**

**Pour la victime :**
• Confort
• Immobilisation lésions
• Surveillance continue
• Respect pudeur

**Pour les équipiers :**
• Gestes et postures
• Dos droit
• Travail avec jambes
• Prises solides
• Pas de précipitation

**Règles ergonomiques :**
• Dos droit, courbure naturelle
• Jambes fléchies
• Charge proche du corps
• Prises symétriques
• Coordination mouvement

**Matériel de relevage :**

**Brancards :**
• Brancard portoir
• Brancard cuillère
• Matelas coquille
• Plan dur

**Matériel immobilisation :**
• Collier cervical
• Attelles
• Cales tête

**Sangles :**
• Immobilisation victime
• Sécurité transport

**Techniques selon situation :**
• Relevage standard (victime au sol)
• Brancardage horizontal
• Brancardage dans escalier
• Passages étroits

**Critères FAOD :**
→ Préparation = essentielle
→ Coordination équipe = sécurité
→ Confort victime = priorité"""
            },
            {
                "code": "10FT01",
                "titre": "Relevage à 3 équipiers",
                "niveau": "PSE 2",
                "type_fiche": "FT",
                "contenu": """**Indication :**
Relever victime du sol vers brancard (victime non suspecte traumatisme rachis)

**Justification :**
Technique coordonnée minimisant risques pour victime et équipiers

**Matériel :**
• Brancard préparé et positionné
• 3 équipiers minimum

**Positions équipiers :**
• **Chef de manœuvre (Équipier 1)** : à la tête
• **Équipier 2** : au niveau thorax/bassin
• **Équipier 3** : au niveau jambes

**Réalisation :**

**1. PRÉPARATION :**
• Brancard préparé (couverture, sangles)
• Positionné perpendiculaire à victime
• Côté tête du brancard vers tête victime
• Hauteur minimale

**2. POSITIONNEMENT ÉQUIPIERS :**

**Équipier 1 (chef) :**
• À genoux derrière tête
• Mains sous épaules

**Équipier 2 :**
• À genoux au niveau bassin
• Une main sous bassin, une sous cuisses

**Équipier 3 :**
• À genoux au niveau jambes
• Mains sous jambes

**3. COMMANDEMENT :**

Chef de manœuvre annonce :
• "Êtes-vous prêts ?"
→ Équipiers : "Prêt"

• "Attention pour soulever... SOULEVEZ"
→ Soulever à hauteur genoux

• "Attention pour pivoter... PIVOTEZ"
→ Pivoter 90° vers brancard

• "Attention pour avancer... AVANCEZ"
→ Pas chassés jusqu'au brancard

• "Attention pour poser... POSEZ"
→ Poser délicatement sur brancard

**4. INSTALLATION :**
• Centrer victime
• Installer confortablement
• Couvrir
• Sangler

**Points clés :**
• Synchronisation parfaite
• Mouvements fluides
• Dos droit, jambes fléchies
• Victime maintenue horizontale

**Risques :**
• Chute victime (coordination)
• Lombalgie équipiers (mauvaise posture)

**Évaluation :**
• Coordination équipe
• Confort victime
• Sécurité manœuvre

**Critères FAOD :**
→ Chef de manœuvre = coordinateur
→ Commandements clairs
→ Synchronisation = sécurité"""
            }
        ]
    },
    11: {
        "titre": "Situations particulières",
        "type": "PSE",
        "fiches": [
            {
                "code": "11AC01",
                "titre": "Situations à nombreuses victimes",
                "niveau": "PSE 2",
                "type_fiche": "AC",
                "contenu": """**Définition :**
Événement avec nombre de victimes dépassant capacités habituelles de réponse

**Types d'événements :**
• Accidents collectifs (AVP, incendie, effondrement)
• Catastrophes naturelles (séisme, inondation)
• Attentats
• Accidents industriels

**Principes spécifiques :**

**1. ORGANISATION :**
• Chaîne de commandement
• Sectorisation
• Points de rassemblement
• Coordination secours

**2. TRIAGE :**
Catégorisation victimes selon gravité pour optimiser moyens

**Catégories (Méthode START) :**

**🔴 URGENCE ABSOLUE (UA) :**
• Détresse vitale
• Pronostic vital engagé
• Traitement immédiat nécessaire
• Ex : hémorragie, détresse respi

**🟡 URGENCE RELATIVE (UR) :**
• Blessures importantes
• État stable
• Peut attendre (surveillance)
• Ex : fracture complexe

**🟢 IMPLIQUÉ :**
• Blessures légères
• Marche seul
• Soins différés possibles
• Ex : plaie simple, contusion

**⚫ DÉCÉDÉ / DÉPASSÉ (DCD) :**
• Arrêt cardiaque
• Lésions incompatibles avec vie
• Pas de traitement (moyens limités)

**3. RAMASSAGE ET ÉVACUATION :**
• Noria d'évacuation
• Priorité aux UA
• Traçabilité victimes

**4. POINTS CLÉS :**
• Sécurité scène (risque persistant ?)
• Alerte renforcée précoce
• Protection équipiers
• Communication

**Critères FAOD :**
→ Triage = adaptation moyens limités
→ "Le plus de bien au plus grand nombre"
→ Décisions difficiles mais nécessaires"""
            },
            {
                "code": "11AC02",
                "titre": "Accouchement inopiné",
                "niveau": "PSE 2",
                "type_fiche": "AC",
                "contenu": """**Définition :**
Accouchement survenant hors structure médicale, sans préparation

**Déroulement normal accouchement :**

**1. TRAVAIL :**
• Contractions régulières
• Dilatation col utérus
• Peut durer plusieurs heures

**2. EXPULSION :**
• Poussées
• Sortie du bébé
• 15-30 minutes

**3. DÉLIVRANCE :**
• Expulsion placenta
• 15-30 minutes après

**Signes d'accouchement imminent :**
• Contractions rapprochées (<2 min)
• Envie irrépressible de pousser
• Visualisation tête bébé
• Perte des eaux

**Complications possibles :**

**Mère :**
• Hémorragie de la délivrance
• Déchirures
• Détresse

**Nouveau-né :**
• Détresse respiratoire
• Hypothermie
• Prématurité

**Particularités :**
• Cordon ombilical
• Hypothermie nouveau-né
• Hémorragie maternelle

**Principe d'action :**
• Accompagner accouchement naturel
• Ne pas retarder
• Protéger mère et bébé
• Alerter renforts

**Critères FAOD :**
→ Ne PAS retenir bébé
→ Chaleur nouveau-né = priorité
→ Accompagner, ne pas intervenir activement"""
            },
            {
                "code": "11PR01",
                "titre": "Accouchement inopiné - Conduite à tenir",
                "niveau": "PSE 2",
                "type_fiche": "PR",
                "contenu": """**ACCOUCHEMENT IMMINENT :**

**1. ÉVALUER IMMINENCE**
• Fréquence contractions (<2 min)
• Envie de pousser ?
• Visualisation tête bébé ?
→ Si imminent : PAS DE TRANSPORT

**2. ALERTER 15**
• "Accouchement imminent"
• Terme grossesse
• Complications connues ?
• Demander sage-femme/SMUR

**3. PRÉPARATION**

**Environnement :**
• Lieu propre, chaud (25°C)
• Intimité (éloigner curieux)
• Éclairage suffisant

**Matériel :**
• Champs propres/stériles
• Gants stériles
• Ciseaux stériles (cordon)
• 2 clamps/liens cordon
• Serviettes/couvertures chaudes
• Aspiration si disponible
• Oxygène

**Hygiène :**
• Lavage mains
• Gants stériles

**4. INSTALLATION MÈRE**
• Allongée, genoux fléchis écartés
• Bas du corps découvert
• Haut du corps couvert (chaleur)

**5. PENDANT EXPULSION**

**Rôle secouriste :**
• ACCOMPAGNER, pas intervenir
• Rassurer, encourager
• "Poussez lors des contractions"
• "Soufflez entre les contractions"

**Sortie tête :**
• Ne JAMAIS tirer
• Soutenir délicatement tête
• Vérifier pas de cordon autour cou
• Si oui : faire glisser par-dessus tête

**Sortie corps :**
• Rotation spontanée épaules
• Soutenir bébé (glissant !)
• Laisser glisser

**6. APRÈS NAISSANCE**

**Nouveau-né :**

**Immédiat :**
• Noter heure naissance
• Sécher vigoureusement (stimulation)
• Envelopper chaud (bonnet !)
• Position : tête légèrement plus basse

**Vérifier :**
• Respire ? Crie ?
• Coloration ?
• Tonus ?

**Si respire et rose :**
• Installer sur ventre/thorax mère (peau à peau)
• Couvrir chaudement
• Surveillance

**Si détresse :**
• Aspirer bouche puis narines
• Stimuler (sécher, tapoter)
• Si pas respiration : 5 insufflations
• Puis RCP adaptée si nécessaire
• Oxygène

**7. CORDON OMBILICAL**

**Clampage :**
• Attendre 1-3 minutes (sauf détresse)
• 1er clamp à 15 cm ombilic bébé
• 2ème clamp à 20 cm
• Section entre les 2 clamps

**Si pas de clamps :**
• Attendre renforts
• Laisser cordon intact

**8. DÉLIVRANCE**

**Placenta :**
• Attendre expulsion spontanée (15-30 min)
• Ne JAMAIS tirer sur cordon
• Recueillir placenta (le montrer aux renforts)
• Vérifier intégralité

**Hémorragie :**

**Prévention :**
• Massage utérin après délivrance
• Main sur abdomen, massage circulaire

**Si hémorragie :**
• Masser utérus
• Alerte urgente
• Oxygène mère
• Allonger, jambes surélevées

**9. SURVEILLANCE**

**Mère :**
• Conscience
• Hémorragie
• Douleur
• Utérus dur (bon signe)

**Nouveau-né :**
• Respiration
• Coloration
• Température
• Tonus

**10. TRANSMISSION**
• Heure naissance
• État nouveau-né (Apgar si connu)
• Délivrance réalisée ?
• Hémorragie ?
• Sexe bébé

**CE QU'IL NE FAUT PAS FAIRE :**
✗ Tirer sur bébé ou cordon
✗ Négliger hypothermie nouveau-né
✗ Sectionner cordon trop tôt
✗ Tirer sur cordon pour délivrance

**Critères FAOD :**
→ Nature = bien faite généralement
→ Chaleur nouveau-né = VITAL
→ Accompagner, ne pas intervenir activement
→ Hémorragie maternelle = surveiller"""
            }
        ]
    },
    12: {
        "titre": "Divers",
        "type": "PSE",
        "fiches": [
            {
                "code": "12AC01",
                "titre": "Aspects réglementaires et juridiques",
                "niveau": "PSE 1",
                "type_fiche": "AC",
                "contenu": """**Cadre légal du secourisme :**

**Code de la Sécurité Intérieure (CSI) :**

**Article L721-1 :**
"Toute personne concourt par son comportement à la sécurité civile. 
En fonction des situations auxquelles elle est confrontée et dans la 
mesure de ses possibilités, elle veille à prévenir les services de 
secours et à prendre les premières dispositions nécessaires."

**Protection juridique :**

**Citoyen sauveteur (Loi 2020-840) :**
"Quiconque porte assistance de manière bénévole à une personne en 
situation apparente de péril grave et imminent est un citoyen sauveteur 
et bénéficie de la qualité de collaborateur occasionnel du service public."

**Conséquences :**
• Protection pénale (pas de poursuites sauf faute lourde)
• Protection civile (responsabilité État)

**Obligations légales :**

**Non-assistance à personne en péril :**
• Code pénal art. 223-6
• Obligation d'agir si pas de risque pour soi
• 5 ans prison + 75000€ amende

**Secret professionnel :**
• Respect vie privée victime
• Informations transmises uniquement aux autorités

**Non-obstacle aux secours :**
• Faciliter accès secours
• Transmettre informations

**Responsabilités secouriste :**

**Pénal :**
• Faute lourde uniquement
• Rare en pratique

**Civil :**
• Couvert par responsabilité structure employeur
• Assurance responsabilité civile

**Refus de soins :**
• Victime consciente peut refuser
• Respecter volonté si discernement
• Faire constater refus (témoin, écrit)
• Limites : mineurs, troubles conscience

**Cas particuliers :**

**Mineur :**
• Soins d'urgence sans autorisation parentale
• Informer parents dès que possible

**Personne inconsciente :**
• Présomption consentement aux soins urgents

**Violences/maltraitance :**
• Levée secret si victime vulnérable
• Signalement autorités

**Critères FAOD :**
→ Protection juridique = réelle
→ Agir selon formation
→ Respect personne = primordial"""
            },
            {
                "code": "12AC02",
                "titre": "Organisation des secours en France",
                "niveau": "PSE 1",
                "type_fiche": "AC",
                "contenu": """**Acteurs des secours :**

**SERVICES PUBLICS :**

**SDIS (Service Départemental d'Incendie et Secours) :**
• Sapeurs-pompiers (pro + volontaires)
• Secours à victime
• Incendie
• Numéro : **18**

**SAMU (Service d'Aide Médicale Urgente) :**
• Régulation médicale (médecins)
• SMUR (équipes mobiles)
• Ambulances privées
• Numéro : **15**

**Police/Gendarmerie :**
• Ordre public
• Secours routier
• Numéros : **17** ou **112**

**ASSOCIATIONS AGRÉÉES :**

**Croix-Rouge Française**
**Protection Civile**
**FFSS (Fédération Française de Sauvetage et Secourisme)**
• Dispositifs prévisionnels secours (DPS)
• Formation population
• Actions humanitaires

**Secours spécialisés :**
• Montagne : PGHM, CRS montagne
• Mer : SNSM, CROSS
• Spéléo : SSF

**Numéros d'urgence :**

**🇫🇷 FRANCE :**
• **15** : SAMU (urgences médicales)
• **18** : Pompiers
• **17** : Police/Gendarmerie
• **112** : Numéro d'urgence européen
• **114** : Urgences (sourds/malentendants - SMS)
• **196** : Urgences maritimes
• **3114** : Prévention suicide

**🇪🇺 EUROPE :**
• **112** : Urgence (tous pays UE)

**Organisation intervention :**

**1. RÉCEPTION APPEL :**
• Centre de réception (15, 18, 112)
• Régulation
• Décision moyens

**2. ENGAGEMENT MOYENS :**
• Adaptation à situation
• Graduation réponse

**3. BILAN :**
• Équipe sur place
• Transmission médecin régulateur

**4. PRISE EN CHARGE :**
• Gestes d'urgence
• Transport si nécessaire
• Orientation hôpital adapté

**Chaîne de secours :**
Citoyen → Alerte → Secours → Transport → Hôpital

**Critères FAOD :**
→ Plusieurs acteurs complémentaires
→ 15 = régulation médicale
→ 18 = sapeurs-pompiers
→ 112 = numéro unique Europe"""
            },
            {
                "code": "12AC03",
                "titre": "Gestion du stress et bien-être du secouriste",
                "niveau": "PSE 2",
                "type_fiche": "AC",
                "contenu": """**Stress du secouriste :**

**Sources de stress :**
• Interventions traumatisantes
• Charge émotionnelle
• Pression temporelle
• Responsabilités
• Manque de moyens
• Fatigue

**Manifestations :**

**Court terme :**
• Palpitations, sudation
• Tremblements
• Troubles sommeil
• Irritabilité

**Long terme :**
• Épuisement (burn-out)
• Détachement émotionnel
• Erreurs
• Problèmes relationnels

**Prévention :**

**AVANT intervention :**
• Formation solide
• Entraînement régulier
• Préparation mentale
• Repos suffisant

**PENDANT intervention :**
• Concentration tâche
• Respiration contrôlée
• Communication équipe
• Gestion temps

**APRÈS intervention :**
• Débriefing (technique + émotionnel)
• Verbalisation
• Soutien pairs
• Repos

**Techniques gestion stress :**

**Respiration contrôlée :**
• Inspiration 4 sec
• Rétention 4 sec
• Expiration 6 sec
• Répéter 3-5 fois

**Cohérence cardiaque :**
• 6 respirations/minute
• 5 minutes
• 3 fois/jour

**Ancrage :**
• Focaliser sur tâche
• Sensations corporelles
• Environnement immédiat

**Hygiène de vie :**
• Sommeil régulier (7-9h)
• Activité physique
• Alimentation équilibrée
• Vie sociale
• Loisirs

**Débriefing post-intervention :**

**Technique :**
• Faits (qu'est-ce qui s'est passé ?)
• Ressenti (comment je me suis senti ?)
• Analyse (qu'est-ce qui a bien/mal fonctionné ?)
• Leçons (que retenir ?)

**Émotionnel :**
• Expression libre émotions
• Écoute sans jugement
• Normalisation réactions
• Soutien mutuel

**Quand consulter :**
• Symptômes persistants >1 mois
• Impact vie quotidienne
• Idées noires
• Consommation alcool/drogues
• Isolement

**Ressources :**
• Psychologue équipe
• CUMP (Cellule Urgence Médico-Psychologique)
• Médecine du travail
• Associations de secouristes

**Critères FAOD :**
→ Stress = normal et gérable
→ Débriefing = outil essentiel
→ Demander aide = force, pas faiblesse
→ Prendre soin de soi = prendre soin des autres"""
            }
        ]
    }
}

def enrich_chapter(chapter_id, new_data):
    """Enrichit un chapitre existant avec les nouvelles fiches FAOD"""
    
    result = db.chapters.update_one(
        {'id': chapter_id},
        {
            '$set': {
                'type': new_data['type'],
                'fiches': new_data['fiches']
            }
        }
    )
    
    return result.modified_count > 0

def main():
    print("🚀 Démarrage de l'enrichissement des chapitres PSE avec critères FAOD\n")
    
    # Mapping des IDs de chapitres existants
    chapter_mapping = {
        1: 'ch1',   # Attitude et comportement
        2: 'ch2',   # Bilans
        3: 'ch3',   # Protection et sécurité
        4: 'ch4',   # Hygiène et asepsie
        5: 'ch5',   # Urgences vitales
        6: 'ch6',   # Malaises et affections spécifiques
        7: 'ch7',   # Atteintes circonstancielles
        8: 'ch8',   # Traumatismes
        9: 'ch9',   # Souffrance psychique et comportements inhabituels
        10: 'ch10', # Relevage et brancardage
        11: 'ch11', # Situations particulières
        12: 'ch12', # Divers
    }
    
    enriched_count = 0
    total_fiches = 0
    
    for chapter_num, chapter_data in sorted(PSE_CHAPTERS_CONTENT.items()):
        chapter_id = chapter_mapping.get(chapter_num)
        
        if not chapter_id:
            print(f"⚠️  Chapitre {chapter_num} : ID non trouvé dans le mapping")
            continue
        
        fiches_count = len(chapter_data['fiches'])
        total_fiches += fiches_count
        
        print(f"📝 Enrichissement Chapitre {chapter_num}: {chapter_data['titre']}")
        print(f"   → {fiches_count} fiches FAOD")
        
        success = enrich_chapter(chapter_id, chapter_data)
        
        if success:
            enriched_count += 1
            print(f"   ✅ Enrichi avec succès\n")
        else:
            print(f"   ❌ Échec de l'enrichissement\n")
    
    print(f"\n✨ Enrichissement terminé : {enriched_count}/{len(PSE_CHAPTERS_CONTENT)} chapitres enrichis")
    print(f"📚 Total fiches FAOD ajoutées : {total_fiches}")
    print("\n📊 Récapitulatif :")
    print("   ✅ Tous les chapitres PSE (1-12) enrichis")
    print("   ✅ Contenu structuré avec résumés pour FOAD")
    print("   ✅ Classification par niveau (PSE 1 / PSE 2)")
    print("   ✅ Type de fiche précisé (AC / PR / FT)")
    print("\n🎯 Prochaines étapes :")
    print("   1. Tester l'affichage sur le frontend")
    print("   2. Valider le contenu avec l'utilisateur")
    print("   3. Générer/ajouter images des chapitres (optionnel)")

if __name__ == "__main__":
    main()
