# Carpeta: docs/gemini/ - Integración con Google AI Studio

**Fecha creación:** 8 Enero 2026 - 20:15h
**Última actualización:** 9 Enero 2026 - 15:30h ⭐
**Propósito:** Facilitar la colaboración entre Claude (Sonnet/Opus) y Gemini 2.0

**🎉 ESTADO ACTUAL: CÓDIGO FUNCIONAL AL 100%**
- ✅ Todos los problemas de FASE 6.4 resueltos
- ✅ Sistema 3D completo (tabs + renderizado)
- ✅ Contexto actualizado con código que funciona
- ✅ Listo para compartir con Google AI Studio

---

## 📁 CONTENIDO DE ESTA CARPETA

### 1. `generar_contexto_gemini.py` ⭐
**Script principal** que genera el archivo de contexto completo.

**Qué hace:**
- Recorre todo el proyecto (backend + frontend)
- Ignora carpetas basura (venv, node_modules, .git, __pycache__)
- Genera un único archivo MD con TODO el código
- Consulta Supabase para obtener esquema de BD
- Incluye estructura del proyecto

**Uso:**
```bash
cd /Volumes/Akitio01/Claude_MCP/formulas-web
source venv/bin/activate
python3 docs/gemini/generar_contexto_gemini.py
```

**Salida:**
`docs/gemini/contexto_completo_proyecto.md` (~130 KB)

---

### 2. `contexto_completo_proyecto.md`
**Archivo generado** por el script. Contiene:

- ✅ Información del proyecto (stack, URLs, estado)
- ✅ Estructura completa de carpetas
- ✅ TODO el código backend (Python)
- ✅ TODO el código frontend (JS/HTML/CSS)
- ✅ Esquema de base de datos Supabase
- ✅ Instrucciones para usar en Google AI Studio

**Tamaño:** ~130 KB
**Formato:** Markdown con bloques de código
**Tokens estimados:** ~40,000 tokens (cabe perfectamente en Gemini 2M)

---

### 3. `20260108_2007_prompt_opus_fix_fase64.md`
**Prompt específico** para Opus con los 5 problemas actuales.

También sirve para Gemini si quieres que arregle los mismos problemas.

---

## 🚀 CÓMO USAR CON GOOGLE AI STUDIO

### Paso 1: Preparar archivos
```bash
# Generar contexto actualizado
cd /Volumes/Akitio01/Claude_MCP/formulas-web
source venv/bin/activate
python3 docs/gemini/generar_contexto_gemini.py
```

### Paso 2: Subir a AI Studio
1. Abre https://aistudio.google.com/
2. Crea un nuevo chat
3. Haz clic en **+ (Add)**
4. Sube estos archivos:
   - `docs/gemini/contexto_completo_proyecto.md` ⭐
   - `docs/contexto_opus/20260108_estado_fase_6_4_problemas.md`
   - (Opcional) Capturas de pantalla de los errores

### Paso 3: Configurar System Instructions (Opcional)
```
Eres un experto en Python (FastAPI) y JavaScript Vanilla.

Este proyecto usa:
- Backend: Python + Supabase (Railway)
- Frontend: JS puro + Plotly.js (Cloudflare)

REGLAS:
- NO inventes columnas de BD sin verificar el esquema
- Ten en cuenta problemas de CORS entre dominios
- El código debe funcionar en Railway (variables de entorno)
- Documenta TODOS los cambios con comentarios
```

### Paso 4: Prompt inicial
```
Analiza este proyecto Full Stack de visualización de fórmulas.

He subido:
1. contexto_completo_proyecto.md → TODO el código
2. 20260108_estado_fase_6_4_problemas.md → 5 problemas actuales

PREGUNTA:
1. ¿Entiendes la arquitectura del proyecto?
2. ¿Ves los 5 problemas identificados por Claude?
3. ¿Hay errores adicionales que Claude no detectó?
4. ¿Las soluciones propuestas son correctas?

Dame código específico para arreglar cada problema.
```

---

