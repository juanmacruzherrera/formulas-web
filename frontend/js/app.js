// frontend/js/app.js
// ============================================
// QUÉ HACE: Lógica principal de la aplicación (controlador)
// CONSUME: api.js (funciones HTTP), graficos.js (renderizado Plotly)
// EXPONE: Funciones de inicialización y manejo de eventos
// RELACIONADO CON:
//   - Usa: api.js, graficos.js
//   - Manipula: DOM (index.html)
// ============================================

// Estado global de la aplicación
let formulasDisponibles = [];
let formulaActual = null;

/**
 * Inicializa la aplicación cuando el DOM está listo
 */
document.addEventListener('DOMContentLoaded', async () => {
    console.log('🚀 Inicializando aplicación...');

    // Verificar que el backend esté funcionando
    const backendOk = await api.verificarBackend();

    if (!backendOk) {
        api.mostrarToast('⚠️  El backend no está disponible. Inicia el servidor FastAPI.', 'warning');
        return;
    }

    // Cargar fórmulas disponibles
    await cargarFormulas();

    // Cargar historial
    await cargarHistorial();

    // Configurar event listeners
    configurarEventListeners();

    console.log('✅ Aplicación inicializada correctamente');
});

/**
 * Carga todas las fórmulas disponibles desde el backend
 */
async function cargarFormulas() {
    const selector = document.getElementById('formulaSelector');

    // Obtener fórmulas
    formulasDisponibles = await api.obtenerFormulas();

    if (formulasDisponibles.length === 0) {
        selector.innerHTML = '<option disabled selected>No hay fórmulas disponibles</option>';
        return;
    }

    // Limpiar selector
    selector.innerHTML = '';

    // Añadir opción por defecto
    const optionDefault = document.createElement('option');
    optionDefault.disabled = true;
    optionDefault.selected = true;
    optionDefault.textContent = 'Selecciona una fórmula...';
    selector.appendChild(optionDefault);

    // Añadir cada fórmula como opción
    formulasDisponibles.forEach(formula => {
        const option = document.createElement('option');
        option.value = formula.id;
        option.textContent = formula.nombre;
        option.dataset.categoria = formula.categoria;
        selector.appendChild(option);
    });

    // Seleccionar la primera fórmula automáticamente
    if (formulasDisponibles.length > 0) {
        selector.selectedIndex = 1; // Índice 1 (la primera fórmula real)
        await cargarFormulaSeleccionada();
    }
}

/**
 * Carga los detalles de la fórmula actualmente seleccionada
 */
async function cargarFormulaSeleccionada() {
    const selector = document.getElementById('formulaSelector');
    const formulaId = parseInt(selector.value);

    if (isNaN(formulaId)) {
        return;
    }

    // Obtener detalles completos de la fórmula
    formulaActual = await api.obtenerFormula(formulaId);

    if (!formulaActual) {
        return;
    }

    // Actualizar UI
    mostrarFormulaLatex(formulaActual.formula_latex);
    mostrarCategoria(formulaActual.categoria);
    generarInputsDinamicos(formulaActual);
}

/**
 * Muestra la fórmula LaTeX renderizada con MathJax
 * @param {string} latex - Fórmula en formato LaTeX
 */
function mostrarFormulaLatex(latex) {
    const display = document.getElementById('formulaDisplay');

    // Formatear para MathJax (delimitadores $$)
    display.innerHTML = `$$${latex}$$`;

    // Re-renderizar MathJax si está disponible
    if (window.MathJax) {
        MathJax.typesetPromise([display]).catch(err => {
            console.error('Error al renderizar LaTeX:', err);
        });
    }
}

/**
 * Muestra la categoría de la fórmula
 * @param {string} categoria - Nombre de la categoría
 */
function mostrarCategoria(categoria) {
    const badge = document.getElementById('categoriaDisplay');
    badge.textContent = categoria || 'Sin categoría';
}

/**
 * Diccionario de etiquetas amigables para variables comunes
 */
