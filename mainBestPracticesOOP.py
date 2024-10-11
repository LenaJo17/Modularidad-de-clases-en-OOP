# Importamos la clase Alumno desde claseBestPracticesOOP.py
# Importamos la clase desde el archivo mi_clase.py
from mi_clase import MiClase
from  claseAlumno import Alumno

from claseBestPracticesOOP import  Alumno
#Diccionario para almacenar los alumnos
alumnos_dict = {}

# Bucle para ingresar 3 alumnos desde teclado
for i in range(3):
    alumno = Alumno()  # Crear un objeto Alumno vacío

    # Ingresar datos por teclado
    nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
    apellido_paterno = input(f"Ingrese el apellido paterno del alumno {i + 1}: ")
    apellido_materno = input(f"Ingrese el apellido materno del alumno {i + 1}: ")
    no_control = input(f"Ingrese el número de control del alumno {i + 1}: ")
    semestre = int(input(f"Ingrese el semestre del alumno {i + 1}: "))

    # Asignar valores a los atributos usando los métodos set
    alumno.set_nombre(nombre)
    alumno.set_apellido_paterno(apellido_paterno)
    alumno.set_apellido_materno(apellido_materno)
    alumno.set_no_control(no_control)
    alumno.set_semestre(semestre)

    # Guardar el objeto alumno en el diccionario
    alumnos_dict[alumno.get_no_control()] = alumno

# Verificar los alumnos almacenados
print("\n--- Lista de Alumnos ---")
for no_control, alumno in alumnos_dict.items():
    print(f"Nombre: {alumno.get_nombre()} " )