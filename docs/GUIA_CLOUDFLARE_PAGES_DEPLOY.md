# GUÍA COMPLETA: Deploy Frontend en Cloudflare Pages

**Actualizado:** 7 Enero 2026
**Plataforma:** Cloudflare Pages (Gratuito, ilimitado)

---

## ¿Por qué Cloudflare Pages?

✅ **GRATIS e ilimitado** (sin límite de requests, ancho de banda ilimitado)
✅ **CDN global** (red de distribución de contenido en 300+ ciudades)
✅ **HTTPS automático** (SSL gratis)
✅ **Deploy automático** desde GitHub
✅ **Velocidad extrema** (archivos estáticos servidos desde el servidor más cercano al usuario)

---

## PASO 1: Crear cuenta en Cloudflare

1. **Ir a:** https://dash.cloudflare.com
2. **Click en:** "Sign up" (si no tienes cuenta)
3. **Registrarse:**
   - Puedes usar email + contraseña
   - O usar "Sign in with GitHub" (recomendado, más rápido)

**NO pide tarjeta de crédito** para Pages.

---

## PASO 2: Navegar a Workers & Pages

1. **En el dashboard de Cloudflare:**
   - Menú izquierdo → **"Workers & Pages"**

2. **Verás:**
   - Una sección unificada que muestra Workers y Pages juntos
   - "No projects found" (si es tu primera vez)

---

## PASO 3: Crear aplicación de Pages

1. **Click en:** **"Create application"** (botón azul arriba a la derecha)

2. **Te mostrará 2 opciones:**
   - **"Create a Worker"** → NO es lo que quieres
   - **"Ship something new"** con varias opciones

3. **IMPORTANTE:** Busca abajo el texto:
   ```
   Looking to deploy Pages? Get started
   ```

4. **Click en "Get started"** (link azul)

**¿Por qué este flujo confuso?**
Cloudflare unificó Workers y Pages en 2024. Pages ahora se accede desde un link secundario.

---

## PASO 4: Conectar a GitHub

1. **En la pantalla de Pages, verás:**
   - **"Connect to Git"** ← Elige esta opción
   - "Upload assets directly" (solo si no usas Git)

2. **Click en "Connect to Git"**

3. **Autorizar Cloudflare en GitHub:**
   - Te redirigirá a GitHub
   - GitHub pregunta: "¿Permitir que Cloudflare acceda a tus repos?"
   - **Click en "Authorize Cloudflare"**

4. **Configurar acceso:**
   - Puedes dar acceso a TODOS los repos
   - O solo a `formulas-web` (más seguro)
   - **Recomendación:** Solo a `formulas-web`

---

## PASO 5: Seleccionar repositorio

1. **Lista de repositorios:**
   - Verás tus repos de GitHub
   - Busca: **`juanmacruzherrera/formulas-web`**

2. **Click en el repositorio**

3. **Click en "Begin setup"**

---

## PASO 6: Configurar el proyecto ⚠️ CRÍTICO

Esta es la pantalla MÁS IMPORTANTE. Cada campo debe configurarse correctamente.

### ✅ Configuración CORRECTA:

| Campo | Valor | ¿Por qué? |
|-------|-------|-----------|
| **Project name** | `formulas-web` | Nombre que aparecerá en la URL |
| **Production branch** | `main` | Rama de GitHub a desplegar |
| **Build command** | *(VACÍO)* | No hay proceso de compilación |
| **Build output directory** | `/frontend` | Carpeta donde están los archivos HTML/JS |

### Desglose detallado de cada campo:

---

#### **Project name**

**Qué es:**
El nombre de tu proyecto en Cloudflare. También se usa para generar la URL.

**Valor:** `formulas-web`

**Resultado:**
Tu app será accesible en: `https://formulas-web.pages.dev`

**Reglas:**
- Solo letras, números y guiones
- No espacios, no mayúsculas
- Debe ser único en Cloudflare (si ya existe, añade un número)

---

#### **Production branch**

**Qué es:**
La rama de GitHub que se desplegará en producción.

**Valor:** `main`

**¿Por qué main?**
Es la rama principal donde está tu código estable. Cada vez que haces `git push` a `main`, Cloudflare re-despliega automáticamente.