const ETIQUETAS_VARIABLES = {
    // Posiciones y coordenadas
    'x0': { label: 'Posición inicial x₀', placeholder: 'metros', unidad: 'm' },
    'y0': { label: 'Posición inicial y₀', placeholder: 'metros', unidad: 'm' },
    'x': { label: 'Coordenada x', placeholder: 'unidades', unidad: '' },

    // Velocidades
    'v': { label: 'Velocidad', placeholder: 'm/s', unidad: 'm/s' },
    'v0': { label: 'Velocidad inicial', placeholder: 'm/s', unidad: 'm/s' },

    // Aceleración y gravedad
    'a': { label: 'Aceleración a', placeholder: 'm/s²', unidad: 'm/s²' },
    'g': { label: 'Gravedad g', placeholder: 'm/s²', unidad: 'm/s²' },

    // Coeficientes matemáticos
    'A': { label: 'Coeficiente A', placeholder: 'número', unidad: '' },
    'B': { label: 'Coeficiente B', placeholder: 'número', unidad: '' },
    'C': { label: 'Coeficiente C', placeholder: 'número', unidad: '' },
    'b': { label: 'Coeficiente b', placeholder: 'número', unidad: '' },
    'c': { label: 'Coeficiente c', placeholder: 'número', unidad: '' },
    'k': { label: 'Constante k', placeholder: 'número', unidad: '' },

    // Variables paramétricas y polares
    't': { label: 'Parámetro t', placeholder: 'unidades', unidad: '' },
    'theta': { label: 'Ángulo θ', placeholder: 'radianes', unidad: 'rad' },
    'r': { label: 'Radio r', placeholder: 'unidades', unidad: '' },
    'omega': { label: 'Frecuencia angular ω', placeholder: 'rad/s', unidad: 'rad/s' },
    'phi': { label: 'Fase φ', placeholder: 'radianes', unidad: 'rad' }
};

/**
 * Genera inputs dinámicos según las variables de la fórmula
 * @param {Object} formula - Objeto fórmula con variables_usuario
 */
function generarInputsDinamicos(formula) {
    const container = document.getElementById('inputsContainer');
    container.innerHTML = '';

    // FIX: variables_usuario a veces viene como STRING en lugar de OBJECT
    // Cuando viene como string '{"x0": 0, "v0": 5}', hay que parsearlo
    let variables = formula.variables_usuario || {};

    if (typeof variables === 'string') {
        try {
            variables = JSON.parse(variables);
            console.log('✅ variables_usuario parseado de string a object');
        } catch (e) {
            console.error('❌ Error al parsear variables_usuario:', e);
            variables = {};
        }
    }

    // 1. Generar inputs para cada variable en variables_usuario
    Object.entries(variables).forEach(([nombreVar, valorDefecto]) => {
        const config = ETIQUETAS_VARIABLES[nombreVar] || {
            label: nombreVar,
            placeholder: 'valor',
            unidad: ''
        };

        const div = document.createElement('div');
        div.className = 'form-control w-full';

        const label = document.createElement('label');
        label.className = 'label';
        label.innerHTML = `<span class="label-text text-slate-300 text-sm">${config.label}</span>`;

        const input = document.createElement('input');
        input.type = 'number';
        input.name = nombreVar;
        input.id = `input_${nombreVar}`;
        input.className = 'input input-bordered input-sm bg-slate-700 text-slate-100 border-slate-600 focus:border-blue-500 w-full';
        input.placeholder = config.placeholder;
        input.step = '0.1';
        input.required = true;
        input.value = valorDefecto;

        div.appendChild(label);
        div.appendChild(input);
        container.appendChild(div);
    });

    // 2. Generar sliders para el rango (variable_rango_min, variable_rango_max)
    const rangoMin = {
        nombre: `${formula.variable_rango}_min`,
        label: `${formula.variable_rango} mínimo`,
        valor: formula.rango_min || 0,
        min: formula.rango_min !== null ? formula.rango_min - 10 : -10,
        max: formula.rango_max !== null ? formula.rango_max : 100
    };

    const rangoMax = {
        nombre: `${formula.variable_rango}_max`,
        label: `${formula.variable_rango} máximo`,
        valor: formula.rango_max || 10,
        min: formula.rango_min !== null ? formula.rango_min : 0,
        max: formula.rango_max !== null ? formula.rango_max + 10 : 100
    };

    [rangoMin, rangoMax].forEach(rango => {
        const div = document.createElement('div');
        div.className = 'form-control w-full';

        const labelContainer = document.createElement('div');
        labelContainer.className = 'flex justify-between items-center mb-1';

        const label = document.createElement('label');
        label.className = 'label-text text-slate-300 text-sm';
        label.textContent = rango.label;

        const valorDisplay = document.createElement('span');
        valorDisplay.id = `display_${rango.nombre}`;
        valorDisplay.className = 'text-blue-400 text-sm font-mono';
        valorDisplay.textContent = rango.valor;

        labelContainer.appendChild(label);
        labelContainer.appendChild(valorDisplay);

        const slider = document.createElement('input');
        slider.type = 'range';
        slider.name = rango.nombre;
        slider.id = `input_${rango.nombre}`;
        slider.className = 'range range-primary range-sm';
        slider.min = rango.min;
        slider.max = rango.max;
        slider.step = '0.1';
        slider.value = rango.valor;
        slider.required = true;

        // Actualizar display del valor cuando cambia el slider
        slider.addEventListener('input', (e) => {
            valorDisplay.textContent = e.target.value;
        });

        div.appendChild(labelContainer);
        div.appendChild(slider);
        container.appendChild(div);
    });
}

