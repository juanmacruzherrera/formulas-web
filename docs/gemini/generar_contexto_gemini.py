#!/usr/bin/env python3
"""
Script para generar contexto completo del proyecto para Google AI Studio (Gemini)

Fecha: 8 Enero 2026 - 20:15h
Autor: Claude Sonnet 4.5

USO:
    cd /Volumes/Akitio01/Claude_MCP/formulas-web
    python3 docs/gemini/generar_contexto_gemini.py

SALIDA:
    docs/gemini/contexto_completo_proyecto.md
"""

import os
import sys
from datetime import datetime
from pathlib import Path

# Añadir raíz al path para importar supabase_client
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

# Carpetas a incluir
CARPETAS_BACKEND = [
    'backend/services',
    'backend/routes',
    'backend/scripts'
]

CARPETAS_FRONTEND = [
    'frontend/js',
    'frontend/css',
    'frontend'  # Para index.html
]

# Archivos raíz importantes
ARCHIVOS_RAIZ = [
    'CLAUDE.md',
    'README.md'
]

# Extensiones a incluir
EXTENSIONES_BACKEND = {'.py', '.sql'}
EXTENSIONES_FRONTEND = {'.js', '.html', '.css'}

# Carpetas/archivos a IGNORAR
IGNORAR = {
    '__pycache__',
    'venv',
    'node_modules',
    '.git',
    '.pytest_cache',
    'dist',
    'build',
    '.DS_Store',
    '.env'
}

def debe_ignorar(path):
    """Verifica si un path debe ser ignorado"""
    parts = Path(path).parts
    return any(ig in parts for ig in IGNORAR)

def obtener_esquema_supabase():
    """Obtiene el esquema de las tablas de Supabase"""
    try:
        from backend.services.supabase_client import supabase

        # Consultar esquema de tabla formulas
        result = supabase.table("formulas").select("*").limit(1).execute()

        if result.data:
            columnas_formulas = list(result.data[0].keys())
        else:
            columnas_formulas = []

        # Consultar esquema de tabla calculos
        result2 = supabase.table("calculos").select("*").limit(1).execute()

        if result2.data:
            columnas_calculos = list(result2.data[0].keys())
        else:
            columnas_calculos = []

        esquema = f"""
## Tabla: formulas
Columnas:
{chr(10).join(f'- {col}' for col in columnas_formulas)}

## Tabla: calculos
Columnas:
{chr(10).join(f'- {col}' for col in columnas_calculos)}

**Relaciones:**
- calculos.formula_id → formulas.id (FK)
"""
        return esquema

    except Exception as e:
        return f"⚠️ No se pudo conectar a Supabase: {e}\n\nPor favor, añade manualmente el esquema de las tablas."

