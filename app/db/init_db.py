from app.db.base import Base
from app.db.session import engine
import app.models

def init_db():
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Tablas creadas correctamente")
    except Exception as e:
        print("❌ Error", e)
    

if __name__ == "__main__":
    init_db()