/**
 * Configura todos los event listeners de la aplicación
 */
function configurarEventListeners() {
    // Selector de fórmula
    const selector = document.getElementById('formulaSelector');
    selector.addEventListener('change', cargarFormulaSeleccionada);

    // Botón calcular
    const btnCalcular = document.getElementById('btnCalcular');
    btnCalcular.addEventListener('click', realizarCalculo);

    // Botón refrescar historial
    const btnRefrescar = document.getElementById('btnRefrescarHistorial');
    btnRefrescar.addEventListener('click', cargarHistorial);
}

/**
 * Realiza el cálculo con los valores ingresados
 */
async function realizarCalculo() {
    if (!formulaActual) {
        api.mostrarToast('Selecciona una fórmula primero', 'warning');
        return;
    }

    const btnCalcular = document.getElementById('btnCalcular');

    // Recopilar valores de los inputs
    const valores = {};
    const inputs = document.querySelectorAll('#inputsContainer input');
    let valido = true;

    inputs.forEach(input => {
        const valor = parseFloat(input.value);

        if (isNaN(valor) || input.value.trim() === '') {
            input.classList.add('input-error');
            valido = false;
        } else {
            input.classList.remove('input-error');
            valores[input.name] = valor;
        }
    });

    if (!valido) {
        api.mostrarToast('Por favor completa todos los campos correctamente', 'warning');
        return;
    }

    // Mostrar loading en el botón
    const textoOriginal = btnCalcular.innerHTML;
    btnCalcular.disabled = true;
    btnCalcular.innerHTML = '<span class="loading loading-spinner loading-sm"></span> Calculando...';

    try {
        // Llamar a la API para calcular
        const resultado = await api.calcularFormula(formulaActual.id, valores);

        if (!resultado) {
            throw new Error('No se obtuvo resultado del cálculo');
        }

        // Renderizar el gráfico
        graficos.renderizarGrafico(resultado, formulaActual);

        // Actualizar historial
        await cargarHistorial();

    } catch (error) {
        console.error('Error en el cálculo:', error);
        api.mostrarToast('Error al realizar el cálculo', 'error');
    } finally {
        // Restaurar botón
        btnCalcular.disabled = false;
        btnCalcular.innerHTML = textoOriginal;
    }
}

/**
 * Carga y muestra el historial de cálculos
 */
