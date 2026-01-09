# CONTEXTO PARA OPUS: Fase 6 - Corrección de Bugs y Mejoras 3D

**Fecha:** 7 Enero 2026
**Destinatario:** Claude Opus 4.5
**Propósito:** Planificar y ejecutar correcciones de bugs + implementación de gráficos 3D

---

## 📊 RESUMEN EJECUTIVO

### Estado Actual

**La aplicación está DESPLEGADA EN PRODUCCIÓN y FUNCIONANDO:**

- ✅ **Frontend:** https://formulas-web.pages.dev (Cloudflare Pages)
- ✅ **Backend:** https://web-production-daa0.up.railway.app (Railway.app)
- ✅ **Base de datos:** Supabase (configurada con RLS)
- ✅ **GitHub:** https://github.com/juanmacruzherrera/formulas-web

**Deploy continuo activo:**
- Cada `git push` a `main` → Auto-deploy en Railway + Cloudflare
- Preview URLs generados automáticamente en branches

**PERO: Se detectaron 4 problemas importantes que requieren corrección.**

---

## ⛔ REGLA CRÍTICA: VERIFICAR DESTINO ANTES DE ESCRIBIR CÓDIGO

> **SIEMPRE verifica qué ESPERA el destino ANTES de escribir código que envía datos.**

```
Cualquier conexión:  A → B
ANTES de escribir A, pregunta: "¿Qué espera B?"
```

| Origen | Destino | Qué verificar ANTES |
|--------|---------|---------------------|
| Python | Supabase | ¿Qué columnas tiene? ¿Qué formato los datos existentes? |
| JavaScript | Python API | ¿Qué endpoints existen? ¿Qué JSON esperan? |
| Función X | Función Y | ¿Qué parámetros espera Y? |

**Esta verificación toma 30 segundos y evita 30 minutos de debugging.**

---

## 🔴 PROBLEMAS DETECTADOS (Resumen)

### Problema 1: Inputs dinámicos rotos (Alta prioridad)
- **Síntoma:** Algunas fórmulas (MRUA, Caída Libre) muestran "0, 1, 2, 3..." en lugar de nombres de variables
- **Causa:** Inconsistencia en Supabase (`variables_usuario` como array en lugar de objeto)
- **Impacto:** Usuario no sabe qué valor ingresar en cada campo

### Problema 2: Spinners molestos en inputs (Media prioridad)
- **Síntoma:** Inputs `type="number"` muestran flechas arriba/abajo
- **Causa:** Comportamiento por defecto de HTML5
- **Solución:** CSS para ocultarlos

### Problema 3: Gráficos en 2D (Alta prioridad - REQUISITO ORIGINAL INCUMPLIDO)
- **Síntoma:** Todos los gráficos son 2D (X vs Y)
- **Causa:** Código solo implementa `scatter` de Plotly, no `scatter3d`
- **Impacto:** 12 de 15 fórmulas NECESITAN 3D (Tiro Parabólico, Espiral, Esfera...)
- **Requisito original:** Visualización 3D interactiva

### Problema 4: Área pequeña en pantallas grandes (Media prioridad)
- **Síntoma:** En monitor de 27", gráfico se ve enano
- **Causa:** Altura fija (500px) no escala con pantalla
- **Solución:** Media queries responsive

---

## 📂 ARCHIVOS QUE DEBES LEER (EN ORDEN)

### 1. PRIMERO: Documento de problemas y plan
📄 **`docs/PROBLEMAS_Y_MEJORAS_FASE6.md`** (~500 líneas)

**Qué contiene:**
- Descripción detallada de cada problema
- Diagnóstico técnico con capturas descritas
- Soluciones propuestas paso a paso
- Plan de trabajo dividido en Fases 6.1, 6.2, 6.3
- Archivos a modificar
- Checklist de testing
- Criterios de aceptación

**Por qué leerlo:** Es el documento MAESTRO de esta fase. Contiene TODO lo que necesitas saber.

---

### 2. SEGUNDO: Guías de deploy y arquitectura

#### 📄 `docs/GUIA_RAILWAY_DEPLOY.md` (~500 líneas)
**Qué contiene:**
- Cómo funciona Railway (explicado "para tontos")
- Procfile explicado palabra por palabra
- Variables de entorno (SUPABASE_URL, SUPABASE_KEY)
- Networking / Generate Domain
- Deploy continuo desde GitHub

**Por qué leerlo:** Entender cómo el backend está desplegado y cómo probarlo.

#### 📄 `docs/GUIA_CLOUDFLARE_PAGES_DEPLOY.md` (~600 líneas)
**Qué contiene:**
- Pages vs Workers (diferencias conceptuales)
- Build output directory: por qué `/frontend`
- Flujo completo: Cloudflare → Railway → Supabase
- Preview deployments (cómo probar cambios antes de producción)

