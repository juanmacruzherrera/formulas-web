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


def calcular_mrua(x0: float, v0: float, a: float, t_min: float, t_max: float, puntos: int = 100) -> dict:
    """MRUA: x = x0 + v0*t + 0.5*a*t²"""
    t = np.linspace(t_min, t_max, puntos)
    x = x0 + v0 * t + 0.5 * a * t**2
    return {"t": t.tolist(), "x": x.tolist()}


def calcular_caida_libre(y0: float, g: float, t_min: float, t_max: float, puntos: int = 100) -> dict:
    """Caída libre: y = y0 - 0.5*g*t²"""
    t = np.linspace(t_min, t_max, puntos)
    y = y0 - 0.5 * g * t**2
    y = np.maximum(y, 0)  # No puede bajar de 0
    return {"t": t.tolist(), "y": y.tolist()}


def calcular_tiro_parabolico(v0: float, theta: float, g: float, t_min: float, t_max: float, puntos: int = 100) -> dict:
    """Tiro parabólico: calcula x e y"""
    theta_rad = np.radians(theta)
    t = np.linspace(t_min, t_max, puntos)
    x = v0 * np.cos(theta_rad) * t
    y = v0 * np.sin(theta_rad) * t - 0.5 * g * t**2
    y = np.maximum(y, 0)
    return {"t": t.tolist(), "x": x.tolist(), "y": y.tolist()}


def calcular_armonico_simple(A: float, omega: float, phi: float, t_min: float, t_max: float, puntos: int = 100) -> dict:
    """MAS: x = A*cos(ω*t + φ)"""
    t = np.linspace(t_min, t_max, puntos)
    x = A * np.cos(omega * t + phi)
    return {"t": t.tolist(), "x": x.tolist()}


def calcular_onda_sinusoidal(A: float, k: float, omega: float, x_min: float, x_max: float, puntos: int = 100) -> dict:
    """Onda: y = A*sin(k*x - ω*t) en t=0"""
    x = np.linspace(x_min, x_max, puntos)
    y = A * np.sin(k * x)  # t=0
    return {"x": x.tolist(), "y": y.tolist()}


def calcular_parabola(a: float, b: float, c: float, x_min: float, x_max: float, puntos: int = 100) -> dict:
    """Parábola: y = ax² + bx + c"""
    x = np.linspace(x_min, x_max, puntos)
    y = a * x**2 + b * x + c
    return {"x": x.tolist(), "y": y.tolist()}


def calcular_exponencial(a: float, b: float, x_min: float, x_max: float, puntos: int = 100) -> dict:
    """Exponencial: y = a*e^(bx)"""
    x = np.linspace(x_min, x_max, puntos)
    y = a * np.exp(b * x)
    return {"x": x.tolist(), "y": y.tolist()}


def calcular_logaritmica(a: float, b: float, x_min: float, x_max: float, puntos: int = 100) -> dict:
    """Logarítmica: y = a*ln(x) + b"""
    x = np.linspace(max(x_min, 0.001), x_max, puntos)  # Evitar ln(0)
    y = a * np.log(x) + b
    return {"x": x.tolist(), "y": y.tolist()}


def calcular_seno(A: float, B: float, C: float, x_min: float, x_max: float, puntos: int = 100) -> dict:
    """Seno: y = A*sin(Bx + C)"""
    x = np.linspace(x_min, x_max, puntos)
    y = A * np.sin(B * x + C)
    return {"x": x.tolist(), "y": y.tolist()}


def calcular_circunferencia(r: float, theta_min: float, theta_max: float, puntos: int = 100) -> dict:
    """Circunferencia paramétrica"""
    theta = np.linspace(theta_min, theta_max, puntos)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return {"theta": theta.tolist(), "x": x.tolist(), "y": y.tolist()}


def calcular_espiral_arquimedes(a: float, b: float, theta_min: float, theta_max: float, puntos: int = 200) -> dict:
    """Espiral de Arquímedes: r = a + b*θ"""
    theta = np.linspace(theta_min, theta_max, puntos)
    r = a + b * theta
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return {"theta": theta.tolist(), "x": x.tolist(), "y": y.tolist()}


def calcular_espiral_logaritmica(a: float, b: float, theta_min: float, theta_max: float, puntos: int = 200) -> dict:
    """Espiral logarítmica: r = a*e^(b*θ)"""
    theta = np.linspace(theta_min, theta_max, puntos)
    r = a * np.exp(b * theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return {"theta": theta.tolist(), "x": x.tolist(), "y": y.tolist()}


def calcular_cardioide(a: float, theta_min: float, theta_max: float, puntos: int = 200) -> dict:
    """Cardioide: r = a*(1 + cos(θ))"""
    theta = np.linspace(theta_min, theta_max, puntos)
    r = a * (1 + np.cos(theta))
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return {"theta": theta.tolist(), "x": x.tolist(), "y": y.tolist()}


def calcular_lemniscata(a: float, theta_min: float, theta_max: float, puntos: int = 200) -> dict:
    """Lemniscata: r² = a²*cos(2θ)"""
    theta = np.linspace(theta_min, theta_max, puntos)
    cos_2theta = np.cos(2 * theta)
    # Solo donde cos(2θ) >= 0
    valid = cos_2theta >= 0
    r = np.where(valid, a * np.sqrt(np.abs(cos_2theta)), np.nan)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    # También el lado negativo
    r_neg = np.where(valid, -a * np.sqrt(np.abs(cos_2theta)), np.nan)
    x_neg = r_neg * np.cos(theta)
    y_neg = r_neg * np.sin(theta)
    # Combinar ambos lados
    x_full = np.concatenate([x, x_neg])
    y_full = np.concatenate([y, y_neg])
    return {"x": x_full.tolist(), "y": y_full.tolist()}


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
