#!/usr/bin/env python3
# insertar_formulas.py
# ============================================
# QUÉ HACE: Inserta las 14 fórmulas nuevas en Supabase
# CONSUME: Cliente de Supabase
# EXPONE: Función para insertar fórmulas
# ============================================

from backend.services.supabase_client import supabase
import json

# Definir las 14 fórmulas nuevas
# NOTA: Estructura adaptada al esquema real de Supabase
# - NO incluir "descripcion" (no existe en la tabla)
# - variables_usuario: objeto plano {variable: valor_default}
# - Incluir rango_dinamico: False
FORMULAS_NUEVAS = [
    # =============================================
    # FÍSICA (5 fórmulas) - Ya existe MRU (id=1)
    # =============================================

    # 2. MRUA - Movimiento Rectilíneo Uniformemente Acelerado
    {
        "nombre": "MRUA - Movimiento Uniformemente Acelerado",
        "categoria": "fisica",
        "formula_latex": r"x = x_0 + v_0 \cdot t + \frac{1}{2} a \cdot t^2",
        "variables_usuario": {"x0": 0, "v0": 5, "a": 2},
        "variable_rango": "t",
        "rango_min": 0,
        "rango_max": 10,
        "rango_dinamico": False
    },

    # 3. Caída Libre
    {
        "nombre": "Caída Libre",
        "categoria": "fisica",
        "formula_latex": r"y = y_0 - \frac{1}{2} g \cdot t^2",
        "variables_usuario": {"y0": 100, "g": 9.8},
        "variable_rango": "t",
        "rango_min": 0,
        "rango_max": 5,
        "rango_dinamico": False
    },

    # 4. Tiro Parabólico
    {
        "nombre": "Tiro Parabólico",
        "categoria": "fisica",
        "formula_latex": r"y = v_0 \cdot \sin(\theta) \cdot t - \frac{1}{2} g \cdot t^2",
        "variables_usuario": {"v0": 20, "theta": 45, "g": 9.8},
        "variable_rango": "t",
        "rango_min": 0,
        "rango_max": 5,
        "rango_dinamico": False
    },

    # 5. Movimiento Armónico Simple
    {
        "nombre": "Movimiento Armónico Simple",
        "categoria": "fisica",
        "formula_latex": r"x = A \cdot \cos(\omega \cdot t + \phi)",
        "variables_usuario": {"A": 5, "omega": 2, "phi": 0},
        "variable_rango": "t",
        "rango_min": 0,
        "rango_max": 10,
        "rango_dinamico": False
    },

    # 6. Onda Sinusoidal
    {
        "nombre": "Onda Sinusoidal",
        "categoria": "fisica",
        "formula_latex": r"y = A \cdot \sin(k \cdot x - \omega \cdot t)",
        "variables_usuario": {"A": 3, "k": 1, "omega": 0},
        "variable_rango": "x",
        "rango_min": 0,
        "rango_max": 20,
        "rango_dinamico": False
    },

    # =============================================
    # MATEMÁTICAS (5 fórmulas)
    # =============================================

    # 7. Parábola
    {
        "nombre": "Parábola",
        "categoria": "matematicas",
        "formula_latex": r"y = a \cdot x^2 + b \cdot x + c",
        "variables_usuario": {"a": 1, "b": 0, "c": 0},
        "variable_rango": "x",
        "rango_min": -10,
        "rango_max": 10,
        "rango_dinamico": False
    },

    # 8. Función Exponencial
    {
        "nombre": "Función Exponencial",
        "categoria": "matematicas",
        "formula_latex": r"y = a \cdot e^{b \cdot x}",
        "variables_usuario": {"a": 1, "b": 0.5},
        "variable_rango": "x",
        "rango_min": -2,
        "rango_max": 5,
        "rango_dinamico": False
    },

    # 9. Función Logarítmica
    {
        "nombre": "Función Logarítmica",
        "categoria": "matematicas",
        "formula_latex": r"y = a \cdot \ln(x) + b",
        "variables_usuario": {"a": 1, "b": 0},
        "variable_rango": "x",
        "rango_min": 0.1,
        "rango_max": 10,
        "rango_dinamico": False
    },

    # 10. Función Seno
    {
        "nombre": "Función Seno",
        "categoria": "matematicas",
        "formula_latex": r"y = A \cdot \sin(B \cdot x + C)",
        "variables_usuario": {"A": 1, "B": 1, "C": 0},
        "variable_rango": "x",
        "rango_min": 0,
        "rango_max": 12.57,
        "rango_dinamico": False
    },

    # 11. Circunferencia (paramétrica)
    {
        "nombre": "Circunferencia",
        "categoria": "matematicas",
        "formula_latex": r"x = r \cdot \cos(\theta), \quad y = r \cdot \sin(\theta)",
        "variables_usuario": {"r": 5},
        "variable_rango": "theta",
        "rango_min": 0,
        "rango_max": 6.28,
        "rango_dinamico": False
    },

    # =============================================
    # CURVAS EXÓTICAS (4 fórmulas)
    # =============================================

    # 12. Espiral de Arquímedes
    {
        "nombre": "Espiral de Arquímedes",
        "categoria": "curvas_exoticas",
        "formula_latex": r"r = a + b \cdot \theta",
        "variables_usuario": {"a": 0, "b": 0.5},
        "variable_rango": "theta",
        "rango_min": 0,
        "rango_max": 31.4,
        "rango_dinamico": False
    },

    # 13. Espiral Logarítmica
    {
        "nombre": "Espiral Logarítmica",
        "categoria": "curvas_exoticas",
        "formula_latex": r"r = a \cdot e^{b \cdot \theta}",
        "variables_usuario": {"a": 0.5, "b": 0.15},
        "variable_rango": "theta",
        "rango_min": 0,
        "rango_max": 25,
        "rango_dinamico": False
    },

    # 14. Cardioide
    {
        "nombre": "Cardioide",
        "categoria": "curvas_exoticas",
        "formula_latex": r"r = a \cdot (1 + \cos(\theta))",
        "variables_usuario": {"a": 3},
        "variable_rango": "theta",
        "rango_min": 0,
        "rango_max": 6.28,
        "rango_dinamico": False
    },

    # 15. Lemniscata de Bernoulli
    {
        "nombre": "Lemniscata de Bernoulli",
        "categoria": "curvas_exoticas",
        "formula_latex": r"r^2 = a^2 \cdot \cos(2\theta)",
        "variables_usuario": {"a": 5},
        "variable_rango": "theta",
        "rango_min": 0,
        "rango_max": 6.28,
        "rango_dinamico": False
    }
]