**Por qué leerlo:** Entender el flujo de trabajo para probar cambios (rama `dev` → preview → `main` → producción).

---

### 3. TERCERO: Documentación técnica del código

#### 📄 `docs/aprendizaje/16_fase5_mejoras_ui_deploy.md` (~700 líneas + ANEXO con diffs)
**Qué contiene:**
- Explicación socrática de toda la Fase 5
- ANEXO: Diffs completos (rojo → verde) de todos los cambios
- Cambio Render → Railway documentado con diffs
- Inputs dinámicos, sliders, layout invertido
- Historial de decisiones

**Por qué leerlo:** Ver exactamente QUÉ se cambió y POR QUÉ en la última fase. El ANEXO tiene todos los diffs.

---

### 4. CUARTO: Bitácora del proyecto

#### 📄 `docs/bitacora.md` (primeras 200 líneas)
**Qué contiene:**
- Entrada de hoy (7 Enero 2026 - tarde)
- Resumen de deploy completado
- Tabla de archivos MD creados
- URLs de producción
- Próximos pasos

**Por qué leerlo:** Contexto de lo que se hizo hoy antes de que llegaras.

---

### 5. OPCIONAL: Si necesitas entender el código fuente

#### Código Frontend:
- `frontend/js/app.js` → Lógica principal, generación de inputs, renderizado
- `frontend/js/api.js` → Comunicación con backend, detección de entorno
- `frontend/index.html` → Estructura HTML, layout

#### Código Backend:
- `backend/services/calculadora.py` → Lógica de cálculo de fórmulas
- `backend/routes/calculos.py` → Endpoints de cálculo
- `backend/main.py` → Configuración FastAPI, CORS

**NO leas estos archivos TODAVÍA** - primero lee la documentación MD. Solo léelos si necesitas ver implementación concreta.

---

## 🎯 TU MISIÓN (Fase 6)

### Objetivo General
Corregir los 4 problemas detectados y dejar la aplicación funcionando al 100% con gráficos 3D.

### Fases de Trabajo

#### **Fase 6.1: Bugs Críticos** (Prioridad: Alta, Tiempo: 2-3h)
1. **Problema 1: Arreglar inputs dinámicos**
   - Conectar a Supabase
   - Leer fórmulas con `variables_usuario` como array
   - Convertir a objetos
   - Actualizar en BD
   - Verificar en localhost
   - Verificar en producción

2. **Problema 2: Ocultar spinners**
   - Añadir CSS
   - Probar en Chrome/Firefox/Safari

#### **Fase 6.2: Gráficos 3D** (Prioridad: Alta, Tiempo: 4-6h)
3. **Problema 3: Implementar 3D**
   - Añadir campo `dimension` en Supabase
   - Marcar fórmulas 3D (Tiro Parabólico, Espiral, Esfera...)
   - Backend: Calcular coordenada Z
   - Frontend: Renderizar `scatter3d` cuando corresponda
   - Ajustar cámara, ejes, colores

#### **Fase 6.3: UX** (Prioridad: Media, Tiempo: 1-2h)
4. **Problema 4: Responsive para pantallas grandes**
   - Media queries en CSS
   - Altura basada en viewport (70vh)
   - Probar en diferentes resoluciones

---

## 🔄 FLUJO DE TRABAJO RECOMENDADO

### CRÍTICO: Trabajar en rama `dev` primero

**NO trabajar directamente en `main`** → Producción podría romperse

**Flujo correcto:**

```bash
# 1. Crear rama dev (si no existe)
git checkout -b dev

# 2. Hacer cambios en localhost
# ... editar código ...

# 3. Probar en localhost
# Backend: http://localhost:8000
# Frontend: abrir index.html en navegador

# 4. Commit y push a dev
git add .
git commit -m "Fix: Arreglar inputs dinámicos de fórmulas"
git push -u origin dev

# 5. Cloudflare genera preview URL automáticamente
# Ejemplo: https://abc123.formulas-web.pages.dev

# 6. Verificar en preview URL
# ¿Todo funciona? → Continuar
# ¿Algo roto? → Arreglar y volver al paso 2

# 7. Merge a main SOLO si todo funciona
git checkout main
git merge dev
git push

# 8. Producción se actualiza automáticamente
# Railway: https://web-production-daa0.up.railway.app
# Cloudflare: https://formulas-web.pages.dev
```

**Ventaja:** Producción NUNCA se rompe. Pruebas siempre en preview primero.

---

## 🗂️ ESTRUCTURA DEL REPOSITORIO

