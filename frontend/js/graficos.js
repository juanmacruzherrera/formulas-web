// frontend/js/graficos.js
// ============================================
// QUÉ HACE: Configuración y renderizado de gráficos con Plotly.js
// CONSUME: Datos de cálculos (arrays de puntos t, x)
// EXPONE: Funciones para crear y actualizar gráficos
// RELACIONADO CON:
//   - Usado por: frontend/js/app.js
//   - Usa: Plotly.js (librería global cargada vía CDN)
// ============================================

/**
 * Configuración global de Plotly (botones, comportamiento)
 */
const configPlotly = {
    responsive: true,                // Adaptar al tamaño del contenedor
    displayModeBar: true,            // Mostrar barra de herramientas
    displaylogo: false,              // No mostrar logo de Plotly
    modeBarButtonsToRemove: [        // Quitar botones innecesarios
        'lasso2d',
        'select2d'
    ],
    toImageButtonOptions: {          // Opciones del botón "Descargar como imagen"
        format: 'png',
        filename: 'formula_grafico',
        height: 800,
        width: 1200,
        scale: 2                     // Mayor resolución
    }
};

/**
 * Layout (diseño) del gráfico con tema oscuro elegante
 */
const layoutOscuro = {
    // Colores de fondo
    paper_bgcolor: '#1e293b',        // Fondo del "papel" (exterior)
    plot_bgcolor: '#1e293b',         // Fondo del área de gráfico

    // Tipografía
    font: {
        color: '#f8fafc',            // Color de texto (slate-50)
        family: 'Inter, sans-serif',
        size: 12
    },

    // Configuración del eje X
    xaxis: {
        title: {
            text: 't (tiempo)',
            font: { size: 14, color: '#94a3b8' }  // slate-400
        },
        gridcolor: '#334155',        // Color de las líneas de cuadrícula (slate-700)
        zerolinecolor: '#475569',    // Color de la línea del cero (slate-600)
        tickfont: { color: '#cbd5e1' },  // Color de los números (slate-300)
        showgrid: true,
        zeroline: true
    },

    // Configuración del eje Y
    yaxis: {
        title: {
            text: 'x (posición)',
            font: { size: 14, color: '#94a3b8' }
        },
        gridcolor: '#334155',
        zerolinecolor: '#475569',
        tickfont: { color: '#cbd5e1' },
        showgrid: true,
        zeroline: true
    },

    // Márgenes
    margin: {
        t: 50,   // Top
        r: 30,   // Right
        b: 60,   // Bottom
        l: 70    // Left
    },

    // Configuración de hover (tooltip)
    hovermode: 'closest',
    hoverlabel: {
        bgcolor: '#0f172a',         // Fondo del tooltip
        bordercolor: '#3b82f6',     // Borde azul
        font: {
            color: '#f8fafc',
            family: 'Inter, sans-serif',
            size: 13
        }
    },

    // Título del gráfico (se añade dinámicamente)
    title: {
        text: '',
        font: {
            size: 18,
            color: '#3b82f6',       // blue-500
            family: 'Inter, sans-serif'
        },
        x: 0.5,                     // Centrado
        xanchor: 'center'
    },

    // Mostrar leyenda
    showlegend: true,
    legend: {
        bgcolor: '#0f172a',
        bordercolor: '#334155',
        borderwidth: 1,
        font: { color: '#f8fafc' }
    }
};

/**
 * Renderiza un gráfico con los datos de un cálculo
 * ACTUALIZADO: Detecta automáticamente el tipo de datos (temporal, función o paramétrica)
 * @param {Object} datosCalculo - Objeto con resultado del cálculo
 * @param {Object} formula - Objeto con información de la fórmula
 */
