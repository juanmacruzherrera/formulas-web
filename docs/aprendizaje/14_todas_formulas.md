# 14. Catálogo de las 15 Fórmulas Implementadas

**Fecha:** 30 diciembre 2025
**Tarea:** Documentar todas las fórmulas matemáticas y físicas del sistema
**Total de fórmulas:** 15 (6 Física + 5 Matemáticas + 4 Curvas Exóticas)

---

## 1. ¿Qué vamos a hacer?

Documentar **cada una de las 15 fórmulas** implementadas en el sistema, explicando:
- Qué representa la fórmula
- Qué parámetros necesita
- Cómo se calcula
- Qué tipo de gráfico genera

---

## 2. ¿Por qué lo necesitamos?

Este catálogo sirve como:
- **Referencia rápida** para saber qué fórmulas están disponibles
- **Guía de parámetros** para cada fórmula
- **Documentación educativa** sobre cada concepto matemático/físico
- **Especificación** para futuros desarrolladores

---

## 3. Organización del Catálogo

Las fórmulas están organizadas en 3 categorías:

```
FÍSICA (6 fórmulas)
├── Cinemática
│   ├── MRU
│   ├── MRUA
│   └── Caída Libre
└── Dinámica/Ondas
    ├── Tiro Parabólico
    ├── Movimiento Armónico Simple
    └── Onda Sinusoidal

MATEMÁTICAS (5 fórmulas)
├── Funciones básicas
│   ├── Parábola
│   ├── Exponencial
│   └── Logarítmica
└── Trigonometría/Geometría
    ├── Función Seno
    └── Circunferencia

CURVAS EXÓTICAS (4 fórmulas)
└── Geometría avanzada
    ├── Espiral de Arquímedes
    ├── Espiral Logarítmica
    ├── Cardioide
    └── Lemniscata de Bernoulli
```

---

## FÍSICA

### 1. MRU - Movimiento Rectilíneo Uniforme

**ID:** 1
**Categoría:** fisica
**Fórmula LaTeX:** `x = x_0 + v \cdot t`

**¿Qué es?**
Movimiento en línea recta con velocidad constante. La posición aumenta linealmente con el tiempo.

**Parámetros:**
- `x0`: Posición inicial (metros)
- `v`: Velocidad (m/s)
- `t_min`, `t_max`: Rango de tiempo (segundos)

**Función de cálculo:** `calcular_mru(x0, v, t_min, t_max)`

**Devuelve:** `{t: [...], x: [...]}`

**Gráfico esperado:** Línea recta (pendiente = velocidad)

**Ejemplo:**
```python
x0 = 0
v = 5  # 5 m/s
t_min = 0
t_max = 10

# Resultado: en t=10s, x = 0 + 5*10 = 50 metros
```

---

### 2. MRUA - Movimiento Rectilíneo Uniformemente Acelerado

**ID:** 2
**Categoría:** fisica
**Fórmula LaTeX:** `x = x_0 + v_0 \cdot t + \frac{1}{2} a \cdot t^2`

**¿Qué es?**
Movimiento en línea recta con aceleración constante. La posición crece cuadráticamente (parábola).

**Parámetros:**
- `x0`: Posición inicial (m)
- `v0`: Velocidad inicial (m/s)
- `a`: Aceleración (m/s²)
- `t_min`, `t_max`: Rango de tiempo (s)

**Función de cálculo:** `calcular_mrua(x0, v0, a, t_min, t_max)`

**Devuelve:** `{t: [...], x: [...]}`

**Gráfico esperado:** Parábola (cóncava si a>0, convexa si a<0)

---

### 3. Caída Libre

**ID:** 3
**Categoría:** fisica
**Fórmula LaTeX:** `y = y_0 - \frac{1}{2} g \cdot t^2`

**¿Qué es?**
Movimiento vertical de un objeto que cae desde una altura inicial. La altura disminuye con el cuadrado del tiempo.

