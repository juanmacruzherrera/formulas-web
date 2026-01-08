# backend/routes/calculos.py
# ============================================
# QUÉ HACE: Endpoints para realizar cálculos de fórmulas
# CONSUME:
#   - Datos del usuario (formula_id + valores) vía POST
#   - Fórmulas de Supabase (tabla formulas)
#   - Historial de cálculos (tabla calculos)
# EXPONE:
#   - POST /api/calcular → Calcula, guarda y devuelve resultado
#   - GET /api/historial → Devuelve historial de cálculos con JOIN a formulas
# RELACIONADO CON:
#   - Usa: backend/services/supabase_client.py (conexión BD)
#   - Usa: backend/services/calculadora.py (función calcular_mru)
#   - Usado por: frontend/js/api.js (próxima fase)
# ============================================

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict, Any
from backend.services.supabase_client import supabase
from backend.services.calculadora import (
    calcular_mru,
    calcular_mrua,
    calcular_caida_libre,
    calcular_tiro_parabolico,
    calcular_armonico_simple,
    calcular_onda_sinusoidal,
    calcular_parabola,
    calcular_exponencial,
    calcular_logaritmica,
    calcular_seno,
    calcular_circunferencia,
    calcular_espiral_arquimedes,
    calcular_espiral_logaritmica,
    calcular_cardioide,
    calcular_lemniscata,
    # Funciones 3D
    calcular_helice,
    calcular_lorenz,
    calcular_toro,
    calcular_ondas_3d
)

# Crear router con prefijo /api y etiqueta "calculos"
router = APIRouter(
    prefix="/api",
    tags=["calculos"]
)

# Modelo Pydantic: define qué datos esperamos recibir
class DatosCalculo(BaseModel):
    """
    Modelo de datos para una petición de cálculo.

    Attributes:
        formula_id (int): ID de la fórmula a calcular
        valores (dict): Diccionario con los parámetros necesarios
                       Ejemplo para MRU: {"x0": 0, "v": 5, "t_min": 0, "t_max": 10}
    """
    formula_id: int
    valores: Dict[str, Any]  # Dict puede contener cualquier tipo de valor


