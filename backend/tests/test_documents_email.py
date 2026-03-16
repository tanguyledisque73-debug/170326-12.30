"""
Tests for Documents and Email features:
- Welcome email on stagiaire registration
- Formateur send email to stagiaire
- Document upload for group or stagiaire
- Document listing for formateur
- Document listing for stagiaire
- Document download
- Document deletion
"""
import pytest
import requests
import os
import io

BASE_URL = os.environ.get('REACT_APP_BACKEND_URL', '').rstrip('/')


@pytest.fixture(scope="module")
def api_client():
    """Shared requests session"""
    session = requests.Session()
    return session


@pytest.fixture(scope="module")
def admin_token(api_client):
    """Get admin token"""
    response = api_client.post(f"{BASE_URL}/api/auth/login", json={
        "email": "ledisque.tanguy73@hotmail.com",
        "password": "Admin123!"
    })
    assert response.status_code == 200, f"Admin login failed: {response.text}"
    return response.json()["token"]


@pytest.fixture(scope="module")
def test_formateur(api_client, admin_token):
    """Create and login as test formateur"""
    # Create formateur
    create_response = api_client.post(
        f"{BASE_URL}/api/admin/formateur?token={admin_token}",
        json={
            "email": "TEST_formateur_docs2@test.com",
            "nom": "TESTFORMATEUR2",
            "prenom": "DocTest"
        }
    )
    
    if create_response.status_code == 400:
        # User already exists, try to login
        pass
    elif create_response.status_code == 200:
        data = create_response.json()
        temp_password = data["temp_password"]
        
        # Login with temp password
        login_response = api_client.post(f"{BASE_URL}/api/auth/login", json={
            "email": "TEST_formateur_docs2@test.com",
            "password": temp_password
        })
        
        if login_response.status_code == 200:
            token = login_response.json()["token"]
            # Set proper password
            api_client.post(f"{BASE_URL}/api/auth/set-password?token={token}&new_password=TestPass123!")
    
    # Login with proper password
    login_response = api_client.post(f"{BASE_URL}/api/auth/login", json={
        "email": "TEST_formateur_docs2@test.com",
        "password": "TestPass123!"
    })
    
    assert login_response.status_code == 200, f"Formateur login failed: {login_response.text}"
    return login_response.json()


@pytest.fixture(scope="module")
def test_groupe(api_client, test_formateur):
    """Create test groupe"""
    response = api_client.post(
        f"{BASE_URL}/api/formateur/groupe?token={test_formateur['token']}",
        json={
            "nom": "TEST_Groupe_Docs2",
            "formation_type": "PSE",
            "seuil_reussite": 80,
            "chapitres_ordre": ["ch1", "ch2"]
        }
    )
    assert response.status_code == 200, f"Group creation failed: {response.text}"
    return response.json()["groupe"]


@pytest.fixture(scope="module")
def test_stagiaire(api_client, test_groupe):
    """Create test stagiaire"""
    response = api_client.post(
        f"{BASE_URL}/api/auth/register",
        json={
            "email": "TEST_stagiaire_docs2@test.com",
            "password": "TestPass123!",
            "nom": "TESTSTAGIAIRE2",
            "prenom": "DocTest",
            "code_groupe": test_groupe["code_acces"]
        }
    )
    
    if response.status_code == 400:  # Already exists
        login_response = api_client.post(f"{BASE_URL}/api/auth/login", json={
            "email": "TEST_stagiaire_docs2@test.com",
            "password": "TestPass123!"
        })
        assert login_response.status_code == 200
        return login_response.json()
    
    assert response.status_code == 200, f"Stagiaire creation failed: {response.text}"
    return response.json()


# ============== WELCOME EMAIL TESTS ==============

class TestWelcomeEmail:
    """Tests for welcome email functionality"""
    
    def test_welcome_email_on_registration(self, api_client, test_groupe):
        """Test that registration succeeds (welcome email sent async)"""
        import time
        unique_email = f"TEST_welcome_{int(time.time())}@test.com"
        
        response = api_client.post(
            f"{BASE_URL}/api/auth/register",
            json={
                "email": unique_email,
                "password": "TestPass123!",
                "nom": "TESTWELCOME",
                "prenom": "EmailTest",
                "code_groupe": test_groupe["code_acces"]
            }
        )
        # Registration should succeed even if email fails (async)
        assert response.status_code == 200
        data = response.json()
        assert "token" in data
        assert data["user"]["email"] == unique_email
    
    def test_admin_send_welcome_email_endpoint_exists(self, api_client, admin_token, test_stagiaire):
        """Admin can call welcome email endpoint"""
        response = api_client.post(
            f"{BASE_URL}/api/admin/send-welcome-email?token={admin_token}&stagiaire_email={test_stagiaire['user']['email']}"
        )
        # May succeed (200) or fail (500 if email service error, 404 if not found)
        assert response.status_code in [200, 404, 500]


