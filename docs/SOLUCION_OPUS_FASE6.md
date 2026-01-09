# INSTRUCCIONES FASE 6: Corrección Variables + 3D Opcional

> **ARQUITECTO:** Claude Opus
> **EJECUTOR:** Claude Code
> **FECHA:** 8 Enero 2026

---

## ⛔ REGLA CRÍTICA

**ANTES de modificar cualquier dato en Supabase:**
1. Lee los datos actuales
2. Muestra qué vas a cambiar (antes → después)
3. Pide confirmación si es destructivo

---

## PROBLEMA 1: Variables muestran "0, 1, 2" (CRÍTICO)

### Diagnóstico
El frontend itera `Object.entries(variables_usuario)`. Si es array, devuelve índices.

### Solución: Script Python para corregir Supabase

**Archivo a crear:** `scripts/corregir_variables_supabase.py`

```python
"""
Corrige variables_usuario en Supabase.
Convierte arrays a objetos con nombres correctos.
"""
import os
from dotenv import load_dotenv
from supabase import create_client

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

# Mapeo EXACTO de qué variables espera cada fórmula
# Sacado de backend/routes/calculos.py
VARIABLES_CORRECTAS = {
    "MRU": {"x0": 0, "v": 5},
    "MRUA": {"x0": 0, "v0": 5, "a": 2},
    "Caída Libre": {"y0": 100, "g": 9.8},
    "Tiro Parabólico": {"v0": 20, "theta": 45, "g": 9.8},
    "Armónico Simple": {"A": 5, "omega": 2, "phi": 0},
    "Onda Sinusoidal": {"A": 3, "k": 1, "omega": 0},
    "Parábola": {"a": 1, "b": 0, "c": 0},
    "Exponencial": {"a": 1, "b": 0.5},
    "Logarítmica": {"a": 1, "b": 0},
    "Seno": {"A": 1, "B": 1, "C": 0},
    "Circunferencia": {"r": 5},
    "Espiral de Arquímedes": {"a": 0, "b": 0.5},
    "Espiral Logarítmica": {"a": 0.5, "b": 0.15},
    "Cardioide": {"a": 3},
    "Lemniscata": {"a": 5},
}

def encontrar_variables_correctas(nombre_formula):
    """Busca en VARIABLES_CORRECTAS por coincidencia parcial"""
    for key, variables in VARIABLES_CORRECTAS.items():
        if key.lower() in nombre_formula.lower():
            return variables
    return None

def main():
    # 1. Leer todas las fórmulas
    response = supabase.table("formulas").select("id, nombre, variables_usuario").execute()
    formulas = response.data
    
    print(f"📊 Total fórmulas: {len(formulas)}\n")
    
    cambios = []
    
    for formula in formulas:
        nombre = formula["nombre"]
        actual = formula["variables_usuario"]
        
        # Detectar si es array (problema) u objeto (ok)
        es_array = isinstance(actual, list)
        
        if es_array:
            # Buscar las variables correctas
            correctas = encontrar_variables_correctas(nombre)
            
            if correctas:
                print(f"❌ {nombre}")
                print(f"   ACTUAL (array): {actual}")
                print(f"   CORRECTO (objeto): {correctas}")
                print()
                
                cambios.append({
                    "id": formula["id"],
                    "nombre": nombre,
                    "actual": actual,
                    "nuevo": correctas
                })
            else:
                print(f"⚠️  {nombre} - No encontré mapeo, revisar manualmente")
                print(f"   Actual: {actual}")
                print()
        else:
            print(f"✅ {nombre} - OK (ya es objeto)")
    
    # 2. Confirmar cambios
    if cambios:
        print(f"\n{'='*50}")
        print(f"Se encontraron {len(cambios)} fórmulas para corregir.")
        confirmar = input("¿Aplicar cambios? (s/n): ")
        
        if confirmar.lower() == 's':
            for cambio in cambios:
                supabase.table("formulas").update({
                    "variables_usuario": cambio["nuevo"]
                }).eq("id", cambio["id"]).execute()
                print(f"✅ Actualizado: {cambio['nombre']}")
            
            print("\n🎉 Todas las correcciones aplicadas!")
        else:
            print("❌ Cancelado, no se hicieron cambios.")
    else:
        print("\n✅ Todas las fórmulas tienen formato correcto!")

if __name__ == "__main__":
    main()
```

### Ejecución

```bash
cd /Volumes/Akitio01/Claude_MCP/formulas-web
source venv/bin/activate
python scripts/corregir_variables_supabase.py
```

### Verificación

