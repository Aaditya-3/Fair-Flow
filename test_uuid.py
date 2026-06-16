import uuid
from database import SessionLocal
from models import Audit
db = SessionLocal()
audit = db.query(Audit).first()
if audit:
    print(f"Found audit: {audit.id}")
    q1 = db.query(Audit).filter(Audit.id == audit.id).first()
    print(f"Query by UUID object: {q1 is not None}")
    q2 = db.query(Audit).filter(Audit.id == str(audit.id)).first()
    print(f"Query by str(UUID): {q2 is not None}")
    q3 = db.query(Audit).filter(Audit.id == audit.id.hex).first()
    print(f"Query by UUID.hex: {q3 is not None}")
