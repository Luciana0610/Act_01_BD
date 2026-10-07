# Ciencia de Datos con Python - Semana 1

## 1. Descripción del proyecto

Este proyecto corresponde a la actividad de aprendizaje de la Semana 1 de Ciencia de Datos con Python del SENA.

El objetivo es comprender cómo los datos pueden convertirse en información útil para apoyar la toma de decisiones, aplicando conceptos básicos de análisis de datos, estructuras de información, ética, privacidad y reproducibilidad.

---

## 2. Objetivos

- Comprender la diferencia entre dato, información y decisión.
- Identificar conocimientos previos relacionados con datos.
- Reconocer conceptos básicos de ciencia de datos.
- Comprender el ciclo de vida del dato.
- Formular preguntas analíticas.
- Conocer conceptos básicos de SQL, Python y JSON.
- Configurar un entorno reproducible con Python.
- Verificar el funcionamiento del entorno y sus dependencias.
- Reflexionar sobre la privacidad y el uso responsable de los datos.

---

## A. Diagnóstico de conocimientos previos

## 1. ¿Qué representan una tabla, una fila y una clave primaria?

Una **tabla** organiza información relacionada en filas y columnas. Una **fila** representa un registro o elemento individual dentro de la tabla. Una **clave primaria** es un campo que identifica de manera única cada registro.

Por ejemplo, para iniciativas de emprendimiento:

| id_iniciativa | nombre | sector | emprendedor |
| --- | --- | --- | --- |  
| 1 | EcoApp | tecnologia | Ana |
| 2 | Repostería Creativa | alimentos | Carlos |

En este caso, `id_iniciativa` es la clave primaria porque identifica de forma única cada iniciativa.

---

## 2. ¿Para qué sirve una clave foránea?

Una **clave foránea** permite relacionar una tabla con otra. Su función es hacer referencia a un registro existente en otra tabla.

Por ejemplo, una iniciativa puede tener un campo `id_emprendedor` que haga referencia al `id` de un emprendedor.

Si una iniciativa referencia a un emprendedor que no existe, se genera un problema de **integridad referencial**, porque queda una relación sin un registro válido al cual apuntar.

---

## 3. ¿Qué devuelve `SELECT codigo FROM iniciativas WHERE sector = 'tecnologia';`?

Esta consulta busca en la tabla `iniciativas` los registros cuyo sector sea `tecnologia` y devuelve únicamente el campo `codigo`.

```sql
SELECT codigo
FROM iniciativas
WHERE sector = 'tecnologia';
```

Esta consulta no modifica los registros. Solamente consulta y devuelve información.

Las instrucciones como `INSERT`, `UPDATE` y `DELETE` son utilizadas para modificar datos.

---

## 4. Diferencia entre una lista y un diccionario en Python

Una lista permite almacenar varios elementos en un orden determinado y se identifica principalmente mediante posiciones o índices.

Un diccionario almacena información mediante pares clave: valor.

Para representar una sola iniciativa utilizaría un diccionario:

```python
iniciativa = {
    "codigo": "INI001",
    "nombre": "EcoApp",
    "sector": "tecnologia"
}
```

Para representar varias iniciativas utilizaría una lista de diccionarios:

```python
iniciativas = [
    {
        "codigo": "INI001",
        "nombre": "EcoApp",
        "sector": "tecnologia"
    },
    {
        "codigo": "INI002",
        "nombre": "Repostería Creativa",
        "sector": "alimentos"
    }
]
```

---

## 5. ¿Son equivalentes `false` y `"false"` en JSON?

No son equivalentes.

`false` es un valor booleano que representa falso:

```json
false
```

Mientras que `"false"` es una cadena de texto:

```json
"false"
```

Por lo tanto, tienen tipos de datos diferentes. El primero es booleano y el segundo es texto.

---

## 6. Diferencia entre un campo ausente, `null` y una cadena vacía

Son tres situaciones diferentes:

- **Campo ausente:** la propiedad no aparece en el objeto.
- **`null`:** el campo existe, pero no tiene un valor.
- **Cadena vacía `""`:** el campo existe y contiene un texto vacío.

Ejemplo:

```json
{
    "nombre": "EcoApp",
    "sector": null,
    "descripcion": ""
}
```

En este ejemplo, `emprendedor` podría estar ausente si no aparece en el objeto.

`sector: null` significa que el campo existe, pero no tiene un valor registrado.

`descripcion: ""` significa que el campo existe, pero contiene una cadena vacía.

Estas diferencias son importantes al validar y analizar datos.

---

## 7. ¿Qué ventaja tiene una función que retorna datos frente a otra que únicamente los imprime?