Después de ejecutar, probar en https://formulas-web.pages.dev:
1. Seleccionar MRUA → debe mostrar "Posición inicial x₀", "Velocidad inicial", "Aceleración"
2. Seleccionar Caída Libre → debe mostrar "Posición inicial y₀", "Gravedad"
3. Todas las 15 fórmulas deben mostrar nombres descriptivos

---

## PROBLEMA 2: Ocultar spinners de inputs

### Solución: Añadir CSS

**Archivo:** `frontend/css/styles.css`

**Añadir al final:**

```css
/* Ocultar spinners de inputs numéricos */
input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
}

input[type="number"] {
    -moz-appearance: textfield;
    appearance: textfield;
}
```

### Verificación
- Chrome: Sin flechas arriba/abajo
- Firefox: Sin flechas
- Safari: Sin flechas

---

## PROBLEMA 3: Gráficos 3D (OPCIONAL - Segunda prioridad)

### Análisis de Opus

**Fórmulas que tienen sentido en 3D:**
| Fórmula | Por qué 3D | Coordenadas |
|---------|------------|-------------|
| Tiro Parabólico | Ver evolución temporal | x, y, t |
| Espiral Arquímedes | Convertir a hélice | x, y, theta |
| Espiral Logarítmica | Hélice exponencial | x, y, theta |

**Fórmulas que NO necesitan 3D:**
- MRU, MRUA, Caída libre (son posición vs tiempo)
- Parábola, Seno, Exponencial (son y = f(x))
- Cardioide, Lemniscata, Circunferencia (curvas planas)

### Implementación (si se decide hacer)

**Paso 1: Añadir campo en Supabase**

```sql
ALTER TABLE formulas ADD COLUMN IF NOT EXISTS dimension INTEGER DEFAULT 2;

UPDATE formulas SET dimension = 3 
WHERE nombre IN ('Tiro Parabólico', 'Espiral de Arquímedes', 'Espiral Logarítmica');
```

**Paso 2: Modificar calculadora.py**

Para Tiro Parabólico, ya devuelve `{t, x, y}`. Solo renombrar para 3D:

```python
def calcular_tiro_parabolico(...) -> dict:
    # ... cálculo actual ...
    return {
        "x": x.tolist(),  # Distancia horizontal
        "y": y.tolist(),  # Altura
        "z": t.tolist(),  # Tiempo como tercera dimensión
        "dimension": 3
    }
```

**Paso 3: Modificar frontend/js/graficos.js**

```javascript
function renderizarGrafico(resultado, formula) {
    const datos = resultado.resultado || resultado;
    const es3D = datos.dimension === 3 || (datos.x && datos.y && datos.z);
    
    if (es3D) {
        // Plotly 3D
        const trace = {
            x: datos.x,
            y: datos.y,
            z: datos.z,
            type: 'scatter3d',
            mode: 'lines',
            line: { color: '#3b82f6', width: 4 }
        };
        
        const layout = {
            scene: {
                xaxis: { title: 'X' },
                yaxis: { title: 'Y' },
                zaxis: { title: 'Z/Tiempo' },
                camera: { eye: { x: 1.5, y: 1.5, z: 1.2 } }
            },
            paper_bgcolor: '#1e293b',
            margin: { l: 0, r: 0, t: 30, b: 0 }
        };
        
        Plotly.newPlot('graficoContainer', [trace], layout, {responsive: true});
    } else {
        // Código 2D actual (mantener)
    }
}
```

---

## ORDEN DE EJECUCIÓN

```
1. ✅ Crear scripts/corregir_variables_supabase.py
2. ✅ Ejecutar script (corrige datos en Supabase)
3. ✅ Añadir CSS para ocultar spinners
4. ✅ Probar en localhost
5. ✅ Commit y push
6. ✅ Verificar en producción
7. ⏳ (Opcional) Implementar 3D si Juan lo quiere
```

---

## VERIFICACIÓN FINAL

### Test 1: Variables dinámicas
- [ ] MRU muestra: "Posición inicial x₀", "Velocidad"
- [ ] MRUA muestra: "Posición inicial x₀", "Velocidad inicial", "Aceleración a"
- [ ] Caída Libre muestra: "Posición inicial y₀", "Gravedad g"
- [ ] Tiro Parabólico muestra: "Velocidad inicial", "Ángulo θ", "Gravedad g"
- [ ] Todas las 15 fórmulas tienen nombres descriptivos (no números)

### Test 2: Sin spinners
- [ ] Inputs no muestran flechas arriba/abajo

### Test 3: Funcionalidad
- [ ] Calcular funciona en todas las fórmulas
- [ ] Gráficos se renderizan correctamente
- [ ] Historial funciona

---

*Documento creado por Claude Opus - 8 Enero 2026*
