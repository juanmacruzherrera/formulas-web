# GUÍA: Subir el Proyecto a GitHub

**IMPORTANTE:** Debes hacer esto ANTES de los pasos 7-8 (deploy en Railway/Cloudflare)

---

## ¿Por qué necesitamos GitHub?

Tanto Railway como Cloudflare Pages se conectan directamente a repositorios de GitHub para obtener el código y desplegarlo automáticamente.

**Sin GitHub → No puedes hacer deploy automático**

---

## PASO A: Inicializar Git en el proyecto

1. **Abrir terminal** y navegar al proyecto:
```bash
cd /Volumes/Akitio01/Claude_MCP/formulas-web
```

2. **Inicializar repositorio Git:**
```bash
git init
```

Verás: `Initialized empty Git repository in ...`

3. **Configurar tu identidad** (si es la primera vez usando Git):
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu.email@example.com"
```

4. **Verificar que .gitignore está correcto:**
```bash
cat .gitignore
```

Debe incluir:
- `.env` (¡IMPORTANTE! No subir secretos)
- `venv/`
- `__pycache__/`

---

## PASO B: Hacer el primer commit

1. **Añadir todos los archivos:**
```bash
git add .
```

2. **Verificar qué se va a subir:**
```bash
git status
```

**⚠️ CRÍTICO:** Verifica que `.env` NO aparece en verde. Si aparece:
```bash
git reset .env
echo ".env" >> .gitignore
git add .gitignore
```

3. **Crear el primer commit:**
```bash
git commit -m "Fase 5 completa: Aplicación lista para deploy

- 15 fórmulas matemáticas y físicas funcionando
- Inputs dinámicos según fórmula seleccionada
- Sliders para ajustar rangos
- Layout optimizado (gráfica grande izquierda)
- Historial lateral colapsable
- Backend FastAPI + Supabase
- Frontend Plotly.js + MathJax
- Preparado para deploy en Railway + Cloudflare Pages"
```

Verás algo como: `XX files changed, XXXX insertions(+)`

---

## PASO C: Crear repositorio en GitHub

1. **Ir a GitHub:**
   - Abre https://github.com
   - Si no tienes cuenta, créala (gratis)

2. **Crear nuevo repositorio:**
   - Click en tu avatar (arriba derecha) → "Your repositories"
   - Click en "New" (botón verde)

3. **Configurar el repositorio:**
   - **Repository name:** `formulas-web` (o el nombre que prefieras)
   - **Description:** "Aplicación web para visualizar fórmulas matemáticas y físicas interactivas"
   - **Visibilidad:**
     - ✅ **Public** (recomendado - funciona con Railway/Cloudflare gratis)
     - ⚠️ Private (Railway gratis permite privados, pero más fácil en público)
   - **NO marques:** "Initialize with README" (ya tienes código)
   - Click "Create repository"

4. **Copiar la URL del repositorio:**
   - Verás algo como: `https://github.com/TU-USUARIO/formulas-web.git`
   - **Copia esta URL**

---

## PASO D: Subir el código a GitHub

1. **Conectar tu proyecto local con GitHub:**
```bash
git remote add origin https://github.com/TU-USUARIO/formulas-web.git
```

Reemplaza `TU-USUARIO` con tu nombre de usuario de GitHub.

2. **Verificar la conexión:**
```bash
git remote -v
```

Debe mostrar:
```
origin  https://github.com/TU-USUARIO/formulas-web.git (fetch)
origin  https://github.com/TU-USUARIO/formulas-web.git (push)
```

3. **Subir el código:**
```bash
git push -u origin main
```

Si te pide credenciales:
- **Usuario:** tu nombre de usuario de GitHub
- **Contraseña:** usa un **Personal Access Token** (no tu contraseña)

### Crear Personal Access Token (si te lo pide):

1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. "Generate new token (classic)"
3. Nombre: "formulas-web-deploy"
4. Scopes: Marca "repo" (todo)
5. "Generate token"
6. **Copia el token** (solo lo verás una vez)
7. Úsalo como contraseña al hacer `git push`

4. **Verificar que se subió:**
   - Abre: `https://github.com/TU-USUARIO/formulas-web`
   - Debes ver todos tus archivos

---

## PASO E: Verificar que todo está correcto

### ✅ Checklist de seguridad:

Abre tu repositorio en GitHub y verifica:

- [ ] ¿Ves la carpeta `backend/`? → ✅
- [ ] ¿Ves la carpeta `frontend/`? → ✅
- [ ] ¿Ves el archivo `Procfile`? → ✅
- [ ] ¿Ves el archivo `.env`? → ❌ **NO DEBE ESTAR** (es secreto)
- [ ] ¿Ves el archivo `.env.example`? → ✅ (este sí puede estar)
- [ ] ¿Ves la carpeta `venv/`? → ❌ **NO DEBE ESTAR** (es muy grande)

**Si ves `.env` en GitHub:**

```bash
# Eliminar del repositorio (pero mantener local)
git rm --cached .env
git commit -m "Eliminar .env del repositorio"
git push

# Asegurarse de que está en .gitignore
echo ".env" >> .gitignore
git add .gitignore
git commit -m "Actualizar .gitignore"
git push
```

---

## PASO F: Futuras actualizaciones

Cada vez que hagas cambios en el código:

```bash
# Ver qué archivos cambiaron
git status

# Añadir los cambios
git add .

# Crear commit con mensaje descriptivo
git commit -m "Descripción de lo que cambiaste"

# Subir a GitHub
git push
```

**Railway y Cloudflare se actualizarán automáticamente** cuando hagas `git push` 🚀

---

## Resumen del flujo completo

```
1. ✅ Inicializar Git (git init)
2. ✅ Primer commit (git add . && git commit)
3. ✅ Crear repo en GitHub
4. ✅ Conectar local con GitHub (git remote add origin)
5. ✅ Subir código (git push -u origin main)
6. ⏳ Deploy backend en Railway (conecta GitHub)
7. ⏳ Deploy frontend en Cloudflare (conecta GitHub)
```

---

## Troubleshooting

### Error: "permission denied"
- Necesitas crear un Personal Access Token (ver arriba)
- No uses tu contraseña de GitHub directamente

### Error: "failed to push some refs"
```bash
git pull origin main --rebase
git push
```

### Error: "src refspec main does not exist"
Tu rama se llama `master` en lugar de `main`:
```bash
git branch -M main
git push -u origin main
```

### Olvidé añadir algo al .gitignore antes del primer commit
```bash
git rm --cached ARCHIVO_O_CARPETA
echo "ARCHIVO_O_CARPETA" >> .gitignore
git add .gitignore
git commit -m "Actualizar .gitignore"
git push
```

---

## Recursos útiles

- **Documentación Git:** https://git-scm.com/doc
- **Guías GitHub:** https://docs.github.com/es
- **Git visual:** https://learngitbranching.js.org/?locale=es_ES

---

**Próximo paso:** Una vez que el código esté en GitHub, sigue con `docs/GUIA_JUAN_PASOS_MANUALES.md` pasos 7-8 para el deploy.