**Opciones:**
- `main` → Rama principal (estándar moderno)
- `master` → Rama principal (estándar antiguo)
- Puedes crear ramas de desarrollo (`dev`, `staging`) para probar antes de producción

---

#### **Build command** ⚠️ DEBE ESTAR VACÍO

**Qué es:**
Un comando que se ejecuta ANTES de desplegar, para "compilar" o "procesar" el código.

**Valor:** *(vacío - no escribir nada)*

**¿Por qué vacío?**
Tu frontend es **HTML + JavaScript puro** (vanilla JS). No necesita compilación:
- ❌ NO usas React (que necesita `npm run build`)
- ❌ NO usas Vue (que necesita `npm run build`)
- ❌ NO usas TypeScript (que necesita `tsc`)
- ✅ Usas HTML + JS directo → funciona tal cual

**Si pones algo aquí:**
Cloudflare intentará ejecutar ese comando y probablemente falle si no existe.

---

#### **Build output directory** ⚠️ CRÍTICO

**Qué es:**
La carpeta de tu repositorio donde están los archivos HTML/CSS/JS que quieres servir.

**Valor:** `/frontend` o `frontend` (ambos funcionan)

**¿Por qué `/frontend`?**
Tu estructura de proyecto es:
```
formulas-web/
├── backend/        ← Python, NO es frontend
├── frontend/       ← ⭐ HTML, CSS, JS ← ESTO es lo que quieres desplegar
│   ├── index.html
│   ├── css/
│   └── js/
├── docs/
└── ...
```

Cloudflare necesita saber: "¿Dónde están los archivos web?". La respuesta es: `frontend/`

**Si pones `/` (raíz):**
Cloudflare intentaría servir `backend/`, `docs/`, etc. → ERROR

**Cómo lo usa Cloudflare:**
1. Descarga todo tu repo de GitHub
2. Entra en la carpeta `frontend/`
3. Busca `index.html` ahí dentro
4. Sirve TODO lo que esté en esa carpeta

---

#### **Framework preset** (si aparece)

**Qué es:**
Configuración predefinida para frameworks populares.

**Valor:** `None` o déjalo sin seleccionar

**¿Por qué None?**
No usas ningún framework (React, Next.js, Vue, etc.). Usas vanilla JS.

---

### ❌ Campos que NO debes configurar:

#### **Deploy command**
- NO existe en Pages (solo en Workers)
- Si aparece, déjalo vacío

#### **Root directory**
- Solo si tu frontend no está en `/frontend` sino en otro sitio
- En tu caso, déjalo vacío (usa el default `/`)

#### **Environment variables (advanced)**
- NO necesario para el frontend
- El frontend detecta automáticamente el entorno en `api.js`:
  ```javascript
  const API_BASE = window.location.hostname === 'localhost'
      ? 'http://localhost:8000'
      : 'https://web-production-daa0.up.railway.app';
  ```

---

## PASO 7: Desplegar

1. **Verificar que todo está correcto:**
   - Build command: vacío ✅
   - Build output directory: `/frontend` ✅

2. **Click en:** **"Save and Deploy"**

3. **Esperar:**
   - Cloudflare descarga tu repo de GitHub
   - Copia los archivos de `/frontend` a su CDN global
   - Genera certificado SSL
   - Tiempo: **1-2 minutos**

4. **Verás:**
   ```
   ✓ Cloning repository...
   ✓ Building application...
   ✓ Deploying to Cloudflare's global network...
   ✓ Success! Your site is live
   ```

---

## PASO 8: Obtener la URL

1. **Al terminar el deploy, Cloudflare te muestra:**
   ```
   https://formulas-web.pages.dev
   ```

2. **Copiar esa URL**

3. **Abrir en el navegador**

---

## PASO 9: Verificar que funciona

1. **Abre:** `https://formulas-web.pages.dev`

2. **Debe cargar:**
   - ✅ Título: "Visualizador de Fórmulas"
   - ✅ Selector de fórmulas (dropdown)
   - ✅ Área de visualización
   - ✅ Botón "Calcular"

3. **Probar funcionalidad completa:**
   - Seleccionar una fórmula (ej: MRU)
   - Ingresar valores
   - Click "Calcular y Graficar"
   - **Debe aparecer el gráfico** ← Si esto funciona, TODO está bien

