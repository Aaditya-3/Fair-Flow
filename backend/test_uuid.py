import uuid
from database import SessionLocal
from models import Audit
db = SessionLocal()
uid = uuid.UUID("9d2f2b94-99e6-411f-8878-7505f6e33258")
audit = db.query(Audit).filter(Audit.id == uid).first()
if audit:
    print(f"Found audit: {audit.id}")
    print(f"User ID: {audit.user_id}")
    user_uid = uuid.UUID("4da74fcc-1c06-4a11-9193-145835f437c2")
    q = db.query(Audit).filter(Audit.id == uid, Audit.user_id == user_uid).first()
    print(f"Query with user_id: {q is not None}")
else:
    print("Audit not found by UUID object!")
    print(db.query(Audit).filter(Audit.id == "9d2f2b9499e6411f88787505f6e33258").first())
