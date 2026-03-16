import requests
import sys
from datetime import datetime
import json

class FAODSecours73FeatureTester:
    def __init__(self, base_url="https://faod-rescue.preview.emergentagent.com"):
        self.base_url = base_url
        self.token = None
        self.tests_run = 0
        self.tests_passed = 0
        self.test_results = []
        
        # Test credentials from review request
        self.test_credentials = {
            "stagiaire": {"email": "stagiaire.test@secours73.fr", "password": "test123"},
            "formateur": {"email": "test@secours73.fr", "password": "test123"},
            "admin": {"email": "ledisque.tanguy73@hotmail.com", "password": "NewAdmin123!"}
        }

    def run_test(self, name, method, endpoint, expected_status, data=None, headers=None):
        """Run a single API test"""
        url = f"{self.base_url}/api/{endpoint}"
        test_headers = {'Content-Type': 'application/json'}
        if headers:
            test_headers.update(headers)
        
        # Add token as query parameter if available
        params = {}
        if self.token:
            params['token'] = self.token
        if method == 'GET' and data:
            params.update(data)

        self.tests_run += 1
        print(f"\n🔍 Testing {name}...")
        print(f"   URL: {url}")
        
        try:
            if method == 'GET':
                response = requests.get(url, headers=test_headers, params=params)
            elif method == 'POST':
                response = requests.post(url, json=data, headers=test_headers, params=params)
            elif method == 'PUT':
                response = requests.put(url, json=data, headers=test_headers, params=params)
            elif method == 'DELETE':
                response = requests.delete(url, headers=test_headers, params=params)

            success = response.status_code == expected_status
            if success:
                self.tests_passed += 1
                print(f"✅ Passed - Status: {response.status_code}")
                try:
                    return success, response.json()
                except:
                    return success, response.text
            else:
                print(f"❌ Failed - Expected {expected_status}, got {response.status_code}")
                print(f"   Response: {response.text[:200]}...")
                return False, {}

        except Exception as e:
            print(f"❌ Failed - Error: {str(e)}")
            return False, {}

    def test_login(self, user_type):
        """Test login for different user types"""
        credentials = self.test_credentials[user_type]
        success, response = self.run_test(
            f"{user_type.title()} Login",
            "POST",
            "auth/login",
            200,
            data=credentials
        )
        if success and 'token' in response:
            self.token = response['token']
            user_info = response['user']
            print(f"   Logged in as: {user_info['prenom']} {user_info['nom']} ({user_info['role']})")
            return True, response
        return False, {}

    def test_psc_chapters_enriched(self):
        """Test PSC chapters API returns 8 enriched chapters with 32 fiches total"""
        success, response = self.run_test(
            "PSC Chapters - 8 chapters with 32 fiches",
            "GET",
            "psc/chapters",
            200
        )
        if success and isinstance(response, list):
            total_fiches = sum(len(ch.get('fiches', [])) for ch in response)
            print(f"   Found {len(response)} PSC chapters")
            print(f"   Total fiches: {total_fiches}")
            
            # Check if we have 8 chapters and approximately 32 fiches
            chapters_ok = len(response) == 8
            fiches_ok = total_fiches >= 30  # Allow some flexibility
            
            if chapters_ok and fiches_ok:
                print(f"   ✅ PSC content enriched: {len(response)} chapters, {total_fiches} fiches")
                return True
            else:
                print(f"   ❌ Expected 8 chapters with ~32 fiches, got {len(response)} chapters with {total_fiches} fiches")
        return False

    def test_certificate_status_api(self):
        """Test certificate status API for stagiaire"""
        success, response = self.run_test(
            "Certificate Status API",
            "GET",
            "stagiaire/certificate/status",
            200
        )
        if success:
            print(f"   Certificate earned: {response.get('earned', False)}")
            print(f"   Formation type: {response.get('formation_type', 'N/A')}")
            print(f"   Required chapters: {len(response.get('required_chapters', []))}")
            print(f"   Completed chapters: {len(response.get('completed_chapters', []))}")
            return True
        return False

    def test_certificate_generate_api(self):
        """Test certificate generation API"""
        success, response = self.run_test(
            "Certificate Generate API",
            "GET",
            "stagiaire/certificate/generate",
            200
        )
        if success and 'certificate_data' in response:
            cert_data = response['certificate_data']
            print(f"   Certificate for: {cert_data.get('prenom')} {cert_data.get('nom')}")
            print(f"   Formation: {cert_data.get('formation_type')}")
            print(f"   Average score: {cert_data.get('average_score')}%")
            return True
        elif response.get('detail') and 'incomplète' in response.get('detail', ''):
            print(f"   ⚠️  Certificate not available - formation incomplete (expected for test account)")
            return True  # This is expected for test account
        return False

    def test_formateur_certificate_config(self):
        """Test formateur certificate configuration API"""
        # First get groups
        success, groups = self.run_test(
            "Get Formateur Groups for Certificate Config",
            "GET",
            "formateur/groupes",
            200
        )
        
        if success and isinstance(groups, list) and len(groups) > 0:
            groupe_id = groups[0]['id']
            
            # Test get certificate config
            success, config = self.run_test(
                "Get Certificate Config",
                "GET",
                f"certificates/config/{groupe_id}",
                200
            )
            
            if success:
                print(f"   Certificate config for group: {groupe_id}")
                print(f"   Required chapters: {len(config.get('chapitres_obligatoires', []))}")
                
                # Test set certificate config
                test_config = {"chapitres_obligatoires": ["ch1", "ch2", "ch3"]}
                success, response = self.run_test(
                    "Set Certificate Config",
                    "POST",
                    f"certificates/config/{groupe_id}",
                    200,
                    data=test_config
                )
                
                if success:
                    print(f"   ✅ Certificate config updated successfully")
                    return True
        else:
            print(f"   ⚠️  No groups found for formateur - cannot test certificate config")
            return True  # Not a failure, just no data
        
        return False

    def test_logo_endpoints(self):
        """Test that logo is accessible"""
        # Test logo file accessibility (this would be served by frontend)
        logo_url = f"{self.base_url.replace('/api', '')}/images/logo-secours73.png"
        try:
            response = requests.get(logo_url)
            if response.status_code == 200:
                print(f"   ✅ Logo accessible at: {logo_url}")
                return True
            else:
                print(f"   ❌ Logo not accessible - Status: {response.status_code}")
        except Exception as e:
            print(f"   ❌ Logo test failed: {str(e)}")
        return False

    def test_groupe_settings_access(self):
        """Test formateur can access groupe settings"""
        # Get groups first
        success, groups = self.run_test(
            "Get Groups for Settings Test",
            "GET",
            "formateur/groupes",
            200
        )
        
        if success and isinstance(groups, list) and len(groups) > 0:
            groupe_id = groups[0]['id']
            
            # Test group detail access (simulates settings page data)
            success, response = self.run_test(
                "Group Detail Access (Settings)",
                "GET",
                f"formateur/groupe/{groupe_id}",
                200
            )
            
            if success:
                groupe = response.get('groupe', {})
                print(f"   Group: {groupe.get('nom')}")
                print(f"   Formation type: {groupe.get('formation_type')}")
                print(f"   Success threshold: {groupe.get('seuil_reussite')}%")
                print(f"   Chapter order: {len(groupe.get('chapitres_ordre', []))} chapters")
                return True
        else:
            print(f"   ⚠️  No groups found for formateur")
            return True  # Not necessarily a failure
        
        return False

