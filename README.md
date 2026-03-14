# TFG - Determinantes del gasto en seguros sanitarios privados

Repositorio del TFG en LaTeX (Ismael Quesada García).

## Nueva Estructura del Proyecto

El proyecto ha sido organizado para mantener un espacio de trabajo limpio y eficiente:

### Núcleo del Documento (LaTeX)
- `main.tex`: Documento principal de LaTeX.
- `referencias.bib`: Base de datos bibliográfica.
- `capitulos/`: Archivos `.tex` individuales para cada capítulo.
- `figuras/`: Gráficos, diagramas y logos utilizados en el documento.

### Datos y Análisis
- `data/`: Contiene los datasets finales y brutos (`.csv`, `.xlsx`).
- `scripts/`: Scripts de Python para el procesamiento de datos, estimación de modelos y generación de gráficos.
- `borradores/`: Resultados intermedios de las regresiones y borradores en formato Markdown (`.md`).

### Otros Recursos
- `notas/`: Instrucciones y registros de cambios (`.txt`).
- `archivo/`: Versiones antiguas, plantillas de Word y copias de seguridad comprimidas (`.zip`).
- `requirements.txt`: Dependencias de Python necesarias para ejecutar los scripts.
- `.gitignore`: Configuración para evitar subir archivos temporales de LaTeX y Python.

## Ejecución del Análisis

Para replicar los resultados:
1. Asegúrate de tener las dependencias instaladas: `pip install -r requirements.txt`.
2. Los scripts se encuentran en la carpeta `scripts/`. Puedes ejecutarlos desde la raíz:
   ```bash
   python scripts/regresiones_panel.py
   ```
3. Los resultados se guardarán automáticamente en la carpeta `borradores/` o `figuras/`.

---
*Nota: Este proyecto utiliza un panel de 17 comunidades autónomas (2016-2024).*