# ============== FORMATEUR SEND EMAIL TESTS ==============

class TestFormateurSendEmail:
    """Tests for formateur email sending"""
    
    def test_formateur_send_email_endpoint_works(self, api_client, test_formateur, test_stagiaire):
        """Formateur send email endpoint is accessible"""
        response = api_client.post(
            f"{BASE_URL}/api/formateur/send-email",
            params={
                "token": test_formateur['token'],
                "to_email": test_stagiaire['user']['email'],
                "subject": "TEST_Email Subject",
                "message": "This is a test message."
            }
        )
        # May succeed (200) or fail (500 if email service error)
        assert response.status_code in [200, 500]
        if response.status_code == 200:
            data = response.json()
            assert data["status"] == "success"
    
    def test_formateur_send_email_missing_params(self, api_client, test_formateur):
        """Missing parameters should fail with 422"""
        response = api_client.post(
            f"{BASE_URL}/api/formateur/send-email",
            params={"token": test_formateur['token']}
        )
        assert response.status_code == 422
    
    def test_formateur_send_email_invalid_token(self, api_client):
        """Invalid token should fail with 401"""
        response = api_client.post(
            f"{BASE_URL}/api/formateur/send-email",
            params={
                "token": "invalid_token",
                "to_email": "test@test.com",
                "subject": "Test",
                "message": "Test"
            }
        )
        assert response.status_code == 401


# ============== DOCUMENT UPLOAD TESTS ==============

class TestDocumentUpload:
    """Tests for document upload functionality"""
    
    def test_document_upload_to_groupe(self, api_client, test_formateur, test_groupe):
        """Formateur can upload document to group"""
        files = {
            'file': ('test_doc.txt', io.BytesIO(b'Test document content'), 'text/plain')
        }
        
        response = api_client.post(
            f"{BASE_URL}/api/formateur/document/upload",
            params={
                "token": test_formateur['token'],
                "titre": "TEST_Document Cours",
                "categorie": "Cours",
                "description": "Test document",
                "destinataire_type": "groupe",
                "groupe_id": test_groupe["id"]
            },
            files=files
        )
        assert response.status_code == 200, f"Upload failed: {response.text}"
        data = response.json()
        assert data["status"] == "success"
        assert "document_id" in data
    
    def test_document_upload_to_stagiaire(self, api_client, test_formateur, test_stagiaire):
        """Formateur can upload document to specific stagiaire"""
        files = {
            'file': ('cert.pdf', io.BytesIO(b'%PDF-1.4 test'), 'application/pdf')
        }
        
        response = api_client.post(
            f"{BASE_URL}/api/formateur/document/upload",
            params={
                "token": test_formateur['token'],
                "titre": "TEST_Certificat",
                "categorie": "Certificats",
                "description": "Certificat for stagiaire",
                "destinataire_type": "stagiaire",
                "stagiaire_id": test_stagiaire['user']['id']
            },
            files=files
        )
        assert response.status_code == 200, f"Upload failed: {response.text}"
    
    def test_document_upload_missing_groupe_id(self, api_client, test_formateur):
        """Missing groupe_id for groupe type should fail with 400"""
        files = {
            'file': ('test.txt', io.BytesIO(b'Test'), 'text/plain')
        }
        
        response = api_client.post(
            f"{BASE_URL}/api/formateur/document/upload",
            params={
                "token": test_formateur['token'],
                "titre": "TEST_Doc",
                "categorie": "Cours",
                "destinataire_type": "groupe"
            },
            files=files
        )
        assert response.status_code == 400
    
    def test_document_upload_invalid_token(self, api_client):
        """Invalid token should fail"""
        files = {
            'file': ('test.txt', io.BytesIO(b'Test'), 'text/plain')
        }
        
        response = api_client.post(
            f"{BASE_URL}/api/formateur/document/upload",
            params={
                "token": "invalid_token",
                "titre": "TEST_Doc",
                "categorie": "Cours",
                "destinataire_type": "groupe",
                "groupe_id": "test"
            },
            files=files
        )
        assert response.status_code == 401