def generar_contexto():
    """Genera el archivo MD con todo el contexto del proyecto"""

    raiz = Path(__file__).parent.parent.parent
    output_path = raiz / 'docs' / 'gemini' / 'contexto_completo_proyecto.md'

    contenido = []

    # Header
    contenido.append(f"""# Contexto Completo del Proyecto - Formulas Web
**Generado:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Para:** Google AI Studio (Gemini 2.0)
**Proyecto:** Visualizador de Fórmulas Matemáticas y Físicas

---

## 📋 INFORMACIÓN DEL PROYECTO

**Stack Tecnológico:**
- **Backend:** Python (FastAPI) + Supabase (PostgreSQL)
- **Frontend:** HTML + CSS + JavaScript Vanilla
- **Gráficos:** Plotly.js
- **Hosting:** Railway (Backend) + Cloudflare Pages (Frontend)

**URLs:**
- Frontend: https://formulas-web.pages.dev
- Backend: https://web-production-daa0.up.railway.app
- GitHub: https://github.com/juanmacruzherrera/formulas-web

**Estado actual:**
- ✅ FASES 6.1, 6.2, 6.3 completas
- ✅ Backend FASE 6.4 completo (4 fórmulas 3D)
- ❌ Frontend FASE 6.4 incompleto (5 problemas críticos)

**Documentación de problemas actuales:**
`docs/contexto_opus/20260108_estado_fase_6_4_problemas.md`

---

## 🗂️ ESTRUCTURA DEL PROYECTO

```
formulas-web/
├── backend/
│   ├── main.py                 # Entry point FastAPI
│   ├── services/
│   │   ├── supabase_client.py  # Conexión Supabase
│   │   └── calculadora.py      # Funciones matemáticas
│   ├── routes/
│   │   ├── formulas.py         # Endpoints /api/formulas
│   │   └── calculos.py         # Endpoints /api/calcular
│   └── scripts/                # Scripts de utilidad
├── frontend/
│   ├── index.html              # HTML principal
│   ├── js/
│   │   ├── api.js              # Llamadas al backend
│   │   ├── app.js              # Lógica principal
│   │   ├── graficos.js         # Renderizado Plotly
│   │   └── animacion.js        # Animaciones 2D/3D
│   └── css/
│       └── styles.css          # Estilos custom
└── docs/                       # Documentación
    ├── contexto_opus/          # Contexto para Opus
    └── aprendizaje/            # Registro de cambios
```

---
""")

    # Archivos raíz
    contenido.append("## 📄 ARCHIVOS RAÍZ\n")
    for archivo in ARCHIVOS_RAIZ:
        path = raiz / archivo
        if path.exists():
            contenido.append(f"### Archivo: {archivo}\n")
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    codigo = f.read()
                contenido.append(f"```markdown\n{codigo}\n```\n")
            except Exception as e:
                contenido.append(f"⚠️ Error al leer: {e}\n")

    # Backend
    contenido.append("\n---\n\n# 🐍 BACKEND (Python + FastAPI)\n")

    for carpeta in CARPETAS_BACKEND:
        carpeta_path = raiz / carpeta
        if not carpeta_path.exists():
            continue

        contenido.append(f"\n## Carpeta: {carpeta}\n")

        for archivo in sorted(carpeta_path.rglob('*')):
            if archivo.is_file() and archivo.suffix in EXTENSIONES_BACKEND:
                if debe_ignorar(archivo):
                    continue

                relpath = archivo.relative_to(raiz)
                contenido.append(f"\n### Archivo: {relpath}\n")

                try:
                    with open(archivo, 'r', encoding='utf-8') as f:
                        codigo = f.read()
                    contenido.append(f"```python\n{codigo}\n```\n")
                except Exception as e:
                    contenido.append(f"⚠️ Error al leer: {e}\n")

    # Frontend
    contenido.append("\n---\n\n# 🌐 FRONTEND (HTML + CSS + JavaScript)\n")

    for carpeta in CARPETAS_FRONTEND:
        carpeta_path = raiz / carpeta
        if not carpeta_path.exists():
            continue

        if carpeta == 'frontend':
            # Solo index.html de la raíz
            index_path = carpeta_path / 'index.html'
            if index_path.exists():
                contenido.append(f"\n### Archivo: frontend/index.html\n")
                try:
                    with open(index_path, 'r', encoding='utf-8') as f:
                        codigo = f.read()
                    contenido.append(f"```html\n{codigo}\n```\n")
                except Exception as e:
                    contenido.append(f"⚠️ Error al leer: {e}\n")
            continue

        contenido.append(f"\n## Carpeta: {carpeta}\n")

        for archivo in sorted(carpeta_path.rglob('*')):
            if archivo.is_file() and archivo.suffix in EXTENSIONES_FRONTEND:
                if debe_ignorar(archivo):
                    continue

                relpath = archivo.relative_to(raiz)
                contenido.append(f"\n### Archivo: {relpath}\n")

                ext = archivo.suffix.lstrip('.')
                lang = 'javascript' if ext == 'js' else ext

                try:
                    with open(archivo, 'r', encoding='utf-8') as f:
                        codigo = f.read()
                    contenido.append(f"```{lang}\n{codigo}\n```\n")
                except Exception as e:
                    contenido.append(f"⚠️ Error al leer: {e}\n")

    # Base de datos
    contenido.append("\n---\n\n# 🗄️ BASE DE DATOS (Supabase)\n")
    contenido.append(obtener_esquema_supabase())

    # Footer
    contenido.append(f"""
---

## 📊 ESTADÍSTICAS

- **Total líneas de código:** ~{sum(1 for _ in contenido if '```' not in _)}
- **Archivos incluidos:** Backend (Python) + Frontend (JS/HTML/CSS)
- **Esquema BD:** Supabase (PostgreSQL)

## 🎯 CÓMO USAR ESTE ARCHIVO EN GOOGLE AI STUDIO

1. **Sube este archivo** a Google AI Studio (botón +)
2. **Sube también las capturas** de los errores (si las tienes)
3. **Sube el documento de problemas:** `docs/contexto_opus/20260108_estado_fase_6_4_problemas.md`

4. **Usa este prompt:**

```
Analiza este proyecto Full Stack de visualización de fórmulas.

CONTEXTO:
- Backend: Python/FastAPI en Railway
- Frontend: JS Vanilla en Cloudflare
- BD: Supabase (PostgreSQL)

ESTADO ACTUAL:
- Backend 3D completo ✅
- Frontend 3D con 5 problemas ❌

Lee el archivo "20260108_estado_fase_6_4_problemas.md" para ver los problemas.

PREGUNTA:
¿Ves los 5 problemas identificados?
¿Hay errores adicionales que Claude no detectó?
¿Las soluciones propuestas son correctas?
Dame código específico para arreglar cada problema.
```

---

**FIN DEL CONTEXTO**
**Generado con:** Claude Sonnet 4.5
""")

    # Escribir archivo
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(contenido))

    print(f"✅ Contexto generado en: {output_path}")
    print(f"📊 Tamaño: {output_path.stat().st_size / 1024:.1f} KB")
    print(f"📄 Listo para subir a Google AI Studio")

if __name__ == "__main__":
    print("🚀 Generando contexto para Google AI Studio (Gemini)...")
    generar_contexto()