**Parámetros:**
- `y0`: Altura inicial (m)
- `g`: Aceleración de la gravedad (m/s²), típicamente 9.8
- `t_min`, `t_max`: Rango de tiempo (s)

**Función de cálculo:** `calcular_caida_libre(y0, g, t_min, t_max)`

**Devuelve:** `{t: [...], y: [...]}`

**Nota:** La función limita y ≥ 0 (no puede bajar del suelo)

**Gráfico esperado:** Parábola invertida que termina en y=0

---

### 4. Tiro Parabólico

**ID:** 4
**Categoría:** fisica
**Fórmula LaTeX:** `y = v_0 \cdot \sin(\theta) \cdot t - \frac{1}{2} g \cdot t^2`

**¿Qué es?**
Trayectoria vertical de un proyectil lanzado con un ángulo. La componente Y combina movimiento uniforme hacia arriba con caída libre.

**Parámetros:**
- `v0`: Velocidad inicial (m/s)
- `theta`: Ángulo de lanzamiento (grados)
- `g`: Gravedad (m/s²)
- `t_min`, `t_max`: Rango de tiempo (s)

**Función de cálculo:** `calcular_tiro_parabolico(v0, theta, g, t_min, t_max)`

**Devuelve:** `{t: [...], x: [...], y: [...]}`

**Nota:** También calcula la componente X para graficar la trayectoria completa

**Gráfico esperado:** Parábola (asciende y luego cae)

---

### 5. Movimiento Armónico Simple

**ID:** 5
**Categoría:** fisica
**Fórmula LaTeX:** `x = A \cdot \cos(\omega \cdot t + \phi)`

**¿Qué es?**
Oscilación periódica, como un péndulo o un resorte. La posición varía sinusoidalmente.

**Parámetros:**
- `A`: Amplitud (m) - máximo desplazamiento
- `omega`: Frecuencia angular (rad/s) - velocidad de oscilación
- `phi`: Fase inicial (rad) - posición de inicio del ciclo
- `t_min`, `t_max`: Rango de tiempo (s)

**Función de cálculo:** `calcular_armonico_simple(A, omega, phi, t_min, t_max)`

**Devuelve:** `{t: [...], x: [...]}`

**Gráfico esperado:** Onda coseno (oscilación)

**Relación:** Período T = 2π/ω

---

### 6. Onda Sinusoidal

**ID:** 6
**Categoría:** fisica
**Fórmula LaTeX:** `y = A \cdot \sin(k \cdot x - \omega \cdot t)`

**¿Qué es?**
Propagación de una onda en el espacio (como una onda en una cuerda). Esta implementación muestra la onda en t=0.

**Parámetros:**
- `A`: Amplitud (m)
- `k`: Número de onda (rad/m) - determina la longitud de onda
- `omega`: Frecuencia angular (rad/s) - velocidad de propagación (fijado en 0 para t=0)
- `x_min`, `x_max`: Rango espacial (m)

**Función de cálculo:** `calcular_onda_sinusoidal(A, k, omega, x_min, x_max)`

**Devuelve:** `{x: [...], y: [...]}`

**Gráfico esperado:** Onda seno

**Relación:** Longitud de onda λ = 2π/k

---

## MATEMÁTICAS

### 7. Parábola

**ID:** 7
**Categoría:** matematicas
**Fórmula LaTeX:** `y = a \cdot x^2 + b \cdot x + c`

**¿Qué es?**
Función cuadrática básica. La forma depende del signo de a.

**Parámetros:**
- `a`: Coeficiente cuadrático (a > 0 → U, a < 0 → ∩)
- `b`: Coeficiente lineal (desplaza el vértice horizontalmente)
- `c`: Término independiente (desplaza verticalmente)
- `x_min`, `x_max`: Rango de x

**Función de cálculo:** `calcular_parabola(a, b, c, x_min, x_max)`

**Devuelve:** `{x: [...], y: [...]}`