## 🔄 FLUJO DE TRABAJO: Claude + Gemini

### Escenario 1: Segunda opinión
1. Claude detecta problemas → Documenta en `contexto_opus/`
2. Generar contexto → `python3 docs/gemini/generar_contexto_gemini.py`
3. Subir a Gemini → Pedir segunda opinión
4. Comparar soluciones → Elegir la mejor
5. Implementar → Documentar en `aprendizaje/`

### Escenario 2: Gemini como implementador
1. Subir contexto a Gemini
2. Darle el prompt de Opus (`20260108_2007_prompt_opus_fix_fase64.md`)
3. Gemini genera código
4. Claude revisa el código
5. Implementar y testear

### Escenario 3: Colaboración continua
1. Cada vez que haya cambios importantes → Regenerar contexto
2. Subir a Gemini → "¿Qué te parece este cambio?"
3. Gemini detecta posibles bugs
4. Claude implementa las correcciones

---

## 📋 CHECKLIST: Actualizar contexto

**Cuándo regenerar `contexto_completo_proyecto.md`:**
- ✅ Después de implementar una fase completa
- ✅ Cuando se añadan nuevos archivos importantes
- ✅ Antes de pedir ayuda a Gemini
- ✅ Si cambia la estructura de BD en Supabase

**Comando rápido:**
```bash
cd /Volumes/Akitio01/Claude_MCP/formulas-web
source venv/bin/activate && python3 docs/gemini/generar_contexto_gemini.py
```

---

## 🎯 VENTAJAS DE ESTA ESTRATEGIA

### vs. Subir .zip
- ✅ Gemini puede leer el código directamente (no binario)
- ✅ Estructura clara y organizada
- ✅ Sin archivos basura (node_modules, .git)

### vs. Arrastrar carpeta
- ✅ Más rápido de cargar (1 archivo vs 100+)
- ✅ Gemini ve la estructura completa de golpe
- ✅ Reutilizable (regenerar cuando cambie el código)

### Para Claude/Opus
- ✅ Pueden leer `contexto_completo_proyecto.md` para ver qué vio Gemini
- ✅ Facilita colaboración entre IAs
- ✅ Mismo contexto para todos

---

## 📊 ESTADÍSTICAS DEL PROYECTO

**Generado:** 8 Enero 2026

- **Backend:** ~1,500 líneas Python
- **Frontend:** ~1,000 líneas JS + ~500 HTML/CSS
- **Total:** ~3,000 líneas de código
- **Tamaño MD:** ~130 KB
- **Tokens Gemini:** ~40,000 / 2,000,000 (2% del contexto)

---

## 🔗 REFERENCIAS

### Documentación relacionada:
- `CLAUDE.md` → Instrucciones para Claude (actualizado 9 Enero)
- `docs/5_FIXES_EXACTOS.md` → ⭐ **Soluciones aplicadas (9 Enero 2026)**
- `docs/REDISENO_COMPLETO_V2.md` → Plan original (Opus)
- `docs/aprendizaje/17_rediseno_v2.md` → Registro de cambios
- `docs/contexto_opus/20260108_estado_fase_6_4_problemas.md` → Problemas identificados (RESUELTOS)

### Enlaces externos:
- Google AI Studio: https://aistudio.google.com/
- Gemini API Docs: https://ai.google.dev/

---

## 📅 HISTORIAL DE VERSIONES

### v2.0 - 9 Enero 2026 - 15:30h ✅
- ✅ Contexto regenerado con código funcional
- ✅ Sistema 3D completo implementado
- ✅ Todos los problemas FASE 6.4 resueltos
- ✅ 19 fórmulas funcionando (15 en 2D + 4 en 3D)

### v1.0 - 8 Enero 2026 - 20:15h
- ✅ Primera generación del contexto
- ❌ Código con 5 problemas pendientes

---

**Última actualización:** 9 Enero 2026 - 15:30h
**Mantenido por:** Claude Sonnet 4.5
**Para preguntas:** Consultar CLAUDE.md o docs/5_FIXES_EXACTOS.md