Una función que retorna datos permite que el resultado sea utilizado posteriormente por otra parte del programa.

Por ejemplo:

```python
def obtener_iniciativa():
    return {
        "codigo": "INI001",
        "nombre": "EcoApp"
    }
```

El resultado puede almacenarse, analizarse, modificarse o enviarse a otra función.

En cambio, una función que solamente utiliza `print()` muestra el resultado en pantalla, pero no lo entrega directamente para continuar trabajando con él.

Por esta razón, retornar datos proporciona mayor reutilización y flexibilidad.

---

## 8. Si falla la lectura de un archivo JSON, ¿qué revisarías antes de cambiar el programa?

Antes de modificar el programa revisaría:

- Que el archivo exista.
- Que la ruta y el nombre del archivo sean correctos.
- Que el archivo tenga permisos de lectura.
- Que el contenido tenga una estructura JSON válida.
- Que las comillas, llaves, corchetes y comas estén correctamente escritos.
- Que la codificación del archivo sea adecuada.
- El mensaje exacto del error generado por Python.

Primero se debe identificar la causa del problema antes de modificar el código.

---

## 9. ¿Qué información reconoces en `2026-10-06T13:00:00Z`?

La fecha `2026-10-06T13:00:00Z` representa:

- **2026-10-06:** fecha, 6 de octubre de 2026.
- **T:** separa la fecha de la hora.
- **13:00:00:** hora, 1:00 p. m.
- **Z:** indica que la hora está expresada en UTC.

Este formato evita varias ambigüedades que pueden existir en formatos locales como `06/10/26 8:00`.

Por ejemplo, `06/10/26` puede interpretarse como 6 de octubre o como 10 de junio dependiendo de la región. Además, no indica claramente la zona horaria.

El formato ISO 8601 permite representar la fecha y hora de una manera más precisa y estandarizada.

---

## 10. Se publicó por error una contraseña en Git. ¿Qué acciones propondrías?

Si una contraseña fue publicada accidentalmente en Git, no es suficiente con borrarla únicamente del archivo actual.

Las acciones recomendadas son:

1. Revocar o cambiar inmediatamente la contraseña expuesta.
2. Revisar dónde fue publicada.
3. Eliminar el secreto del código.
4. Evitar volver a almacenarlo directamente en el repositorio.
5. Utilizar variables de entorno o un sistema seguro para gestionar secretos.
6. Si la contraseña quedó registrada en el historial de Git, limpiar también el historial cuando sea necesario.
7. Revisar el repositorio para comprobar que no existan otras credenciales expuestas.

La razón principal es que eliminar la contraseña del archivo actual no la elimina necesariamente del historial de Git. Una persona podría seguir encontrándola en un commit anterior.

---

### Conclusión del diagnóstico

Este diagnóstico permitió identificar conocimientos básicos sobre bases de datos, SQL, estructuras de datos en Python, JSON, manejo de archivos, fechas y seguridad de la información.

También permitió reconocer la importancia de mantener la integridad de los datos, validar la información antes de procesarla y proteger las credenciales y demás datos sensibles.

---

## B. Reflexión inicial: del dato a la decisión

Los datos por sí solos representan valores o hechos que pueden ser registrados y almacenados. Cuando estos datos son organizados, analizados y relacionados con un contexto, pueden convertirse en información útil para comprender una situación y apoyar la toma de decisiones.

## 1. Seguimiento académico

| **Elemento** | **Descripción** |
| --- | --- |
| **Dato** | Asistencia del 68% y promedio de actividades de 3.1 |
| **Información** | El aprendiz presenta una asistencia baja y un desempeño académico que requiere atención. |
| **Decisión posible** | Programar un acompañamiento formativo, revisar las dificultades y establecer acciones de mejora. |

---

## 2. Control de inventario

| **Elemento** | **Descripción** |
| --- | --- |
| **Dato** | Hay 6 unidades disponibles de un producto y se venden aproximadamente 4 unidades por día. |
| **Información** | Al ritmo actual de ventas, el inventario disponible podría agotarse en aproximadamente dos días. |
| **Decisión posible** | Solicitar una reposición del producto antes de que se agote el inventario. |

---

## 3. Sostenibilidad

| **Elemento** | **Descripción** |
| --- | --- |
| **Dato** | Se generan 120 kg de residuos aprovechables al mes. |
| **Información** | Existe una cantidad significativa de material que podría ser reutilizado o aprovechado. |
| **Decisión posible** | Diseñar una estrategia de separación, aprovechamiento o alianza para gestionar esos residuos. |

