# GUÍA PARA JUAN: Pasos Manuales (1, 7, 8)

> **Esto lo haces TÚ en el navegador, no Claude Code**

---

## PASO 1: ACTIVAR SEGURIDAD EN SUPABASE (RLS)

### Qué es RLS y por qué importa:
Row Level Security = "Quién puede ver/modificar qué filas". Sin esto, cualquiera con tu URL de Supabase podría borrar todas tus fórmulas.

### Instrucciones:

1. **Abre Supabase:** https://supabase.com/dashboard
2. **Entra a tu proyecto** (el de formulas-web)
3. **Menú izquierdo → SQL Editor** (icono de código)
4. **Click en "New query"**
5. **Pega este código:**

```sql
-- Activar seguridad en tabla formulas
ALTER TABLE formulas ENABLE ROW LEVEL SECURITY;

-- Activar seguridad en tabla calculos
ALTER TABLE calculos ENABLE ROW LEVEL SECURITY;

-- Permitir que cualquiera LEA las fórmulas
CREATE POLICY "formulas_lectura_publica" ON formulas
    FOR SELECT USING (true);

-- Permitir que cualquiera LEA los cálculos
CREATE POLICY "calculos_lectura_publica" ON calculos
    FOR SELECT USING (true);

-- Permitir que cualquiera GUARDE cálculos
CREATE POLICY "calculos_escritura_publica" ON calculos
    FOR INSERT WITH CHECK (true);
```

6. **Click en "Run"** (o Cmd+Enter)
7. **Debe salir:** "Success. No rows returned"

### Verificar que funcionó:

1. **Menú izquierdo → Table Editor**
2. **Click en tabla "formulas"**
3. **Arriba debe aparecer un candado** con "RLS Enabled"
4. **Repetir para tabla "calculos"**

### Si algo falla:
- Error "policy already exists" → Ya estaba creada, todo bien
- Error "permission denied" → Verifica que estás en tu proyecto correcto

---

## PASO 7: DEPLOY BACKEND EN RENDER

### Qué es Render:
Un servicio que ejecuta tu código Python en internet 24/7. Gratis para proyectos pequeños.

### Antes de empezar:
- Tu código debe estar en GitHub (si no está, primero sube el proyecto)

### Instrucciones:

1. **Abre Render:** https://render.com
2. **Click "Get Started for Free"** → Registrarte con GitHub
3. **Dashboard → "New +"** → **"Web Service"**
4. **"Connect a repository"** → Busca `formulas-web` → Click "Connect"
5. **Configurar:**

| Campo | Valor |
|-------|-------|
| Name | `formulas-api` |
| Region | Frankfurt (EU Central) - el más cercano a España |
| Branch | `main` |
| Runtime | `Python 3` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `uvicorn backend.main:app --host 0.0.0.0 --port $PORT` |

6. **Scroll abajo → "Advanced" → "Add Environment Variable":**

| Key | Value |
|-----|-------|
| `SUPABASE_URL` | (copia de tu archivo .env) |
| `SUPABASE_KEY` | (copia de tu archivo .env) |

7. **Click "Create Web Service"**
8. **Espera 2-5 minutos** (verás logs de instalación)
9. **Cuando termine:** Te da una URL tipo `https://formulas-api.onrender.com`

### Verificar que funcionó:

Abre en el navegador:
```
https://formulas-api.onrender.com/health
```

Debe mostrar:
```json
{"status":"ok"}
```

### Si algo falla:
- Revisa los logs en Render (botón "Logs")
- Error común: olvidar las variables de entorno SUPABASE_URL y SUPABASE_KEY

---

## PASO 8: DEPLOY FRONTEND EN CLOUDFLARE PAGES

### Qué es Cloudflare Pages:
Hosting gratuito para archivos estáticos (HTML/CSS/JS). Muy rápido, CDN global.

### Antes de empezar:
- Tienes que haber completado el PASO 7 (necesitas la URL de Render)
- Actualizar `frontend/js/api.js` con la URL de Render (esto lo hace Claude Code en paso 6)

### Instrucciones:

1. **Abre Cloudflare:** https://dash.cloudflare.com
2. **Crear cuenta** si no tienes (gratis)
3. **Menú izquierdo → "Workers & Pages"**
4. **Click "Create application"** → **"Pages"** → **"Connect to Git"**
5. **Autorizar GitHub** si te lo pide
6. **Selecciona repositorio** `formulas-web` → Click "Begin setup"
7. **Configurar:**

| Campo | Valor |
|-------|-------|
| Project name | `formulas-web` |
| Production branch | `main` |
| Build command | (DÉJALO VACÍO) |
| Build output directory | `frontend` |

