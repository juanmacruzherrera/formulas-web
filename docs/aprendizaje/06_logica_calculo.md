# 06 - Lógica de Cálculo: Función para MRU

> **Archivo(s) creado(s):** `backend/services/calculadora.py`
> **Fecha:** 2025-12-29
> **Estado:** ✅ Completado

---

## 1. ¿QUÉ VAMOS A HACER?

Vamos a crear una función de Python que calcule los valores de la fórmula de **Movimiento Rectilíneo Uniforme (MRU)**.

**Analogía:**
Hasta ahora solo hemos creado la "biblioteca" donde están guardadas las fórmulas (Supabase) y el "mostrador" para consultarlas (endpoints de FastAPI). Ahora vamos a crear la **"calculadora"** que realmente hace los cálculos matemáticos.

**La fórmula MRU:**
```
x = x₀ + v·t
```

Donde:
- **x**: Posición en el tiempo t
- **x₀**: Posición inicial
- **v**: Velocidad constante
- **t**: Tiempo

**¿Qué hace nuestra función?**
Dado x₀=0, v=5, y un rango de tiempo (0 a 10 segundos), la función calcula:
- t = [0, 0.1, 0.2, 0.3, ..., 9.9, 10.0]  (100 puntos)
- x = [0, 0.5, 1.0, 1.5, ..., 49.5, 50.0]  (calculado para cada t)

Estos puntos se usarán después para **graficar** la fórmula en el frontend.

---

## 2. ¿POR QUÉ LO NECESITAMOS?

### Problema que resuelve:

El usuario quiere ver cómo se comporta una fórmula con diferentes valores. Para graficar, necesitamos:
1. **Muchos puntos** (no solo uno): Para hacer una línea suave necesitamos 50-100 puntos
2. **Cálculos precisos**: Usar fórmulas matemáticas correctamente
3. **Formato adecuado**: Arrays de datos que Plotly.js pueda graficar

### Sin esta lógica:

**❌ Problema:**
```python
# Calcular un solo punto
t = 5
x = 0 + 5 * 5  # x = 25

# ¿Cómo graficamos una línea? No podemos, solo tenemos un punto
```

**✅ Solución:**
```python
# Calcular 100 puntos
t = [0, 0.1, 0.2, ..., 10.0]
x = [0, 0.5, 1.0, ..., 50.0]

# Ahora podemos graficar: 100 puntos crean una línea suave
```

### En el flujo completo:

```
1. Usuario elige MRU y pone v=5, x₀=0
2. Frontend llama: POST /api/calcular
3. Backend usa calculadora.py → calcular_mru(0, 5, 0, 10, 100)
4. Devuelve: {t: [0, 0.1, ...], x: [0, 0.5, ...]}
5. Frontend grafica con Plotly.js
```

---

## 3. ¿CÓMO ENCAJA EN EL PROYECTO?

```
ARQUITECTURA ACTUAL:

┌─────────────────────────────────────────────────┐
│  FRONTEND (futuro)                              │
│  Usuario ingresa: v=5, x₀=0                    │
└──────────────┬──────────────────────────────────┘
               │
               │ POST /api/calcular
               ↓
┌─────────────────────────────────────────────────┐
│  BACKEND - routes/calculos.py (próxima tarea)  │
│                                                 │
│  Recibe: formula_id=1, valores={v:5, x0:0}     │
│         ↓                                       │
│  Llama: calcular_mru(0, 5, 0, 10, 100)         │
└──────────────┬──────────────────────────────────┘
               │
               ↓
┌─────────────────────────────────────────────────┐
│  CALCULADORA - services/calculadora.py          │
│  ← ESTAMOS AQUÍ                                 │
│                                                 │
│  def calcular_mru(x0, v, t_min, t_max, puntos):│
│      import numpy as np                         │
│      t = np.linspace(t_min, t_max, puntos)     │
│      x = x0 + v * t                            │
│      return {"t": t.tolist(), "x": x.tolist()} │
└─────────────────────────────────────────────────┘
               │
               │ Devuelve arrays
               ↓
       Frontend grafica con Plotly
```

