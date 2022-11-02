# Lab4
## Integrantes

* Maria Paula Gonzalez Escallon 
* Jessica Alejandra Robles Moreno
* Juan Esteban Vergara Ascencio

## Las pruebas realizadas en postman se encuentran en la carpeta JSON-Endpoints

### Despliegue API:

-Desde cmd sobre la carpeta lab4 donde se encuentra el laboratorio del grupo 15 ejecute el comando: uvicorn main:app --reload

-En el navegador de preferencia ingrese a: http://127.0.0.1:8000/docs

-En la pagina abierta previamente encontrara los 2 metodos GET predeterminados y los metodos POST de los enpoints 1 y 2

### Ejecución endpoint 1

-Para hacer peticiones POST del endpoint 1 se debe desplegar previamente la API: Pueden hacerse las pruebas a traves de la interfaz de navegador de fastAPI o desde el programa POSTMAN creando peticiones

-(Para postman):Se debe crear una colección dentro del programa para almacenar las peticiones, dentro de la colección crear una nueva petición.

-(Para postman):Se debe cambia ekl tipo de petición de GET a POST (se coloca GET como predeterminado) y se coloca la ruta: http://127.0.0.1:8000/predict

-En el cuerpo de la petición (en la secciómn Body de Postman) se elige entrada de texto tipo JSON y se copia texto con el siguiente formato JSON:

Ejemplo:

{
    "list_of_inputs": [
        {
            "serial_no": 0,
            "gre_score": 327.0,
            "toefl_score": 113.0,
            "University Rating": 4.0,
            "sop": 4.0,
            "lor": 0.0,
            "CGPA": 8.88,
            "Research": 1.0
        },
        {
            "serial_no": 0,
            "gre_score": 327.0,
            "toefl_score": 113.0,
            "University Rating": 4.0,
            "sop": 4.0,
            "lor": 0.0,
            "CGPA": 8.88,
            "Research": 1.0
        }
    ]
}

-Envia la petición y espera el resultado (puede tardar un poco con volumenes grandes de datos), se retorna en el mismo orden en el que se ingresaron los registros a traves de una lista JSON "result"

-Para hacer pruebas se uso el archivo data.json que se encuentra en el repositorio, que contiene alrededor de 1400 registros sin la columna "Admission Points" en el formato JSON que se mostro previamente. Se puede ingresar este texto a la petición para probar. 

### Ejecución Endpoint 2

-Para hacer peticiones POST del endpoint 2 se debe desplegar previamente la API: Pueden hacerse las pruebas a traves de la interfaz de navegador de fastAPI o desde el programa POSTMAN creando peticiones

-(Para postman):Se debe crear una colección dentro del programa para almacenar las peticiones, dentro de la colección crear una nueva petición.

-(Para postman):Se debe cambia el tipo de petición de GET a POST (se coloca GET como predeterminado) y se coloca la ruta: http://127.0.0.1:8000/newData

-En el cuerpo de la petición (en la secciómn Body de Postman) se elige entrada de texto tipo JSON y se copia texto con el siguiente formato JSON:

Ejemplo:

{
    "list_of_inputs": [
        {
            "serial_no": 0,
            "gre_score": 327.0,
            "toefl_score": 113.0,
            "University Rating": 4.0,
            "sop": 4.0,
            "lor": 0.0,
            "CGPA": 8.88,
            "Research": 1.0,
            "Admission Points": 64.0
        },
        {
            "serial_no": 0,
            "gre_score": 327.0,
            "toefl_score": 113.0,
            "University Rating": 4.0,
            "sop": 4.0,
            "lor": 0.0,
            "CGPA": 8.88,
            "Research": 1.0,
            "Admission Points": 64.0
        }
    ]
}

-Envia la petición y espera el resultado (Para que funcione, deben ser minimo 2 registros, ya que no puede sacar raiz del error cuadratico medio con un solo registro), se retorna los valores "RMSE" y "R^2".

-Para hacer pruebas se uso el archivo data2.json que se encuentra en el repositorio, que contiene alrededor de 1400 registros en el formato JSON que se mostro previamente. Se puede ingresar este texto a la petición para probar
