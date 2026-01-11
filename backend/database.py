from supabase import create_client


SUPABASE_URL="https://pxbcnguqaznuqsvisspl.supabase.co"
SUPABASE_KEY="sb_secret_cbDG2Jf63XmTVpcI0eeC-Q_Xg-2w2LF"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
