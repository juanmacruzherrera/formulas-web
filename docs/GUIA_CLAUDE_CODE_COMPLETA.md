# GUÍA COMPLETA DE CLAUDE CODE
## Para estudiantes que aprenden a programar con IA

**Autor:** Claude Opus 4.5
**Fecha:** 9 Enero 2026
**Nivel:** Principiante → Intermedio
**Requisitos previos:** Saber usar la terminal, conocimientos básicos de Python

---

# PARTE 1: ¿QUÉ ES CLAUDE CODE?

## 1.1 Concepto Simple

Claude Code es **Claude en tu terminal**. En vez de usar el chat web (claude.ai), usas la línea de comandos de tu ordenador para hablar con Claude.

**Analogía del restaurante:**
- **Claude.ai (web)** = Ir al restaurante, sentarte, pedir al camarero
- **Claude Code (terminal)** = El chef viene a tu cocina y cocina contigo

## 1.2 ¿Por qué usar Claude Code?

| Ventaja | Explicación |
|---------|-------------|
| **Acceso a tus archivos** | Claude puede leer, crear y modificar archivos en tu ordenador |
| **Ejecutar comandos** | Puede correr scripts de Python, instalar paquetes, usar git |
| **Contexto del proyecto** | Entiende la estructura de tu proyecto completo |
| **Flujo continuo** | No necesitas copiar/pegar código entre el chat y tu editor |

## 1.3 ¿Cuándo NO usar Claude Code?

- Para preguntas rápidas → Usa claude.ai (es más rápido)
- Para planificación/arquitectura → Usa claude.ai con Opus
- Cuando no necesitas modificar archivos → Usa claude.ai

---

# PARTE 2: INSTALACIÓN

## 2.1 Requisitos

```bash
# Verificar que tienes Node.js instalado
node --version
# Debe mostrar v18.0.0 o superior

# Si no lo tienes, instálalo:
# Mac: brew install node
# Windows: Descarga de https://nodejs.org
# Linux: sudo apt install nodejs
```

## 2.2 Instalación de Claude Code

```bash
# Instalar globalmente con npm
npm install -g @anthropic-ai/claude-code

# Verificar instalación
claude --version
```

## 2.3 Autenticación

```bash
# Primera vez: te pedirá iniciar sesión
claude

# Se abrirá el navegador para autenticarte con tu cuenta de Anthropic
# Después de autenticarte, ya puedes usar Claude Code
```

---

# PARTE 3: COMANDOS BÁSICOS

## 3.1 Iniciar Claude Code

```bash
# Forma básica: iniciar en el directorio actual
claude

# Iniciar en un directorio específico
claude /ruta/a/tu/proyecto

# Ejemplo real:
claude /Users/juan/proyectos/formulas-web
```

**¿Qué pasa cuando ejecutas `claude`?**
1. Se abre una sesión interactiva
2. Claude lee los archivos de tu directorio
3. Busca archivos especiales como `CLAUDE.md` para entender el contexto
4. Queda esperando tus instrucciones

## 3.2 Comandos dentro de la sesión