@router.post("/calcular")
def calcular(datos: DatosCalculo):
    """
    Calcula una fórmula matemática, guarda el resultado en BD y lo devuelve.

    Flujo:
    1. Valida que la fórmula existe en la BD
    2. Según el tipo de fórmula, llama a la función de cálculo apropiada
    3. Guarda el cálculo en la tabla 'calculos' (historial)
    4. Devuelve los puntos calculados para que el frontend grafique

    Args:
        datos (DatosCalculo): Objeto validado por Pydantic con formula_id y valores

    Returns:
        dict: {
            "data": {
                "formula": {...},      # Info de la fórmula usada
                "valores": {...},      # Valores que se usaron
                "resultado": {...}     # Puntos calculados (t, x)
            },
            "error": None
        }

    Raises:
        HTTPException 404: Si la fórmula no existe
        HTTPException 400: Si faltan valores requeridos
        HTTPException 500: Si hay error en BD o cálculo
    """
    try:
        # PASO 1: Obtener la fórmula de la base de datos
        formula_response = supabase.table("formulas").select("*").eq("id", datos.formula_id).execute()

        if not formula_response.data:
            return {
                "data": None,
                "error": f"Fórmula con ID {datos.formula_id} no encontrada"
            }

        formula = formula_response.data[0]

        # PASO 2: Calcular según el tipo de fórmula
        # Identificamos el tipo por el nombre ya que el campo 'tipo' no existe en la BD
        # Extraemos rango dinámico de la fórmula o usamos valores del usuario
        rango_min = datos.valores.get(formula["variable_rango"] + "_min", formula.get("rango_min", 0))
        rango_max = datos.valores.get(formula["variable_rango"] + "_max", formula.get("rango_max", 10))

        # Identificar fórmula por nombre y llamar función correspondiente
        if "MRU" in formula["nombre"] and "Uniformemente Acelerado" not in formula["nombre"]:
            resultado = calcular_mru(
                x0=datos.valores.get("x0", 0),
                v=datos.valores.get("v", 5),
                t_min=rango_min,
                t_max=rango_max
            )

        elif "MRUA" in formula["nombre"] or "Uniformemente Acelerado" in formula["nombre"]:
            resultado = calcular_mrua(
                x0=datos.valores.get("x0", 0),
                v0=datos.valores.get("v0", 5),
                a=datos.valores.get("a", 2),
                t_min=rango_min,
                t_max=rango_max
            )

        elif "Caída Libre" in formula["nombre"]:
            resultado = calcular_caida_libre(
                y0=datos.valores.get("y0", 100),
                g=datos.valores.get("g", 9.8),
                t_min=rango_min,
                t_max=rango_max
            )

        elif "Tiro Parabólico" in formula["nombre"]:
            resultado = calcular_tiro_parabolico(
                v0=datos.valores.get("v0", 20),
                theta=datos.valores.get("theta", 45),
                g=datos.valores.get("g", 9.8),
                t_min=rango_min,
                t_max=rango_max
            )

        elif "Armónico Simple" in formula["nombre"]:
            resultado = calcular_armonico_simple(
                A=datos.valores.get("A", 5),
                omega=datos.valores.get("omega", 2),
                phi=datos.valores.get("phi", 0),
                t_min=rango_min,
                t_max=rango_max
            )

        elif "Onda Sinusoidal" in formula["nombre"]:
            resultado = calcular_onda_sinusoidal(
                A=datos.valores.get("A", 3),
                k=datos.valores.get("k", 1),
                omega=datos.valores.get("omega", 0),
                x_min=rango_min,
                x_max=rango_max
            )

        elif "Parábola" in formula["nombre"]:
            resultado = calcular_parabola(
                a=datos.valores.get("a", 1),
                b=datos.valores.get("b", 0),
                c=datos.valores.get("c", 0),
                x_min=rango_min,
                x_max=rango_max
            )

        elif "Exponencial" in formula["nombre"]:
            resultado = calcular_exponencial(
                a=datos.valores.get("a", 1),
                b=datos.valores.get("b", 0.5),
                x_min=rango_min,
                x_max=rango_max
            )

        elif "Logarítmica" in formula["nombre"] and "Espiral" not in formula["nombre"]:
            resultado = calcular_logaritmica(
                a=datos.valores.get("a", 1),
                b=datos.valores.get("b", 0),
                x_min=rango_min,
                x_max=rango_max
            )

        elif "Seno" in formula["nombre"]:
            resultado = calcular_seno(
                A=datos.valores.get("A", 1),
                B=datos.valores.get("B", 1),
                C=datos.valores.get("C", 0),
                x_min=rango_min,
                x_max=rango_max
            )

        elif "Circunferencia" in formula["nombre"]:
            resultado = calcular_circunferencia(
                r=datos.valores.get("r", 5),
                theta_min=rango_min,
                theta_max=rango_max
            )

        elif "Arquímedes" in formula["nombre"]:
            resultado = calcular_espiral_arquimedes(
                a=datos.valores.get("a", 0),
                b=datos.valores.get("b", 0.5),
                theta_min=rango_min,
                theta_max=rango_max
            )

        elif "Logarítmica" in formula["nombre"] and "Espiral" in formula["nombre"]:
            resultado = calcular_espiral_logaritmica(
                a=datos.valores.get("a", 0.5),
                b=datos.valores.get("b", 0.15),
                theta_min=rango_min,
                theta_max=rango_max
            )

        elif "Cardioide" in formula["nombre"]:
            resultado = calcular_cardioide(
                a=datos.valores.get("a", 3),
                theta_min=rango_min,
                theta_max=rango_max
            )

        elif "Lemniscata" in formula["nombre"]:
            resultado = calcular_lemniscata(
                a=datos.valores.get("a", 5),
                theta_min=rango_min,
                theta_max=rango_max
            )

        # ============================================
        # FÓRMULAS 3D
        # ============================================

        elif "Hélice" in formula["nombre"]:
            resultado = calcular_helice(
                r=datos.valores.get("r", 5),
                c=datos.valores.get("c", 0.5),
                t_min=rango_min,
                t_max=rango_max
            )

        elif "Lorenz" in formula["nombre"]:
            resultado = calcular_lorenz(
                sigma=datos.valores.get("sigma", 10),
                rho=datos.valores.get("rho", 28),
                beta=datos.valores.get("beta", 8/3),
                t_max=rango_max,
                puntos=datos.valores.get("puntos", 2000)
            )

        elif "Toro" in formula["nombre"]:
            resultado = calcular_toro(
                R=datos.valores.get("R", 3),
                r=datos.valores.get("r", 1),
                u_min=datos.valores.get("u_min", 0),
                u_max=datos.valores.get("u_max", 6.28),
                v_min=datos.valores.get("v_min", 0),
                v_max=datos.valores.get("v_max", 6.28),
                puntos_u=datos.valores.get("puntos_u", 50),
                puntos_v=datos.valores.get("puntos_v", 50)
            )

        elif "Ondas 3D" in formula["nombre"]:
            resultado = calcular_ondas_3d(
                amplitud=datos.valores.get("amplitud", 1),
                frecuencia=datos.valores.get("frecuencia", 1),
                x_min=datos.valores.get("x_min", -5),
                x_max=datos.valores.get("x_max", 5),
                y_min=datos.valores.get("y_min", -5),
                y_max=datos.valores.get("y_max", 5),
                puntos=datos.valores.get("puntos", 50)
            )

        else:
            # Si el tipo de fórmula no está implementado
            return {
                "data": None,
                "error": f"Fórmula '{formula['nombre']}' no tiene implementación de cálculo aún"
            }

        # PASO 3: Guardar el cálculo en la tabla 'calculos' (historial)
        calculo_guardado = supabase.table("calculos").insert({
            "formula_id": datos.formula_id,
            "valores_entrada": datos.valores,  # La columna se llama 'valores_entrada' en Supabase
            "resultado": resultado
        }).execute()

        # PASO 4: Devolver el resultado
        return {
            "data": {
                "formula": {
                    "id": formula["id"],
                    "nombre": formula["nombre"],
                    "categoria": formula.get("categoria", "")
                },
                "valores": datos.valores,
                "resultado": resultado,
                "calculo_id": calculo_guardado.data[0]["id"] if calculo_guardado.data else None
            },
            "error": None
        }

    except Exception as e:
        # Capturar cualquier error inesperado
        return {
            "data": None,
            "error": f"Error al procesar el cálculo: {str(e)}"
        }


