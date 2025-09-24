# 🚀 Kamina Backend

Sistema de gestión de **libros**, **autores** y **usuarios** con autenticación **JWT**, desarrollado con **FastAPI** y **SQLAlchemy**.

[Documentación] (https://github.com/enriqueperez21/fastapi-library-management/blob/master/app/docs/Redoc)

---

## 📂 Estructura del Proyecto

```
app/
 ├── main.py              # Punto de entrada FastAPI
 ├── core/                # Configuración principal
 ├── crud/                # Operaciones CRUD
 ├── db/                  # Conexión e inicialización de la BD
 ├── models/              # Modelos SQLAlchemy
 ├── routers/             # Endpoints (usuarios, autores, libros, auth)
 ├── schemas/             # Esquemas Pydantic
 ├── services/            # Lógica adicional
 └── test/                # Pruebas unitarias
.env
requirements.txt
README.md
```

---

## 🛠️ Requisitos

- Python **3.11+**
- [pip](https://pip.pypa.io/en/stable/)
- [Docker](https://www.docker.com/) (opcional, para base de datos PostgreSQL)

---

## ⚙️ Instalación

1. **Clonar el repositorio**
   ```sh
   git clone https://github.com/enriqueperez21/fastapi-library-management
   cd fastapi-library-management
   ```

2. **Instalar dependencias**
   ```sh
   pip install -r requirements.txt
   ```

3. **Configurar variables de entorno (.env)**
   Ejemplo con PostgreSQL:
   ```env
   DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/database
   SECRET_KEY=tu_clave_secreta
   ```

   Ejemplo para crear una instancia de PostgreSQL en Docker:
   ```sh
   docker run --name postgres-container \
   -e POSTGRES_PASSWORD=user_password \
   -e POSTGRES_USER=user_name \
   -e POSTGRES_DB=database \
   -p 5432:5432 -d postgres
   ```

4. **Inicializar la base de datos**
   Crea todas las tablas en la base de datos para realizar las operaciones
   ```sh
   python -m app.db.init_db
   ```

5. **Ejecutar el proyecto**
   ```sh
   uvicorn app.main:app --reload
   ```

   👉 Accede a la documentación interactiva: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Pruebas

Ejecutar todos los tests:
```sh
python -m pytest -v
```

Ver cobertura de tests:
```sh
python -m pytest --cov=app
```

Para ver los resultados de cobertura visitar 
[Results] (https://github.com/enriqueperez21/fastapi-library-management/blob/master/app/test/TEST_RESULTS.md)

---

## 📚 Endpoints Principales

- **Usuarios** → `/users`
- **Autores** → `/authors`
- **Libros** → `/books`
- **Autenticación** → `/auth`

---

## 📝 Archivos Importantes

- `.env` — Variables de entorno  
- `requirements.txt` — Dependencias Python  
- `app/main.py` — Punto de entrada FastAPI  
- `app/db/init_db.py` — Inicialización de la base de datos  

---

## ✅ Funcionalidades del Proyecto

- CRUD de **Usuarios**, **Autores** y **Libros**  
- Búsqueda de libros por **título**, **autor** o **año de publicación**  
- Registro de **préstamos** y **devoluciones** de libros  
- Autenticación mediante **JWT**  
- Documentación automática con **Swagger UI**  
- Pruebas unitarias con **pytest** y uso de **mocks**  