4. **Si NO aparece el gráfico:**
   - Abre consola del navegador (F12 → Console)
   - Busca errores tipo "CORS" o "Failed to fetch"
   - Ver sección Troubleshooting abajo

---

## 📖 EXPLICACIÓN DETALLADA: Pages vs Workers

### ¿Qué es Cloudflare Pages?

**Pages** = Hosting para **archivos estáticos** (HTML, CSS, JS, imágenes)

**¿Qué son archivos estáticos?**
- Archivos que NO cambian
- El servidor simplemente los envía tal cual
- No hay procesamiento del lado del servidor

**Tu frontend ES estático:**
```
frontend/
├── index.html        ← Archivo HTML estático
├── css/styles.css    ← Archivo CSS estático
└── js/
    ├── api.js        ← JavaScript estático
    └── app.js        ← JavaScript estático
```

Cuando un usuario visita `https://formulas-web.pages.dev`:
1. Su navegador pide `index.html`
2. Cloudflare envía `index.html` tal cual está
3. El navegador ve que necesita `js/api.js`
4. Cloudflare envía `js/api.js` tal cual está
5. El JavaScript se ejecuta EN EL NAVEGADOR (no en el servidor)

---

### ¿Qué es Cloudflare Workers?

**Workers** = **Código que se ejecuta en los servidores** de Cloudflare

**Diferencia clave:**
- **Pages:** Sirve archivos (como un Dropbox público)
- **Workers:** Ejecuta código JavaScript en el servidor (como Railway pero para JS)

**Ejemplo de Worker:**
```javascript
// Este código se ejecuta EN EL SERVIDOR
export default {
  async fetch(request) {
    // Hacer cálculos
    // Acceder a bases de datos
    // Procesar imágenes
    return new Response("Hola desde el servidor");
  }
}
```

**¿Cuándo usar Workers?**
- Necesitas procesar datos en el servidor
- Necesitas acceder a APIs con claves secretas
- Necesitas hacer redirecciones complejas
- Necesitas autenticación del lado del servidor

**Tu proyecto NO necesita Workers porque:**
- Tu frontend solo sirve archivos HTML/JS ✅ Pages
- El procesamiento lo hace el backend FastAPI en Railway ✅ Railway
- No hay lógica del lado del servidor en el frontend ✅ Pages es suficiente

---

### Tabla comparativa: Pages vs Workers

| Característica | Pages | Workers |
|----------------|-------|---------|
| **Propósito** | Hosting de archivos estáticos | Ejecutar código JavaScript en servidor |
| **Tecnología** | HTML, CSS, JS (cliente) | JavaScript (servidor) |
| **Ejecución** | En el navegador del usuario | En servidores de Cloudflare |
| **Deploy** | Archivos desde GitHub | Código JavaScript |
| **Ejemplo** | Blog, landing page, **tu frontend** | API, proxy, autenticación |
| **Costo** | Gratis ilimitado | Gratis (100,000 requests/día) |
| **Configuración** | Build output directory | Deploy command + código |

---

### ¿Por qué existe la confusión?

**Cloudflare unificó Workers y Pages en 2024:**

**Antes (hasta 2023):**
- Workers: `workers.cloudflare.com`
- Pages: `pages.cloudflare.com`
- 2 dashboards separados

**Ahora (2024+):**
- Todo en: `dash.cloudflare.com` → Workers & Pages
- Mismo dashboard, misma interfaz
- Flujo confuso: Pages está "escondido" detrás de "Get started"

**Por eso en tu captura viste:**
- Pantalla principal: "Create a Worker"
- Abajo: "Looking to deploy Pages? Get started"

---

### Flujo completo de tu aplicación

```
Usuario escribe: formulas-web.pages.dev
           ↓
[Cloudflare Pages: sirve archivos estáticos]
           ↓
Navegador descarga: index.html, api.js, app.js
           ↓
JavaScript ejecuta EN EL NAVEGADOR
           ↓
Usuario selecciona fórmula y hace click "Calcular"
           ↓
JavaScript hace fetch() a Railway
           ↓
[Railway Backend: ejecuta Python, consulta Supabase]
           ↓
Railway devuelve JSON con datos del gráfico
           ↓
JavaScript recibe datos y renderiza gráfico con Plotly
           ↓
Usuario ve el gráfico
```

