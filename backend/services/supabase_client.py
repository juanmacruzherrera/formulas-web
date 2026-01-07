# backend/services/supabase_client.py
# ============================================
# QUÉ HACE: Crea y exporta el cliente de Supabase
# CONSUME: Variables de entorno (.env)
# EXPONE: Objeto 'supabase' para usar en otros archivos
# RELACIONADO CON:
#   - Usado por: routes/formulas.py, routes/calculos.py
#   - Depende de: .env
# ============================================

import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener credenciales desde variables de entorno
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")

# Validar que las credenciales existen
if not url or not key:
    raise ValueError(
        "❌ Error: Falta SUPABASE_URL o SUPABASE_KEY en el archivo .env\n"
        "Asegúrate de que el archivo .env existe y tiene estas variables."
    )

# Crear el cliente de Supabase (singleton)
supabase: Client = create_client(url, key)

# Función de prueba para verificar la conexión
def test_conexion():
    """
    Función de prueba que verifica la conexión con Supabase.
    Intenta obtener todas las fórmulas de la tabla 'formulas'.

    Returns:
        list: Lista de fórmulas si la conexión es exitosa

    Raises:
        Exception: Si hay error en la conexión
    """
    try:
        # Intentar leer la tabla 'formulas'
        response = supabase.table("formulas").select("*").execute()

        # Mostrar resultado
        print(f"✅ Conexión exitosa con Supabase")
        print(f"📊 Fórmulas encontradas: {len(response.data)}")

        # Mostrar las fórmulas encontradas
        if response.data:
            print("\n📋 Fórmulas en la base de datos:")
            for formula in response.data:
                print(f"   - ID: {formula['id']} | {formula['nombre']} | {formula['categoria']}")

        return response.data

    except Exception as e:
        print(f"❌ Error al conectar con Supabase: {str(e)}")
        raise

# Este bloque solo se ejecuta si ejecutamos este archivo directamente
# No se ejecuta cuando importamos el módulo en otros archivos
if __name__ == "__main__":
    print("🔍 Probando conexión con Supabase...")
    test_conexion()
