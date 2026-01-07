# Plantilla de Documentación Socrática

**Usa esta plantilla para cada tarea. Copia y adapta.**

> ⚠️ **REGLA DE ORO:** Una vez escrito algo en este documento, NUNCA se borra.
> Si hay que corregir o actualizar, se AÑADE una nueva sección con fecha.
> El historial de errores y correcciones es parte del aprendizaje.

---

# [NÚMERO] - [TÍTULO DE LA TAREA]

> **Archivo(s) creado(s):** `ruta/al/archivo.py`
> **Fecha:** YYYY-MM-DD
> **Estado:** ✅ Completado / ❌ Falló / 🔄 En progreso

---

## 1. ¿QUÉ VAMOS A HACER?

*Explica en lenguaje simple qué vas a construir. Como si se lo explicaras a alguien que no sabe programar.*

Ejemplo: "Vamos a crear un archivo que conecte Python con nuestra base de datos en Supabase. Es como darle a Python la dirección y la llave de nuestra despensa para que pueda entrar a buscar cosas."

---

## 2. ¿POR QUÉ LO NECESITAMOS?

*Explica por qué esta pieza es necesaria en el proyecto. Qué problema resuelve.*

Ejemplo: "Sin esta conexión, Python no puede leer las fórmulas que guardamos en Supabase. Sería como tener una despensa llena pero sin llave para entrar."

---

## 3. ¿CÓMO ENCAJA EN EL PROYECTO?

*Dibuja o explica dónde está esta pieza en la arquitectura.*

```
[Frontend] → [Backend/Python] → [ESTA PIEZA] → [Supabase]
                                     ↑
                              Estamos aquí
```

---

## 4. CONCEPTOS PREVIOS

*¿Qué necesitas entender antes de ver el código?*

### Concepto 1: [Nombre]
- **Qué es:** ...
- **Analogía:** ...
- **Ejemplo simple:** ...

### Concepto 2: [Nombre]
- **Qué es:** ...
- **Analogía:** ...

---

## 5. EL CÓDIGO

### Archivo: `ruta/al/archivo.py`

```python
# Aquí va el código completo
```

### Explicación línea por línea:

| Líneas | Qué hacen | Por qué |
|--------|-----------|---------|
| 1-3 | Importamos librerías | Necesitamos X para hacer Y |
| 5-7 | Leemos el .env | Para obtener las credenciales sin exponerlas |
| ... | ... | ... |

---

## 5.1 HISTORIAL DE CAMBIOS EN EL CÓDIGO

> **IMPORTANTE:** Cada vez que modifiques código, documenta el cambio aquí.
> NUNCA borres entradas anteriores. El historial completo es valioso.

*Usa este formato para cada cambio:*

### Cambio #1 - YYYY-MM-DD HH:MM

**Archivo:** `ruta/al/archivo.py`

**Qué cambié (diff):**
```diff
- codigo_anterior = "esto había antes"
- otra_linea_vieja = True
+ codigo_nuevo = "esto puse ahora"
+ otra_linea_nueva = False
+ linea_adicional = "añadí esta"
```

**Por qué lo cambié:**
Porque [explicación del problema que había o mejora que quería hacer]

**Resultado:**
- ✅ Funcionó: [explicar qué mejoró]
- ❌ Falló: [ver sección 7 para el diagnóstico]

---

### Cambio #2 - YYYY-MM-DD HH:MM

*(copiar el formato de arriba para cada cambio adicional)*

---

## 6. PROBANDO QUE FUNCIONA

### Comando para probar:
```bash
python backend/services/supabase_client.py
```

### Resultado esperado:
```
Conexión exitosa. Fórmulas encontradas: 1
```

### Resultado obtenido:
```
[Pega aquí lo que realmente salió]
```

---

## 7. ¿FUNCIONÓ?

### ✅ Si funcionó:
- Qué confirmamos que funciona
- Siguiente paso lógico

### ❌ Si falló:

#### El error:
```
[Pega el error completo]
```

#### ¿Por qué falló? (Diagnóstico)
- Posible causa 1: ...
- Posible causa 2: ...

#### ¿Cómo lo solucioné?
1. Primero intenté: ... → No funcionó porque...
2. Luego probé: ... → Tampoco porque...
3. Finalmente: ... → ¡Funcionó!

#### Lección aprendida:
*¿Qué aprendimos de este error que nos servirá en el futuro?*

---

## 8. RESUMEN

| Pregunta | Respuesta |
|----------|-----------|
| ¿Qué construimos? | ... |
| ¿Para qué sirve? | ... |
| ¿Cómo se usa? | ... |
| ¿Con qué se conecta? | ... |

---

## 9. CONEXIÓN CON EL SIGUIENTE PASO

*¿Qué viene después y por qué depende de lo que acabamos de hacer?*

"Ahora que Python puede conectarse a Supabase, el siguiente paso es crear un endpoint que use esta conexión para devolver las fórmulas al frontend."

---

## 10. ACTUALIZACIONES POSTERIORES

*Si hay que añadir información después de completar este documento, usa este formato:*

### Actualización YYYY-MM-DD

**Qué cambió:**
[descripción del cambio]

**Por qué:**
[razón del cambio]

**Resultado:**
[éxito o nuevo error]

---

*Documentación generada por Claude Code siguiendo el método socrático*
*NUNCA borrar contenido de este archivo - solo añadir*