**3 piezas separadas:**
1. **Cloudflare Pages:** Sirve archivos (frontend)
2. **Railway:** Ejecuta Python (backend)
3. **Supabase:** Almacena datos (base de datos)

---

## 🔄 Futuras actualizaciones

**Cada vez que hagas `git push` a GitHub:**

→ Cloudflare **automáticamente** re-despliega tu frontend

**No necesitas hacer nada más** - deploy continuo activado por defecto.

**Ver deploys:**
1. En Cloudflare → Workers & Pages
2. Click en tu proyecto `formulas-web`
3. Pestaña "Deployments"
4. Verás historial de deploys

---

## 📊 Ventajas de Cloudflare Pages

### 1. CDN Global

**¿Qué es un CDN?**
Content Delivery Network = Red de distribución de contenido

**Cómo funciona:**
- Cloudflare tiene servidores en 300+ ciudades del mundo
- Cuando despliegas en Pages, tus archivos se copian a TODOS esos servidores
- Cuando un usuario accede, recibe los archivos desde el servidor MÁS CERCANO

**Ejemplo:**
- Usuario en Madrid → Servidor de Madrid (10 ms)
- Usuario en Buenos Aires → Servidor de Buenos Aires (15 ms)
- Usuario en Tokio → Servidor de Tokio (12 ms)

**Sin CDN (servidor único):**
- Usuario en Madrid → Servidor en USA (150 ms)
- Usuario en Buenos Aires → Servidor en USA (200 ms)
- Usuario en Tokio → Servidor en USA (300 ms)

**Resultado:** Tu app carga 10-20x más rápido

---

### 2. HTTPS automático

**¿Qué es HTTPS?**
- HTTP**S** = HTTP + Seguridad (S = Secure)
- Cifra la comunicación entre navegador y servidor
- Necesario para que Google no marque tu sitio como "No seguro"

**Cloudflare Pages:**
- Genera certificado SSL automáticamente
- Renueva antes de que expire (cada 90 días)
- Gratis
- **TÚ NO HACES NADA** → automático

**Sin Cloudflare:**
- Configurar Let's Encrypt manualmente
- Renovar certificados cada 90 días
- Configurar Nginx/Apache para usar HTTPS

---

### 3. Ancho de banda ilimitado

**Otros servicios gratuitos:**
- Netlify: 100 GB/mes
- Vercel: 100 GB/mes
- GitHub Pages: 100 GB/mes

**Cloudflare Pages:**
- **Ilimitado**
- Puede servir 1 TB sin coste adicional

**¿Por qué gratis?**
Cloudflare gana dinero con otros servicios (CDN empresarial, Workers, R2...). Pages es un "anzuelo" para atraer usuarios que luego paguen por otros productos.

---

### 4. Número de requests ilimitado

**Otros servicios:**
- Netlify: 3,000,000 requests/mes
- Vercel: 10,000,000 requests/mes

**Cloudflare Pages:**
- **Sin límite oficial**
- Puede manejar millones sin problema

---

## ⚠️ Troubleshooting

### Error: "Build failed"

**Ver logs:**
1. Cloudflare → Workers & Pages
2. Click en tu proyecto
3. Click en el deployment fallido
4. Lee los logs

**Errores comunes:**

#### "Build command failed"
**Causa:** Pusiste algo en "Build command" pero el comando no existe

**Solución:** Dejar "Build command" vacío

#### "Directory not found: /frontend"
**Causa:** Pusiste `/frontend` pero la carpeta no existe o se llama diferente

**Solución:**
Verificar en GitHub que la carpeta se llama exactamente `frontend` (minúsculas)

#### "No index.html found"
**Causa:** Cloudflare busca `index.html` en `/frontend` pero no lo encuentra

**Solución:**
Verificar que existe `frontend/index.html` en GitHub

---

### La página carga pero "Cargando fórmulas..." no termina

**Diagnóstico:**
1. F12 → Console
2. Busca errores

**Error común:**
```
Failed to fetch https://web-production-daa0.up.railway.app/api/formulas
```

