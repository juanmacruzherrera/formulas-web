# PLAN DE TRABAJO - Proyecto Fórmulas Web

> **LEE CLAUDE.md PRIMERO** antes de empezar cualquier tarea.

> ⛔ **REGLA CRÍTICA:** Actualizar documentación = AÑADIR contenido.
> NUNCA borrar ni sobreescribir archivos `.md` existentes.
> Los errores y el proceso completo son parte del aprendizaje.

Este archivo contiene todas las tareas ordenadas. Claude Code debe:
1. Ejecutar tareas EN ORDEN (no saltar)
2. Documentar cada una en `docs/aprendizaje/`
3. Marcar ✅ cuando complete
4. Si falla, documentar el error y la solución

---

## ESTADO GENERAL

| Fase | Descripción | Tareas | Completadas |
|------|-------------|--------|-------------|
| 0 | Preparación | 1 | 1 |
| 1 | Conexión Python ↔ Supabase | 4 | 4 |
| 2 | Lógica de cálculo | 3 | 3 |
| 3 | Frontend básico | 4 | 4 |
| 4 | Integración completa | 2 | 2 |

---

## FASE 0: PREPARACIÓN

### Tarea 0.1: Crear entorno virtual e instalar dependencias
- **Estado:** ✅ Completado
- **Documentar en:** `docs/aprendizaje/01_entorno_virtual.md`

#### Qué hacer:
1. Crear entorno virtual en la carpeta del proyecto
2. Instalar dependencias: `fastapi`, `uvicorn`, `supabase`, `python-dotenv`
3. Crear `requirements.txt`

#### Comandos:
```bash
cd /Volumes/Akitio01/Claude_MCP/formulas-web
python3 -m venv venv
source venv/bin/activate
pip install fastapi uvicorn supabase python-dotenv
pip freeze > requirements.txt
```

#### Verificar:
```bash
pip list | grep fastapi
# Debe mostrar: fastapi 0.x.x
```

#### Documentar:
- Qué es un entorno virtual y por qué lo usamos
- Qué hace cada librería instalada
- Qué es requirements.txt y para qué sirve

---

## FASE 1: CONEXIÓN PYTHON ↔ SUPABASE

### Tarea 1.1: Crear el cliente de Supabase
- **Estado:** ✅ Completado
- **Archivo a crear:** `backend/services/supabase_client.py`
- **Documentar en:** `docs/aprendizaje/02_conexion_supabase.md`

#### Qué hacer:
1. Crear archivo que lea credenciales de .env
2. Crear cliente de Supabase
3. Función de prueba que obtenga las fórmulas

#### Código base:
```python
# supabase_client.py
import os
from dotenv import load_dotenv
from supabase import create_client, Client

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

# Función de prueba
def test_conexion():
    response = supabase.table("formulas").select("*").execute()
    print(f"Conexión exitosa. Fórmulas encontradas: {len(response.data)}")
    return response.data

if __name__ == "__main__":
    test_conexion()
```

#### Verificar:
```bash
cd /Volumes/Akitio01/Claude_MCP/formulas-web
source venv/bin/activate
python backend/services/supabase_client.py
# Debe mostrar: Conexión exitosa. Fórmulas encontradas: 1
```

#### Documentar:
- Qué es un cliente de API
- Cómo funciona dotenv
- Por qué separamos la conexión en su propio archivo

---

### Tarea 1.2: Crear endpoint de prueba (health check)
- **Estado:** ✅ Completado
- **Archivo a crear:** `backend/main.py`
- **Documentar en:** `docs/aprendizaje/03_primer_endpoint.md`

#### Qué hacer:
1. Crear aplicación FastAPI básica
2. Endpoint GET /health que devuelve {"status": "ok"}

