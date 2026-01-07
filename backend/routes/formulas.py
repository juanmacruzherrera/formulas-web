# backend/routes/formulas.py
# ============================================
# QUÉ HACE: Endpoints relacionados con fórmulas
# CONSUME: backend.services.supabase_client (para consultar BD)
# EXPONE: Router con endpoints /api/formulas
# RELACIONADO CON:
#   - Usado por: backend/main.py (incluye este router)
#   - Usa: backend/services/supabase_client.py
# ============================================

from fastapi import APIRouter
from backend.services.supabase_client import supabase

# Crear router con prefijo y tag
router = APIRouter(
    prefix="/api",
    tags=["formulas"]
)

@router.get("/formulas")
def listar_formulas():
    """
    Devuelve todas las fórmulas disponibles en la base de datos.

    Este endpoint consulta la tabla 'formulas' en Supabase y devuelve
    todos los registros.

    Returns:
        dict: Diccionario con formato estándar
            - data: Lista de fórmulas (list)
            - error: None si éxito, mensaje si error (str | None)

    Example:
        GET http://localhost:8000/api/formulas

        Response 200 OK:
        {
            "data": [
                {
                    "id": 1,
                    "nombre": "MRU - Movimiento Rectilíneo Uniforme",
                    "categoria": "fisica",
                    "formula_latex": "x = x_0 + v \\cdot t",
                    "descripcion": "...",
                    "variables": {...},
                    "ejemplo": {...}
                }
            ],
            "error": null
        }

        Response 200 OK (con error):
        {
            "data": null,
            "error": "Error al consultar la base de datos: [detalle]"
        }
    """
    try:
        # Consultar la tabla 'formulas' en Supabase
        response = supabase.table("formulas").select("*").execute()

        # Devolver los datos con formato estándar
        return {
            "data": response.data,
            "error": None
        }

    except Exception as e:
        # Si hay error, devolver formato estándar con error
        return {
            "data": None,
            "error": f"Error al consultar la base de datos: {str(e)}"
        }

# ============================================
# ENDPOINT PARA OBTENER FÓRMULA POR ID
# ============================================

@router.get("/formula/{formula_id}")
def obtener_formula(formula_id: int):
    """
    Devuelve una fórmula específica por su ID.

    Este endpoint busca una fórmula en la base de datos filtrando por ID.
    Si la fórmula no existe, devuelve un error descriptivo.

    Args:
        formula_id (int): ID de la fórmula a buscar (parámetro de ruta)

    Returns:
        dict: Diccionario con formato estándar
            - data: Objeto con la fórmula (dict) o None si no existe
            - error: None si éxito, mensaje si error (str | None)

    Example:
        GET http://localhost:8000/api/formula/1

        Response 200 OK (fórmula encontrada):
        {
            "data": {
                "id": 1,
                "nombre": "MRU - Movimiento Rectilíneo Uniforme",
                "categoria": "fisica",
                "formula_latex": "x = x_0 + v \\cdot t",
                ...
            },
            "error": null
        }

        Response 200 OK (fórmula NO encontrada):
        {
            "data": null,
            "error": "Fórmula no encontrada"
        }

        Response 200 OK (error de BD):
        {
            "data": null,
            "error": "Error al consultar la base de datos: [detalle]"
        }
    """
    try:
        # Consultar la tabla 'formulas' filtrando por ID
        response = supabase.table("formulas").select("*").eq("id", formula_id).execute()

        # Verificar si se encontró la fórmula
        if not response.data:
            # Lista vacía = no se encontró
            return {
                "data": None,
                "error": "Fórmula no encontrada"
            }

        # Devolver solo el primer elemento (el objeto, no la lista)
        return {
            "data": response.data[0],
            "error": None
        }

    except Exception as e:
        # Si hay error de conexión/consulta, devolver formato estándar con error
        return {
            "data": None,
            "error": f"Error al consultar la base de datos: {str(e)}"
        }