**Este archivo es pura lógica matemática:**
- No se comunica con la BD
- No maneja HTTP
- Solo hace cálculos numéricos
- Será usado por el endpoint POST /api/calcular (próxima tarea)

---

## 4. CONCEPTOS PREVIOS

### Concepto 1: NumPy - Librería para cálculo numérico

- **Qué es:** Librería de Python especializada en operaciones con arrays y matemáticas

- **Analogía:** Es como tener una calculadora científica supersónica. En lugar de sumar números de uno en uno, NumPy puede sumar millones simultáneamente.

- **Operaciones vectorizadas:**
  ```python
  # Sin NumPy (lento)
  t = []
  x = []
  for i in range(100):
      t_val = i * 0.1
      x_val = 0 + 5 * t_val
      t.append(t_val)
      x.append(x_val)

  # Con NumPy (rápido y elegante)
  import numpy as np
  t = np.linspace(0, 10, 100)  # Genera 100 valores entre 0 y 10
  x = 0 + 5 * t                # Multiplica cada elemento automáticamente
  ```

- **Ventajas de NumPy:**
  - Mucho más rápido (implementado en C)
  - Sintaxis matemática natural
  - Funciones especializadas (linspace, sin, cos, exp, etc.)

### Concepto 2: np.linspace()

- **Qué hace:** Genera un array de números igualmente espaciados

- **Sintaxis:**
  ```python
  np.linspace(inicio, fin, cantidad)
  ```

- **Ejemplos:**
  ```python
  np.linspace(0, 10, 5)
  # → array([0, 2.5, 5, 7.5, 10])

  np.linspace(0, 1, 11)
  # → array([0, 0.1, 0.2, 0.3, ..., 0.9, 1.0])

  np.linspace(0, 10, 100)
  # → array([0, 0.101..., 0.202..., ..., 10])
  ```

- **Por qué lo usamos:**
  - Perfecto para gráficos: queremos puntos igualmente espaciados
  - Genera exactamente la cantidad de puntos que pedimos
  - Incluye el inicio y el fin

### Concepto 3: Operaciones vectorizadas

- **Qué son:** Operaciones que se aplican a todo un array automáticamente

- **Ejemplos:**
  ```python
  import numpy as np

  # Crear array
  t = np.array([0, 1, 2, 3, 4])

  # Multiplicar por escalar (cada elemento se multiplica)
  v = 5
  resultado = v * t
  # → array([0, 5, 10, 15, 20])

  # Sumar escalar (cada elemento se suma)
  x0 = 10
  resultado = x0 + v * t
  # → array([10, 15, 20, 25, 30])
  ```

- **En MRU:**
  ```python
  t = np.linspace(0, 10, 5)  # [0, 2.5, 5, 7.5, 10]
  x = 0 + 5 * t              # [0, 12.5, 25, 37.5, 50]
  # ↑ Multiplica 5 por CADA elemento de t automáticamente
  ```

### Concepto 4: .tolist() - Convertir NumPy array a lista Python

- **Qué hace:** Convierte un NumPy array en una lista normal de Python

- **Por qué lo necesitamos:**
  ```python
  import numpy as np

  t = np.linspace(0, 10, 3)
  # → t es un numpy.ndarray

  # NumPy array NO es serializable a JSON directamente
  # Necesitamos convertirlo a lista Python

  t_lista = t.tolist()
  # → t_lista es una lista normal de Python
  # → Ahora SÍ se puede convertir a JSON
  ```

- **Ejemplo:**
  ```python
  import numpy as np
  import json

  t = np.linspace(0, 2, 3)
  # array([0., 1., 2.])

  # ❌ Esto falla
  json.dumps(t)  # TypeError: Object of type ndarray is not JSON serializable

  # ✅ Esto funciona
  json.dumps(t.tolist())  # "[0.0, 1.0, 2.0]"
  ```

### Concepto 5: Type hints para retorno de función

- **Sintaxis:**
  ```python
  def nombre_funcion() -> tipo_retorno:
      ...
  ```