```
formulas-web/
├── backend/
│   ├── main.py                 ← FastAPI app, CORS
│   ├── routes/
│   │   ├── formulas.py         ← GET /api/formulas
│   │   └── calculos.py         ← POST /api/calcular
│   └── services/
│       ├── supabase_client.py  ← Conexión Supabase
│       └── calculadora.py      ← ⚠️ MODIFICAR AQUÍ para 3D
│
├── frontend/
│   ├── index.html              ← ⚠️ MODIFICAR para responsive
│   ├── css/
│   │   └── styles.css          ← ⚠️ AÑADIR CSS spinners + responsive
│   └── js/
│       ├── api.js              ← Detección entorno (ya correcto)
│       └── app.js              ← ⚠️ MODIFICAR para renderizar 3D
│
├── docs/
│   ├── PROBLEMAS_Y_MEJORAS_FASE6.md  ← ⭐ LEE PRIMERO
│   ├── GUIA_RAILWAY_DEPLOY.md
│   ├── GUIA_CLOUDFLARE_PAGES_DEPLOY.md
│   ├── bitacora.md
│   ├── aprendizaje/
│   │   └── 16_fase5_mejoras_ui_deploy.md  ← Diffs completos
│   └── contexto_opus/
│       └── 20260107_contexto_fase6.md  ← ⭐ ESTE ARCHIVO
│
├── Procfile                     ← Railway config (ya correcto)
├── requirements.txt             ← Dependencias Python
├── .env                         ← Secretos (NO en GitHub)
├── .gitignore                   ← Protege .env
└── CLAUDE.md                    ← Instrucciones generales
```

---

## 🔑 CREDENCIALES Y ACCESOS

### Base de Datos (Supabase)

**IMPORTANTE:** Las credenciales están en `.env` (archivo local, NO en GitHub).

**Para acceder a Supabase desde Python:**
```python
import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

# Leer fórmulas
formulas = supabase.table("formulas").select("*").execute()
```

**Tablas existentes:**
- `formulas` → 15 fórmulas con metadatos
  - Columnas: id, nombre, categoria, formula_latex, variables_usuario, variable_rango, rango_min, rango_max
- `calculos` → Historial de cálculos
  - Columnas: id, formula_id, valores_entrada, resultado_grafico, created_at

**RLS activado:** Las políticas permiten lectura pública (`SELECT`) y escritura pública en `calculos` (`INSERT`).

---

### URLs de Producción

| Componente | URL | Propósito |
|------------|-----|-----------|
| **Frontend** | https://formulas-web.pages.dev | App web accesible por usuarios |
| **Backend** | https://web-production-daa0.up.railway.app | API REST FastAPI |
| **Health check** | https://web-production-daa0.up.railway.app/health | Verificar backend funciona |
| **API fórmulas** | https://web-production-daa0.up.railway.app/api/formulas | Listar fórmulas |
| **Supabase Dashboard** | https://supabase.com/dashboard | Ver/editar datos BD |
| **Railway Dashboard** | https://railway.app/dashboard | Ver logs, deployments |
| **Cloudflare Dashboard** | https://dash.cloudflare.com | Ver deploys, preview URLs |

---

## 📝 CHECKLIST ANTES DE EMPEZAR

Antes de escribir código, asegúrate de:

- [ ] Has leído `docs/PROBLEMAS_Y_MEJORAS_FASE6.md` completo
- [ ] Entiendes los 4 problemas y sus causas
- [ ] Sabes qué archivos modificar para cada problema
- [ ] Conoces el flujo de trabajo (dev → preview → main)
- [ ] Sabes acceder a Supabase con Python
- [ ] Entiendes la estructura del repositorio
- [ ] Has leído el ANEXO con diffs en `16_fase5_mejoras_ui_deploy.md`

---

## ⚠️ REGLAS IMPORTANTES

### 1. NUNCA trabajar directamente en `main`
Crear rama `dev` para desarrollo. Solo hacer merge a `main` cuando TODO funcione.

### 2. Probar SIEMPRE en localhost primero
Antes de hacer push:
- Backend: Ejecutar `uvicorn backend.main:app --reload`
- Frontend: Abrir `frontend/index.html` en navegador
- Verificar que funciona

### 3. Verificar en preview URL antes de merge a main
Cloudflare genera preview URL automáticamente. Probar ahí antes de merge.

### 4. NO modificar `.env` ni subirlo a GitHub
Credenciales son locales. `.gitignore` ya protege esto.

### 5. Documentar TODOS los cambios
Crear archivo en `docs/aprendizaje/17_fase6_correccion_bugs_3d.md` con:
- Qué se cambió
- Por qué
- Diffs (rojo → verde)
- Resultado

### 6. Actualizar bitácora
Añadir entrada en `docs/bitacora.md` (al PRINCIPIO, nunca borrar entradas antiguas).

