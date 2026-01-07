# FASE 5: CORRECCIONES + SEGURIDAD + DEPLOY

> **PARA:** Claude Code
> **ESTADO:** Proyecto funcional con 15 fórmulas, pendiente correcciones y deploy

---

## PASO 1: SEGURIDAD SUPABASE (RLS) - JUAN MANUAL

Ejecutar en Supabase SQL Editor:

```sql
ALTER TABLE formulas ENABLE ROW LEVEL SECURITY;
ALTER TABLE calculos ENABLE ROW LEVEL SECURITY;

CREATE POLICY "formulas_select_public" ON formulas FOR SELECT USING (true);
CREATE POLICY "calculos_select_public" ON calculos FOR SELECT USING (true);
CREATE POLICY "calculos_insert_public" ON calculos FOR INSERT WITH CHECK (true);
```

---

## PASO 2: BUG - VARIABLES DINÁMICAS

**Problema:** Inputs siempre muestran "Posición inicial", "Velocidad" aunque la fórmula use otras variables.

**Archivo:** `frontend/js/app.js`

**ANTES de modificar:** Verificar estructura de `variables_usuario` en Supabase:
```bash
cd /Volumes/Akitio01/Claude_MCP/formulas-web && venv/bin/python -c "
from backend.services.supabase_client import supabase
r = supabase.table('formulas').select('nombre,variables_usuario').limit(3).execute()
for f in r.data: print(f['nombre'], '→', f['variables_usuario'])"
```

**Solución:** Función que genera inputs dinámicos leyendo `formula.variables_usuario`

---

## PASO 3: BUG - SLIDERS PARA RANGO

**Problema:** t_min/t_max son inputs numéricos, deberían ser sliders.

**Archivo:** `frontend/js/app.js`

**Solución:** Usar `formula.variable_rango`, `formula.rango_min`, `formula.rango_max` para generar sliders.

---

## PASO 4: LAYOUT INVERTIDO

**Problema:** Gráfica a la derecha, config a la izquierda. Debe ser al revés.

**Archivo:** `frontend/index.html`

**Solución:** Invertir orden de columnas en el flex/grid.

---

## PASO 5: HISTORIAL LATERAL

**Problema:** Historial ocupa mucho espacio abajo.

**Archivos:** `frontend/index.html`, `frontend/js/app.js`

**Solución:** Mover al panel derecho, hacerlo colapsable.

---

## PASO 6: PREPARAR DEPLOY

1. Verificar `.gitignore` incluye: `.env`, `venv/`, `__pycache__/`
2. Crear `Procfile`: `web: uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
3. Modificar `frontend/js/api.js`:
```javascript
const API_BASE = window.location.hostname === 'localhost' 
    ? 'http://localhost:8000' 
    : 'https://TU-APP.onrender.com';
```

---

## PASO 7-8: DEPLOY - JUAN MANUAL

- Backend → Render
- Frontend → Cloudflare Pages

---

## ORDEN EJECUCIÓN CLAUDE CODE

```
PASO 2 → PASO 3 → PASO 4 → PASO 5 → PASO 6
```

Documentar en `docs/aprendizaje/` y actualizar `docs/bitacora.md`