- **Ejemplo:**
  ```python
  def calcular_mru(...) -> dict:
      # Indica que la función devuelve un diccionario
      return {"t": [...], "x": [...]}
  ```

- **Beneficio:** Los editores de código saben qué esperar y pueden autocompletar

---

## 5. EL CÓDIGO

### Archivo NUEVO: `backend/services/calculadora.py`

```python
# backend/services/calculadora.py
# ============================================
# QUÉ HACE: Funciones de cálculo matemático para fórmulas
# CONSUME: Valores numéricos de entrada (parámetros de fórmulas)
# EXPONE: Funciones de cálculo que devuelven arrays de puntos
# RELACIONADO CON:
#   - Usado por: backend/routes/calculos.py (próxima tarea)
#   - No depende de BD ni HTTP
# ============================================

import numpy as np

def calcular_mru(x0: float, v: float, t_min: float, t_max: float, puntos: int = 100) -> dict:
    """
    Calcula posición en Movimiento Rectilíneo Uniforme (MRU).

    Fórmula: x = x₀ + v·t

    Esta función genera un array de valores de tiempo entre t_min y t_max,
    y calcula la posición correspondiente para cada tiempo usando la fórmula MRU.

    Args:
        x0 (float): Posición inicial (en metros)
        v (float): Velocidad constante (en m/s)
        t_min (float): Tiempo inicial (en segundos)
        t_max (float): Tiempo final (en segundos)
        puntos (int, optional): Cantidad de puntos a calcular. Por defecto 100.

    Returns:
        dict: Diccionario con dos claves:
            - "t": Lista de valores de tiempo (list[float])
            - "x": Lista de valores de posición (list[float])

    Example:
        >>> resultado = calcular_mru(x0=0, v=5, t_min=0, t_max=10, puntos=5)
        >>> print(resultado)
        {
            "t": [0.0, 2.5, 5.0, 7.5, 10.0],
            "x": [0.0, 12.5, 25.0, 37.5, 50.0]
        }

        # Con valores por defecto de puntos (100)
        >>> resultado = calcular_mru(0, 5, 0, 10)
        >>> len(resultado["t"])
        100

    Mathematical Background:
        En MRU, la velocidad es constante, por lo que:
        - Si v > 0: el objeto se mueve hacia adelante
        - Si v < 0: el objeto se mueve hacia atrás
        - Si v = 0: el objeto está en reposo (x siempre es x₀)

        La posición aumenta linealmente con el tiempo.
    """
    # Generar array de tiempos igualmente espaciados
    # linspace(inicio, fin, cantidad) incluye ambos extremos
    t = np.linspace(t_min, t_max, puntos)

    # Calcular posición para cada tiempo
    # Operación vectorizada: v*t multiplica v por cada elemento de t
    x = x0 + v * t

    # Convertir NumPy arrays a listas Python (para JSON)
    # .tolist() es necesario porque NumPy arrays no son JSON-serializables
    return {
        "t": t.tolist(),
        "x": x.tolist()
    }


# Bloque de prueba (solo se ejecuta si ejecutamos este archivo directamente)
if __name__ == "__main__":
    print("🧮 Probando función calcular_mru()...\n")

    # Prueba 1: Valores del ejemplo (v=5 m/s, desde reposo)
    print("Prueba 1: v=5 m/s, x₀=0 m, t=0-10s")
    resultado = calcular_mru(x0=0, v=5, t_min=0, t_max=10, puntos=5)
    print(f"  t: {resultado['t']}")
    print(f"  x: {resultado['x']}")
    print(f"  ✓ Generó {len(resultado['t'])} puntos\n")

    # Prueba 2: Partiendo desde x₀=10
    print("Prueba 2: v=3 m/s, x₀=10 m, t=0-5s")
    resultado = calcular_mru(x0=10, v=3, t_min=0, t_max=5, puntos=6)
    print(f"  t: {resultado['t']}")
    print(f"  x: {resultado['x']}")
    print(f"  ✓ La posición inicial es {resultado['x'][0]} (debe ser 10)\n")

    # Prueba 3: Velocidad negativa (retroceso)
    print("Prueba 3: v=-2 m/s (retroceso), x₀=20 m, t=0-5s")
    resultado = calcular_mru(x0=20, v=-2, t_min=0, t_max=5, puntos=6)
    print(f"  t: {resultado['t']}")
    print(f"  x: {resultado['x']}")
    print(f"  ✓ La posición disminuye (velocidad negativa)\n")

    # Prueba 4: Reposo (v=0)
    print("Prueba 4: v=0 m/s (reposo), x₀=15 m, t=0-10s")
    resultado = calcular_mru(x0=15, v=0, t_min=0, t_max=10, puntos=3)
    print(f"  t: {resultado['t']}")
    print(f"  x: {resultado['x']}")
    print(f"  ✓ Posición constante (reposo)\n")

    # Prueba 5: Muchos puntos (para graficar)
    print("Prueba 5: 100 puntos (típico para gráfico)")
    resultado = calcular_mru(x0=0, v=5, t_min=0, t_max=10)  # puntos=100 por defecto
    print(f"  Cantidad de puntos: {len(resultado['t'])}")
    print(f"  Primeros 3 valores t: {resultado['t'][:3]}")
    print(f"  Primeros 3 valores x: {resultado['x'][:3]}")
    print(f"  Últimos 3 valores t: {resultado['t'][-3:]}")
    print(f"  Últimos 3 valores x: {resultado['x'][-3:]}")
    print(f"  ✓ Listo para graficar\n")

    print("✅ Todas las pruebas completadas")
```

