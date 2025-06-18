````markdown
# Análisis de Retención de Clientes con Cohortes

## Descripción

Este proyecto analiza la retención de usuarios en función de su mes de registro (cohorte) y seguimiento de su actividad a lo largo del tiempo. Se utiliza análisis de cohortes para entender patrones de abandono y fidelización, identificar tendencias y ofrecer recomendaciones para mejorar la retención.

---

## Objetivos

- Calcular la matriz de retención mensual por cohorte.
- Visualizar la evolución de la retención a lo largo del tiempo.
- Comparar la retención entre cohortes antiguas y recientes.
- Analizar la retención segmentada por país.
- Extraer insights clave y proponer acciones para marketing y producto.

---

## Dataset

- Datos de actividad de usuarios con columnas principales:
  - `user_id`: identificador único de usuario
  - `signup_date`: fecha de registro del usuario
  - `activity_date`: fecha de actividad o uso del producto
  - `country`: país de procedencia del usuario (para segmentación)

Los datos se encuentran en `data/user_activity.csv`.

---

## Metodología y Código Principal

- Conversión de fechas a periodos mensuales para agrupar cohortes y actividad.
- Cálculo del índice de cohorte (meses desde el registro).
- Conteo de usuarios activos únicos por cohorte y mes relativo.
- Cálculo de la matriz de retención como proporción del tamaño inicial de cada cohorte.
- Visualizaciones con Matplotlib y Seaborn (heatmaps y curvas de retención).
- Segmentación de retención promedio por país.
- Identificación de mejores y peores cohortes.

Se puede encontrar el código completo y reproducible en el notebook `cohort_analysis.ipynb`.

---

## Resultados y Visualizaciones

- **Heatmap de retención por cohorte mensual:** visualiza el porcentaje de usuarios activos mes a mes.
- **Curvas de retención por cohorte:** muestran la evolución de la retención para cada cohorte individualmente.
- **Retención promedio por cohorte y por país:** permite comparar comportamiento entre segmentos geográficos.
- **Ranking de mejores y peores cohortes:** identifica cohortes con desempeño sobresaliente o bajo.

Las imágenes generadas se encuentran en la carpeta `images/`:

- `heatmap_retencion.png`
- `curvas_retencion_cohorte.png`
- `retencion_promedio_por_pais.png`
- `curvas_retencion_top_cohortes.png`

---

## Conclusiones clave

- La retención cae fuertemente después del primer mes, de casi 100% a menos del 30% en la mayoría de cohortes.
- Cohortes recientes (ej. 2024-05) presentan mejor retención sostenida, sugiriendo mejoras recientes en onboarding o campañas.
- Diferencias significativas entre países, indicando adaptación cultural o estrategia de comunicación variable.
- Algunas cohortes con bajo desempeño inicial indican posibles fallos en campañas o experiencia de usuario.

---

## Recomendaciones

### Marketing

- Replicar estrategias exitosas de cohortes con buena retención en otros meses y países.
- Reforzar campañas de retención durante los primeros 30 días (notificaciones, emails personalizados).
- Optimizar mensajes y canales en países con baja retención.

### Producto

- Mejorar el proceso de onboarding para reducir abandono temprano.
- Detectar y corregir fricciones que afectan cohortes con peor desempeño.
- Implementar tests A/B con cohortes nuevas para validar mejoras.

---

## Cómo reproducir el análisis

1. Clonar este repositorio.  
2. Instalar dependencias:

```bash
pip install pandas numpy matplotlib seaborn jupyter python-pptx
```

3. Ejecutar el notebook `cohort_analysis.ipynb` para generar las visualizaciones.
4. Ejecutar el script `generate_presentation.py` (opcional) para crear automáticamente la presentación PowerPoint con los gráficos.
5. Explorar las imágenes y presentación generadas en `images/` y `Analisis_Cohortes.pptx`.

---

## Presentación

Se generó una presentación PowerPoint (`Analisis_Cohortes.pptx`) que resume el análisis, visualizaciones clave y recomendaciones.

---

## Autor

Tobias - [Tobix2 (GitHub)](https://github.com/Tobix2) | [LinkedIn](https://www.linkedin.com/in/tobias-schmidt-2533b2180/)

---

## Licencia

[MIT License](https://opensource.org/licenses/MIT)

