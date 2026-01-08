#!/usr/bin/env python3
"""
Script para insertar fórmulas 3D en Supabase
Ejecutar desde la raíz del proyecto:
    python3 backend/scripts/insertar_formulas_3d.py
"""

import sys
import os

# Añadir el directorio raíz al PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from backend.services.supabase_client import supabase

# Definir las 4 fórmulas 3D
formulas_3d = [
    {
        "nombre": "Hélice 3D",
        "formula_latex": r"x = r \cdot \cos(t), \quad y = r \cdot \sin(t), \quad z = c \cdot t",
        "categoria": "geometria_3d",
        "variables_usuario": {"r": 5, "c": 0.5},
        "variable_rango": "t",
        "rango_min": 0,
        "rango_max": 20,
        "rango_dinamico": True
    },
    {
        "nombre": "Atractor de Lorenz",
        "formula_latex": r"\frac{dx}{dt} = \sigma(y-x), \quad \frac{dy}{dt} = x(\rho-z)-y, \quad \frac{dz}{dt} = xy-\beta z",
        "categoria": "geometria_3d",
        "variables_usuario": {"sigma": 10, "rho": 28, "beta": 2.667, "puntos": 2000},
        "variable_rango": "t",
        "rango_min": 0,
        "rango_max": 50,
        "rango_dinamico": True
    },
    {
        "nombre": "Toro 3D",
        "formula_latex": r"x = (R + r\cos v)\cos u, \quad y = (R + r\cos v)\sin u, \quad z = r\sin v",
        "categoria": "geometria_3d",
        "variables_usuario": {"R": 3, "r": 1, "u_min": 0, "u_max": 6.28, "v_min": 0, "v_max": 6.28, "puntos_u": 50, "puntos_v": 50},
        "variable_rango": "u",
        "rango_min": 0,
        "rango_max": 6.28,
        "rango_dinamico": True
    },
    {
        "nombre": "Ondas 3D",
        "formula_latex": r"z = A \cdot \sin(f \cdot \sqrt{x^2 + y^2})",
        "categoria": "geometria_3d",
        "variables_usuario": {"amplitud": 1, "frecuencia": 1, "x_min": -5, "x_max": 5, "y_min": -5, "y_max": 5, "puntos": 50},
        "variable_rango": "x",
        "rango_min": -5,
        "rango_max": 5,
        "rango_dinamico": True
    }
]

def insertar_formulas():
    """Inserta las fórmulas 3D en Supabase"""
    print("🚀 Insertando fórmulas 3D en Supabase...\n")

    for formula in formulas_3d:
        try:
            # Verificar si ya existe
            existing = supabase.table("formulas").select("id").eq("nombre", formula["nombre"]).execute()

            if existing.data:
                print(f"⚠️  '{formula['nombre']}' ya existe (ID: {existing.data[0]['id']})")
                continue

            # Insertar nueva fórmula
            result = supabase.table("formulas").insert(formula).execute()

            if result.data:
                print(f"✅ '{formula['nombre']}' insertada (ID: {result.data[0]['id']})")
            else:
                print(f"❌ Error al insertar '{formula['nombre']}'")

        except Exception as e:
            print(f"❌ Error con '{formula['nombre']}': {e}")

    print("\n✅ Proceso completado. Verificando...")

    # Verificar fórmulas 3D
    result = supabase.table("formulas").select("id, nombre, categoria").eq("categoria", "geometria_3d").execute()

    if result.data:
        print(f"\n📊 Fórmulas 3D en Supabase ({len(result.data)} total):")
        for formula in result.data:
            print(f"   - ID {formula['id']}: {formula['nombre']}")
    else:
        print("\n⚠️  No se encontraron fórmulas 3D en la base de datos")

if __name__ == "__main__":
    insertar_formulas()