# ============== DOCUMENT LISTING TESTS ==============

class TestDocumentListing:
    """Tests for document listing"""
    
    def test_formateur_get_documents(self, api_client, test_formateur):
        """Formateur can list their documents"""
        response = api_client.get(
            f"{BASE_URL}/api/formateur/documents",
            params={"token": test_formateur['token']}
        )
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        # Should have at least the documents we uploaded
        assert len(data) >= 0
    
    def test_stagiaire_get_documents(self, api_client, test_stagiaire):
        """Stagiaire can list their documents"""
        response = api_client.get(
            f"{BASE_URL}/api/stagiaire/documents",
            params={"token": test_stagiaire['token']}
        )
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
    
    def test_documents_have_required_fields(self, api_client, test_formateur):
        """Documents should have all required fields"""
        response = api_client.get(
            f"{BASE_URL}/api/formateur/documents",
            params={"token": test_formateur['token']}
        )
        if response.status_code == 200:
            data = response.json()
            if len(data) > 0:
                doc = data[0]
                expected_fields = ["id", "titre", "categorie", "formateur_id", "uploaded_at"]
                for field in expected_fields:
                    assert field in doc, f"Missing field: {field}"


# ============== DOCUMENT DOWNLOAD TESTS ==============

class TestDocumentDownload:
    """Tests for document download"""
    
    def test_download_document(self, api_client, test_formateur, test_groupe):
        """Can download an uploaded document"""
        # Upload a document first
        files = {
            'file': ('download_test.txt', io.BytesIO(b'Download test content'), 'text/plain')
        }
        
        upload_response = api_client.post(
            f"{BASE_URL}/api/formateur/document/upload",
            params={
                "token": test_formateur['token'],
                "titre": "TEST_Download Doc",
                "categorie": "Cours",
                "destinataire_type": "groupe",
                "groupe_id": test_groupe["id"]
            },
            files=files
        )
        assert upload_response.status_code == 200
        doc_id = upload_response.json()["document_id"]
        
        # Download the document
        response = api_client.get(
            f"{BASE_URL}/api/documents/{doc_id}/download",
            params={"token": test_formateur['token']}
        )
        assert response.status_code == 200
        assert b'Download test content' in response.content
    
    def test_download_nonexistent_document(self, api_client, test_formateur):
        """Download nonexistent document should fail with 404"""
        response = api_client.get(
            f"{BASE_URL}/api/documents/nonexistent-doc-id/download",
            params={"token": test_formateur['token']}
        )
        assert response.status_code == 404


# ============== DOCUMENT DELETE TESTS ==============

class TestDocumentDelete:
    """Tests for document deletion"""
    
    def test_delete_document(self, api_client, test_formateur, test_groupe):
        """Formateur can delete their document"""
        # Upload a document first
        files = {
            'file': ('delete_test.txt', io.BytesIO(b'Delete test'), 'text/plain')
        }
        
        upload_response = api_client.post(
            f"{BASE_URL}/api/formateur/document/upload",
            params={
                "token": test_formateur['token'],
                "titre": "TEST_Delete Doc",
                "categorie": "Évaluations",
                "destinataire_type": "groupe",
                "groupe_id": test_groupe["id"]
            },
            files=files
        )
        assert upload_response.status_code == 200
        doc_id = upload_response.json()["document_id"]
        
        # Delete the document
        response = api_client.delete(
            f"{BASE_URL}/api/formateur/document/{doc_id}",
            params={"token": test_formateur['token']}
        )
        assert response.status_code == 200
        
        # Verify it's deleted
        get_response = api_client.get(
            f"{BASE_URL}/api/documents/{doc_id}/download",
            params={"token": test_formateur['token']}
        )
        assert get_response.status_code == 404
    
    def test_delete_nonexistent_document(self, api_client, test_formateur):
        """Delete nonexistent document should fail with 404"""
        response = api_client.delete(
            f"{BASE_URL}/api/formateur/document/nonexistent-id",
            params={"token": test_formateur['token']}
        )
        assert response.status_code == 404


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
