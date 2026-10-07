# A2 - Modelos de bases de datos NoSQL

## Introducción

Las bases de datos NoSQL son sistemas de almacenamiento de información
que no utilizan necesariamente el modelo tradicional de tablas,
filas y columnas propio de las bases de datos relacionales.

Estos sistemas permiten trabajar con diferentes estructuras de datos
y ofrecen alternativas flexibles para almacenar información,
especialmente cuando se manejan grandes volúmenes de datos o
información que puede cambiar con frecuencia.

En esta actividad se estudian los principales modelos de bases de
datos NoSQL, sus características, ventajas, desventajas y algunos
ejemplos de sistemas que utilizan cada modelo.

## 1. Modelo orientado a documentos

### ¿Qué es?

El modelo orientado a documentos almacena la información en
documentos, generalmente utilizando formatos como JSON, BSON o XML.

A diferencia de una base de datos relacional, la información no tiene
que estar organizada en tablas relacionadas entre sí. Cada documento
puede contener diferentes campos y estructuras, dependiendo de las
necesidades de la información que se desea almacenar.

### ¿Cómo almacena los datos?

Los datos se almacenan como documentos. Un documento puede contener
información organizada mediante pares clave-valor y también puede
incluir listas, objetos anidados y diferentes tipos de datos.

Por ejemplo:

```json
{
  "nombre": "Ana",
  "edad": 25,
  "programa": "Análisis y Desarrollo de Software",
  "habilidades": [
    "Python",
    "Bases de datos",
    "Git"
  ]
}

## 2. Modelo clave-valor

### ¿Qué es?

El modelo clave-valor almacena la información mediante pares formados
por una clave y un valor.

La clave permite identificar un dato específico, mientras que el valor
contiene la información asociada a esa clave.

Este modelo es uno de los más sencillos dentro de las bases de datos
NoSQL y está diseñado para realizar operaciones rápidas de lectura y
escritura.

### ¿Cómo almacena los datos?

La información se organiza mediante pares:

```text
clave → valor
## 3. Modelo orientado a grafos

### ¿Qué es?

El modelo orientado a grafos representa la información mediante
entidades y las relaciones existentes entre ellas.

En este modelo se utilizan principalmente dos elementos:

- **Nodos:** representan las entidades o elementos de información.
- **Relaciones o aristas:** representan las conexiones entre los nodos.

Este modelo es especialmente útil cuando las relaciones entre los
datos son tan importantes como los datos mismos.

### ¿Cómo almacena los datos?

La información se representa mediante nodos conectados por relaciones.

Por ejemplo, en una red social:

```text
Ana ── es amiga de ── Carlos
 │
 └── sigue a ── María
 ## 4. Modelo orientado a columnas

### ¿Qué es?

El modelo orientado a columnas organiza y almacena la información
agrupándola por columnas en lugar de organizarla únicamente mediante
filas como ocurre tradicionalmente en las bases de datos relacionales.

Este modelo está diseñado para trabajar con grandes cantidades de
información y puede distribuir los datos entre diferentes servidores.

Es especialmente utilizado en escenarios donde se necesitan realizar
consultas y análisis sobre grandes volúmenes de datos.

### ¿Cómo almacena los datos?

La información se organiza en familias de columnas. En lugar de
almacenar necesariamente todos los campos de un registro juntos, los
datos pueden organizarse agrupando columnas relacionadas.

Un ejemplo conceptual sería:

```text
Usuarios

Columna: nombre
----------------
Ana
Carlos
María

Columna: edad
----------------
25
30
28

Columna: programa
----------------
ADSO
ADSO
ADSO

## 5. Comparación de los modelos NoSQL

La siguiente tabla permite comparar las principales características de
los cuatro modelos estudiados:

| Modelo | Forma de almacenar los datos | Principal característica | Ejemplos | Usos comunes |
|---|---|---|---|---|
| Documentos | Documentos JSON, BSON o XML | Estructura flexible | MongoDB, CouchDB | Catálogos, perfiles, contenido |
| Clave-valor | Pares clave-valor | Acceso rápido mediante una clave | Redis, DynamoDB | Caché, sesiones, carritos |
| Grafos | Nodos y relaciones | Representación de conexiones | Neo4j, Neptune | Redes sociales, recomendaciones, fraude |
| Columnas | Familias de columnas | Manejo de grandes volúmenes de datos | Cassandra, HBase | Sistemas distribuidos y análisis de datos |

### Diferencias principales

Cada modelo NoSQL está diseñado para resolver diferentes tipos de
problemas:

- **Documentos:** es adecuado cuando la información tiene una
  estructura flexible y puede contener objetos o listas anidadas.

- **Clave-valor:** es apropiado cuando se necesita recuperar
  rápidamente información utilizando una clave.

- **Grafos:** es recomendable cuando las relaciones entre los datos
  son fundamentales para el funcionamiento de la aplicación.

- **Columnas:** es útil para sistemas distribuidos que necesitan
  trabajar con grandes cantidades de información.
  