#### Código base:
```python
# main.py
from fastapi import FastAPI

app = FastAPI(
    title="API Fórmulas Matemáticas",
    description="Backend para visualización de fórmulas",
    version="0.1.0"
)

@app.get("/health")
def health_check():
    """Verifica que el servidor está funcionando."""
    return {"status": "ok", "message": "Servidor funcionando correctamente"}
```

#### Verificar:
```bash
# Terminal 1: Iniciar servidor
cd /Volumes/Akitio01/Claude_MCP/formulas-web
source venv/bin/activate
uvicorn backend.main:app --reload

# Terminal 2: Probar endpoint
curl http://localhost:8000/health
# Debe devolver: {"status":"ok","message":"Servidor funcionando correctamente"}
```

#### Documentar:
- Qué es FastAPI y por qué lo elegimos
- Qué es un endpoint y cómo funciona el decorador @app.get
- Qué hace uvicorn
- Qué significa --reload

---

### Tarea 1.3: Endpoint para listar fórmulas
- **Estado:** ✅ Completado
- **Archivo a crear:** `backend/routes/formulas.py`
- **Archivo a modificar:** `backend/main.py` (importar el router)
- **Documentar en:** `docs/aprendizaje/04_endpoint_formulas.md`

#### Qué hacer:
1. Crear router de FastAPI para fórmulas
2. Endpoint GET /api/formulas que devuelve todas las fórmulas
3. Conectar el router con main.py

#### Código base (formulas.py):
```python
# routes/formulas.py
from fastapi import APIRouter
from backend.services.supabase_client import supabase

router = APIRouter(prefix="/api", tags=["formulas"])

@router.get("/formulas")
def listar_formulas():
    """Devuelve todas las fórmulas disponibles."""
    response = supabase.table("formulas").select("*").execute()
    return {"data": response.data, "error": None}
```

#### Código a añadir en main.py:
```python
from backend.routes.formulas import router as formulas_router
app.include_router(formulas_router)
```

#### Verificar:
```bash
curl http://localhost:8000/api/formulas
# Debe devolver la fórmula MRU en formato JSON
```

#### Documentar:
- Qué es un Router y por qué separamos las rutas
- Cómo funciona el prefijo /api
- Flujo: petición HTTP → router → supabase → respuesta

---

### Tarea 1.4: Endpoint para una fórmula específica
- **Estado:** ✅ Completado
- **Archivo a modificar:** `backend/routes/formulas.py`
- **Documentar en:** `docs/aprendizaje/05_endpoint_formula_id.md`

#### Qué hacer:
1. Añadir endpoint GET /api/formula/{id}
2. Manejar caso de fórmula no encontrada

#### Código a añadir:
```python
@router.get("/formula/{formula_id}")
def obtener_formula(formula_id: int):
    """Devuelve una fórmula específica por su ID."""
    response = supabase.table("formulas").select("*").eq("id", formula_id).execute()
    
    if not response.data:
        return {"data": None, "error": "Fórmula no encontrada"}
    
    return {"data": response.data[0], "error": None}
```

#### Verificar:
```bash
curl http://localhost:8000/api/formula/1
# Debe devolver la fórmula MRU

curl http://localhost:8000/api/formula/999
# Debe devolver: {"data": null, "error": "Fórmula no encontrada"}
```

#### Documentar:
- Qué son los parámetros de ruta ({formula_id})
- Cómo funciona .eq() en Supabase
- Por qué manejamos el caso de "no encontrado"

---

## FASE 2: LÓGICA DE CÁLCULO

### Tarea 2.1: Función de cálculo para fórmulas
- **Estado:** ✅ Completado
- **Archivo a crear:** `backend/services/calculadora.py`
- **Documentar en:** `docs/aprendizaje/06_logica_calculo.md`

#### Qué hacer:
1. Crear funciones que calculen puntos para cada tipo de fórmula
2. Empezar con MRU: x = x0 + v*t