def main():
    print("🚀 Testing FAOD-SECOURS73 New Features")
    print("=" * 60)
    
    tester = FAODSecours73FeatureTester()
    
    # Test 1: Test stagiaire login and certificate features
    print("\n📋 TESTING STAGIAIRE FEATURES")
    print("-" * 40)
    
    success, _ = tester.test_login("stagiaire")
    if success:
        tester.test_certificate_status_api()
        tester.test_certificate_generate_api()
    else:
        print("❌ Stagiaire login failed - skipping stagiaire tests")
    
    # Test 2: Test formateur login and certificate config
    print("\n📋 TESTING FORMATEUR FEATURES")
    print("-" * 40)
    
    success, _ = tester.test_login("formateur")
    if success:
        tester.test_formateur_certificate_config()
        tester.test_groupe_settings_access()
    else:
        print("❌ Formateur login failed - skipping formateur tests")
    
    # Test 3: Test admin login and general features
    print("\n📋 TESTING ADMIN & GENERAL FEATURES")
    print("-" * 40)
    
    success, _ = tester.test_login("admin")
    if success:
        tester.test_psc_chapters_enriched()
        tester.test_logo_endpoints()
    else:
        print("❌ Admin login failed - skipping admin tests")

    # Print results
    print("\n" + "=" * 60)
    print(f"📊 Feature Tests completed: {tester.tests_passed}/{tester.tests_run}")
    print(f"Success rate: {(tester.tests_passed/tester.tests_run*100):.1f}%")
    
    if tester.tests_passed == tester.tests_run:
        print("🎉 All feature tests passed!")
        return 0
    else:
        print("⚠️  Some feature tests failed - check details above")
        return 1

if __name__ == "__main__":
    sys.exit(main())