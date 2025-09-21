import logging
from app.db.base import Base
from app.db.session import engine
import app.models

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(" DB ")

def init_db():
    try:
        Base.metadata.create_all(bind=engine)
        logger.info("✅ Tablas creadas correctamente")
    except Exception as e:
        logger.error("❌ Error al crear las tablas", exc_info=True)
    

if __name__ == "__main__":
    init_db()