---

## 🎨 TECNOLOGÍAS USADAS

### Backend
- **Python 3.11+**
- **FastAPI** (framework web)
- **Supabase** (PostgreSQL con API REST)
- **Uvicorn** (servidor ASGI)

### Frontend
- **HTML5 + CSS3**
- **Vanilla JavaScript** (ES6+, NO frameworks)
- **Plotly.js** (gráficos 2D y 3D)
  - **IMPORTANTE:** Plotly YA soporta 3D con `scatter3d`
  - Documentación: https://plotly.com/javascript/3d-scatter-plots/
- **MathJax** (renderizado LaTeX)
- **TailwindCSS + DaisyUI** (estilos)

### Deploy
- **Railway.app** (backend)
- **Cloudflare Pages** (frontend)
- **GitHub** (control de versiones, CI/CD)

---

## 🔍 DEBUGGING: Cómo Ver Logs

### Backend (Railway)
1. Ir a: https://railway.app/dashboard
2. Click en proyecto `formulas-web`
3. Click en servicio
4. Pestaña **"Deployments"**
5. Click en deployment activo
6. Ver logs en tiempo real

### Frontend (Cloudflare)
1. Abrir: https://formulas-web.pages.dev
2. Abrir DevTools (F12)
3. Pestaña **Console** → Ver errores JavaScript
4. Pestaña **Network** → Ver requests al backend

---

## 📚 RECURSOS ÚTILES

### Plotly 3D
- **Scatter 3D:** https://plotly.com/javascript/3d-scatter-plots/
- **Line 3D:** https://plotly.com/javascript/3d-line-plots/
- **Surface 3D:** https://plotly.com/javascript/3d-surface-plots/

### Supabase
- **Python Client:** https://supabase.com/docs/reference/python/introduction
- **SQL Editor:** https://supabase.com/dashboard (proyecto → SQL Editor)

### Railway
- **Docs FastAPI:** https://docs.railway.com/guides/fastapi
- **Logs:** https://railway.app/dashboard

### Cloudflare
- **Pages Docs:** https://developers.cloudflare.com/pages/
- **Preview URLs:** Automático en cada commit a branches

---

## 🎯 CRITERIOS DE ÉXITO (Fase 6 completada cuando)

- [ ] **Problema 1 resuelto:** Todas las 15 fórmulas muestran inputs con nombres descriptivos (no 0,1,2,3)
- [ ] **Problema 2 resuelto:** Inputs no muestran spinners (flechas arriba/abajo)
- [ ] **Problema 3 resuelto:** Fórmulas 3D (Tiro Parabólico, Espiral, Esfera...) muestran gráficos 3D interactivos con ejes X, Y, Z
- [ ] **Problema 4 resuelto:** Gráficos se ven proporcionales en pantallas de 27 pulgadas
- [ ] **Todo funciona en localhost** (probado)
- [ ] **Todo funciona en preview URL** (probado)
- [ ] **Todo funciona en producción** (https://formulas-web.pages.dev)
- [ ] **Documentación actualizada** en `docs/aprendizaje/17_fase6_correccion_bugs_3d.md`
- [ ] **Bitácora actualizada** con entrada de Fase 6

---

## 💡 CONSEJO FINAL

**No te abrumes.** Los problemas parecen muchos, pero:

1. **Problema 1** es solo arreglar datos en Supabase (1h)
2. **Problema 2** es solo añadir CSS (15 min)
3. **Problema 3** es el más complejo (4-6h) pero Plotly YA tiene `scatter3d` - solo necesitas calcular Z y usarlo
4. **Problema 4** es solo media queries CSS (1h)

**Total: ~7-9 horas de trabajo.** Hazlo paso a paso, fase por fase.

**Y RECUERDA:** Trabajar en `dev`, probar en localhost, verificar en preview, merge a `main`.

---

## 📞 CONTACTO / REFERENCIAS

**Usuario:** Juan Manuel (51 años, estudiante Ciencia de Datos UOC)
**Proyecto:** Aplicación educativa de visualización de fórmulas matemáticas
**Objetivo:** Que Juan entienda CÓMO funciona, no solo que funcione

**Chat completo de hoy guardado en:**
`/Volumes/Akitio01/Claude_MCP/formulas-web/docs/chats_register/20250107_formulas_web_Claude_Code_CHAT_COMPLETO.txt`

Si necesitas más contexto histórico, lee ese archivo.

---

**¡Buena suerte! Cualquier duda, lee primero `docs/PROBLEMAS_Y_MEJORAS_FASE6.md` 🚀**

---

*Documento creado: 7 Enero 2026*
*Por: Claude Sonnet 4.5*
*Para: Claude Opus 4.5*