@router.get("/historial")
def obtener_historial(limite: int = 20):
    """
    Obtiene el historial de cálculos realizados, ordenados por más recientes primero.

    Este endpoint consulta la tabla 'calculos' y hace un JOIN automático con la tabla
    'formulas' para incluir información completa de cada fórmula utilizada.

    Args:
        limite (int, optional): Cantidad máxima de cálculos a devolver. Por defecto 20.
                               El usuario puede personalizar: /api/historial?limite=10

    Returns:
        dict: {
            "data": [
                {
                    "id": 2,
                    "formula_id": 1,
                    "valores_entrada": {"x0": 0, "v": 5, ...},
                    "resultado": {"t": [...], "x": [...]},
                    "created_at": "2025-12-29T14:30:00+00:00",
                    "formulas": {
                        "id": 1,
                        "nombre": "MRU - Movimiento Rectilíneo Uniforme",
                        "categoria": "fisica",
                        "formula_latex": "x = x_0 + v \\\\cdot t",
                        ...
                    }
                },
                ...
            ],
            "error": None
        }

    Example:
        GET http://localhost:8000/api/historial         # Últimos 20
        GET http://localhost:8000/api/historial?limite=5  # Últimos 5

    Technical notes:
        - Usa .select("*, formulas(*)") para hacer JOIN automático
        - Ordenado por created_at DESC (más recientes primero)
        - El nombre "formulas" viene de la relación foreign key en Supabase
    """
    try:
        # Consultar tabla calculos con JOIN a formulas
        # "*" = todos los campos de calculos
        # "formulas(*)" = JOIN con tabla formulas, traer todos sus campos
        response = supabase.table("calculos") \
            .select("*, formulas(*)") \
            .order("created_at", desc=True) \
            .limit(limite) \
            .execute()

        # Supabase devuelve los datos con la fórmula anidada en cada cálculo
        # El objeto "formulas" contiene toda la info de la fórmula asociada

        return {
            "data": response.data,
            "error": None
        }

    except Exception as e:
        # Capturar cualquier error inesperado
        return {
            "data": None,
            "error": f"Error al obtener el historial: {str(e)}"
        }


# Bloque de prueba (solo se ejecuta si ejecutamos este archivo directamente)
if __name__ == "__main__":
    print("⚠️  Este archivo define rutas de FastAPI.")
    print("   Para probarlo, ejecuta:")
    print("   uvicorn backend.main:app --reload")
    print("   Luego usa curl o Postman para hacer POST a /api/calcular")
