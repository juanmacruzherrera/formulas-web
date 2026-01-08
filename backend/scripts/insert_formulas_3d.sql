-- ============================================
-- INSERTAR FÓRMULAS 3D EN SUPABASE
-- ============================================
-- Ejecutar este script en Supabase SQL Editor
-- Ubicación: Supabase Dashboard > SQL Editor > New Query

-- 1. HÉLICE 3D
INSERT INTO formulas (
    nombre,
    formula_latex,
    categoria,
    descripcion,
    variables_usuario,
    variable_rango,
    rango_min,
    rango_max
) VALUES (
    'Hélice 3D',
    'x = r \cdot \cos(t), \quad y = r \cdot \sin(t), \quad z = c \cdot t',
    'geometria_3d',
    'Curva helicoidal en el espacio 3D. Radio r y constante de elevación c.',
    '{"r": 5, "c": 0.5}',
    't',
    0,
    20
);

-- 2. ATRACTOR DE LORENZ
INSERT INTO formulas (
    nombre,
    formula_latex,
    categoria,
    descripcion,
    variables_usuario,
    variable_rango,
    rango_min,
    rango_max
) VALUES (
    'Atractor de Lorenz',
    '\frac{dx}{dt} = \sigma(y-x), \quad \frac{dy}{dt} = x(\rho-z)-y, \quad \frac{dz}{dt} = xy-\beta z',
    'geometria_3d',
    'Sistema de ecuaciones diferenciales que genera un atractor caótico. Parámetros clásicos: σ=10, ρ=28, β=8/3.',
    '{"sigma": 10, "rho": 28, "beta": 2.667, "puntos": 2000}',
    't',
    0,
    50
);

-- 3. TORO 3D
INSERT INTO formulas (
    nombre,
    formula_latex,
    categoria,
    descripcion,
    variables_usuario,
    variable_rango,
    rango_min,
    rango_max
) VALUES (
    'Toro 3D',
    'x = (R + r\cos v)\cos u, \quad y = (R + r\cos v)\sin u, \quad z = r\sin v',
    'geometria_3d',
    'Superficie toroidal (dona) en 3D. R es el radio mayor y r el radio del tubo.',
    '{"R": 3, "r": 1, "u_min": 0, "u_max": 6.28, "v_min": 0, "v_max": 6.28, "puntos_u": 50, "puntos_v": 50}',
    'u',
    0,
    6.28
);

-- 4. ONDAS 3D
INSERT INTO formulas (
    nombre,
    formula_latex,
    categoria,
    descripcion,
    variables_usuario,
    variable_rango,
    rango_min,
    rango_max
) VALUES (
    'Ondas 3D',
    'z = A \cdot \sin(f \cdot \sqrt{x^2 + y^2})',
    'geometria_3d',
    'Superficie de ondas circulares concéntricas. A es amplitud y f frecuencia.',
    '{"amplitud": 1, "frecuencia": 1, "x_min": -5, "x_max": 5, "y_min": -5, "y_max": 5, "puntos": 50}',
    'x',
    -5,
    5
);

-- Verificar que se insertaron correctamente
SELECT id, nombre, categoria FROM formulas WHERE categoria = 'geometria_3d';
