from registerstudents import registrar_estudiante, mostrar_estudiante
from registermateriasynotas import registrar_materias
from showstudentsinformation import mostrar_informacion_estudiante, mostrar_todos, mejor_estudiante
 
lista_estudiantes = []
 
def menu():
    opciones = {
        "1": ("Registrar estudiante",            lambda: registrar_estudiante(lista_estudiantes)),
        "2": ("Mostrar lista de estudiantes",     lambda: mostrar_estudiante(lista_estudiantes)),
        "3": ("Registrar materias y notas",       lambda: registrar_materias(lista_estudiantes)),
        "4": ("Ver información de un estudiante", lambda: mostrar_informacion_estudiante(lista_estudiantes)),
        "5": ("Ver información completa",         lambda: mostrar_todos(lista_estudiantes)),
        "6": ("Encontrar al mejor estudiante",    lambda: mejor_estudiante(lista_estudiantes)),
        "0": ("Salir", None),
    }
 
    opcion = ""
    while opcion != "0":
        try:
            print("========== Menú Principal ==========")
            for clave, (descripcion, _) in opciones.items():
                print(f"  {clave}. {descripcion}")
            print("=====================================")
 
            opcion = input("Seleccione una opción: ").strip()
 
            if opcion == "0":
                print("¡Hasta luego!")
            elif opcion in opciones:
                _, funcion = opciones[opcion]
                print()
                funcion()
            else:
                print("Opción no válida. Intente de nuevo.\n")
 
        except KeyboardInterrupt:
            print("\n\n¡Hasta luego!")
            opcion = "0"
        except Exception as e:
            print(f"\nOcurrió un error inesperado: {e}")
            print("El programa continúa funcionando.\n")
 
if __name__ == "__main__":
    menu()