async function cargarHistorial() {
    const container = document.getElementById('historialContainer');

    // Obtener historial (últimos 5)
    const historial = await api.obtenerHistorial(5);

    if (historial.length === 0) {
        container.innerHTML = '<p class="text-slate-400 text-sm">No hay cálculos en el historial aún</p>';
        return;
    }

    // Generar cards de historial (layout vertical para panel lateral)
    const cardsHTML = historial.map((calculo, index) => {
        const formula = calculo.formulas || {};
        const fecha = new Date(calculo.created_at);
        const fechaFormateada = fecha.toLocaleString('es-ES', {
            day: '2-digit',
            month: 'short',
            hour: '2-digit',
            minute: '2-digit'
        });

        const miniaturaId = `miniatura-${calculo.id}`;

        return `
            <div class="card bg-slate-600 shadow-md hover:bg-slate-500 transition-colors duration-200 cursor-pointer border border-slate-500"
                 data-calculo-id="${calculo.id}"
                 onclick="cargarCalculoDeHistorial(${calculo.id})">
                <div class="card-body p-3">
                    <h3 class="text-xs font-semibold text-blue-300 truncate">${formula.nombre || 'Sin nombre'}</h3>
                    <p class="text-xs text-slate-400">${fechaFormateada}</p>

                    <!-- Miniatura del gráfico -->
                    <div id="${miniaturaId}" class="h-16 mt-2 rounded bg-slate-700"></div>

                    <!-- Valores -->
                    <div class="text-xs text-slate-300 mt-2">
                        ${calculo.valores_entrada ? Object.entries(calculo.valores_entrada).map(([k, v]) =>
                            `<span class="badge badge-xs badge-outline mr-1 mb-1">${k}: ${v}</span>`
                        ).join('') : 'Sin datos'}
                    </div>
                </div>
            </div>
        `;
    }).join('');

    container.innerHTML = cardsHTML;

    // Renderizar miniaturas de gráficos (después de que el DOM esté actualizado)
    setTimeout(() => {
        historial.forEach(calculo => {
            if (calculo.resultado) {
                const miniaturaId = `miniatura-${calculo.id}`;
                graficos.renderizarMiniaturaGrafico(miniaturaId, calculo.resultado);
            }
        });
    }, 100);
}

/**
 * Carga un cálculo del historial (al hacer click)
 * @param {number} calculoId - ID del cálculo a cargar
 */
async function cargarCalculoDeHistorial(calculoId) {
    const historial = await api.obtenerHistorial(20);
    const calculo = historial.find(c => c.id === calculoId);

    if (!calculo) {
        api.mostrarToast('No se pudo cargar el cálculo', 'error');
        return;
    }

    // Cargar fórmula
    const selector = document.getElementById('formulaSelector');
    selector.value = calculo.formula_id;
    await cargarFormulaSeleccionada();

    // Rellenar inputs con los valores del historial
    if (calculo.valores_entrada) {
        Object.entries(calculo.valores_entrada).forEach(([nombre, valor]) => {
            const input = document.getElementById(`input_${nombre}`);
            if (input) {
                input.value = valor;
            }
        });
    }

    // Renderizar el gráfico
    if (calculo.resultado) {
        graficos.renderizarGrafico(calculo, calculo.formulas || {});
    }

    api.mostrarToast('Cálculo cargado desde el historial', 'info');

    // Scroll al inicio
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Exponer funciones globalmente para onclick en HTML
window.cargarCalculoDeHistorial = cargarCalculoDeHistorial;

// ============================================
// REDISEÑO V2.0: Toggle panel + Tabs 2D/3D
// 8 Enero 2026
// ============================================

/**
 * Inicializar funcionalidad del toggle del panel de controles
 */
function initToggleControls() {
    const toggleBtn = document.getElementById('toggleControls');
    const content = document.getElementById('controlsContent');
    const icon = document.getElementById('toggleIcon');
    
    if (!toggleBtn || !content) return;
    
    toggleBtn.addEventListener('click', () => {
        const isHidden = content.classList.contains('hidden');
        
        if (isHidden) {
            // Expandir
            content.classList.remove('hidden');
            toggleBtn.classList.remove('collapsed');
        } else {
            // Colapsar
            content.classList.add('hidden');
            toggleBtn.classList.add('collapsed');
        }
    });
}

/**
 * Inicializar funcionalidad de tabs 2D/3D
 */
function initTabs() {
    const tab2D = document.getElementById('tab2D');
    const tab3D = document.getElementById('tab3D');
    
    if (!tab2D || !tab3D) return;
    
    tab2D.addEventListener('click', () => {
        tab2D.classList.add('tab-active');
        tab3D.classList.remove('tab-active');
        console.log('🎨 Modo 2D activado');
        // TODO FASE 6.4: Filtrar fórmulas 2D
    });
    
    tab3D.addEventListener('click', () => {
        tab3D.classList.add('tab-active');
        tab2D.classList.remove('tab-active');
        console.log('🎨 Modo 3D activado');
        // TODO FASE 6.4: Filtrar fórmulas 3D
    });
}

// Inicializar cuando el DOM esté listo
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', () => {
        initToggleControls();
        initTabs();
    });
} else {
    // DOM ya está listo
    initToggleControls();
    initTabs();
}
