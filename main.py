from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from backend.utils import get_and_lock_token, create_candidate
from backend.database import supabase
from backend.utils import delete_candidate

app = FastAPI()

# Autoriser uniquement ton domaine WordPress
origins = [
    "https://ioai.indabaxniger.com",
    "https://www.ioai.indabaxniger.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.options("/{path:path}")
def preflight_handler(path: str):
    return {}



@app.post("/candidate")
def register_candidate(candidate: dict):


        # Vérifier si le téléphone existe déjà
    exists = supabase.table("candidates") \
        .select("id") \
        .eq("phone", candidate.get("phone")) \
        .limit(1) \
        .execute()

    if exists.data:
        raise HTTPException(
            status_code=400,
            detail="Vous êtes déjà inscrit. Candidature non retenue."
        )
        


    token = get_and_lock_token()
    if not token:
        raise HTTPException(status_code=400, detail="Aucun token disponible")

    candidate["token"] = token["token"]
    candidate["id"] = token["id"]

    create_candidate(candidate)

    return candidate

# --- Route pour candidats ---

@app.get("/candidates")
def get_candidates():
    res = supabase.table("candidates").select("*").order("id").execute()
    return res.data



# --- Route pour supprimer une candidature ---

@app.delete("/candidate/{candidate_id}")
def remove_candidate(candidate_id: int):
    success = delete_candidate(candidate_id)
    if not success:
        raise HTTPException(status_code=404, detail="Candidat introuvable")

    return {"success": True}



# --- Route pour tous les tokens ---
# --- Route pour tous les tokens ---
@app.get("/tokens")
def get_all_tokens():
    all_tokens = []
    start = 0
    batch_size = 1000

    while True:
        # Récupère un lot de tokens
        res = supabase.table("tokens").select("*").range(start, start + batch_size - 1).execute()
        batch = res.data
        if not batch:
            break  # stop quand il n'y a plus de données
        all_tokens.extend(batch)
        start += batch_size

    return all_tokens