def insertar_formulas():
    """
    Inserta las 14 fórmulas nuevas en Supabase.

    Returns:
        int: Número de fórmulas insertadas exitosamente
    """
    print("🚀 Iniciando inserción de fórmulas...")
    print(f"📊 Total de fórmulas a insertar: {len(FORMULAS_NUEVAS)}")
    print()

    insertadas = 0
    errores = 0

    for i, formula in enumerate(FORMULAS_NUEVAS, start=1):
        try:
            # Convertir variables_usuario a JSON (Supabase espera JSONB)
            formula_para_bd = formula.copy()
            formula_para_bd["variables_usuario"] = json.dumps(formula["variables_usuario"])

            # Insertar en Supabase
            response = supabase.table("formulas").insert(formula_para_bd).execute()

            print(f"✅ [{i}/{len(FORMULAS_NUEVAS)}] Insertada: {formula['nombre']}")
            insertadas += 1

        except Exception as e:
            print(f"❌ [{i}/{len(FORMULAS_NUEVAS)}] Error al insertar {formula['nombre']}: {str(e)}")
            errores += 1

    print()
    print("="*60)
    print(f"✅ Fórmulas insertadas exitosamente: {insertadas}")
    print(f"❌ Errores: {errores}")
    print("="*60)

    # Verificar total de fórmulas en la BD
    response = supabase.table("formulas").select("*").execute()
    print(f"📊 Total de fórmulas en la base de datos ahora: {len(response.data)}")

    # Mostrar las fórmulas por categoría
    if response.data:
        print("\n📋 Fórmulas por categoría:")
        categorias = {}
        for f in response.data:
            cat = f.get('categoria', 'sin_categoria')
            if cat not in categorias:
                categorias[cat] = []
            categorias[cat].append(f['nombre'])

        for cat, formulas in sorted(categorias.items()):
            print(f"\n  {cat.upper()}:")
            for nombre in formulas:
                print(f"    - {nombre}")

    return insertadas


if __name__ == "__main__":
    print("🔍 Script de inserción de fórmulas\n")
    insertadas = insertar_formulas()

    if insertadas == len(FORMULAS_NUEVAS):
        print("\n🎉 ¡TODAS LAS FÓRMULAS INSERTADAS CORRECTAMENTE!")
    else:
        print(f"\n⚠️  Solo se insertaron {insertadas}/{len(FORMULAS_NUEVAS)} fórmulas")
