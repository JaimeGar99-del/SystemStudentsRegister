def calcular_promedio(estudiante):
    materias = estudiante["materias"]
    if not materias:
        return 0.0
    return sum(m["nota"] for m in materias) / len(materias)
 
 
def _imprimir_tabla(estudiantes):
    materias_unicas = []
    for estudiante in estudiantes:
        for m in estudiante["materias"]:
            if m["materia"] not in materias_unicas:
                materias_unicas.append(m["materia"])
 
    if not materias_unicas:
        print("Ningun estudiante tiene materias registradas.\n")
        return
    ancho_nombre = max(len(e["nombre"]) for e in estudiantes)
    ancho_nombre = max(ancho_nombre, len("Estudiante"))
    ancho_materia = max(len(m) for m in materias_unicas)
    ancho_materia = max(ancho_materia, 6)
    ancho_promedio = 10

    encabezado = f"{'Estudiante':<{ancho_nombre}}"
    for materia in materias_unicas:
        encabezado += f"  {materia:^{ancho_materia}}"
    encabezado += f"  {'Promedio':^{ancho_promedio}}"
    separador = "-" * len(encabezado)
 
    print(f"\n{separador}")
    print(encabezado)
    print(separador)

    for estudiante in estudiantes:
        notas = {m["materia"]: m["nota"] for m in estudiante["materias"]}
        fila = f"{estudiante['nombre']:<{ancho_nombre}}"
        for materia in materias_unicas:
            nota = notas.get(materia, "-")
            nota_str = f"{nota:.1f}" if isinstance(nota, float) else nota
            fila += f"  {nota_str:^{ancho_materia}}"
        promedio = calcular_promedio(estudiante)
        fila += f"  {promedio:^{ancho_promedio}.2f}"
        print(fila)
 
    print(f"{separador}\n")
 
 
def mostrar_informacion_estudiante(lista_estudiantes):
    if not lista_estudiantes:
        print("No hay estudiantes registrados.\n")
        return

    print("\n--- Lista de estudiantes ---")
    for i, est in enumerate(lista_estudiantes, 1):
        print(f"  {i}. {est['nombre']}")
    print()
 
    nombre_buscado = input("Ingrese el nombre del estudiante: ")
 
    for estudiante in lista_estudiantes:
        if estudiante["nombre"] == nombre_buscado:
            if not estudiante["materias"]:
                print(f"\n{estudiante['nombre']} no tiene materias registradas.\n")
                return
            _imprimir_tabla([estudiante])
            return
 
    print(f"Estudiante '{nombre_buscado}' no encontrado.\n")
 
 
def mostrar_todos(lista_estudiantes):
    if not lista_estudiantes:
        print("No hay estudiantes registrados.\n")
        return
    _imprimir_tabla(lista_estudiantes)
 
 
def mejor_estudiante(lista_estudiantes):
    con_materias = [e for e in lista_estudiantes if e["materias"]]
    if not con_materias:
        print("No hay estudiantes con materias registradas.\n")
        return
 
    mejor = max(con_materias, key=calcular_promedio)
    print(f"\n Mejor estudiante: {mejor['nombre']} con promedio {calcular_promedio(mejor):.2f}\n")