**Gráfico esperado:** Parábola (U o ∩)

**Vértice:** x = -b/(2a), y = c - b²/(4a)

---

### 8. Función Exponencial

**ID:** 8
**Categoría:** matematicas
**Fórmula LaTeX:** `y = a \cdot e^{b \cdot x}`

**¿Qué es?**
Crecimiento o decrecimiento exponencial.

**Parámetros:**
- `a`: Factor de escala
- `b`: Tasa de crecimiento (b > 0) o decrecimiento (b < 0)
- `x_min`, `x_max`: Rango de x

**Función de cálculo:** `calcular_exponencial(a, b, x_min, x_max)`

**Devuelve:** `{x: [...], y: [...]}`

**Gráfico esperado:**
- b > 0: Curva creciente (crece rápidamente)
- b < 0: Curva decreciente (tiende a 0)

**Aplicaciones:** Crecimiento poblacional, desintegración radiactiva, interés compuesto

---

### 9. Función Logarítmica

**ID:** 9
**Categoría:** matematicas
**Fórmula LaTeX:** `y = a \cdot \ln(x) + b`

**¿Qué es?**
Logaritmo natural. Inversa de la función exponencial.

**Parámetros:**
- `a`: Factor de escala
- `b`: Desplazamiento vertical
- `x_min`, `x_max`: Rango de x (debe ser x > 0)

**Función de cálculo:** `calcular_logaritmica(a, b, x_min, x_max)`

**Devuelve:** `{x: [...], y: [...]}`

**Nota:** La función garantiza x_min ≥ 0.001 para evitar ln(0) (indefinido)

**Gráfico esperado:** Curva que crece lentamente (asíntota vertical en x=0)

---

### 10. Función Seno

**ID:** 10
**Categoría:** matematicas
**Fórmula LaTeX:** `y = A \cdot \sin(B \cdot x + C)`

**¿Qué es?**
Función trigonométrica seno con amplitud, frecuencia y fase ajustables.

**Parámetros:**
- `A`: Amplitud (altura de la onda)
- `B`: Frecuencia (cantidad de ciclos)
- `C`: Fase (desplazamiento horizontal)
- `x_min`, `x_max`: Rango de x

**Función de cálculo:** `calcular_seno(A, B, C, x_min, x_max)`

**Devuelve:** `{x: [...], y: [...]}`

**Gráfico esperado:** Onda senoidal

**Período:** T = 2π/B

---

### 11. Circunferencia

**ID:** 11
**Categoría:** matematicas
**Fórmula LaTeX:** `x = r \cdot \cos(\theta), \quad y = r \cdot \sin(\theta)`

**¿Qué es?**
Circunferencia de radio r centrada en el origen. Curva paramétrica.

**Parámetros:**
- `r`: Radio (distancia del centro a cualquier punto)
- `theta_min`, `theta_max`: Rango angular (radianes), típicamente [0, 2π]

**Función de cálculo:** `calcular_circunferencia(r, theta_min, theta_max)`

**Devuelve:** `{theta: [...], x: [...], y: [...]}`

**Gráfico esperado:** Círculo cerrado (si theta va de 0 a 2π)

**Nota:** El frontend usa aspect ratio 1:1 para que se vea como círculo, no elipse

---

## CURVAS EXÓTICAS

### 12. Espiral de Arquímedes

**ID:** 12
**Categoría:** curvas_exoticas
**Fórmula LaTeX:** `r = a + b \cdot \theta`

**¿Qué es?**
Espiral donde la distancia al centro crece linealmente con el ángulo. Como el surco de un disco de vinilo.

**Parámetros:**
- `a`: Radio inicial
- `b`: Velocidad de expansión (distancia entre vueltas = 2πb)
- `theta_min`, `theta_max`: Rango angular (rad)

**Función de cálculo:** `calcular_espiral_arquimedes(a, b, theta_min, theta_max)`

**Devuelve:** `{theta: [...], x: [...], y: [...]}`

