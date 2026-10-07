# 3.5 Caso integrador inicial

## Introducción

El análisis de datos puede utilizarse para apoyar diferentes procesos
de una organización. En este caso se plantea una situación relacionada
con el seguimiento académico de aprendices.

La información disponible incluye datos de asistencia, actividades
realizadas, evidencias entregadas y observaciones. A partir de estos
datos se pueden formular preguntas que permitan identificar situaciones
que requieran atención.

## 1. Descripción del caso

Un programa de formación desea realizar un seguimiento del desempeño
académico de sus aprendices. Para ello dispone de información relacionada
con la asistencia, el promedio de actividades, las evidencias
entregadas y las observaciones realizadas durante el proceso formativo.

El objetivo inicial es utilizar estos datos para identificar posibles
dificultades y generar información que facilite el acompañamiento
formativo.

## 2. Variables disponibles

| Variable | Descripción |
| --- | --- |
| **id_aprendiz** | Identificador único del aprendiz. |
| **ficha** | Número o código de la ficha de formación. |
| **asistencia_porcentaje** | Porcentaje de asistencia del aprendiz. |
| **promedio_actividades** | Promedio obtenido en las actividades realizadas. |
| **evidencias_entregadas** | Cantidad de evidencias entregadas por el aprendiz. |
| **observacion** | Comentario relacionado con el proceso formativo. |

## 3. Preguntas analíticas

### Pregunta 1

¿Qué aprendices presentan un porcentaje de asistencia inferior al 70%?

Esta pregunta permite identificar posibles casos que requieren
seguimiento debido a una baja asistencia.

### Pregunta 2

¿Qué aprendices tienen un promedio de actividades inferior a 3.0?

Esta pregunta permite identificar aprendices que pueden presentar
dificultades en el desarrollo de las actividades formativas.

### Pregunta 3

¿Qué aprendices tienen pocas evidencias entregadas?

Esta pregunta permite identificar posibles retrasos en la entrega de
las actividades y evidencias solicitadas.

### Pregunta 4

¿Existe una relación entre el porcentaje de asistencia y el promedio de
actividades?

Esta pregunta busca analizar si los aprendices con menor asistencia
también presentan un menor desempeño en las actividades.

### Pregunta 5

¿Qué aprendices presentan simultáneamente baja asistencia, bajo
promedio y pocas evidencias entregadas?

Esta pregunta permite identificar situaciones que podrían requerir un
acompañamiento prioritario.

## 4. Posibles indicadores

Para realizar un seguimiento inicial pueden utilizarse los siguientes
indicadores:

| Indicador | Descripción |
| --- | --- |
| **Promedio de asistencia** | Permite conocer el nivel general de asistencia del grupo. |
| **Promedio de actividades** | Permite observar el desempeño académico general. |
| **Cantidad de evidencias entregadas** | Permite conocer el nivel de cumplimiento de las actividades. |
| **Aprendices con asistencia baja** | Cantidad de aprendices con asistencia inferior al 70%. |
| **Aprendices con desempeño bajo** | Cantidad de aprendices con promedio inferior a 3.0. |

## 5. Posibles decisiones

A partir de los resultados obtenidos se podrían tomar decisiones como:

- Realizar seguimiento individual a los aprendices con baja asistencia.
- Orientar a los aprendices que presenten dificultades académicas.
- Revisar las causas de las evidencias pendientes.
- Establecer acciones de acompañamiento formativo.
- Realizar un nuevo seguimiento después de aplicar las acciones de
  mejora.

Las decisiones deben basarse en información suficiente y no únicamente
en un indicador aislado.

## 6. Ética y uso responsable de los datos

Los datos utilizados para el seguimiento académico deben manejarse de
forma responsable. El identificador del aprendiz y cualquier otra
información personal deben protegerse y utilizarse únicamente para los
fines establecidos.

Los resultados no deben utilizarse para etiquetar o discriminar a los
aprendices. El análisis debe servir como apoyo para identificar
necesidades y establecer acciones de acompañamiento.

## 7. Reflexión

El caso demuestra que los datos pueden convertirse en una herramienta
para comprender situaciones del entorno académico. Formular preguntas
antes de analizar la información permite definir mejor qué se quiere
conocer y qué decisiones podrían tomarse posteriormente.

También es importante recordar que los resultados de un análisis deben
interpretarse dentro de su contexto y utilizarse de manera responsable.

## 8.  Conclusión

El seguimiento académico mediante datos permite identificar posibles
dificultades y generar información útil para apoyar a los aprendices.

La formulación de preguntas analíticas constituye un primer paso para
desarrollar procesos de análisis de datos y posteriormente utilizar
herramientas como Python para procesar, analizar y visualizar la
información.
