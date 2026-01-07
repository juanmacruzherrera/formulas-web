# Índice de Aprendizaje

Esta carpeta contiene la documentación paso a paso de cómo se construyó el proyecto.
Cada archivo explica UNA pieza del proyecto con el método socrático.

---

## ¿Cómo usar esta documentación?

1. **Lee en orden** → Los archivos están numerados por una razón
2. **No saltes** → Cada archivo asume que entendiste los anteriores
3. **Si algo no está claro** → Relee el archivo anterior
4. **Los errores están documentados** → Aprende de ellos

---

## Estructura de cada archivo

Cada documento responde estas preguntas:

| # | Pregunta | Por qué importa |
|---|----------|-----------------|
| 1 | ¿Qué vamos a hacer? | Contexto claro antes de ver código |
| 2 | ¿Por qué lo necesitamos? | Motivación y problema que resuelve |
| 3 | ¿Cómo encaja en el proyecto? | Visión de arquitectura |
| 4 | ¿Qué conceptos previos necesito? | No asumir conocimiento |
| 5 | ¿Cómo es el código? | Código + explicación línea a línea |
| 6 | ¿Funcionó? | Prueba y resultado real |
| 7 | ¿Qué aprendimos? | Resumen y lecciones |
| 8 | ¿Qué viene después? | Conexión con siguiente paso |

---

## Lista de documentos

### Fase 0: Preparación
- [ ] `01_entorno_virtual.md` - Configurar Python y dependencias

### Fase 1: Conexión Python ↔ Supabase
- [ ] `02_conexion_supabase.md` - Cliente para hablar con la BD
- [ ] `03_primer_endpoint.md` - Servidor FastAPI básico
- [ ] `04_endpoint_formulas.md` - Listar todas las fórmulas
- [ ] `05_endpoint_formula_id.md` - Obtener una fórmula por ID

### Fase 2: Lógica de cálculo
- [ ] `06_logica_calculo.md` - Funciones matemáticas
- [ ] `07_endpoint_calcular.md` - Calcular y guardar
- [ ] `08_endpoint_historial.md` - Ver cálculos anteriores

### Fase 3: Frontend
- [ ] `09_html_estructura.md` - Página web base
- [ ] `10_js_fetch_api.md` - JavaScript llamando al backend
- [ ] `11_plotly_graficos.md` - Visualización de gráficas
- [ ] `12_css_estilos.md` - Diseño visual

### Fase 4: Integración
- [ ] `13_integracion.md` - Todo conectado
- [ ] `14_todas_formulas.md` - Las 15 fórmulas completas

---

## Archivos especiales

- `00_PLANTILLA.md` - Plantilla para crear nuevos documentos
- `00_GUIA_ENDPOINTS_REST.md` - **📚 GUÍA FUNDAMENTAL: Qué son endpoints, métodos HTTP y REST**
- `00_MAPA_FRONTEND_TECNOLOGIAS.md` - **🗺️ MAPA FRONTEND: Tailwind, Plotly, cómo se conecta todo**

---

## Cómo se marca el progreso

- [ ] Pendiente
- [x] Completado

Cuando Claude Code complete un documento, actualiza esta lista.

---

*Este índice se actualiza conforme avanza el proyecto*