function renderizarGrafico(datosCalculo, formula) {
    const contenedor = document.getElementById('graficoContainer');
    const placeholder = document.getElementById('placeholderGrafico');

    // Ocultar mensaje placeholder
    if (placeholder) {
        placeholder.style.display = 'none';
    }

    const resultado = datosCalculo.resultado;

    // NUEVO: Detectar si es 3D
    const es3D = resultado.z !== undefined && Array.isArray(resultado.z) && resultado.z.length > 0;

    if (es3D) {
        // Renderizado 3D
        const trace = {
            type: 'scatter3d',
            mode: 'lines',
            x: resultado.x,
            y: resultado.y,
            z: resultado.z,
            line: {
                color: resultado.z,
                colorscale: 'Viridis',
                width: 3
            }
        };

        const layout = {
            scene: {
                xaxis: { title: 'X', gridcolor: '#334155', color: '#94a3b8' },
                yaxis: { title: 'Y', gridcolor: '#334155', color: '#94a3b8' },
                zaxis: { title: 'Z', gridcolor: '#334155', color: '#94a3b8' },
                bgcolor: '#0f172a',
                camera: { eye: { x: 1.5, y: 1.5, z: 1.2 } }
            },
            paper_bgcolor: '#0f172a',
            margin: { l: 0, r: 0, t: 30, b: 0 }
        };

        Plotly.newPlot(contenedor, [trace], layout, { responsive: true });
        return; // Salir, no ejecutar código 2D
    }

    let xData, yData, xLabel, yLabel, hoverTemplate;

    // DETECTAR TIPO DE DATOS según las claves presentes
    if (resultado.t !== undefined) {
        // TIPO 1: Fórmulas temporales (t, x) o (t, y)
        xData = resultado.t;
        xLabel = 't (tiempo)';

        if (resultado.x !== undefined) {
            yData = resultado.x;
            yLabel = 'x (posición)';
            hoverTemplate = '<b>t</b>: %{x:.2f}<br><b>x</b>: %{y:.2f}<extra></extra>';
        } else if (resultado.y !== undefined) {
            yData = resultado.y;
            yLabel = 'y (altura)';
            hoverTemplate = '<b>t</b>: %{x:.2f}<br><b>y</b>: %{y:.2f}<extra></extra>';
        }

    } else if (resultado.theta !== undefined) {
        // TIPO 2: Curvas paramétricas polares (theta, x, y)
        // Graficar en plano cartesiano (x, y)
        xData = resultado.x;
        yData = resultado.y;
        xLabel = 'x';
        yLabel = 'y';
        hoverTemplate = '<b>x</b>: %{x:.2f}<br><b>y</b>: %{y:.2f}<extra></extra>';

    } else {
        // TIPO 3: Funciones matemáticas (x, y)
        xData = resultado.x;
        yData = resultado.y;
        xLabel = 'x';
        yLabel = 'y';
        hoverTemplate = '<b>x</b>: %{x:.2f}<br><b>y</b>: %{y:.2f}<extra></extra>';
    }

    // Configurar los datos de la traza (línea)
    const traza = {
        x: xData,
        y: yData,
        type: 'scatter',
        mode: 'lines',
        name: formula.nombre || 'Resultado',
        line: {
            color: '#3b82f6',        // blue-500
            width: 3,
            shape: 'spline',         // Línea suave
            smoothing: 1.3
        },
        hovertemplate: hoverTemplate
    };

    // Clonar el layout base y personalizar
    const layout = {
        ...layoutOscuro,
        title: {
            ...layoutOscuro.title,
            text: formula.nombre || 'Gráfico'
        },
        xaxis: {
            ...layoutOscuro.xaxis,
            title: { text: xLabel, font: { size: 14, color: '#94a3b8' } }
        },
        yaxis: {
            ...layoutOscuro.yaxis,
            title: { text: yLabel, font: { size: 14, color: '#94a3b8' } }
        }
    };

    // Para curvas paramétricas: aspect ratio 1:1 (escala igual en x e y)
    if (resultado.theta !== undefined) {
        layout.yaxis.scaleanchor = 'x';
        layout.yaxis.scaleratio = 1;
    }

    // Renderizar con Plotly (con animación)
    Plotly.newPlot(
        contenedor,
        [traza],
        layout,
        configPlotly
    );

    // Añadir animación de entrada
    contenedor.style.animation = 'fadeIn 0.5s ease-in';
}

/**
 * Actualiza un gráfico existente con nuevos datos (con animación)
 * @param {Object} datosCalculo - Nuevos datos del cálculo
 */
function actualizarGrafico(datosCalculo) {
    const contenedor = document.getElementById('graficoContainer');

    const { t, x } = datosCalculo.resultado;

    // Actualizar datos con animación suave
    Plotly.animate(
        contenedor,
        {
            data: [{
                x: t,
                y: x
            }]
        },
        {
            transition: {
                duration: 500,       // Duración de la animación en ms
                easing: 'cubic-in-out'
            },
            frame: {
                duration: 500
            }
        }
    );
}