---

### Explicación línea por línea:

| Líneas | Qué hacen | Por qué |
|--------|-----------|---------|
| 1-9 | Comentario de cabecera | Documenta el propósito del archivo |
| 11 | `import numpy as np` | Importa NumPy con alias estándar `np` |
| 13 | `def calcular_mru(...)` | Define la función con type hints |
| 13 | Parámetros x0, v, t_min, t_max | Valores necesarios para MRU |
| 13 | `puntos: int = 100` | Parámetro opcional con valor por defecto |
| 13 | `-> dict` | Indica que retorna un diccionario |
| 14-60 | Docstring | Documentación completa con ejemplos |
| 63-64 | `t = np.linspace(...)` | Genera array de tiempos igualmente espaciados |
| 67-68 | `x = x0 + v * t` | Aplica la fórmula MRU (operación vectorizada) |
| 71-74 | `.tolist()` | Convierte NumPy arrays a listas Python |
| 71-74 | Return dict | Devuelve estructura con dos arrays |
| 78-115 | Bloque `if __name__` | Pruebas que solo se ejecutan al correr el archivo |
| 81-115 | 5 casos de prueba | Valida diferentes escenarios (normal, negativo, cero, etc.) |

---

## 5.1 HISTORIAL DE CAMBIOS EN EL CÓDIGO

*(Se llenará cuando haya modificaciones posteriores)*

---

## 6. PROBANDO QUE FUNCIONA

### Paso 1: Instalar NumPy

NumPy no estaba en nuestras dependencias iniciales. Necesitamos instalarlo:

```bash
cd /Volumes/Akitio01/Claude_MCP/formulas-web
source venv/bin/activate
pip install numpy
pip freeze > requirements.txt
```

---

### Paso 2: Ejecutar el archivo directamente

```bash
cd /Volumes/Akitio01/Claude_MCP/formulas-web
source venv/bin/activate
python backend/services/calculadora.py
```

**Resultado esperado:**

