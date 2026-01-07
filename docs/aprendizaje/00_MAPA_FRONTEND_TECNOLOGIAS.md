# Mapa del Frontend: Tecnologías y Conexiones

> **Propósito:** Entender QUÉ es cada pieza, POR QUÉ la usamos, y CÓMO se conectan.
> **No es:** Un tutorial de JavaScript. Es un mapa mental de arquitectura.

---

## PARTE 0: CORS - El guardián de seguridad

### El problema (sin CORS)

Imagina esto:

```
Tu frontend está en:     http://localhost:3000
Tu backend está en:      http://localhost:8000
```

Son dos "orígenes" diferentes (diferente puerto = diferente origen).

**Por seguridad, los navegadores BLOQUEAN que una página hable con servidores de otro origen.**

Es como si tu navegador dijera:

> "Oye, esta página viene de localhost:3000, pero quiere hablar con localhost:8000. 
> ¿Y si es un hacker intentando robar datos? BLOQUEADO."

---

### ¿Qué es CORS?

**CORS = Cross-Origin Resource Sharing** (Compartir recursos entre orígenes)

Es un mecanismo donde el SERVIDOR dice:

> "Tranquilo navegador, SÍ permito que localhost:3000 me hable. Déjalo pasar."

---

### Analogía: El portero del edificio

```
┌─────────────────────────────────────────────────────────────┐
│                                                             │
│   EDIFICIO (Backend en puerto 8000)                         │
│                                                             │
│   ┌─────────┐                                               │
│   │ PORTERO │  "¿Quién eres y de dónde vienes?"             │
│   │ (CORS)  │                                               │
│   └────┬────┘                                               │
│        │                                                    │
│        ▼                                                    │
│   ┌─────────────────────────────────────────────────────┐   │
│   │ Lista de permitidos:                                │   │
│   │                                                     │   │
│   │   ✅ localhost:3000  → "Pasa, eres de confianza"   │   │
│   │   ✅ midominio.com   → "Pasa, te conozco"          │   │
│   │   ❌ hacker.com      → "No estás en la lista"      │   │
│   │                                                     │   │
│   └─────────────────────────────────────────────────────┘   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

**Sin CORS configurado** = Portero que no deja pasar a NADIE
**Con CORS configurado** = Portero con lista de invitados permitidos

---

### El error típico sin CORS

Si no configuras CORS, al abrir el frontend verás este error en la consola:

```
❌ Access to fetch at 'http://localhost:8000/api/formulas' 
   from origin 'http://localhost:3000' has been blocked by CORS policy
```

El navegador bloqueó la petición porque el backend no dijo "sí, permito esto".

---

### Cómo se configura en FastAPI

```python
# backend/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # ← Importar

app = FastAPI(...)

# Configurar CORS (el portero)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # ← Quién puede entrar (* = todos)
    allow_credentials=True,     # ← Permitir cookies
    allow_methods=["*"],        # ← Qué métodos (GET, POST, etc.)
    allow_headers=["*"],        # ← Qué cabeceras HTTP
)
```

**`allow_origins=["*"]`** significa "deja pasar a TODOS".

En producción pondrías tu dominio real:
```python
allow_origins=["https://miapp.com", "https://www.miapp.com"]
```

---

### ¿Por qué es ANTES del frontend?

Porque si el frontend intenta hablar con el backend y CORS no está configurado:

1. El navegador bloquea
2. No ves datos
3. Parece que nada funciona
4. Pierdes 2 horas buscando el error

**Configurar CORS primero = Evitar dolor de cabeza.**

---

### Resumen CORS

| Concepto | Explicación simple |
|----------|--------------------|
| **CORS** | Permiso del servidor para que otros orígenes le hablen |
| **Origen** | Combinación de protocolo + dominio + puerto |
| **Sin CORS** | El navegador bloquea las peticiones |
| **Con CORS** | El navegador permite las peticiones |
| **`allow_origins`** | Lista de quién puede hablar con el servidor |
| **`"*"`** | Todos pueden (solo para desarrollo) |

---

## VISIÓN GENERAL: ¿Qué estamos construyendo?

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           NAVEGADOR DEL USUARIO                         │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │                         index.html                               │   │
│  │                    (La estructura/esqueleto)                     │   │
│  │                                                                  │   │
│  │   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │   │
│  │   │   TAILWIND   │  │   DAISYUI    │  │   PLOTLY     │          │   │
│  │   │   (Estilos)  │  │ (Componentes)│  │  (Gráficos)  │          │   │
│  │   └──────────────┘  └──────────────┘  └──────────────┘          │   │
│  │                                                                  │   │
│  │   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │   │
│  │   │   MATHJAX    │  │    api.js    │  │   app.js     │          │   │
│  │   │   (LaTeX)    │  │(Habla con API)│  │  (Cerebro)  │          │   │
│  │   └──────────────┘  └──────────────┘  └──────────────┘          │   │
│  │                                                                  │   │
│  └─────────────────────────────────────────────────────────────────┘   │
│                                    │                                    │
│                                    │ HTTP (fetch)                       │
│                                    ▼                                    │
└────────────────────────────────────┼────────────────────────────────────┘
                                     │
                                     ▼
                    ┌────────────────────────────────┐
                    │     BACKEND (FastAPI)          │
                    │     http://localhost:8000      │
                    └────────────────────────────────┘
                                     │
                                     ▼
                    ┌────────────────────────────────┐
                    │     SUPABASE (PostgreSQL)      │
                    └────────────────────────────────┘
```