**Causas posibles:**

#### 1. Backend de Railway no está funcionando
**Verificar:**
```
https://web-production-daa0.up.railway.app/health
```

**Debe responder:**
```json
{"status":"ok"}
```

**Si no responde:**
- Railway puede estar "dormido" (primera request tarda ~30s)
- O el backend tiene un error (ver logs en Railway)

#### 2. URL incorrecta en api.js
**Verificar:**
- Abrir: `frontend/js/api.js`
- Línea 15 debe tener la URL correcta de Railway:
  ```javascript
  : 'https://web-production-daa0.up.railway.app';
  ```

**Si está mal:**
- Editar `api.js`
- Commit y push a GitHub
- Cloudflare re-desplegará automáticamente en 1-2 minutos

---

### La página se ve rota (sin estilos)

**Causa:**
Rutas incorrectas en `index.html`

**Verificar:**
```html
<!-- ❌ INCORRECTO (rutas absolutas) -->
<link href="/frontend/css/styles.css">

<!-- ✅ CORRECTO (rutas relativas) -->
<link href="css/styles.css">
```

**¿Por qué?**
- Cloudflare sirve desde `/frontend` como raíz
- Si tu HTML dice `/frontend/css`, busca `/frontend/frontend/css` → 404

---

## 🚀 Optimizaciones avanzadas (opcional)

### Custom Domain (dominio personalizado)

**Por defecto:** `https://formulas-web.pages.dev`

**Puedes cambiar a:** `https://formulas.tudominio.com`

**Pasos:**
1. Comprar un dominio (ej: Namecheap, Google Domains)
2. Cloudflare → tu proyecto → "Custom domains"
3. Añadir tu dominio
4. Configurar DNS (Cloudflare te da instrucciones)
5. Esperar propagación (5-60 min)

**Coste:** Solo el dominio (~10-15€/año). Cloudflare Pages sigue siendo gratis.

---

### Preview Deployments (despliegues de previsualización)

**¿Qué es?**
Cada vez que creas un Pull Request en GitHub, Cloudflare genera una URL temporal para ver los cambios ANTES de hacer merge a `main`.

**Ejemplo:**
1. Creas rama `feature/nueva-formula`
2. Haces cambios y push
3. Abres Pull Request en GitHub
4. Cloudflare comenta en el PR: "Preview: https://abc123.formulas-web.pages.dev"
5. Revisas los cambios en esa URL temporal
6. Si todo bien → Merge a `main`
7. Cloudflare despliega en `https://formulas-web.pages.dev`

**Activado por defecto** - no necesitas configurar nada.

---

## 📚 Recursos

- **Documentación oficial:** https://developers.cloudflare.com/pages/
- **Diferencias Pages vs Workers:** https://developers.cloudflare.com/pages/platform/comparing-pages-to-workers/
- **Limits del plan gratuito:** https://developers.cloudflare.com/pages/platform/limits/
- **Cloudflare Dashboard:** https://dash.cloudflare.com

---

## ✅ Resumen: ¿Qué hiciste?

| Paso | Qué hiciste | ¿Por qué? |
|------|-------------|-----------|
| 1 | Crear cuenta en Cloudflare | Acceso a Pages |
| 2 | Navegar a Workers & Pages | Sección unificada |
| 3 | Click en "Looking to deploy Pages? Get started" | Acceder a Pages (oculto) |
| 4 | Conectar GitHub | Cloudflare necesita acceso al código |
| 5 | Seleccionar repo `formulas-web` | Elegir qué desplegar |
| 6 | Configurar: Build output = `/frontend` | Decirle dónde están los archivos web |
| 7 | Dejar Build command vacío | No hay proceso de compilación |
| 8 | Deploy | Copiar archivos a CDN global |
| 9 | Obtener URL | `https://formulas-web.pages.dev` |

---

**Próximo paso:** Tu aplicación está COMPLETA y DESPLEGADA 🎉

**3 URLs de producción:**
- 🗄️ Base de datos: `https://qfeatlcnilhqjcacniih.supabase.co`
- 🐍 Backend: `https://web-production-daa0.up.railway.app`
- 🌐 Frontend: `https://formulas-web.pages.dev`

---

*Guía creada: 7 Enero 2026*