```
🧮 Probando función calcular_mru()...

Prueba 1: v=5 m/s, x₀=0 m, t=0-10s
  t: [0.0, 2.5, 5.0, 7.5, 10.0]
  x: [0.0, 12.5, 25.0, 37.5, 50.0]
  ✓ Generó 5 puntos

Prueba 2: v=3 m/s, x₀=10 m, t=0-5s
  t: [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
  x: [10.0, 13.0, 16.0, 19.0, 22.0, 25.0]
  ✓ La posición inicial es 10.0 (debe ser 10)

Prueba 3: v=-2 m/s (retroceso), x₀=20 m, t=0-5s
  t: [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
  x: [20.0, 18.0, 16.0, 14.0, 12.0, 10.0]
  ✓ La posición disminuye (velocidad negativa)

Prueba 4: v=0 m/s (reposo), x₀=15 m, t=0-10s
  t: [0.0, 5.0, 10.0]
  x: [15.0, 15.0, 15.0]
  ✓ Posición constante (reposo)

Prueba 5: 100 puntos (típico para gráfico)
  Cantidad de puntos: 100
  Primeros 3 valores t: [0.0, 0.10101010101010101, 0.20202020202020202]
  Primeros 3 valores x: [0.0, 0.5050505050505051, 1.0101010101010102]
  Últimos 3 valores t: [9.797979797979798, 9.8989898989899, 10.0]
  Últimos 3 valores x: [48.98989898989899, 49.494949494949495, 50.0]
  ✓ Listo para graficar

✅ Todas las pruebas completadas
```

---

### Paso 3: Prueba desde Python interactivo (opcional)

```python
from backend.services.calculadora import calcular_mru

# Calcular MRU
resultado = calcular_mru(0, 5, 0, 10, 5)
print(resultado)
# {'t': [0.0, 2.5, 5.0, 7.5, 10.0], 'x': [0.0, 12.5, 25.0, 37.5, 50.0]}

# Verificar tipos
print(type(resultado))        # <class 'dict'>
print(type(resultado['t']))   # <class 'list'>
```

---

### Resultado obtenido:

```
🧮 Probando función calcular_mru()...

Prueba 1: v=5 m/s, x₀=0 m, t=0-10s
  t: [0.0, 2.5, 5.0, 7.5, 10.0]
  x: [0.0, 12.5, 25.0, 37.5, 50.0]
  ✓ Generó 5 puntos

Prueba 2: v=3 m/s, x₀=10 m, t=0-5s
  t: [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
  x: [10.0, 13.0, 16.0, 19.0, 22.0, 25.0]
  ✓ La posición inicial es 10.0 (debe ser 10)

Prueba 3: v=-2 m/s (retroceso), x₀=20 m, t=0-5s
  t: [0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
  x: [20.0, 18.0, 16.0, 14.0, 12.0, 10.0]
  ✓ La posición disminuye (velocidad negativa)

Prueba 4: v=0 m/s (reposo), x₀=15 m, t=0-10s
  t: [0.0, 5.0, 10.0]
  x: [15.0, 15.0, 15.0]
  ✓ Posición constante (reposo)

Prueba 5: 100 puntos (típico para gráfico)
  Cantidad de puntos: 100
  Primeros 3 valores t: [0.0, 0.10101010101010101, 0.20202020202020202]
  Primeros 3 valores x: [0.0, 0.5050505050505051, 1.0101010101010102]
  Últimos 3 valores t: [9.797979797979798, 9.8989898989899, 10.0]
  Últimos 3 valores x: [48.98989898989899, 49.494949494949495, 50.0]
  ✓ Listo para graficar

✅ Todas las pruebas completadas
```

---

## 7. ¿FUNCIONÓ?

### ✅ Si funcionó:

**¡SÍ, FUNCIONÓ PERFECTAMENTE!**

- Confirmamos que:
  1. ✅ NumPy se instaló correctamente (versión 2.0.2)
  2. ✅ El archivo calculadora.py se creó sin errores
  3. ✅ La función calcular_mru() funciona correctamente
  4. ✅ Todas las 5 pruebas pasaron exitosamente
  5. ✅ Los cálculos matemáticos son correctos
  6. ✅ La conversión .tolist() funciona (listas Python estándar)

**Validación de las pruebas:**

**Prueba 1 - Caso básico (v=5, x₀=0):**
- ✅ Generó correctamente 5 puntos
- ✅ Valores correctos: x = 0 + 5*t
- ✅ t=[0, 2.5, 5, 7.5, 10] → x=[0, 12.5, 25, 37.5, 50]

**Prueba 2 - Posición inicial (x₀=10):**
- ✅ Respeta la posición inicial x₀=10
- ✅ Incrementa correctamente: x = 10 + 3*t