---

## PARTE 1: LAS TECNOLOGÍAS

---

### 1. HTML - El esqueleto

**¿Qué es?**
El lenguaje que define la ESTRUCTURA de una página web. Como los huesos de un cuerpo.

**¿Por qué lo necesitamos?**
Sin HTML no hay página. Es obligatorio. Todo lo demás se "monta" sobre el HTML.

**Analogía:**
```
HTML = Los ladrillos y estructura de una casa
CSS  = La pintura, decoración, muebles
JS   = La electricidad, fontanería, cosas que "funcionan"
```

**Link oficial:** https://developer.mozilla.org/es/docs/Web/HTML

**En nuestro proyecto:**
`frontend/index.html` define:
- Dónde va el selector de fórmulas
- Dónde va el gráfico
- Dónde van los inputs
- Dónde va el historial

---

### 2. TAILWIND CSS - Estilos con clases

**¿Qué es?**
Una librería CSS que te da clases predefinidas para estilizar.

**¿Por qué lo usamos?**
En lugar de escribir CSS desde cero:
```css
/* CSS tradicional - tedioso */
.mi-boton {
  background-color: blue;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
}
```

Escribes clases directamente en HTML:
```html
<!-- Tailwind - rápido y consistente -->
<button class="bg-blue-500 text-white px-5 py-2 rounded">
```

**Ventajas:**
- No inventas nombres de clases
- Diseño consistente
- Responsive fácil (`md:`, `lg:`)
- Claude lo domina perfectamente

**Link oficial:** https://tailwindcss.com/docs

**Clases que verás mucho:**
| Clase | Qué hace |
|-------|----------|
| `bg-slate-900` | Fondo color slate oscuro |
| `text-white` | Texto blanco |
| `p-4` | Padding de 1rem (16px) |
| `rounded-lg` | Bordes redondeados |
| `flex` | Display flexbox |
| `grid` | Display grid |
| `hover:bg-blue-600` | Color al pasar ratón |

---

### 3. DAISYUI - Componentes bonitos

**¿Qué es?**
Una librería que añade COMPONENTES prediseñados sobre Tailwind.

**¿Por qué lo usamos?**
Tailwind te da las piezas. DaisyUI te da muebles ya montados.

```html
<!-- Sin DaisyUI: montar botón manualmente -->
<button class="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded">
  Calcular
</button>

<!-- Con DaisyUI: componente listo -->
<button class="btn btn-primary">Calcular</button>
```

**Componentes que usamos:**
| Componente | Para qué |
|------------|----------|
| `btn` | Botones con estilos |
| `card` | Contenedores con sombra |
| `select` | Desplegables bonitos |
| `input` | Campos de texto |
| `loading` | Spinners de carga |
| `badge` | Etiquetas pequeñas |