Una vez dentro de Claude Code, puedes escribir:
- **Texto normal** → Claude lo interpreta como instrucción
- **Comandos con /** → Acciones especiales del sistema

### Tabla de comandos con /

| Comando | Qué hace | Ejemplo de uso |
|---------|----------|----------------|
| `/help` | Muestra ayuda | Cuando no sabes qué hacer |
| `/clear` | Limpia la conversación | Cuando quieres empezar de cero |
| `/compact` | Compacta el contexto | Cuando la sesión se vuelve lenta |
| `/status` | Muestra estado actual | Ver cuánto contexto has usado |
| `/quit` o `/exit` | Salir de Claude Code | Cuando terminas de trabajar |
| `/model` | Ver/cambiar modelo | Cambiar entre Sonnet y Opus |
| `/config` | Ver configuración | Revisar parámetros actuales |

## 3.3 Ejemplos de uso básico

```
# Dentro de Claude Code:

> Lee el archivo main.py y explícame qué hace
[Claude lee el archivo y te explica]

> Crea un archivo llamado test.py con una función que sume dos números
[Claude crea el archivo]

> Ejecuta python test.py
[Claude ejecuta el comando y te muestra el resultado]

> /clear
[Limpia la conversación, mantiene los archivos]

> /quit
[Sales de Claude Code]
```

---

# PARTE 4: MODELOS Y CÓMO CAMBIARLOS

## 4.1 ¿Qué modelos hay?

| Modelo | Nombre técnico | Características |
|--------|---------------|-----------------|
| **Sonnet 4** | `claude-sonnet-4-5-20250514` | Rápido, bueno para código, económico |
| **Opus 4.5** | `claude-opus-4-5-20250514` | Más inteligente, mejor razonamiento, más caro |
| **Haiku 4.5** | `claude-haiku-4-5-20251001` | Muy rápido, tareas simples, muy económico |

## 4.2 Ver modelo actual

```bash
# Fuera de Claude Code (en terminal normal)
claude config get model

# Dentro de Claude Code
/model
```

## 4.3 Cambiar modelo permanentemente

```bash
# Cambiar a Opus (más inteligente)
claude config set model claude-opus-4-5-20250514

# Cambiar a Sonnet (equilibrado)
claude config set model claude-sonnet-4-5-20250514

# Cambiar a Haiku (rápido y barato)
claude config set model claude-haiku-4-5-20251001
```

**¿Cuándo usar cada uno?**

| Situación | Modelo recomendado |
|-----------|-------------------|
| Escribir código rutinario | Sonnet |
| Debugging complejo | Opus |
| Arquitectura y diseño | Opus |
| Tareas repetitivas | Haiku |
| Proyecto nuevo desde cero | Opus → luego Sonnet |
| Corregir errores simples | Sonnet o Haiku |

## 4.4 Usar modelo diferente solo una vez

```bash
# Iniciar Claude Code con Opus solo para esta sesión
claude --model claude-opus-4-5-20250514

# El cambio NO es permanente
# La próxima vez que ejecutes `claude` usará el modelo configurado
```

## 4.5 Ejemplo práctico: Cambiar modelo durante un proyecto

```bash
# Estás trabajando con Sonnet y algo no funciona
# Quieres que Opus lo revise

# Opción 1: Cambiar permanentemente
claude config set model claude-opus-4-5-20250514
claude
> Revisa el archivo app.js, hay un bug que no encuentro

# Opción 2: Solo esta sesión
claude --model claude-opus-4-5-20250514
> Revisa el archivo app.js, hay un bug que no encuentro

# Después vuelves a Sonnet
claude config set model claude-sonnet-4-5-20250514
```

---

# PARTE 5: CONFIGURACIÓN AVANZADA

## 5.1 Ver toda la configuración

```bash
claude config list
```

**Parámetros importantes:**

| Parámetro | Qué controla | Valores típicos |
|-----------|--------------|-----------------|
| `model` | Qué modelo usa | sonnet, opus, haiku |
| `contextWindow` | Tamaño de contexto | 100k, 200k tokens |
| `autoCompact` | Compactar automáticamente | true/false |

## 5.2 Archivo CLAUDE.md

Este es el archivo MÁS IMPORTANTE. Claude Code lo lee automáticamente al iniciar.

**¿Dónde ponerlo?**
```
tu-proyecto/
├── CLAUDE.md        ← En la raíz del proyecto
├── src/
├── docs/
└── ...
```

**¿Qué poner en CLAUDE.md?**

```markdown
# CLAUDE.md

## Sobre este proyecto
Breve descripción de qué es y qué hace.

## Stack tecnológico
- Backend: Python + FastAPI
- Frontend: HTML + JavaScript
- Base de datos: Supabase

## Estructura del proyecto
```
proyecto/
├── backend/
├── frontend/
└── docs/
```

## Reglas importantes
- Siempre probar antes de hacer commit
- Documentar cada cambio
- No modificar archivos .env

## Tarea actual
Lo que quieres que Claude haga ahora.
```

**¿Por qué es importante?**
- Claude lo lee PRIMERO cada vez que inicias
- Le da contexto sobre tu proyecto
- Evita que tengas que repetir información
- Puedes poner reglas que siempre debe seguir

## 5.3 Configurar compactación automática

```bash
# Ver si está activada
claude config get autoCompact

# Activar compactación automática
claude config set autoCompact true

# Desactivar (si quieres controlarla manualmente)
claude config set autoCompact false
```

**¿Qué es la compactación?**

Cuando hablas mucho con Claude, el "contexto" (todo lo que se ha dicho) crece. Hay un límite. La compactación es como "resumir" la conversación para liberar espacio.

**Problema:** Al compactar se puede perder información importante.

**Solución:** 
- Guardar información importante en archivos (no solo en la conversación)
- Usar CLAUDE.md para lo que siempre debe recordar

---

# PARTE 6: TÉCNICAS DE TRABAJO EFECTIVAS

## 6.1 La técnica del "archivo de contexto"

**Problema:** Claude Code se compacta y pierde información.

**Solución:** Guardar todo lo importante en un archivo.

```markdown
# docs/CONTEXTO_ACTUAL.md

## Lo que está hecho
- ✅ Backend funcionando
- ✅ Base de datos conectada

## Lo que falta
- ❌ Arreglar bug en login
- ❌ Añadir tests

## Errores encontrados
### Error 1: NaN en cálculo
- Archivo: calculadora.py
- Línea: 45
- Solución: Añadir validación

## Decisiones tomadas
- Usamos PostgreSQL porque...
- El layout es 80-20 porque...
```

**Cómo usarlo:**

```
> Lee docs/CONTEXTO_ACTUAL.md y continúa donde lo dejamos
```

## 6.2 La técnica de "tareas pequeñas"

**Problema:** Pides muchas cosas → Claude se confunde → deja cosas atrás.

**Solución:** Una cosa a la vez.

```
# ❌ MAL: Todo junto
> Arregla el bug del login, añade validación al formulario, 
> crea tests para todo y despliega en producción

# ✅ BIEN: Paso a paso
> Paso 1: Arregla el bug del login
[Esperas a que termine y funcione]

> Paso 2: Ahora añade validación al formulario
[Esperas a que termine y funcione]

> Paso 3: Ahora crea tests para el login
[Y así sucesivamente]
```

## 6.3 La técnica del "checkpoint"

**Problema:** Haces muchos cambios → algo se rompe → no sabes qué fue.

**Solución:** Commit después de cada cambio que funcione.

```
> Arregla el bug del login
[Claude lo arregla]

> Prueba que funciona
[Claude ejecuta tests]

> Si funciona, haz git commit -m "Fix: bug del login"
[Claude hace commit]

> Ahora siguiente tarea...
```

## 6.4 La técnica de "verificación explícita"

**Problema:** Claude dice que hizo algo pero no lo verificó.

**Solución:** Pedir verificación explícita.

```
# ❌ MAL
> Añade la función de validación

# ✅ BIEN
> Añade la función de validación.
> Después de añadirla, muéstrame el código que escribiste
> y ejecuta un test para verificar que funciona.
```

## 6.5 La técnica del "prompt completo"

**Problema:** Das instrucciones vagas → Claude interpreta mal.

**Solución:** Prompt con toda la información necesaria.

```
# ❌ MAL: Vago
> Arregla el error

# ✅ BIEN: Completo
> Arregla el error en el archivo backend/services/calculadora.py
> 
> El error es: "Out of range float values are not JSON compliant: nan"
> 
> Ocurre en la función calcular_lorenz() línea 245
> 
> La solución es añadir validación con np.isfinite()
> 
> Después de arreglarlo, prueba con:
> curl http://localhost:8000/api/calcular -X POST -d '{"formula_id": 17}'
```

---

# PARTE 7: GESTIÓN DEL CONTEXTO

## 7.1 ¿Qué es el contexto?

El "contexto" es TODO lo que Claude "recuerda" en la sesión:
- Tu conversación
- Los archivos que ha leído
- Los comandos que ha ejecutado
- Los errores que ha visto

## 7.2 El problema del contexto largo

```
Inicio sesión: 0% contexto usado
↓
Lees archivos: 10% usado
↓
Haces cambios: 30% usado
↓
Más cambios: 60% usado
↓
Aún más: 90% usado
↓
¡COMPACTACIÓN! → Se "resume" todo → Posible pérdida de info
```

## 7.3 Ver cuánto contexto has usado

```
# Dentro de Claude Code
/status

# Mostrará algo como:
# Context: 45,000 / 200,000 tokens (22%)
```

## 7.4 Compactar manualmente

```
# Cuando el contexto está muy lleno y quieres controlarlo
/compact

# Claude resumirá la conversación
# IMPORTANTE: Antes de compactar, guarda info importante en archivos
```

## 7.5 Estrategia para sesiones largas

```
1. INICIO DE SESIÓN
   - Claude lee CLAUDE.md (automático)
   - Tú le dices qué tarea hacer

2. DURANTE LA SESIÓN
   - Cada cambio importante → commit
   - Cada decisión importante → documentar en archivo
   - Vigilar /status de vez en cuando

3. ANTES DE COMPACTAR
   - Guardar estado actual en un archivo
   - Ejemplo: docs/ESTADO_SESION.md

4. DESPUÉS DE COMPACTAR
   - Decirle a Claude: "Lee docs/ESTADO_SESION.md para continuar"
```

---

# PARTE 8: SOLUCIÓN DE PROBLEMAS COMUNES

## 8.1 "Claude no encuentra mis archivos"

**Síntoma:** Claude dice que no puede leer un archivo que sí existe.

**Causas y soluciones:**

```bash
# Causa 1: Estás en el directorio equivocado
pwd  # Ver dónde estás
cd /ruta/correcta  # Ir al directorio correcto
claude  # Reiniciar Claude Code

# Causa 2: El archivo está fuera del proyecto
# Claude solo puede acceder a archivos dentro del directorio donde lo iniciaste
# Solución: Iniciar Claude Code desde un directorio padre

# Causa 3: Permisos
ls -la archivo.py  # Ver permisos
chmod 644 archivo.py  # Dar permisos de lectura
```

## 8.2 "Claude se compacta muy seguido"

**Síntoma:** Cada poco tiempo se pierde contexto.

**Soluciones:**

```bash
# 1. Usar archivos en vez de conversación larga
# En vez de explicar todo en el chat, ponlo en CLAUDE.md

# 2. Sesiones más cortas y enfocadas
# En vez de una sesión de 4 horas, 4 sesiones de 1 hora

# 3. Desactivar auto-compactación (con cuidado)
claude config set autoCompact false
# Pero entonces TÚ debes compactar manualmente cuando sea necesario
```

## 8.3 "Claude hace cosas que no le pedí"

**Síntoma:** Modifica archivos que no debía o añade código extra.

**Soluciones:**

```
# 1. Ser más específico
> Modifica SOLO el archivo app.js, NO toques ningún otro archivo
> Añade SOLO la función X, no cambies nada más

# 2. Pedir confirmación antes
> Antes de hacer cambios, muéstrame exactamente qué vas a modificar
> Espera mi aprobación antes de guardar

# 3. Usar modo "dry run" (simulación)
> Simula los cambios sin guardarlos, muéstrame qué harías
```

## 8.4 "El código que escribió Claude no funciona"

**Síntoma:** Errores al ejecutar, bugs, comportamiento inesperado.

**Proceso de debugging:**

```
# Paso 1: Pedir que explique el código
> Explícame línea por línea qué hace este código

# Paso 2: Pedir que identifique el error
> Ejecuta el código y muéstrame el error exacto

# Paso 3: Pedir solución específica
> El error es [X]. ¿Cómo lo arreglamos?

# Paso 4: Verificar el arreglo
> Ahora ejecuta de nuevo y confirma que funciona
```

## 8.5 "Claude perdió el hilo de lo que estábamos haciendo"

**Síntoma:** Después de compactar, no recuerda decisiones anteriores.

**Prevención:**

```markdown
# Crear archivo docs/DECISIONES.md

## Decisiones del proyecto

### 2026-01-09: Layout
- Elegimos 80-20 porque el gráfico es lo principal
- Alternativa descartada: 50-50 (gráfico muy pequeño)

### 2026-01-09: Modelo de datos
- Usamos categoría "geometria_3d" para fórmulas 3D
- Las 2D usan: "fisica", "matematicas", "curvas_exoticas"
```

**Recuperación:**

```
> Lee docs/DECISIONES.md para entender el contexto del proyecto
> Luego continúa con [tarea]
```

---

# PARTE 9: FLUJO DE TRABAJO RECOMENDADO

## 9.1 Para un proyecto nuevo

```bash
# 1. Crear estructura
mkdir mi-proyecto
cd mi-proyecto

# 2. Crear CLAUDE.md básico
cat > CLAUDE.md << 'EOF'
# Mi Proyecto

## Descripción
[Qué es y qué hace]

## Stack
- Python 3.11
- FastAPI

## Estructura
[Se irá llenando]

## Tarea actual
Crear la estructura básica del proyecto
EOF

# 3. Iniciar Claude Code con Opus (para diseño inicial)
claude --model claude-opus-4-5-20250514

# 4. Dentro de Claude Code
> Ayúdame a diseñar la estructura del proyecto
> Es una aplicación que [descripción]
```

## 9.2 Para trabajo diario en proyecto existente

```bash
# 1. Ir al proyecto
cd /ruta/a/mi-proyecto

# 2. Actualizar CLAUDE.md con tarea del día
# Añadir al final:
## Tarea de hoy (2026-01-09)
- Arreglar bug X
- Añadir feature Y

# 3. Iniciar Claude Code (Sonnet para trabajo normal)
claude

# 4. Dentro de Claude Code
> Lee CLAUDE.md y empecemos con la primera tarea
```

## 9.3 Cuando algo no funciona

```bash
# 1. Guardar estado actual
# Dentro de Claude Code:
> Documenta el estado actual en docs/ESTADO_DEBUG.md
> Incluye: qué funciona, qué no, errores vistos

# 2. Cambiar a Opus para debugging
/quit
claude --model claude-opus-4-5-20250514

# 3. Pedir análisis
> Lee docs/ESTADO_DEBUG.md
> Analiza el problema y propón solución

# 4. Volver a Sonnet para implementar
# Si la solución es clara, volver a Sonnet (más rápido y barato)
```

---

# PARTE 10: COMANDOS DE TERMINAL ÚTILES

## 10.1 Comandos que Claude Code puede ejecutar

Claude Code puede ejecutar cualquier comando de terminal. Estos son los más útiles:

### Python

```bash
# Ejecutar script
python3 script.py

# Ejecutar con argumentos
python3 script.py --arg valor

# Instalar paquete
pip install nombre-paquete

# Ver paquetes instalados
pip list

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### Git

```bash
# Estado actual
git status

# Añadir cambios
git add .
git add archivo.py  # Solo un archivo

# Commit
git commit -m "Descripción del cambio"

# Ver historial
git log --oneline

# Subir cambios
git push

# Descargar cambios
git pull

# Crear rama
git checkout -b nombre-rama

# Cambiar de rama
git checkout main
git checkout nombre-rama
```

### Archivos y directorios

```bash
# Ver dónde estás
pwd

# Listar archivos
ls
ls -la  # Con detalles

# Crear directorio
mkdir nombre

# Crear archivo vacío
touch archivo.py

# Ver contenido de archivo
cat archivo.py

# Buscar texto en archivos
grep "texto" archivo.py
grep -r "texto" .  # Buscar en todos los archivos

# Copiar archivo
cp origen.py destino.py

# Mover/renombrar
mv viejo.py nuevo.py

# Borrar (¡cuidado!)
rm archivo.py
rm -r directorio/  # Borrar directorio
```

### Servidores de desarrollo

```bash
# Servidor Python simple (para frontend)
cd frontend
python3 -m http.server 3000
# Abre http://localhost:3000

# FastAPI
uvicorn backend.main:app --reload
# Abre http://localhost:8000

# Ver qué usa un puerto
lsof -i :3000

# Matar proceso en puerto
kill -9 $(lsof -t -i:3000)
```

### Curl (probar APIs)

```bash
# GET simple
curl http://localhost:8000/api/formulas

# POST con JSON
curl -X POST http://localhost:8000/api/calcular \
  -H "Content-Type: application/json" \
  -d '{"formula_id": 1, "valores": {"x0": 0, "v": 5}}'

# Ver headers de respuesta
curl -I http://localhost:8000/health
```

---

# PARTE 11: GLOSARIO

| Término | Significado |
|---------|-------------|
| **Terminal** | La aplicación donde escribes comandos (Terminal en Mac, CMD en Windows) |
| **CLI** | Command Line Interface - interfaz de línea de comandos |
| **Contexto** | Todo lo que Claude "recuerda" en una sesión |
| **Token** | Unidad de texto (~4 caracteres). Los modelos tienen límite de tokens |
| **Compactación** | Proceso de "resumir" el contexto para liberar espacio |
| **Modelo** | La versión de Claude (Sonnet, Opus, Haiku) |
| **Prompt** | Las instrucciones que le das a Claude |
| **Endpoint** | URL de una API (ej: /api/formulas) |
| **Stack** | Conjunto de tecnologías de un proyecto |
| **Backend** | La parte del servidor (Python, base de datos) |
| **Frontend** | La parte visual (HTML, CSS, JavaScript) |
| **Commit** | Guardar cambios en Git |
| **Push** | Subir commits al servidor (GitHub) |
| **Pull** | Descargar cambios del servidor |
| **Branch/Rama** | Versión paralela del código para trabajar sin afectar main |

---

# PARTE 12: CHECKLIST RÁPIDO

## Antes de empezar a trabajar

- [ ] ¿Estoy en el directorio correcto? (`pwd`)
- [ ] ¿Existe CLAUDE.md con la tarea actual?
- [ ] ¿El servidor de backend está corriendo? (si lo necesito)
- [ ] ¿Tengo commits de los cambios anteriores? (`git status`)

## Durante el trabajo

- [ ] ¿Estoy pidiendo una cosa a la vez?
- [ ] ¿Verifico que cada cambio funciona antes de continuar?
- [ ] ¿Hago commits después de cada cambio exitoso?
- [ ] ¿Documento decisiones importantes en archivos?

## Antes de terminar

- [ ] ¿Funcionan todos los cambios?
- [ ] ¿Hice commit de todo? (`git status`)
- [ ] ¿Actualicé la documentación si es necesario?
- [ ] ¿Dejé CLAUDE.md listo para la próxima sesión?

---

# APÉNDICE A: Errores frecuentes y soluciones

## Error: "Command not found: claude"

```bash
# No está instalado o no está en el PATH
npm install -g @anthropic-ai/claude-code

# Si sigue sin funcionar, añadir al PATH
export PATH="$PATH:$(npm bin -g)"
```

## Error: "Authentication failed"

```bash
# Volver a autenticarse
claude auth login
```

## Error: "Context window exceeded"

```bash
# El contexto está lleno
# Dentro de Claude Code:
/compact

# O salir y empezar nueva sesión
/quit
claude
```

## Error: "Rate limit exceeded"

```bash
# Demasiadas peticiones, esperar unos minutos
# O cambiar a modelo más pequeño temporalmente
claude --model claude-haiku-4-5-20251001
```

---

# APÉNDICE B: Plantilla de CLAUDE.md

```markdown
# CLAUDE.md - [Nombre del Proyecto]

## 📋 TAREA ACTUAL
[Descripción clara de lo que hay que hacer hoy]

## 📁 ESTRUCTURA DEL PROYECTO
```
proyecto/
├── backend/
│   ├── main.py
│   └── ...
├── frontend/
│   ├── index.html
│   └── ...
└── docs/
```

## 🛠 STACK TECNOLÓGICO
- Backend: [Python/Node/etc] + [Framework]
- Frontend: [HTML/React/etc]
- Base de datos: [PostgreSQL/etc]

## ⚠️ REGLAS IMPORTANTES
1. Siempre probar antes de hacer commit
2. No modificar archivos .env
3. Documentar cada cambio

## 📊 ESTADO ACTUAL
- ✅ Lo que funciona
- ❌ Lo que falta
- ⚠️ Lo que tiene bugs

## 🔗 URLS ÚTILES
- Local: http://localhost:3000
- API: http://localhost:8000
- Producción: https://...

## 📝 NOTAS
[Cualquier otra información relevante]
```

---

**FIN DE LA GUÍA**

*Documento creado por Claude Opus 4.5*
*Fecha: 9 Enero 2026*
*Versión: 1.0*