**Prueba 3 - Velocidad negativa (v=-2):**
- ✅ Maneja velocidades negativas (retroceso)
- ✅ Posición disminuye: 20 → 18 → 16 → 14 → 12 → 10

**Prueba 4 - Reposo (v=0):**
- ✅ Posición constante cuando v=0
- ✅ x = 15.0 en todos los tiempos

**Prueba 5 - Muchos puntos (100):**
- ✅ Genera 100 puntos correctamente
- ✅ Valores igualmente espaciados con np.linspace()
- ✅ Listo para crear gráficos suaves

**Validaciones confirmadas:**
- ✅ np.linspace() genera puntos igualmente espaciados
- ✅ Operaciones vectorizadas funcionan (v * t)
- ✅ .tolist() convierte a listas Python
- ✅ Return devuelve diccionario con estructura correcta
- ✅ Type hints son correctos
- ✅ Bloque `if __name__ == "__main__"` permite pruebas directas

**Lógica matemática verificada:**
- ✅ Fórmula MRU: x = x₀ + v·t se aplica correctamente
- ✅ Casos especiales manejados (v negativa, v=0)
- ✅ Valores numéricos precisos

- Siguiente paso lógico:
  - **Tarea 2.2:** Crear endpoint POST `/api/calcular` que use esta función

### ❌ Si falló:

#### Posibles errores comunes:

1. **Error: "No module named 'numpy'"**
   - Causa: NumPy no está instalado
   - Solución: `pip install numpy`

2. **Error: "cannot import name 'calcular_mru'"**
   - Causa: Ejecutaste desde una carpeta incorrecta
   - Solución: Asegúrate de estar en `/Volumes/Akitio01/Claude_MCP/formulas-web`

3. **Error: "Object of type ndarray is not JSON serializable"**
   - Causa: Olvidaste `.tolist()`
   - Solución: Asegúrate de convertir arrays con `.tolist()`

4. **Valores incorrectos en los cálculos**
   - Debug: Verifica la fórmula x = x0 + v * t
   - Verifica que usas operación vectorizada correctamente

---

## 8. RESUMEN

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué construimos? | Función que calcula valores de MRU para graficar |
| ¿Para qué sirve? | Generar puntos (t, x) que el frontend puede usar con Plotly.js |
| ¿Cómo se usa? | `calcular_mru(x0, v, t_min, t_max, puntos)` → devuelve `{"t": [...], "x": [...]}` |
| ¿Con qué se conecta? | Será usada por el endpoint POST /api/calcular (próxima tarea) |

**Conceptos clave aprendidos:**
- NumPy y operaciones vectorizadas
- np.linspace() para generar valores igualmente espaciados
- Conversión de NumPy arrays a listas con .tolist()
- Lógica matemática separada de HTTP/BD
- Pruebas con `if __name__ == "__main__"`

---

## 9. CONEXIÓN CON EL SIGUIENTE PASO

Ahora que tenemos la función de cálculo lista, el siguiente paso (Tarea 2.2) es **crear el endpoint POST /api/calcular** que:
1. Reciba los valores del usuario (formula_id, valores)
2. Llame a `calcular_mru()` con esos valores
3. Guarde el resultado en la tabla `calculos` de Supabase
4. Devuelva los puntos al frontend para graficar

**Analogía del proceso:**
1. ✅ **Tarea 2.1 completada:** Construimos la calculadora
2. ⏭️ **Tarea 2.2:** Creamos el botón que activa la calculadora (endpoint HTTP)
3. Después: El frontend tendrá el botón para que el usuario haga cálculos

**Flujo completo (cuando terminemos 2.2):**
```
Usuario → Frontend → POST /api/calcular → calculadora.py → Gráfico
```

---

## 10. ACTUALIZACIONES POSTERIORES

*(Se añadirán actualizaciones aquí si hay cambios posteriores)*

---

*Documentación generada por Claude Code siguiendo el método socrático*
*NUNCA borrar contenido de este archivo - solo añadir*
