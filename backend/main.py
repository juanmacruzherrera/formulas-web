# backend/main.py
# ============================================
# QUÉ HACE: Punto de entrada de la aplicación FastAPI
# CONSUME: backend.routes.formulas (router de fórmulas)
#          backend.routes.calculos (router de cálculos)
# EXPONE: Servidor web con endpoints HTTP
# RELACIONADO CON:
#   - Ejecutado por: uvicorn
#   - Importa: backend/routes/formulas.py, backend/routes/calculos.py
# ============================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.formulas import router as formulas_router
from backend.routes.calculos import router as calculos_router

# Crear la aplicación FastAPI
app = FastAPI(
    title="API Fórmulas Matemáticas",
    description="Backend para visualización de fórmulas matemáticas y físicas",
    version="0.1.0"
)

# Configurar CORS para permitir peticiones desde el frontend
# IMPORTANTE: Esto es necesario para que el navegador permita llamadas HTTP
# desde el frontend (localhost:3000) al backend (localhost:8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios exactos
    allow_credentials=True,
    allow_methods=["*"],  # Permite GET, POST, PUT, DELETE, etc.
    allow_headers=["*"],  # Permite todos los headers
)

# Incluir routers
app.include_router(formulas_router)
app.include_router(calculos_router)

# Endpoint de health check
@app.get("/health")
def health_check():
    """
    Endpoint de verificación de salud del servidor.

    Devuelve un mensaje simple indicando que el servidor está funcionando.
    Este endpoint se usa para:
    - Verificar que el servidor está corriendo
    - Monitoreo en producción
    - Tests automatizados

    Returns:
        dict: Diccionario con status y mensaje

    Example:
        GET http://localhost:8000/health

        Response:
        {
            "status": "ok",
            "message": "Servidor funcionando correctamente"
        }
    """
    return {
        "status": "ok",
        "message": "Servidor funcionando correctamente"
    }