#### Estructura:
```python
# calculadora.py
import numpy as np

def calcular_mru(x0: float, v: float, t_min: float, t_max: float, puntos: int = 100):
    """
    Calcula posición en MRU para un rango de tiempo.
    
    Args:
        x0: posición inicial
        v: velocidad
        t_min, t_max: rango de tiempo
        puntos: cantidad de puntos a calcular
    
    Returns:
        dict con arrays de t y x
    """
    t = np.linspace(t_min, t_max, puntos)
    x = x0 + v * t
    return {"t": t.tolist(), "x": x.tolist()}
```

#### Verificar:
```python
# Prueba manual
from backend.services.calculadora import calcular_mru
resultado = calcular_mru(0, 5, 0, 10)
print(resultado)
# Debe mostrar arrays de t y x
```

#### Documentar:
- Qué es numpy y por qué lo usamos
- Qué hace linspace
- Por qué convertimos a lista (.tolist())

---

### Tarea 2.2: Endpoint POST /api/calcular
- **Estado:** ✅ Completado
- **Archivo a crear:** `backend/routes/calculos.py`
- **Documentar en:** `docs/aprendizaje/07_endpoint_calcular.md`

#### Qué hacer:
1. Endpoint que recibe fórmula_id + valores
2. Calcula el resultado
3. Guarda en tabla `calculos`
4. Devuelve los puntos para graficar

#### Estructura:
```python
# routes/calculos.py
from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.supabase_client import supabase
from backend.services.calculadora import calcular_mru

router = APIRouter(prefix="/api", tags=["calculos"])

class DatosCalculo(BaseModel):
    formula_id: int
    valores: dict

@router.post("/calcular")
def calcular(datos: DatosCalculo):
    """Calcula una fórmula y guarda el resultado."""
    # 1. Obtener fórmula de la BD
    # 2. Calcular según el tipo
    # 3. Guardar en tabla calculos
    # 4. Devolver resultado
    pass
```

#### Documentar:
- Qué es Pydantic y BaseModel
- Cómo funciona POST vs GET
- Flujo completo del cálculo

---

### Tarea 2.3: Endpoint GET /api/historial
- **Estado:** ✅ Completado
- **Archivo a modificar:** `backend/routes/calculos.py`
- **Documentar en:** `docs/aprendizaje/08_endpoint_historial.md`

---

## FASE 3: FRONTEND BÁSICO

### Tarea 3.1: HTML estructura base
- **Estado:** ✅ Completado
- **Archivo a crear:** `frontend/index.html`
- **Documentar en:** `docs/aprendizaje/09_html_estructura.md`

### Tarea 3.2: JavaScript para llamar al backend
- **Estado:** ✅ Completado
- **Archivo a crear:** `frontend/js/api.js`
- **Documentar en:** `docs/aprendizaje/10_js_fetch_api.md`

### Tarea 3.3: Visualización con Plotly
- **Estado:** ✅ Completado
- **Archivo a crear:** `frontend/js/graficos.js`
- **Documentar en:** `docs/aprendizaje/11_plotly_graficos.md`

### Tarea 3.4: Estilos CSS
- **Estado:** ✅ Completado
- **Archivo a crear:** `frontend/css/styles.css` + `frontend/js/app.js`
- **Documentar en:** `docs/aprendizaje/12_css_estilos.md`

---

## FASE 4: INTEGRACIÓN

### Tarea 4.1: Conectar flujo completo
- **Estado:** ✅ Completado
- **Documentar en:** `docs/aprendizaje/13_integracion.md`

### Tarea 4.2: Añadir las 15 fórmulas
- **Estado:** ✅ Completado
- **Documentar en:** `docs/aprendizaje/14_todas_formulas.md`

---

## REGISTRO DE PROGRESO

Cada vez que completes una tarea, actualiza esta sección:

| Fecha | Tarea | Estado | Notas |
|-------|-------|--------|-------|
| 2025-12-29 | 0.1 - Entorno virtual y dependencias | ✅ Completado | Instaladas versiones más recientes: fastapi 0.128.0, uvicorn 0.39.0, supabase 2.27.0, python-dotenv 1.2.1 |
| 2025-12-29 | 1.1 - Cliente de Supabase | ✅ Completado | Conexión exitosa, recuperada fórmula MRU. Warning urllib3/OpenSSL ignorado (no afecta funcionalidad) |
| 2025-12-29 | 1.2 - Endpoint health check | ✅ Completado | Servidor FastAPI funcionando en puerto 8000, endpoint /health responde correctamente con JSON |
| 2025-12-29 | 1.3 - Endpoint listar fórmulas | ✅ Completado | Router creado, endpoint /api/formulas funciona, recupera fórmula MRU de Supabase. Primera integración FastAPI+Supabase exitosa |
| 2025-12-29 | 1.4 - Endpoint fórmula por ID | ✅ Completado | Parámetros de ruta funcionan, filtro .eq() exitoso, manejo de "no encontrado". **FASE 1 COMPLETA** 🎉 |
| 2025-12-29 | 2.1 - Función de cálculo MRU | ✅ Completado | Instalado numpy 2.0.2, función calcular_mru() con 5 pruebas exitosas, operaciones vectorizadas, listo para graficar |
| 2025-12-29 | 2.2 - Endpoint POST /api/calcular | ✅ Completado | Pydantic BaseModel funcionando, endpoint calcula+guarda+devuelve. Encontrados y corregidos 2 errores: campo 'tipo' no existe (usar nombre), columna 'valores_entrada' no 'valores'. Primera integración completa: API→BD→cálculo→BD→respuesta |
| 2025-12-29 | 2.3 - Endpoint GET /api/historial | ✅ Completado | JOIN automático con Supabase (.select("*, formulas(*)")), ordenamiento DESC por created_at, parámetro query 'limite' funcionando. Sin errores. **FASE 2 COMPLETA** 🎉 |
| 2025-12-29 | PASO 0 - CORS en backend | ✅ Completado | Añadido CORSMiddleware en backend/main.py para permitir peticiones desde frontend (localhost:3000 → localhost:8000) |
| 2025-12-29 | 3.1-3.4 - Frontend completo | ✅ Completado | Stack: Tailwind+DaisyUI, Plotly.js, MathJax, Google Fonts Inter. Tema oscuro elegante. 5 archivos: index.html (280 líneas), api.js (210 líneas), graficos.js (190 líneas), app.js (280 líneas), styles.css (270 líneas). Layout responsive 3 áreas, gráficos interactivos con animaciones, historial clickeable. **FASE 3 COMPLETA** 🎉 |
| 2025-12-30 | 4.1-4.2 - Integración completa | ✅ Completado | Bug LaTeX corregido (configuración MathJax). 14 fórmulas insertadas en Supabase (total 15). 14 funciones de cálculo añadidas en calculadora.py. Endpoint calculos.py reconoce 15 fórmulas por nombre. Frontend graficos.js detecta automáticamente 3 tipos de datos: {t,x}, {x,y}, {theta,x,y}. Aspect ratio 1:1 para curvas paramétricas. Probadas 6 fórmulas exitosamente: MRU, Parábola, Seno, Circunferencia, Espiral Logarítmica, Cardioide. Sistema completamente funcional extremo a extremo. **FASE 4 COMPLETA** 🎉 **PROYECTO 100% COMPLETADO** 🏆 |

---

## SI ALGO FALLA

1. **NO entres en pánico**
2. **Documenta el error** exacto en el archivo de aprendizaje
3. **Intenta diagnosticar** (¿qué puede estar mal?)
4. **Documenta cada intento** de solución
5. **Cuando lo resuelvas**, documenta la lección aprendida

Los errores son las mejores oportunidades de aprendizaje.

---

*Última actualización: 30 diciembre 2025*
