# Orquestadores

Vamos a revisar las opciones de orquestación que tenemos en Python, incluyendo orquestación que emplea los recursos del sistema informacional ([dbt](https://www.getdbt.com/) y entornos de calidad de datos ([soda](https://docs.soda.io/integrate-soda/integrate-dbt)).

Es importante hacer una distinción entre orquestación y planificación. Por planificación nos referimos a que una ejecución se realice en un momento dado o bajo una orden concreta (llamada API). Por orquestación nos referimos a la concatenación de eventos con lógicas de reintento y bifurcaciones en base a lo acontecido en los elementos anteriores del flujo.

Si bien los procesos [cron](https://es.wikipedia.org/wiki/Cron_(Unix)) han sido la estrella omnipresente de la planificación, poco a poco otros sistemas han ido tomando el relevo. 

[Control-M](https://www.bmcsoftware.es/it-solutions/control-m.html) es una de los opciones más usuales para gran empresa, mientras que [Apache Airflow](https://airflow.apache.org/) es la solución más usual en el mundo de la pequeña empresa y empresa orientada al _open source_. Con la proliferación de procesos de datos y analítica, opciones alternativas han tomado el relevo otras soluciones que mantienen la filosofía de Airflow de definición basada en código.

## Dagster

[Dagster](https://dagster.io/) es un orquestador moderno diseñado específicamente para flujos de datos. Destaca por su facilidad de uso, capacidad de testing, y monitorización de datos. Su principal ventaja es la integración nativa con herramientas de analítica como Pandas, dbt y Spark.

Características principales:
- Desarrollo local con UI integrada
- Testing y debugging avanzado
- Gestión de dependencias entre tareas
- Monitorización de datos y linaje
- Soporte para contenedores y cloud

Un ejemplo sencillo de cómo podemos definir estos flujos de datos basados en código, ess el siguiente:
```python
from dagster import job, op

@op
def get_data():
    return [1, 2, 3]

@op
def process_data(data):
    return [x * 2 for x in data]

@op
def display_results(results):
    print(f"Processed data: {results}")

@job
def basic_etl():
    data = get_data()
    processed = process_data(data)
    display_results(processed)
```

Este workflow simple define 3 operaciones conectadas en un job: obtener datos, procesarlos y mostrar resultados.

## Mage

[Mage.ai](https://www.mage.ai/) es una herramienta moderna de orquestación de datos que se centra en la construcción y gestión de pipelines de datos. Destaca por su interfaz visual intuitiva y su capacidad para transformar datos usando Python, SQL, y R.

Características principales:
- Interfaz visual para diseño de pipelines
- Soporte para múltiples lenguajes
- Integración con fuentes de datos comunes
- Gestión de calidad de datos
- Monitorización en tiempo real

Este ejemplo muestra un pipeline simple que carga datos, aplica transformaciones y realiza validaciones básicas. Mage ofrece además multitud de opciones para guardar artefactos como modelos, versionar los pipelines y editarlos siguiendo una operativa similar a la de los notebooks.

## DBT

Al igual que otras soluciones, es la opción _code first_ que nos permite versionar las transformaciones de datos impuestas sobre el sistema informacional. Su sintaxis no deja de ser una especificación en SQL de las transformaciones a realizar, sin embargo gracias a plantillas `jinja` nos permite realizar macros que facilitan mucho la tarea. Cuenta con un elenco de paquetes que extienden su funcionalidad aunque permite implementar de base controles de calidad y tests sobre las transformaciones de forma que nos alerte de transformaciones con resultado inesperado.

Podemos tomar como ejemplo este repositorio https://github.com/mage-ai/dbt-quickstart que nos permite evaluar de forma sencilla el uso conjunto de Mage junto con dbt.