8. **Click "Save and Deploy"**
9. **Espera 1-2 minutos**
10. **Cuando termine:** Te da una URL tipo `https://formulas-web.pages.dev`

### Verificar que funcionó:

1. Abre la URL que te dio Cloudflare
2. Debe cargar tu aplicación
3. Selecciona una fórmula y click "Calcular"
4. Si aparece el gráfico → ¡TODO FUNCIONA!

### Si el gráfico no aparece:
- Abre la consola del navegador (F12 → Console)
- Si dice "CORS error" o "Failed to fetch":
  - Verifica que `api.js` tiene la URL correcta de Render
  - Verifica que el backend en Render está funcionando

---

## ⚠️ ANTES DE EMPEZAR: SUBIR A GITHUB

**IMPORTANTE:** El proyecto NO está en GitHub todavía.

**Debes hacer esto PRIMERO:**

👉 **Lee y sigue:** `docs/GUIA_GIT_GITHUB.md`

Esta guía te enseña paso a paso:
- Inicializar Git en el proyecto
- Crear repositorio en GitHub
- Subir el código (sin .env ni secretos)
- Verificar que todo esté correcto

**SIN GITHUB → NO PUEDES HACER DEPLOY**

Tanto Render como Cloudflare necesitan conectarse a tu repositorio de GitHub para obtener el código.

---

## ORDEN DE EJECUCIÓN COMPLETO

```
PASO PREVIO:
└─ ⚠️  Subir a GitHub (docs/GUIA_GIT_GITHUB.md) ← HAZLO PRIMERO

PASOS MANUALES:
1. ⏳ Activar RLS en Supabase (este documento, paso 1)
2. ✅ Claude Code ejecuta pasos 2-6 (YA HECHO)
3. ⏳ Deploy backend en Render (este documento, paso 7)
4. ⏳ Deploy frontend en Cloudflare (este documento, paso 8)
```

---

## RESUMEN DE URLs QUE TENDRÁS

| Qué | URL |
|-----|-----|
| Supabase (BD) | https://xxxxx.supabase.co |
| Render (Backend) | https://formulas-api.onrender.com |
| Cloudflare (Frontend) | https://formulas-web.pages.dev |

---

## ACTUALIZACIÓN 7 ENERO 2026

### ✅ Pasos 2-6 completados por Claude Code:

**PASO 2:** Inputs dinámicos funcionando
- Cada fórmula muestra solo sus variables específicas
- MRU → x₀, v | Parábola → a, b, c | Cardioide → a

**PASO 3:** Sliders implementados
- Los rangos (t_min, t_max) ahora son sliders interactivos
- Valor se actualiza en tiempo real

**PASO 4:** Layout invertido
- Gráfica grande a la IZQUIERDA (2/3 del ancho)
- Controles compactos a la DERECHA (1/3 del ancho)

**PASO 5:** Historial lateral colapsable
- Historial movido al panel derecho
- Colapsable por defecto (ahorra espacio)
- Cards verticales adaptadas

**PASO 6:** Archivos de deploy preparados
- ✅ `Procfile` creado para Render
- ✅ `api.js` con detección de entorno (localhost vs producción)
- ✅ `.gitignore` verificado (incluye .env, venv/, __pycache__)

### ⚠️ IMPORTANTE ANTES DEL PASO 8:

Después de completar el PASO 7 (deploy backend en Render), necesitas actualizar la URL del backend:

1. **Editar** `frontend/js/api.js`
2. **Línea 15:** Cambiar `https://TU-BACKEND.onrender.com` por la URL real que te dio Render
3. **Ejemplo:** Si Render te dio `https://formulas-api.onrender.com`, pon eso
4. **Guardar** y hacer commit:
   ```bash
   cd /Volumes/Akitio01/Claude_MCP/formulas-web
   git add frontend/js/api.js
   git commit -m "Configurar URL del backend para producción"
   git push
   ```

### Documentación generada:

- `docs/aprendizaje/16_fase5_mejoras_ui_deploy.md` - Explicación completa de todos los cambios
- `docs/bitacora.md` - Entrada actualizada con resumen de Fase 5

### Tu turno:

**PRIMERO:**
0. ⚠️ **Subir a GitHub** → Lee `docs/GUIA_GIT_GITHUB.md` ← **OBLIGATORIO ANTES DE DEPLOY**

**LUEGO:**
1. ⏳ PASO 1: Activar RLS en Supabase (arriba en este documento)
2. ⏳ PASO 7: Deploy backend en Render (arriba en este documento)
3. ⏳ PASO 8: Deploy frontend en Cloudflare (arriba en este documento)

**¡El código está listo, ahora toca Git + GitHub + Deploy! 🚀**

---

*Documento creado: Enero 2025*
*Última actualización: 7 Enero 2026 - Fase 5 completada*
