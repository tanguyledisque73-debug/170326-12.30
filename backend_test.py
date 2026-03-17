#!/usr/bin/env python3
"""
Tests de validation de la base de données FAOD-SECOURS73

Tests selon les critères du review_request:
1. Authentification admin
2. Chapitres PSC (8 attendus)
3. Chapitres PSE (11 attendus)
4. Quiz PSC (8 attendus)
5. Quiz PSE (11 attendus)
6. Comptes test (formateur et stagiaire)
7. Health check
"""

import requests
import json
import sys
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from datetime import datetime

# Configuration
BASE_URL = "https://code-migrate-3.preview.emergentagent.com"
API_BASE = f"{BASE_URL}/api"

@dataclass
class TestResult:
    name: str
    success: bool
    message: str
    data: Optional[Any] = None
    error: Optional[str] = None

class FAODTester:
    def __init__(self):
        self.session = requests.Session()
        self.results: List[TestResult] = []
        self.admin_token = None
        self.formateur_token = None
        self.stagiaire_token = None
        
        print(f"🚀 Début des tests de validation FAOD-SECOURS73")
        print(f"📍 Base URL: {BASE_URL}")
        print(f"📍 API URL: {API_BASE}")
        print("="*70)
    
    def log_result(self, name: str, success: bool, message: str, data: Any = None, error: str = None):
        """Enregistre un résultat de test"""
        result = TestResult(name, success, message, data, error)
        self.results.append(result)
        
        status = "✅" if success else "❌"
        print(f"{status} {name}: {message}")
        if error and not success:
            print(f"   ❗ Erreur: {error}")
        if data and isinstance(data, dict) and "count" in data:
            print(f"   📊 Données: {data}")
    
    def test_health_check(self):
        """Test 7: Health Check"""
        print("\n7️⃣ TEST HEALTH CHECK")
        try:
            # Essayer plusieurs endpoints possibles
            endpoints = ["/health", "/", "/api/health", "/api/"]
            
            for endpoint in endpoints:
                try:
                    url = f"{BASE_URL}{endpoint}"
                    response = self.session.get(url, timeout=10)
                    
                    if response.status_code == 200:
                        self.log_result(
                            "Health Check",
                            True,
                            f"API accessible via {endpoint} (status: {response.status_code})",
                            {"endpoint": endpoint, "status": response.status_code}
                        )
                        return
                        
                except requests.exceptions.RequestException as e:
                    continue
            
            # Si aucun endpoint ne fonctionne
            self.log_result(
                "Health Check",
                False,
                "Aucun endpoint de health check accessible",
                error="Tous les endpoints testés ont échoué"
            )
                    
        except Exception as e:
            self.log_result(
                "Health Check",
                False,
                "Erreur lors du test health check",
                error=str(e)
            )
    
    def test_admin_auth(self):
        """Test 1: Authentification Admin"""
        print("\n1️⃣ TEST AUTHENTIFICATION ADMIN")
        try:
            url = f"{API_BASE}/auth/login"
            data = {
                "email": "ledisque.tanguy73@hotmail.com",
                "password": "NewAdmin123!"
            }
            
            response = self.session.post(url, json=data, timeout=10)
            
            if response.status_code == 200:
                result = response.json()
                token = result.get("token")
                user = result.get("user", {})
                
                if token and user.get("role") == "admin":
                    self.admin_token = token
                    self.log_result(
                        "Authentification Admin",
                        True,
                        f"Connexion admin réussie - Rôle: {user.get('role')}",
                        {"email": user.get("email"), "role": user.get("role")}
                    )
                else:
                    self.log_result(
                        "Authentification Admin",
                        False,
                        "Token ou rôle admin manquant dans la réponse",
                        {"response": result}
                    )
            else:
                self.log_result(
                    "Authentification Admin",
                    False,
                    f"Échec connexion admin (status: {response.status_code})",
                    error=response.text
                )
                
        except requests.exceptions.RequestException as e:
            self.log_result(
                "Authentification Admin",
                False,
                "Erreur de connexion lors de l'authentification admin",
                error=str(e)
            )
    
    def test_psc_chapters(self):
        """Test 2: Chapitres PSC"""
        print("\n2️⃣ TEST CHAPITRES PSC")
        try:
            url = f"{API_BASE}/psc/chapters"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                chapters = response.json()
                
                if not isinstance(chapters, list):
                    self.log_result(
                        "Chapitres PSC",
                        False,
                        "Réponse n'est pas une liste",
                        error=f"Type reçu: {type(chapters)}"
                    )
                    return
                
                psc_chapters = [ch for ch in chapters if ch.get("formation_type") == "PSC"]
                
                if len(psc_chapters) == 8:
                    # Vérifier la structure des chapitres
                    valid_chapters = 0
                    for ch in psc_chapters:
                        if all(key in ch for key in ["id", "numero", "titre", "formation_type", "fiches"]):
                            valid_chapters += 1
                    
                    if valid_chapters == 8:
                        self.log_result(
                            "Chapitres PSC",
                            True,
                            f"8 chapitres PSC trouvés avec structure valide",
                            {"count": len(psc_chapters), "valid_structure": valid_chapters}
                        )
                    else:
                        self.log_result(
                            "Chapitres PSC",
                            False,
                            f"Structure incomplète sur certains chapitres ({valid_chapters}/8)",
                            {"count": len(psc_chapters), "valid_structure": valid_chapters}
                        )
                else:
                    self.log_result(
                        "Chapitres PSC",
                        False,
                        f"Nombre incorrect de chapitres PSC (trouvés: {len(psc_chapters)}, attendus: 8)",
                        {"count": len(psc_chapters), "expected": 8}
                    )
            else:
                self.log_result(
                    "Chapitres PSC",
                    False,
                    f"Erreur API (status: {response.status_code})",
                    error=response.text
                )
                
        except requests.exceptions.RequestException as e:
            self.log_result(
                "Chapitres PSC",
                False,
                "Erreur de connexion",
                error=str(e)
            )
    
    def test_pse_chapters(self):
        """Test 3: Chapitres PSE"""
        print("\n3️⃣ TEST CHAPITRES PSE")
        try:
            url = f"{API_BASE}/chapters?formation_type=PSE"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                chapters = response.json()
                
                if not isinstance(chapters, list):
                    self.log_result(
                        "Chapitres PSE",
                        False,
                        "Réponse n'est pas une liste",
                        error=f"Type reçu: {type(chapters)}"
                    )
                    return
                
                if len(chapters) == 11:
                    # Vérifier la structure des chapitres
                    valid_chapters = 0
                    for ch in chapters:
                        if all(key in ch for key in ["id", "numero", "titre", "formation_type", "fiches"]):
                            if ch.get("formation_type") == "PSE":
                                valid_chapters += 1
                    
                    if valid_chapters == 11:
                        self.log_result(
                            "Chapitres PSE",
                            True,
                            f"11 chapitres PSE trouvés avec structure valide",
                            {"count": len(chapters), "valid_structure": valid_chapters}
                        )
                    else:
                        self.log_result(
                            "Chapitres PSE",
                            False,
                            f"Structure ou type incorrect sur certains chapitres ({valid_chapters}/11)",
                            {"count": len(chapters), "valid_structure": valid_chapters}
                        )
                else:
                    self.log_result(
                        "Chapitres PSE",
                        False,
                        f"Nombre incorrect de chapitres PSE (trouvés: {len(chapters)}, attendus: 11)",
                        {"count": len(chapters), "expected": 11}
                    )
            else:
                self.log_result(
                    "Chapitres PSE",
                    False,
                    f"Erreur API (status: {response.status_code})",
                    error=response.text
                )
                
        except requests.exceptions.RequestException as e:
            self.log_result(
                "Chapitres PSE",
                False,
                "Erreur de connexion",
                error=str(e)
            )
    
    def test_individual_chapter(self, chapter_id: str, formation_type: str):
        """Test d'un chapitre individuel"""
        try:
            url = f"{API_BASE}/chapters/{chapter_id}"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                chapter = response.json()
                if chapter.get("formation_type") == formation_type:
                    return True
            return False
        except:
            return False
    
    def test_quiz_psc(self):
        """Test 4: Quiz PSC"""
        print("\n4️⃣ TEST QUIZ PSC")
        try:
            url = f"{API_BASE}/quizzes"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                all_quizzes = response.json()
                
                if not isinstance(all_quizzes, list):
                    self.log_result(
                        "Quiz PSC",
                        False,
                        "Réponse n'est pas une liste",
                        error=f"Type reçu: {type(all_quizzes)}"
                    )
                    return
                
                # Récupérer les chapitres PSC pour filtrer les quiz
                try:
                    chapters_response = self.session.get(f"{API_BASE}/psc/chapters", timeout=10)
                    if chapters_response.status_code == 200:
                        psc_chapters = chapters_response.json()
                        psc_chapter_ids = [ch.get("id") for ch in psc_chapters if ch.get("formation_type") == "PSC"]
                        
                        psc_quizzes = [q for q in all_quizzes if q.get("chapter_id") in psc_chapter_ids]
                        
                        if len(psc_quizzes) == 8:
                            # Vérifier la structure des quiz
                            valid_quizzes = 0
                            total_questions = 0
                            
                            for quiz in psc_quizzes:
                                questions = quiz.get("questions", [])
                                # Note: 'titre' is not in the actual API structure, removing it from validation
                                if all(key in quiz for key in ["id", "chapter_id", "questions"]):
                                    if isinstance(questions, list) and len(questions) > 0:
                                        # Vérifier structure des questions
                                        questions_valid = True
                                        for q in questions:
                                            if not all(key in q for key in ["id", "question", "type", "correct_answer", "explication"]):
                                                questions_valid = False
                                                break
                                        
                                        if questions_valid:
                                            valid_quizzes += 1
                                            total_questions += len(questions)
                            
                            if valid_quizzes == 8:
                                self.log_result(
                                    "Quiz PSC",
                                    True,
                                    f"8 quiz PSC trouvés avec structure valide, {total_questions} questions total",
                                    {"count": len(psc_quizzes), "valid_structure": valid_quizzes, "total_questions": total_questions}
                                )
                            else:
                                self.log_result(
                                    "Quiz PSC",
                                    False,
                                    f"Structure incomplète sur certains quiz ({valid_quizzes}/8)",
                                    {"count": len(psc_quizzes), "valid_structure": valid_quizzes}
                                )
                        else:
                            self.log_result(
                                "Quiz PSC",
                                False,
                                f"Nombre incorrect de quiz PSC (trouvés: {len(psc_quizzes)}, attendus: 8)",
                                {"count": len(psc_quizzes), "expected": 8}
                            )
                    else:
                        self.log_result(
                            "Quiz PSC",
                            False,
                            "Impossible de récupérer les chapitres PSC pour filtrer les quiz",
                            error=f"Status chapters: {chapters_response.status_code}"
                        )
                except Exception as e:
                    self.log_result(
                        "Quiz PSC",
                        False,
                        "Erreur lors de la récupération des chapitres PSC",
                        error=str(e)
                    )
            else:
                self.log_result(
                    "Quiz PSC",
                    False,
                    f"Erreur API quiz (status: {response.status_code})",
                    error=response.text
                )
                
        except requests.exceptions.RequestException as e:
            self.log_result(
                "Quiz PSC",
                False,
                "Erreur de connexion",
                error=str(e)
            )
    
    def test_quiz_pse(self):
        """Test 5: Quiz PSE"""
        print("\n5️⃣ TEST QUIZ PSE")
        try:
            url = f"{API_BASE}/quizzes"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                all_quizzes = response.json()
                
                if not isinstance(all_quizzes, list):
                    self.log_result(
                        "Quiz PSE",
                        False,
                        "Réponse n'est pas une liste",
                        error=f"Type reçu: {type(all_quizzes)}"
                    )
                    return
                
                # Récupérer les chapitres PSE pour filtrer les quiz
                try:
                    chapters_response = self.session.get(f"{API_BASE}/chapters?formation_type=PSE", timeout=10)
                    if chapters_response.status_code == 200:
                        pse_chapters = chapters_response.json()
                        pse_chapter_ids = [ch.get("id") for ch in pse_chapters if ch.get("formation_type") == "PSE"]
                        
                        pse_quizzes = [q for q in all_quizzes if q.get("chapter_id") in pse_chapter_ids]
                        
                        if len(pse_quizzes) == 11:
                            # Vérifier la structure des quiz
                            valid_quizzes = 0
                            total_questions = 0
                            quizzes_with_4_5_questions = 0
                            
                            for quiz in pse_quizzes:
                                questions = quiz.get("questions", [])
                                # Note: 'titre' is not in the actual API structure, removing it from validation
                                if all(key in quiz for key in ["id", "chapter_id", "questions"]):
                                    if isinstance(questions, list) and len(questions) > 0:
                                        # Vérifier si le quiz a 4-5 questions (critère spécifique PSE)
                                        if 4 <= len(questions) <= 5:
                                            quizzes_with_4_5_questions += 1
                                        
                                        # Vérifier structure des questions
                                        questions_valid = True
                                        for q in questions:
                                            if not all(key in q for key in ["id", "question", "type", "correct_answer", "explication"]):
                                                questions_valid = False
                                                break
                                        
                                        if questions_valid:
                                            valid_quizzes += 1
                                            total_questions += len(questions)
                            
                            if valid_quizzes == 11:
                                self.log_result(
                                    "Quiz PSE",
                                    True,
                                    f"11 quiz PSE trouvés avec structure valide, {total_questions} questions total, {quizzes_with_4_5_questions} quiz avec 4-5 questions",
                                    {
                                        "count": len(pse_quizzes), 
                                        "valid_structure": valid_quizzes, 
                                        "total_questions": total_questions,
                                        "quizzes_4_5_questions": quizzes_with_4_5_questions
                                    }
                                )
                            else:
                                self.log_result(
                                    "Quiz PSE",
                                    False,
                                    f"Structure incomplète sur certains quiz ({valid_quizzes}/11)",
                                    {"count": len(pse_quizzes), "valid_structure": valid_quizzes}
                                )
                        else:
                            self.log_result(
                                "Quiz PSE",
                                False,
                                f"Nombre incorrect de quiz PSE (trouvés: {len(pse_quizzes)}, attendus: 11)",
                                {"count": len(pse_quizzes), "expected": 11}
                            )
                    else:
                        self.log_result(
                            "Quiz PSE",
                            False,
                            "Impossible de récupérer les chapitres PSE pour filtrer les quiz",
                            error=f"Status chapters: {chapters_response.status_code}"
                        )
                except Exception as e:
                    self.log_result(
                        "Quiz PSE",
                        False,
                        "Erreur lors de la récupération des chapitres PSE",
                        error=str(e)
                    )
            else:
                self.log_result(
                    "Quiz PSE",
                    False,
                    f"Erreur API quiz (status: {response.status_code})",
                    error=response.text
                )
                
        except requests.exceptions.RequestException as e:
            self.log_result(
                "Quiz PSE",
                False,
                "Erreur de connexion",
                error=str(e)
            )
    
    def test_formateur_account(self):
        """Test 6a: Compte formateur test"""
        print("\n6a️⃣ TEST COMPTE FORMATEUR")
        try:
            url = f"{API_BASE}/auth/login"
            data = {
                "email": "test@secours73.fr",
                "password": "test123"
            }
            
            response = self.session.post(url, json=data, timeout=10)
            
            if response.status_code == 200:
                result = response.json()
                token = result.get("token")
                user = result.get("user", {})
                
                if token and user.get("role") == "formateur":
                    self.formateur_token = token
                    self.log_result(
                        "Compte Formateur Test",
                        True,
                        f"Connexion formateur réussie - Rôle: {user.get('role')}",
                        {"email": user.get("email"), "role": user.get("role")}
                    )
                else:
                    self.log_result(
                        "Compte Formateur Test",
                        False,
                        "Token ou rôle formateur manquant",
                        {"response": result}
                    )
            else:
                self.log_result(
                    "Compte Formateur Test",
                    False,
                    f"Échec connexion formateur (status: {response.status_code})",
                    error=response.text
                )
                
        except requests.exceptions.RequestException as e:
            self.log_result(
                "Compte Formateur Test",
                False,
                "Erreur de connexion",
                error=str(e)
            )
    
    def test_stagiaire_account(self):
        """Test 6b: Compte stagiaire test"""
        print("\n6b️⃣ TEST COMPTE STAGIAIRE")
        try:
            url = f"{API_BASE}/auth/login"
            data = {
                "email": "stagiaire.test@secours73.fr",
                "password": "test123"
            }
            
            response = self.session.post(url, json=data, timeout=10)
            
            if response.status_code == 200:
                result = response.json()
                token = result.get("token")
                user = result.get("user", {})
                
                if token and user.get("role") == "stagiaire":
                    self.stagiaire_token = token
                    self.log_result(
                        "Compte Stagiaire Test",
                        True,
                        f"Connexion stagiaire réussie - Rôle: {user.get('role')}",
                        {"email": user.get("email"), "role": user.get("role"), "groupe_id": user.get("groupe_id")}
                    )
                else:
                    self.log_result(
                        "Compte Stagiaire Test",
                        False,
                        "Token ou rôle stagiaire manquant",
                        {"response": result}
                    )
            else:
                self.log_result(
                    "Compte Stagiaire Test",
                    False,
                    f"Échec connexion stagiaire (status: {response.status_code})",
                    error=response.text
                )
                
        except requests.exceptions.RequestException as e:
            self.log_result(
                "Compte Stagiaire Test",
                False,
                "Erreur de connexion",
                error=str(e)
            )
    
    def test_individual_quiz_endpoints(self):
        """Tests supplémentaires sur les endpoints de quiz individuels"""
        print("\n🔍 TESTS SUPPLÉMENTAIRES - QUIZ INDIVIDUELS")
        
        if not hasattr(self, 'sample_chapter_ids'):
            # Récupérer quelques IDs de chapitres pour tester
            try:
                psc_response = self.session.get(f"{API_BASE}/psc/chapters", timeout=10)
                pse_response = self.session.get(f"{API_BASE}/chapters?formation_type=PSE", timeout=10)
                
                self.sample_chapter_ids = []
                
                if psc_response.status_code == 200:
                    psc_chapters = psc_response.json()[:2]  # Prendre 2 premiers
                    self.sample_chapter_ids.extend([ch.get("id") for ch in psc_chapters])
                
                if pse_response.status_code == 200:
                    pse_chapters = pse_response.json()[:2]  # Prendre 2 premiers
                    self.sample_chapter_ids.extend([ch.get("id") for ch in pse_chapters])
                    
            except:
                self.sample_chapter_ids = []
        
        # Tester les endpoints GET /api/quizzes/chapter/{chapter_id}
        successful_tests = 0
        for chapter_id in self.sample_chapter_ids[:3]:  # Limiter à 3 tests
            try:
                url = f"{API_BASE}/quizzes/chapter/{chapter_id}"
                response = self.session.get(url, timeout=10)
                
                if response.status_code == 200:
                    quiz = response.json()
                    if isinstance(quiz, dict) and quiz.get("chapter_id") == chapter_id:
                        successful_tests += 1
                        
            except:
                continue
        
        if successful_tests > 0:
            self.log_result(
                "Quiz par Chapitre",
                True,
                f"{successful_tests} endpoints quiz par chapitre fonctionnels",
                {"successful_tests": successful_tests}
            )
        else:
            self.log_result(
                "Quiz par Chapitre",
                False,
                "Aucun endpoint quiz par chapitre ne fonctionne",
                {"tested_chapters": len(self.sample_chapter_ids[:3])}
            )
    
    def run_all_tests(self):
        """Exécute tous les tests dans l'ordre de priorité"""
        
        # Tests dans l'ordre de priorité du review_request
        self.test_admin_auth()
        self.test_psc_chapters()
        self.test_pse_chapters()
        self.test_quiz_psc()
        self.test_quiz_pse()
        self.test_formateur_account()
        self.test_stagiaire_account()
        self.test_health_check()
        
        # Tests supplémentaires
        self.test_individual_quiz_endpoints()
        
        self.print_summary()
    
    def print_summary(self):
        """Affiche un résumé des tests"""
        print("\n" + "="*70)
        print("📊 RÉSUMÉ DES TESTS DE VALIDATION")
        print("="*70)
        
        total = len(self.results)
        success = len([r for r in self.results if r.success])
        failed = total - success
        
        print(f"Total des tests: {total}")
        print(f"✅ Réussis: {success}")
        print(f"❌ Échoués: {failed}")
        print(f"📈 Taux de réussite: {(success/total)*100:.1f}%")
        
        if failed > 0:
            print("\n❌ TESTS ÉCHOUÉS:")
            for result in self.results:
                if not result.success:
                    print(f"   • {result.name}: {result.message}")
                    if result.error:
                        print(f"     ❗ {result.error}")
        
        print("\n✅ TESTS RÉUSSIS:")
        for result in self.results:
            if result.success:
                print(f"   • {result.name}: {result.message}")
        
        # Critères de succès spécifiques
        print("\n🎯 VALIDATION DES CRITÈRES:")
        
        criteria = {
            "Authentification admin": any(r.name == "Authentification Admin" and r.success for r in self.results),
            "8 chapitres PSC": any(r.name == "Chapitres PSC" and r.success for r in self.results),
            "11 chapitres PSE": any(r.name == "Chapitres PSE" and r.success for r in self.results),
            "8 quiz PSC": any(r.name == "Quiz PSC" and r.success for r in self.results),
            "11 quiz PSE": any(r.name == "Quiz PSE" and r.success for r in self.results),
            "Compte formateur": any(r.name == "Compte Formateur Test" and r.success for r in self.results),
            "Compte stagiaire": any(r.name == "Compte Stagiaire Test" and r.success for r in self.results),
            "API accessible": any(r.name == "Health Check" and r.success for r in self.results)
        }
        
        for criterion, met in criteria.items():
            status = "✅" if met else "❌"
            print(f"   {status} {criterion}")
        
        all_critical_passed = all(criteria.values())
        
        print("\n🏁 VERDICT FINAL:")
        if all_critical_passed:
            print("✅ TOUS LES CRITÈRES DE VALIDATION SONT REMPLIS")
            print("✅ L'application est prête pour la mise en ligne")
        else:
            print("❌ CERTAINS CRITÈRES NE SONT PAS REMPLIS")
            print("❌ Des corrections sont nécessaires avant la mise en ligne")
        
        print("="*70)

def main():
    """Point d'entrée principal"""
    tester = FAODTester()
    try:
        tester.run_all_tests()
        return 0 if all(r.success for r in tester.results) else 1
    except KeyboardInterrupt:
        print("\n⚠️ Tests interrompus par l'utilisateur")
        return 2
    except Exception as e:
        print(f"\n💥 Erreur fatale: {e}")
        return 3

if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)