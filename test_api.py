import requests
import uuid
from backend.database import SessionLocal
from backend.models import Audit, User
from backend.routers.auth import create_access_token
db = SessionLocal()
audit = db.query(Audit).filter(Audit.id == "9d2f2b94-99e6-411f-8878-7505f6e33258").first()
user = db.query(User).filter(User.id == audit.user_id).first()
token = create_access_token({"sub": str(user.id)})
res = requests.get(
    f"http://127.0.0.1:8000/audit/{audit.id}/gemini-summary",
    headers={"Authorization": f"Bearer {token}"}
)
print(f"Status: {res.status_code}")
print(f"Body: {res.text}")