**Conversión a cartesianas:**
```python
x = r * cos(θ) = (a + b·θ) * cos(θ)
y = r * sin(θ) = (a + b·θ) * sin(θ)
```

**Gráfico esperado:** Espiral de separación uniforme

---

### 13. Espiral Logarítmica

**ID:** 13
**Categoría:** curvas_exoticas
**Fórmula LaTeX:** `r = a \cdot e^{b \cdot \theta}`

**¿Qué es?**
Espiral que aparece en la naturaleza: conchas de nautilus, galaxias espirales, huracanes. La distancia al centro crece exponencialmente.

**Parámetros:**
- `a`: Factor de escala
- `b`: Factor de crecimiento (controla qué tan rápido se expande)
- `theta_min`, `theta_max`: Rango angular (rad)

**Función de cálculo:** `calcular_espiral_logaritmica(a, b, theta_min, theta_max)`

**Devuelve:** `{theta: [...], x: [...], y: [...]}`

**Propiedad especial:** El ángulo entre la tangente y el radio es constante

**Gráfico esperado:** Espiral que se expande rápidamente

---

### 14. Cardioide

**ID:** 14
**Categoría:** curvas_exoticas
**Fórmula LaTeX:** `r = a \cdot (1 + \cos(\theta))`

**¿Qué es?**
Curva con forma de corazón. Aparece en óptica (cáusticas) y acústica (patrones de micrófonos).

**Parámetros:**
- `a`: Tamaño de la curva
- `theta_min`, `theta_max`: Rango angular (rad), típicamente [0, 2π]

**Función de cálculo:** `calcular_cardioide(a, theta_min, theta_max)`

**Devuelve:** `{theta: [...], x: [...], y: [...]}`

**Propiedades:**
- Cuando θ = 0: r = 2a (punto más alejado)
- Cuando θ = π: r = 0 (vértice del "corazón")

**Gráfico esperado:** Forma de corazón ❤️

---

### 15. Lemniscata de Bernoulli

**ID:** 15
**Categoría:** curvas_exoticas
**Fórmula LaTeX:** `r^2 = a^2 \cdot \cos(2\theta)`

**¿Qué es?**
Curva en forma de infinito (∞) o número 8 acostado. Solo existe donde cos(2θ) ≥ 0.

**Parámetros:**
- `a`: Tamaño de la curva
- `theta_min`, `theta_max`: Rango angular (rad)

**Función de cálculo:** `calcular_lemniscata(a, theta_min, theta_max)`

**Devuelve:** `{x: [...], y: [...]}`

**Nota:** Esta función es especial porque:
1. Calcula `r = √(a² · cos(2θ))` solo donde cos(2θ) ≥ 0
2. También calcula el lado negativo: `r_neg = -√(a² · cos(2θ))`
3. Combina ambos lados para formar la curva completa

**Rangos válidos:** cos(2θ) ≥ 0 cuando:
- -π/4 ≤ θ ≤ π/4 (lóbulo derecho)
- 3π/4 ≤ θ ≤ 5π/4 (lóbulo izquierdo)

**Gráfico esperado:** Figura en forma de ∞

---

## 4. Tabla Resumen

