def registrar_estudiante(lista_estudiantes):
    try:
        cantidad = int(input("¿Cuántos estudiantes desea registrar? "))
        if cantidad <= 0:
            print("Debe ingresar un número mayor a 0.\n")
            return
    except ValueError:
        print("Ingrese un número válido.\n")
        return
 
    for i in range(1, cantidad + 1):
        nombre = input(f"Nombre del estudiante {i}: ").strip()
        if not nombre:
            print("El nombre no puede estar vacío. Se omitió este estudiante.\n")
            continue
        lista_estudiantes.append({"nombre": nombre, "materias": []})
        print(f"Estudiante '{nombre}' registrado correctamente.\n")
 
    print(f"{cantidad} estudiante(s) procesado(s).\n")
 
 
def mostrar_estudiante(lista_estudiantes):
    if not lista_estudiantes:
        print("No hay estudiantes registrados.\n")
        return
    print("\n--- Lista de estudiantes registrados ---")
    for i, est in enumerate(lista_estudiantes, 1):
        print(f"  {i}. {est['nombre']}")
    print()