**Link oficial:** https://daisyui.com/components/

**Temas:**
DaisyUI incluye temas. Usamos tema oscuro:
```html
<html data-theme="dark">
```

---

### 4. PLOTLY.JS - Gráficos interactivos

**¿Qué es?**
Librería para crear gráficos científicos interactivos.

**¿Por qué lo usamos?**
- Zoom con el ratón
- Hover muestra valores
- Animaciones suaves
- Exportar a PNG
- Perfecto para fórmulas matemáticas

**Alternativas que descartamos:**
| Librería | Por qué no |
|----------|-----------|
| Chart.js | Menos científico, más para dashboards |
| D3.js | Muy potente pero muy complejo |
| Google Charts | Menos personalizable |

**Link oficial:** https://plotly.com/javascript/

**Cómo funciona (concepto):**
```javascript
// Le das datos X e Y
const datos = {
  x: [0, 1, 2, 3, 4],      // Eje horizontal (tiempo)
  y: [0, 5, 10, 15, 20]    // Eje vertical (posición)
};

// Le dices dónde pintarlo
Plotly.newPlot('mi-grafico', [datos]);
```

El backend nos devuelve los arrays `t` y `x`. Plotly los dibuja.

---

### 5. MATHJAX - Renderizar fórmulas LaTeX

**¿Qué es?**
Librería que convierte texto LaTeX en fórmulas matemáticas bonitas.

**¿Por qué lo usamos?**
La base de datos guarda las fórmulas así:
```
x = x_0 + v \cdot t
```

MathJax lo convierte en:
$$x = x_0 + v \cdot t$$

**Link oficial:** https://www.mathjax.org/

**Cómo funciona:**
1. Pones la fórmula en el HTML: `\( x = x_0 + v \cdot t \)`
2. MathJax la detecta automáticamente
3. La renderiza como imagen matemática

---

### 6. GOOGLE FONTS (Inter) - Tipografía

**¿Qué es?**
Servicio gratuito de fuentes tipográficas.

**¿Por qué Inter?**
- Diseñada para pantallas
- Muy legible
- Moderna y limpia
- Usada por muchas apps profesionales

**Link oficial:** https://fonts.google.com/specimen/Inter

**Cómo se carga:**
```html
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
```

---

## PARTE 2: LOS ARCHIVOS JAVASCRIPT

---

### api.js - El mensajero

**¿Qué hace?**
Habla con el backend. Es el único archivo que sabe cómo comunicarse con FastAPI.

**Analogía:**
```
api.js = El cartero
- Lleva cartas (peticiones) al servidor
- Trae respuestas de vuelta
- No le importa qué dicen las cartas, solo entregarlas
```

**Funciones que contiene:**
```
obtenerFormulas()    → Pide la lista de fórmulas
obtenerFormula(id)   → Pide una fórmula específica
calcularFormula()    → Envía valores, recibe puntos
obtenerHistorial()   → Pide cálculos anteriores
```

**¿Por qué separarlo?**
Si mañana cambias la URL del servidor, solo tocas ESTE archivo.

---

### graficos.js - El artista

**¿Qué hace?**
Configura y dibuja los gráficos con Plotly.

**Analogía:**
```
graficos.js = El pintor
- Recibe datos (números)
- Los convierte en arte visual (gráficos)
- Sabe cómo usar los pinceles (Plotly)
```

**Funciones que contiene:**
```
configurarGrafico()   → Prepara el lienzo
dibujarFormula()      → Pinta los puntos
animarTransicion()    → Hace la animación suave
```

**¿Por qué separarlo?**
Si quieres cambiar colores o estilo del gráfico, solo tocas ESTE archivo.

---

### app.js - El cerebro

**¿Qué hace?**
Coordina todo. Es el director de orquesta.

**Analogía:**
```
app.js = El director de orquesta
- No toca ningún instrumento
- Dice cuándo entra cada uno
- Coordina que todo suene bien junto
```

**Qué coordina:**
```
1. Usuario selecciona fórmula  → Llama a api.js para obtenerla
2. Usuario hace clic en Calcular → Llama a api.js para calcular
3. API devuelve datos → Llama a graficos.js para dibujar
4. Todo termina → Actualiza el historial
```

