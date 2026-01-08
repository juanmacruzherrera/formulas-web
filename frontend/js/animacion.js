// frontend/js/animacion.js
// ============================================
// QUÉ HACE: Sistema de animación para gráficos 2D y 3D
// CONSUME: Datos de cálculos (arrays x, y, z, t)
// EXPONE: animarCurva2D(), animarCurva3D()
// RELACIONADO CON:
//   - Usado por: graficos.js (para renderizar con animación)
//   - Usa: Plotly.js (Plotly.extendTraces, Plotly.addFrames)
// ============================================

/**
 * Anima la construcción de una curva 2D punto por punto
 * @param {Object} datos - {x: [...], y: [...]} o {t: [...], x: [...]}
 * @param {number} duracion - Duración total de la animación en ms (default 3000)
 * @returns {number} - ID del timer (para poder cancelar con clearInterval)
 */
function animarCurva2D(datos, duracion = 3000) {
    const container = document.getElementById('graficoContainer');
    const totalPuntos = datos.x.length;
    const intervalo = duracion / totalPuntos;

    // Ocultar placeholder si existe
    const placeholder = document.getElementById('placeholderGrafico');
    if (placeholder) {
        placeholder.style.display = 'none';
    }

    // Configuración inicial (traza vacía)
    const trace = {
        x: [],
        y: datos.y ? [] : [],
        mode: 'lines',
        line: {
            color: '#3b82f6',
            width: 3
        },
        name: 'Curva'
    };

    // Si no hay 'y', usamos 't' como eje Y (para gráficos tiempo-posición)
    const yData = datos.y || datos.t;

    const layout = {
        paper_bgcolor: '#0f172a',
        plot_bgcolor: '#1e293b',
        font: { color: '#94a3b8' },
        xaxis: {
            gridcolor: '#334155',
            zerolinecolor: '#475569',
            color: '#94a3b8',
            title: datos.y ? 'X' : 'Tiempo (s)'
        },
        yaxis: {
            gridcolor: '#334155',
            zerolinecolor: '#475569',
            color: '#94a3b8',
            title: datos.y ? 'Y' : 'Posición (m)'
        },
        margin: { l: 60, r: 40, t: 40, b: 60 },
        showlegend: false
    };

    const config = {
        responsive: true,
        displayModeBar: true,
        displaylogo: false,
        modeBarButtonsToRemove: ['toImage']
    };

    // Crear gráfico vacío
    Plotly.newPlot(container, [trace], layout, config);

    // Animar punto por punto
    let i = 0;
    const timer = setInterval(() => {
        if (i >= totalPuntos) {
            clearInterval(timer);
            console.log('✅ Animación 2D completada');
            return;
        }

        // Añadir siguiente punto usando extendTraces
        Plotly.extendTraces(container, {
            x: [[datos.x[i]]],
            y: [[yData[i]]]
        }, [0]);

        i++;
    }, intervalo);

    return timer;
}

/**
 * Anima una curva 3D con evolución temporal usando frames de Plotly
 * @param {Object} datos - {x: [...], y: [...], z: [...]}
 * @param {number} duracion - Duración total de la animación en ms (default 5000)
 */
function animarCurva3D(datos, duracion = 5000) {
    const container = document.getElementById('graficoContainer');
    const totalPuntos = datos.x.length;

    // Ocultar placeholder si existe
    const placeholder = document.getElementById('placeholderGrafico');
    if (placeholder) {
        placeholder.style.display = 'none';
    }

    // Crear frames de animación (máximo 100 frames para rendimiento)
    const frames = [];
    const step = Math.max(1, Math.floor(totalPuntos / 100));

    for (let i = step; i <= totalPuntos; i += step) {
        frames.push({
            name: `frame${i}`,
            data: [{
                x: datos.x.slice(0, i),
                y: datos.y.slice(0, i),
                z: datos.z.slice(0, i)
            }]
        });
    }

    // Traza inicial (solo primer punto)
    const trace = {
        type: 'scatter3d',
        mode: 'lines',
        x: datos.x.slice(0, 1),
        y: datos.y.slice(0, 1),
        z: datos.z.slice(0, 1),
        line: {
            color: datos.z,  // Color basado en el valor Z
            colorscale: 'Viridis',
            width: 4
        },
        name: 'Curva 3D'
    };

    const layout = {
        scene: {
            xaxis: {
                title: 'X',
                gridcolor: '#334155',
                backgroundcolor: '#0f172a',
                color: '#94a3b8'
            },
            yaxis: {
                title: 'Y',
                gridcolor: '#334155',
                backgroundcolor: '#0f172a',
                color: '#94a3b8'
            },
            zaxis: {
                title: 'Z',
                gridcolor: '#334155',
                backgroundcolor: '#0f172a',
                color: '#94a3b8'
            },
            bgcolor: '#0f172a',
            camera: {
                eye: { x: 1.5, y: 1.5, z: 1.2 }
            }
        },
        paper_bgcolor: '#0f172a',
        font: { color: '#94a3b8' },
        showlegend: false,
        margin: { l: 0, r: 0, t: 0, b: 0 },
        updatemenus: [{
            type: 'buttons',
            showactive: false,
            y: 1,
            x: 0.1,
            yanchor: 'top',
            buttons: [{
                label: '▶ Play',
                method: 'animate',
                args: [null, {
                    fromcurrent: true,
                    frame: { duration: duracion / frames.length, redraw: true },
                    transition: { duration: 0 },
                    mode: 'immediate'
                }]
            }, {
                label: '⏸ Pause',
                method: 'animate',
                args: [[null], {
                    mode: 'immediate',
                    frame: { duration: 0, redraw: false }
                }]
            }]
        }],
        sliders: [{
            active: 0,
            steps: frames.map((f, i) => ({
                label: `${Math.round(i * 100 / frames.length)}%`,
                method: 'animate',
                args: [[f.name], {
                    mode: 'immediate',
                    frame: { duration: 0, redraw: true },
                    transition: { duration: 0 }
                }]
            })),
            x: 0.1,
            len: 0.8,
            y: 0,
            yanchor: 'top',
            currentvalue: {
                prefix: 'Progreso: ',
                visible: true,
                xanchor: 'center',
                font: { color: '#94a3b8' }
            }
        }]
    };

    const config = {
        responsive: true,
        displayModeBar: true,
        displaylogo: false,
        modeBarButtonsToRemove: ['toImage']
    };

    // Crear gráfico 3D con frames
    Plotly.newPlot(container, [trace], layout, config).then(() => {
        Plotly.addFrames(container, frames);
        console.log(`✅ Gráfico 3D creado con ${frames.length} frames`);
    });
}

/**
 * Función auxiliar: Cancela una animación en curso
 * @param {number} timerId - ID del timer devuelto por animarCurva2D
 */
function cancelarAnimacion(timerId) {
    if (timerId) {
        clearInterval(timerId);
        console.log('⏹ Animación cancelada');
    }
}

// Exportar funciones para uso global
window.animacion = {
    animarCurva2D,
    animarCurva3D,
    cancelarAnimacion
};
