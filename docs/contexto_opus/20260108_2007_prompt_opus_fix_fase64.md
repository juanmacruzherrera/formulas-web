# PROMPT PARA OPUS - Arreglar FASE 6.4 Frontend
**Fecha:** 8 Enero 2026 - 20:07h (London/Madrid time)
**Creado por:** Claude Sonnet 4.5
**Para:** Claude Opus 4.5

---

## 📋 PROMPT PARA OPUS:

```
Lee CLAUDE.md en /Volumes/Akitio01/Claude_MCP/formulas-web

Luego lee el archivo clave:
docs/contexto_opus/20260108_estado_fase_6_4_problemas.md

Ese documento tiene TODO el contexto:
- Backend FASE 6.4 completo ✅
- 5 problemas críticos del frontend ❌
- Ubicación exacta de cada error (archivo + líneas)
- Código faltante con ejemplos completos

Arregla los 5 problemas en orden de prioridad (están numerados en el documento).

REGLAS:
- Tests después de cada fix
- Commits pequeños
- Documentar en docs/aprendizaje/17_rediseno_v2.md

Servidores para testing:
- Frontend: http://localhost:3000 (python3 -m http.server 3000 en frontend/)
- Backend: http://localhost:8000 (uvicorn backend.main:app --reload)
```

---

## 🎯 RESUMEN DE LOS 5 PROBLEMAS:

### 1. Filtrado de fórmulas ❌ (ALTA PRIORIDAD)
**Archivo:** `frontend/js/app.js`
**Problema:** Tabs 2D y 3D muestran TODAS las fórmulas mezcladas
**Solución:** Añadir función `filtrarFormulas(modo)` que filtre por categoría

### 2. Renderizado 3D plano ❌ (ALTA PRIORIDAD)
**Archivo:** `frontend/js/graficos.js`
**Problema:** Usa `type: 'scatter'` para todo, gráficos 3D se ven sin profundidad
**Solución:** Detectar `resultado.z` y usar `type: 'scatter3d'` de Plotly

### 3. Lorenz error NaN ❌ (ALTA PRIORIDAD)
**Archivo:** `backend/services/calculadora.py`
**Problema:** "Out of range float values are not JSON compliant: nan"
**Solución:** Añadir filtrado `np.isfinite()` en el loop de integración

### 4. Sin controles 3D ❌ (MEDIA PRIORIDAD)
**Archivo:** `frontend/js/app.js`
**Problema:** No aparece play/pause ni slider en gráficos 3D
**Solución:** Llamar a `window.animacion.animarCurva3D()` para gráficos 3D

### 5. Tabs sin feedback visual ❌ (MEDIA PRIORIDAD)
**Archivo:** `frontend/js/app.js`
**Problema:** Los tabs no cambian de estilo al hacer clic
**Solución:** Añadir/quitar clase `.tab-active` en event listeners

---

## 📁 ARCHIVOS CON SOLUCIONES COMPLETAS:

**TODO está en:**
`docs/contexto_opus/20260108_estado_fase_6_4_problemas.md`

Este archivo contiene:
- ✅ Código completo de cada solución
- ✅ Ubicación exacta (líneas)
- ✅ Ejemplos funcionales
- ✅ Checklist de tareas
- ✅ Orden de prioridad

---

## ✅ LO QUE YA FUNCIONA:

- Layout 80%-20% ✅
- Variables parseadas correctamente ✅
- Inputs sin spinners ✅
- Lemniscata sin error NaN ✅
- Backend 3D completo (4 funciones, rutas, BD) ✅
- Sistema de animación creado ✅

---

## 🚀 RESULTADO ESPERADO:

Después de los fixes:
1. Tab "2D" → Solo fórmulas 2D (física, matemáticas, curvas_exoticas)
2. Tab "3D" → Solo fórmulas 3D (geometria_3d)
3. Hélice 3D → Gráfico rotable con profundidad
4. Lorenz → Atractor caótico sin error, visualización 3D
5. Toro → Superficie toroidal rotable
6. Ondas 3D → Ondas circulares con altura Z visible

---

**FIN DEL PROMPT**
