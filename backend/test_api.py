import requests
import uuid
from database import SessionLocal
from models import Audit, User
from routers.auth import create_access_token
db = SessionLocal()
uid = uuid.UUID("9d2f2b94-99e6-411f-8878-7505f6e33258")
audit = db.query(Audit).filter(Audit.id == uid).first()
if audit:
    user = db.query(User).filter(User.id == audit.user_id).first()
    token = create_access_token({"sub": str(user.id)})
    res = requests.get(
        f"http://127.0.0.1:8000/audit/{audit.id}/gemini-summary",
        headers={"Authorization": f"Bearer {token}"}
    )
    print(f"Status: {res.status_code}")
    print(f"Body: {res.text}")