| ID | Nombre | Categoría | Variables | Devuelve | Tipo de gráfico |
|----|--------|-----------|-----------|----------|-----------------|
| 1  | MRU | fisica | x0, v, t | {t, x} | Línea recta |
| 2  | MRUA | fisica | x0, v0, a, t | {t, x} | Parábola |
| 3  | Caída Libre | fisica | y0, g, t | {t, y} | Parábola invertida |
| 4  | Tiro Parabólico | fisica | v0, θ, g, t | {t, x, y} | Trayectoria parabólica |
| 5  | MAS | fisica | A, ω, φ, t | {t, x} | Onda coseno |
| 6  | Onda Sinusoidal | fisica | A, k, ω, x | {x, y} | Onda seno |
| 7  | Parábola | matematicas | a, b, c, x | {x, y} | Parábola |
| 8  | Exponencial | matematicas | a, b, x | {x, y} | Curva exponencial |
| 9  | Logarítmica | matematicas | a, b, x | {x, y} | Curva logarítmica |
| 10 | Seno | matematicas | A, B, C, x | {x, y} | Onda seno |
| 11 | Circunferencia | matematicas | r, θ | {θ, x, y} | Círculo |
| 12 | Espiral Arquímedes | curvas_exoticas | a, b, θ | {θ, x, y} | Espiral uniforme |
| 13 | Espiral Logarítmica | curvas_exoticas | a, b, θ | {θ, x, y} | Espiral exponencial |
| 14 | Cardioide | curvas_exoticas | a, θ | {θ, x, y} | Corazón |
| 15 | Lemniscata | curvas_exoticas | a, θ | {x, y} | Infinito ∞ |

---

## 5. ¿Cómo añadir una nueva fórmula?

### Paso 1: Insertar en Supabase

```sql
INSERT INTO formulas (nombre, categoria, formula_latex, variables_usuario, variable_rango, rango_min, rango_max, rango_dinamico)
VALUES (
  'Hipérbola',
  'matematicas',
  'xy = k',
  '{"k": 1}',
  'x',
  -10,
  10,
  false
);
```

### Paso 2: Añadir función de cálculo

```python
# backend/services/calculadora.py

def calcular_hiperbola(k: float, x_min: float, x_max: float, puntos: int = 100) -> dict:
    """Hipérbola: xy = k"""
    x = np.linspace(x_min, x_max, puntos)
    # Evitar división por 0
    x = np.where(x == 0, 0.001, x)
    y = k / x
    return {"x": x.tolist(), "y": y.tolist()}
```

### Paso 3: Añadir reconocimiento en endpoint

```python
# backend/routes/calculos.py

# Importar función
from backend.services.calculadora import calcular_hiperbola

# Añadir condición
elif "Hipérbola" in formula["nombre"]:
    resultado = calcular_hiperbola(
        k=datos.valores.get("k", 1),
        x_min=rango_min,
        x_max=rango_max
    )
```

**¡Y listo!** El frontend detectará automáticamente el formato `{x, y}` y lo graficará correctamente.

---

## 6. ¿Qué aprendimos?

### Lección 1: Parametrización

Todas las curvas complejas se pueden expresar mediante **ecuaciones paramétricas**:
- Tiempo t para física
- Ángulo θ para curvas polares
- Variable independiente x para funciones

### Lección 2: Conversión polar ↔ cartesiana

```python
# Polar → Cartesiano
x = r * cos(θ)
y = r * sin(θ)

# Cartesiano → Polar
r = sqrt(x² + y²)
θ = atan2(y, x)
```

### Lección 3: Manejo de casos especiales

- **Logaritmo:** evitar ln(0) con `max(x_min, 0.001)`
- **Caída libre:** limitar y ≥ 0 con `np.maximum(y, 0)`
- **Lemniscata:** filtrar valores válidos con `np.where()`

---

## 7. Recursos de Aprendizaje

Para profundizar en cada fórmula:

**Física:**
- Khan Academy: Cinemática y Dinámica
- Feynman Lectures: Ondas y Oscilaciones

**Matemáticas:**
- Desmos Graphing Calculator (interactivo)
- Wolfram MathWorld (referencia completa)

**Curvas Exóticas:**
- "The Curves of Life" por Theodore Andrea Cook
- Wikipedia: "List of curves"

---

**Resumen:** Sistema completo con 15 fórmulas distribuidas en 3 categorías. Cada fórmula tiene su función de cálculo, parámetros específicos, y genera un tipo de gráfico característico. El sistema es extensible y permite añadir nuevas fórmulas fácilmente.

---

*Documento creado: 30 diciembre 2025*
*Autor: Claude Code*
