from backend.database import supabase
from datetime import datetime


def get_and_lock_token():
    """
    Récupère UN token libre et le marque utilisé immédiatement
    (sécurisé multi-utilisateurs)
    """
    res = supabase.rpc("get_and_lock_token").execute()

    if not res.data or len(res.data) == 0:
        return None

    return res.data[0]   # {id, token}


def create_candidate(data: dict):
    data["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    res = supabase.table("candidates").insert(data).execute()
    return res.data



def delete_candidate(candidate_id: int):
    res = supabase.table("candidates").delete().eq("id", candidate_id).execute()
    return bool(res.data)