**¿Por qué separarlo?**
La lógica de "qué pasa cuando" está en UN solo lugar.

---

## PARTE 3: CÓMO SE CONECTA TODO

---

### El flujo completo (paso a paso)

```
USUARIO                     FRONTEND                      BACKEND
   │                           │                             │
   │  1. Abre la página        │                             │
   │ ─────────────────────────>│                             │
   │                           │                             │
   │                           │  2. app.js arranca          │
   │                           │     Llama a api.js          │
   │                           │                             │
   │                           │  3. api.js hace GET         │
   │                           │ ───────────────────────────>│
   │                           │     /api/formulas           │
   │                           │                             │
   │                           │  4. Backend consulta BD     │
   │                           │<───────────────────────────│
   │                           │     [{id:1, nombre:MRU}]    │
   │                           │                             │
   │  5. Ve lista de fórmulas  │                             │
   │<──────────────────────────│                             │
   │                           │                             │
   │  6. Selecciona MRU        │                             │
   │ ─────────────────────────>│                             │
   │                           │                             │
   │  7. Escribe valores       │                             │
   │     v=5, t=0-10           │                             │
   │                           │                             │
   │  8. Clic en CALCULAR      │                             │
   │ ─────────────────────────>│                             │
   │                           │                             │
   │                           │  9. api.js hace POST        │
   │                           │ ───────────────────────────>│
   │                           │     /api/calcular           │
   │                           │     {formula_id:1,          │
   │                           │      valores:{v:5,...}}     │
   │                           │                             │
   │                           │  10. Backend calcula        │
   │                           │      Guarda en BD           │
   │                           │<───────────────────────────│
   │                           │     {t:[...], x:[...]}      │
   │                           │                             │
   │                           │  11. app.js recibe datos    │
   │                           │      Llama a graficos.js    │
   │                           │                             │
   │  12. Ve el gráfico        │                             │
   │<──────────────────────────│                             │
   │      animado              │                             │
   │                           │                             │
```

---

### Diagrama de archivos y dependencias

```
                    index.html
                        │
         ┌──────────────┼──────────────┐
         │              │              │
         ▼              ▼              ▼
    styles.css      app.js         CDNs
                       │           (externos)
              ┌────────┼────────┐
              │        │        │
              ▼        ▼        ▼
          api.js  graficos.js  Tailwind
              │        │       DaisyUI
              │        │       Plotly
              ▼        ▼       MathJax
         Backend    Plotly     Inter
         (HTTP)     (dibujar)
```

**Regla clave:**
- `app.js` importa/usa a `api.js` y `graficos.js`
- `api.js` y `graficos.js` NO se conocen entre sí
- `app.js` es el único que los conecta

---

## PARTE 4: ¿QUÉ SE ENSEÑA CON CADA PARTE?

---

### Lecciones por archivo

| Archivo | Qué aprendes |
|---------|--------------|
| `index.html` | Estructura semántica, cargar CDNs, layout con CSS Grid/Flexbox |
| `api.js` | Fetch API, async/await, manejo de errores HTTP |
| `graficos.js` | Usar librerías externas, configurar opciones, bindings |
| `app.js` | Event listeners, manipulación DOM, coordinación de módulos |
| `styles.css` | CSS custom, animaciones, variables CSS |

---

### Lecciones por concepto

| Concepto | Dónde se ve | Qué aprendes |
|----------|-------------|--------------|
| **Separación de responsabilidades** | 3 archivos JS | Cada archivo hace UNA cosa |
| **Comunicación HTTP** | api.js | Cómo frontend habla con backend |
| **Asincronía** | api.js | Las peticiones no son instantáneas |
| **Eventos** | app.js | El código reacciona a acciones del usuario |
| **DOM** | app.js | Modificar la página dinámicamente |
| **Librerías externas** | CDNs | Usar código de otros (no reinventar) |
| **Diseño responsive** | Tailwind | Una página, múltiples tamaños |

---

### El concepto más importante: SEPARACIÓN

