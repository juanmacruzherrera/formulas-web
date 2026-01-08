#!/usr/bin/env python3
# backend/scripts/corregir_variables_usuario.py
# ============================================
# QUÉ HACE: Corrige el formato de variables_usuario en Supabase
# CONSUME: Tabla 'formulas' de Supabase
# EXPONE: Actualiza registros con formato correcto
# RELACIONADO CON:
#   - Usa: services/supabase_client.py
#   - Modifica: Tabla formulas en Supabase
# ============================================

import sys
import os

# Añadir el directorio padre al path para poder importar módulos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.supabase_client import supabase

# Mapeo de fórmulas a sus variables correctas
VARIABLES_CORRECTAS = {
    "MRU": ["x₀", "v", "t"],
    "MRUA": ["x₀", "v₀", "a", "t"],
    "Caída Libre": ["h₀", "g", "t"],
    "Parábola": ["a", "b", "c", "x"],
    "Seno": ["A", "ω", "φ", "t"],
    "Coseno": ["A", "ω", "φ", "t"],
    "Exponencial": ["a", "b", "x"],
    "Logaritmo": ["a", "b", "x"],
    "Circunferencia": ["r", "θ"],
}

def verificar_formulas():
    """
    Verifica el estado actual de las fórmulas en Supabase.
    Muestra qué fórmulas tienen variables_usuario incorrectas.
    """
    print("🔍 Verificando fórmulas en Supabase...\n")

    try:
        # Obtener todas las fórmulas
        response = supabase.table("formulas").select("*").execute()
        formulas = response.data

        print(f"✅ Encontradas {len(formulas)} fórmulas\n")
        print("=" * 80)

        formulas_incorrectas = []

        for formula in formulas:
            nombre = formula['nombre']
            variables_actuales = formula.get('variables_usuario', [])
            variables_correctas = VARIABLES_CORRECTAS.get(nombre, [])

            # Verificar si las variables son incorrectas
            # (ej: ["0", "1", "2"] en lugar de ["x₀", "v₀", "a"])
            es_incorrecta = False

            if not variables_actuales:
                es_incorrecta = True
                razon = "Campo vacío"
            elif all(v.isdigit() for v in variables_actuales):
                es_incorrecta = True
                razon = "Contiene solo números (0,1,2...)"
            elif variables_actuales != variables_correctas and variables_correctas:
                es_incorrecta = True
                razon = "Variables no coinciden con el mapeo correcto"

            # Mostrar estado
            status = "❌" if es_incorrecta else "✅"
            print(f"{status} {nombre} (ID: {formula['id']})")
            print(f"   Actual:   {variables_actuales}")
            if variables_correctas:
                print(f"   Correcta: {variables_correctas}")
            if es_incorrecta:
                print(f"   Razón: {razon}")
                formulas_incorrectas.append({
                    'id': formula['id'],
                    'nombre': nombre,
                    'actual': variables_actuales,
                    'correcta': variables_correctas
                })
            print()

        print("=" * 80)
        print(f"\n📊 Resumen:")
        print(f"   Total: {len(formulas)}")
        print(f"   Correctas: {len(formulas) - len(formulas_incorrectas)}")
        print(f"   Incorrectas: {len(formulas_incorrectas)}")

        return formulas_incorrectas

    except Exception as e:
        print(f"❌ Error al verificar fórmulas: {str(e)}")
        raise

def corregir_formulas(formulas_incorrectas):
    """
    Corrige las fórmulas que tienen variables_usuario incorrectas.

    Args:
        formulas_incorrectas: Lista de diccionarios con info de fórmulas a corregir
    """
    if not formulas_incorrectas:
        print("\n✅ No hay fórmulas que corregir. Todo está correcto.")
        return

    print(f"\n🔧 Corrigiendo {len(formulas_incorrectas)} fórmulas...\n")

    corregidas = 0
    errores = 0

    for formula in formulas_incorrectas:
        try:
            # Actualizar la fórmula en Supabase
            response = supabase.table("formulas").update({
                "variables_usuario": formula['correcta']
            }).eq("id", formula['id']).execute()

            print(f"✅ {formula['nombre']} (ID: {formula['id']})")
            print(f"   {formula['actual']} → {formula['correcta']}")
            corregidas += 1

        except Exception as e:
            print(f"❌ Error al corregir {formula['nombre']}: {str(e)}")
            errores += 1

    print(f"\n📊 Resultado:")
    print(f"   Corregidas: {corregidas}")
    print(f"   Errores: {errores}")

def main():
    """
    Función principal del script.
    """
    print("\n" + "=" * 80)
    print(" SCRIPT DE CORRECCIÓN: variables_usuario en Supabase")
    print("=" * 80 + "\n")

    # Verificar estado actual
    formulas_incorrectas = verificar_formulas()

    # Si hay fórmulas incorrectas, preguntar si se deben corregir
    if formulas_incorrectas:
        print("\n" + "=" * 80)
        respuesta = input("\n¿Deseas corregir estas fórmulas? (s/n): ").lower()

        if respuesta == 's':
            corregir_formulas(formulas_incorrectas)
            print("\n✅ Proceso completado.")
        else:
            print("\n❌ Corrección cancelada.")

    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()