---

## Reflexión

Los datos adquieren valor cuando se organizan, analizan y relacionan con un contexto. La información obtenida permite comprender mejor una situación y facilita la toma de decisiones.

Por esta razón, el manejo adecuado de los datos es importante tanto en el ámbito académico como en el entorno laboral y comunitario.

---

## C. Contexto actual de la ciencia de datos

La ciencia de datos permite transformar datos en información útil para comprender situaciones, encontrar patrones y apoyar la toma de decisiones.

## Conceptos principales

| **Concepto** | **Descripción** |
| --- | --- |
| **Datos** | Valores o hechos que pueden ser registrados y analizados. |
| **Ciencia de datos** | Conjunto de métodos y herramientas para obtener conocimiento a partir de los datos. |
| **Inteligencia artificial** | Tecnologías capaces de realizar tareas que requieren capacidades asociadas con la inteligencia humana. |
| **Ética** | Principios que orientan el uso responsable de los datos. |
| **Calidad de datos** | Características que permiten que los datos sean confiables y útiles. |
| **Decisión** | Acción tomada utilizando información obtenida del análisis. |
| **Contexto productivo** | Entorno donde los datos pueden utilizarse para resolver problemas y mejorar procesos. |

---

## Relación entre los conceptos

```text
                         DATOS
                           |
                           v
                  CIENCIA DE DATOS
                     /     |      \
                    /      |       \
                   v       v        v
              CALIDAD   ÉTICA   INTELIGENCIA
               DATOS              ARTIFICIAL
                   \      |        /
                    \     |       /
                     v    v      v
                    INFORMACIÓN
                         |
                         v
                     DECISIÓN
                         |
                         v
                CONTEXTO PRODUCTIVO
```

---

## A. Ciencia de datos

La ciencia de datos es la rama de la ciencia que se encarga de extraer información de datos y utilizarla para tomar decisiones.

## B. Calidad de datos

La calidad de datos es la capacidad de los datos para ser confiables y útiles.

## C. Ética

La ética es la rama de la filosofía que estudia los principios morales y las normas que rigen la conducta humana.

## D. Ciclo de vida del dato

El ciclo de vida del dato permite organizar las diferentes etapas que se realizan desde la identificación de una pregunta hasta la toma de una decisión.

## Etapas

1. **Pregunta:** identificar qué se desea conocer.
2. **Fuente:** obtener los datos necesarios.
3. **Exploración:** revisar y comprender los datos.
4. **Calidad:** detectar errores, datos faltantes o inconsistencias.
5. **Análisis:** encontrar patrones y relaciones.
6. **Comunicación:** presentar los resultados.
7. **Acción:** utilizar los resultados para tomar decisiones.

---

## Aplicación al seguimiento académico

- **Pregunta:** Identificar qué aprendices podrían necesitar acompañamiento formativo.
- **Fuente:** Se pueden utilizar datos como asistencia, actividades, evidencias, calificaciones y observaciones.
- **Exploración:** Se revisan los porcentajes de asistencia, promedios y cantidad de evidencias entregadas.
- **Calidad:** Se verifican datos faltantes, valores fuera de rango, duplicados y posibles inconsistencias.
- **Análisis:** Se pueden comparar la asistencia, el promedio y las evidencias entregadas para identificar posibles situaciones que requieran acompañamiento.
- **Comunicación:** Los resultados pueden presentarse mediante tablas, informes o visualizaciones, evitando mostrar información personal innecesaria.
- **Acción:** Los resultados pueden utilizarse para realizar orientación, acompañamiento y seguimiento académico.
- **Ética:** Los datos académicos deben tratarse de forma responsable, protegiendo la privacidad de las personas y evitando etiquetas o discriminación.

---

## Conclusión general

La actividad de la Semana 1 permitió comprender que los datos son una herramienta fundamental para generar información y apoyar la toma de decisiones.

A través del diagnóstico se reforzaron conceptos relacionados con bases de datos, SQL, Python, JSON, manejo de archivos, fechas y seguridad de la información.

También se comprendió que la ciencia de datos combina diferentes conocimientos y herramientas para transformar datos en información útil. Sin embargo, el análisis no debe enfocarse únicamente en los aspectos técnicos, sino también en la calidad, el contexto y la ética.

Finalmente, el ciclo de vida del dato permite establecer un proceso ordenado para formular preguntas, obtener información, analizarla, comunicar resultados y tomar acciones responsables.

Por lo tanto, aprender ciencia de datos permite desarrollar habilidades importantes para el entorno académico y productivo, facilitando la solución de problemas mediante el uso responsable de la información.
