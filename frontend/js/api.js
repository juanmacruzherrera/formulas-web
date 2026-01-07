// frontend/js/api.js
// ============================================
// QUÉ HACE: Funciones para comunicarse con el backend FastAPI
// CONSUME: API REST en http://localhost:8000
// EXPONE: Funciones async para obtener y enviar datos
// RELACIONADO CON:
//   - Usado por: frontend/js/app.js
//   - Conecta con: backend/main.py (FastAPI)
// ============================================

// Configuración de la API
// Detecta automáticamente si estamos en desarrollo (localhost) o producción
const API_BASE = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
    ? 'http://localhost:8000'
    : 'https://web-production-daa0.up.railway.app'; // ✅ Backend desplegado en Railway

/**
 * Muestra una notificación toast al usuario
 * @param {string} mensaje - Texto a mostrar
 * @param {string} tipo - 'success', 'error', 'info'
 */
function mostrarToast(mensaje, tipo = 'info') {
    const toastContainer = document.getElementById('toastContainer');

    const colores = {
        success: 'alert-success',
        error: 'alert-error',
        info: 'alert-info',
        warning: 'alert-warning'
    };

    const iconos = {
        success: '<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>',
        error: '<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>',
        info: '<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>',
        warning: '<svg xmlns="http://www.w3.org/2000/svg" class="stroke-current shrink-0 h-6 w-6" fill="none" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" /></svg>'
    };

    const toast = document.createElement('div');
    toast.className = `alert ${colores[tipo] || colores.info} shadow-lg mb-2`;
    toast.innerHTML = `
        <div>
            ${iconos[tipo] || iconos.info}
            <span>${mensaje}</span>
        </div>
    `;

    toastContainer.appendChild(toast);

    // Auto-eliminar después de 4 segundos
    setTimeout(() => {
        toast.classList.add('opacity-0', 'transition-opacity');
        setTimeout(() => toast.remove(), 300);
    }, 4000);
}

/**
 * Actualiza el indicador de estado de conexión
 * @param {boolean} conectado - true si está conectado, false si no
 */
function actualizarEstadoConexion(conectado) {
    const indicador = document.getElementById('statusIndicator');
    const texto = document.getElementById('statusText');

    if (conectado) {
        indicador.classList.remove('loading');
        indicador.classList.add('bg-green-500', 'w-2', 'h-2', 'rounded-full');
        texto.textContent = 'Conectado';
    } else {
        indicador.classList.add('loading');
        indicador.classList.remove('bg-green-500', 'w-2', 'h-2', 'rounded-full');
        texto.textContent = 'Desconectado';
    }
}

/**
 * Obtiene todas las fórmulas disponibles desde el backend
 * @returns {Promise<Array>} Array de fórmulas o array vacío si hay error
 */
async function obtenerFormulas() {
    try {
        const response = await fetch(`${API_BASE}/api/formulas`);

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const resultado = await response.json();

        if (resultado.error) {
            throw new Error(resultado.error);
        }

        actualizarEstadoConexion(true);
        return resultado.data || [];

    } catch (error) {
        console.error('Error al obtener fórmulas:', error);
        mostrarToast('Error al cargar las fórmulas', 'error');
        actualizarEstadoConexion(false);
        return [];
    }
}

/**
 * Obtiene una fórmula específica por su ID
 * @param {number} id - ID de la fórmula
 * @returns {Promise<Object|null>} Objeto fórmula o null si hay error
 */
async function obtenerFormula(id) {
    try {
        const response = await fetch(`${API_BASE}/api/formula/${id}`);

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const resultado = await response.json();

        if (resultado.error) {
            throw new Error(resultado.error);
        }

        return resultado.data;

    } catch (error) {
        console.error('Error al obtener fórmula:', error);
        mostrarToast('Error al cargar la fórmula', 'error');
        return null;
    }
}

/**
 * Calcula una fórmula con los valores proporcionados
 * @param {number} formulaId - ID de la fórmula a calcular
 * @param {Object} valores - Objeto con los valores de las variables
 * @returns {Promise<Object|null>} Resultado del cálculo o null si hay error
 */
async function calcularFormula(formulaId, valores) {
    try {
        const response = await fetch(`${API_BASE}/api/calcular`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                formula_id: formulaId,
                valores: valores
            })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const resultado = await response.json();

        if (resultado.error) {
            throw new Error(resultado.error);
        }

        mostrarToast('Cálculo realizado con éxito', 'success');
        return resultado.data;

    } catch (error) {
        console.error('Error al calcular fórmula:', error);
        mostrarToast(`Error en el cálculo: ${error.message}`, 'error');
        return null;
    }
}

/**
 * Obtiene el historial de cálculos realizados
 * @param {number} limite - Cantidad de cálculos a obtener (por defecto 10)
 * @returns {Promise<Array>} Array de cálculos o array vacío si hay error
 */
async function obtenerHistorial(limite = 10) {
    try {
        const response = await fetch(`${API_BASE}/api/historial?limite=${limite}`);

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const resultado = await response.json();

        if (resultado.error) {
            throw new Error(resultado.error);
        }

        return resultado.data || [];

    } catch (error) {
        console.error('Error al obtener historial:', error);
        mostrarToast('Error al cargar el historial', 'error');
        return [];
    }
}

/**
 * Verifica que el backend esté funcionando
 * @returns {Promise<boolean>} true si el servidor responde, false si no
 */
async function verificarBackend() {
    try {
        const response = await fetch(`${API_BASE}/health`);

        if (!response.ok) {
            throw new Error('Backend no responde');
        }

        const resultado = await response.json();

        if (resultado.status === 'ok') {
            actualizarEstadoConexion(true);
            return true;
        }

        return false;

    } catch (error) {
        console.error('Error al verificar backend:', error);
        actualizarEstadoConexion(false);
        mostrarToast('No se puede conectar con el servidor. Verifica que esté corriendo.', 'error');
        return false;
    }
}

// Exportar funciones para uso global
// (En un proyecto moderno usaríamos ES6 modules, pero para simplicidad usamos global)
window.api = {
    obtenerFormulas,
    obtenerFormula,
    calcularFormula,
    obtenerHistorial,
    verificarBackend,
    mostrarToast,
    actualizarEstadoConexion
};
