from utils import get_available_token, mark_token_used, create_candidate

def test_get_token():
    token = get_available_token()
    if token:
        print("Token disponible :", token)
        return token
    else:
        print("Aucun token disponible")
        return None

def test_mark_token(token_id):
    mark_token_used(token_id)
    print(f"Token {token_id} marqué comme utilisé")

def test_create_candidate():
    data = {
        "name": "Jean Dupont",
        "email": "jean@example.com",
        "position": "Test Candidate"
    }
    create_candidate(data)
    print("Candidat créé :", data)

if __name__ == "__main__":
    token = test_get_token()
    if token:
        test_mark_token(token["id"])
    test_create_candidate()