```
❌ MAL: Un solo archivo gigante que hace todo

   todo.js (500 líneas)
   - Estilos mezclados con lógica
   - Fetch mezclado con DOM
   - Imposible de mantener

✅ BIEN: Archivos pequeños especializados

   api.js      → Solo comunicación
   graficos.js → Solo dibujar
   app.js      → Solo coordinar
   
   Cada uno hace UNA cosa bien
   Fácil de entender y modificar
```

---

## PARTE 5: RESUMEN VISUAL

```
┌─────────────────────────────────────────────────────────────────────────┐
│                                                                         │
│   FRONTEND = Varias piezas que trabajan juntas                          │
│                                                                         │
│   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐   │
│   │   TAILWIND  │  │   DAISYUI   │  │   PLOTLY    │  │   MATHJAX   │   │
│   │             │  │             │  │             │  │             │   │
│   │  "Cómo se   │  │ "Muebles    │  │  "Dibuja    │  │ "Renderiza  │   │
│   │   ve"       │  │  listos"    │  │  gráficos"  │  │  fórmulas"  │   │
│   │             │  │             │  │             │  │             │   │
│   │  ESTILOS    │  │ COMPONENTES │  │   DATOS     │  │    LATEX    │   │
│   └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘   │
│          │                │                │                │          │
│          └────────────────┴────────────────┴────────────────┘          │
│                                    │                                    │
│                                    ▼                                    │
│                           ┌─────────────┐                               │
│                           │  index.html │                               │
│                           │ (los junta) │                               │
│                           └─────────────┘                               │
│                                    │                                    │
│          ┌─────────────────────────┼─────────────────────────┐          │
│          │                         │                         │          │
│          ▼                         ▼                         ▼          │
│   ┌─────────────┐          ┌─────────────┐          ┌─────────────┐    │
│   │   api.js    │          │   app.js    │          │ graficos.js │    │
│   │             │◄────────▶│             │◄────────▶│             │    │
│   │  "Cartero"  │          │ "Director"  │          │  "Pintor"   │    │
│   └─────────────┘          └─────────────┘          └─────────────┘    │
│          │                                                              │
│          │  HTTP                                                        │
│          ▼                                                              │
│   ┌─────────────┐                                                       │
│   │   BACKEND   │                                                       │
│   │  (FastAPI)  │                                                       │
│   └─────────────┘                                                       │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## PARTE 6: LINKS DE REFERENCIA

### Documentación oficial

| Tecnología | Link | Para qué consultarlo |
|------------|------|---------------------|
| **HTML** | https://developer.mozilla.org/es/docs/Web/HTML | Etiquetas, atributos |
| **Tailwind** | https://tailwindcss.com/docs | Clases disponibles |
| **DaisyUI** | https://daisyui.com/components/ | Componentes y ejemplos |
| **Plotly.js** | https://plotly.com/javascript/ | Tipos de gráficos, opciones |
| **MathJax** | https://docs.mathjax.org/en/latest/ | Sintaxis LaTeX |
| **Fetch API** | https://developer.mozilla.org/es/docs/Web/API/Fetch_API | Cómo hacer peticiones |
| **Google Fonts** | https://fonts.google.com/ | Buscar fuentes |

### Tutoriales recomendados

| Tema | Link |
|------|------|
| Tailwind en 15 min | https://www.youtube.com/watch?v=mr15Xzb1Ook |
| Plotly.js básico | https://plotly.com/javascript/getting-started/ |
| Fetch API explicado | https://javascript.info/fetch |

---

## PARTE 7: GLOSARIO RÁPIDO

| Término | Significado simple |
|---------|---------------------|
| **CDN** | Servidor externo que nos da librerías listas para usar |
| **DOM** | La estructura de la página que JavaScript puede modificar |
| **Fetch** | Función de JS para hacer peticiones HTTP |
| **async/await** | Forma de esperar respuestas sin bloquear |
| **Responsive** | Que se adapta a móvil, tablet, desktop |
| **Componente** | Pieza visual reutilizable (botón, card, etc.) |
| **CDN** | Content Delivery Network - servidores rápidos |
| **Renderizar** | Convertir código en algo visual |

---

*Documento creado: 29 diciembre 2024*
*Propósito: Mapa mental de las tecnologías frontend y cómo se conectan*