/**
 * Limpia el gráfico y muestra el placeholder inicial
 */
function limpiarGrafico() {
    const contenedor = document.getElementById('graficoContainer');
    const placeholder = document.getElementById('placeholderGrafico');

    // Limpiar contenedor Plotly
    Plotly.purge(contenedor);

    // Mostrar placeholder
    if (placeholder) {
        placeholder.style.display = 'flex';
    }
}

/**
 * Renderiza una previsualización pequeña del gráfico (para historial)
 * ACTUALIZADO: Detecta automáticamente el tipo de datos
 * @param {string} contenedorId - ID del div donde renderizar
 * @param {Object} datos - Datos del cálculo (puede ser t,x o x,y o theta,x,y)
 */
function renderizarMiniaturaGrafico(contenedorId, datos) {
    let xData, yData;

    // Detectar tipo de datos (igual que en renderizarGrafico)
    if (datos.t !== undefined) {
        xData = datos.t;
        yData = datos.x || datos.y;
    } else if (datos.theta !== undefined) {
        xData = datos.x;
        yData = datos.y;
    } else {
        xData = datos.x;
        yData = datos.y;
    }

    const traza = {
        x: xData,
        y: yData,
        type: 'scatter',
        mode: 'lines',
        line: {
            color: '#3b82f6',
            width: 2
        },
        hoverinfo: 'skip'            // Sin hover en miniaturas
    };

    const layoutMiniatura = {
        paper_bgcolor: '#0f172a',
        plot_bgcolor: '#0f172a',
        margin: { t: 10, r: 10, b: 10, l: 10 },
        xaxis: {
            showgrid: false,
            showticklabels: false,
            zeroline: false
        },
        yaxis: {
            showgrid: false,
            showticklabels: false,
            zeroline: false
        },
        showlegend: false,
        hovermode: false
    };

    const configMiniatura = {
        displayModeBar: false,
        staticPlot: true             // Sin interacción
    };

    Plotly.newPlot(
        contenedorId,
        [traza],
        layoutMiniatura,
        configMiniatura
    );
}

/**
 * Renderiza un gráfico con animación (punto por punto)
 * NUEVO en v2.0: Usa el sistema de animación de animacion.js
 * @param {Object} datosCalculo - Objeto con resultado del cálculo
 * @param {Object} formula - Objeto con información de la fórmula
 * @param {boolean} conAnimacion - Si true, anima; si false, renderiza directo (default: true)
 */
function renderizarGraficoAnimado(datosCalculo, formula, conAnimacion = true) {
    const contenedor = document.getElementById('graficoContainer');
    const placeholder = document.getElementById('placeholderGrafico');

    // Ocultar mensaje placeholder
    if (placeholder) {
        placeholder.style.display = 'none';
    }

    const resultado = datosCalculo.resultado;

    // Si no hay sistema de animación o no se quiere animación, usar método tradicional
    if (!window.animacion || !conAnimacion) {
        renderizarGrafico(datosCalculo, formula);
        return;
    }

    // DETECTAR si es 2D o 3D
    const es3D = resultado.z !== undefined;

    if (es3D) {
        // Gráfico 3D con animación
        console.log('🎨 Renderizando gráfico 3D con animación');
        window.animacion.animarCurva3D(resultado, 5000);
    } else {
        // Gráfico 2D con animación
        console.log('🎨 Renderizando gráfico 2D con animación');

        // Preparar datos según el tipo
        let datos = { x: [], y: [] };

        if (resultado.t !== undefined) {
            // Fórmulas temporales (t, x) o (t, y)
            datos.x = resultado.t;
            datos.y = resultado.x || resultado.y;
        } else if (resultado.theta !== undefined) {
            // Curvas paramétricas polares
            datos.x = resultado.x;
            datos.y = resultado.y;
        } else {
            // Funciones matemáticas (x, y)
            datos.x = resultado.x;
            datos.y = resultado.y;
        }

        window.animacion.animarCurva2D(datos, 3000);
    }
}

// Exportar funciones para uso global
window.graficos = {
    renderizarGrafico,
    renderizarGraficoAnimado,  // ← NUEVA función con animación
    actualizarGrafico,
    limpiarGrafico,
    renderizarMiniaturaGrafico,
    configPlotly,
    layoutOscuro
};
