def registrar_materias(lista_estudiantes):
    if not lista_estudiantes:
        print("No hay estudiantes registrados.\n")
        return

    print("¿A quién desea registrarle materias?")
    print("  1. A un estudiante específico")
    print("  2. A todos los estudiantes")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        print("\n--- Lista de estudiantes ---")
        for i, est in enumerate(lista_estudiantes, 1):
            print(f"  {i}. {est['nombre']}")
        print()

        nombre_buscado = input("Nombre del estudiante: ").strip()
        for estudiante in lista_estudiantes:
            if estudiante["nombre"] == nombre_buscado:
                _registrar_materias_a_estudiante(estudiante)
                return
        print(f"Estudiante '{nombre_buscado}' no encontrado.\n")

    elif opcion == "2":
        materias_existentes = []
        for estudiante in lista_estudiantes:
            if estudiante["materias"]:
                materias_existentes = [m["materia"] for m in estudiante["materias"]]
                break

        minimo = len(materias_existentes)
        try:
            if minimo > 0:
                print(f"\nYa hay {minimo} materia(s) registrada(s): {', '.join(materias_existentes)}")
                cantidad = int(input(f"¿Cuántas materias en total? (mínimo {minimo}): "))
                if cantidad < minimo:
                    print(f"Debe ingresar al menos {minimo} materia(s).\n")
                    return
            else:
                cantidad = int(input("¿Cuántas materias desea registrar? "))
                if cantidad <= 0:
                    print("Debe ingresar un número mayor a 0.\n")
                    return
        except ValueError:
            print("Ingrese un número válido.\n")
            return

        nombres_materias = materias_existentes[:]
        for i in range(len(materias_existentes) + 1, cantidad + 1):
            nombre_materia = input(f"  Nombre de la materia {i}: ").strip()
            if not nombre_materia:
                print("El nombre no puede estar vacío. Se omitió esta materia.")
                continue
            nombres_materias.append(nombre_materia)

        for estudiante in lista_estudiantes:
            print(f"\n--- Notas para: {estudiante['nombre']} ---")
            notas_existentes = {m["materia"] for m in estudiante["materias"]}
            for nombre_materia in nombres_materias:
                if nombre_materia in notas_existentes:
                    print(f"  • '{nombre_materia}' ya registrada, se omite.")
                    continue
                nota = _pedir_nota(nombre_materia)
                estudiante["materias"].append({"materia": nombre_materia, "nota": nota})
            print(f"Materias actualizadas para {estudiante['nombre']}.\n")

    else:
        print("Opción no válida.\n")


def _pedir_nota(nombre_materia):
    nota = -1
    while not (0 <= nota <= 5):
        try:
            nota = float(input(f"  Nota de '{nombre_materia}' (0 - 5): "))
            if not (0 <= nota <= 5):
                print("La nota debe estar entre 0 y 5.\n")
        except ValueError:
            print("Ingrese un número válido (ejemplo: 3.5).\n")
    return nota


def _registrar_materias_a_estudiante(estudiante):
    try:
        cantidad = int(input(f"¿Cuántas materias desea registrar para {estudiante['nombre']}? "))
        if cantidad <= 0:
            print("Debe ingresar un número mayor a 0.\n")
            return
    except ValueError:
        print("Ingrese un número válido.\n")
        return

    for i in range(1, cantidad + 1):
        nombre_materia = input(f"  Materia {i}: ").strip()
        if not nombre_materia:
            print(" Nombre vacío, se omitió esta materia.")
            continue
        nota = _pedir_nota(nombre_materia)
        estudiante["materias"].append({"materia": nombre_materia, "nota": nota})
        print(f" '{nombre_materia}' con nota {nota} guardada.\n")