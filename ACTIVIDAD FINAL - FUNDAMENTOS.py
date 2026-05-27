# ============================================================
# Fundamentos de Programación - Fase 5
# Sistema: Videoteca Digital Inteligente
# Autor: Susan Nicolle Pesca Suarez
# Grupo: 213022
# Código fuente: Autoría propia
# ============================================================

peliculas = [
    ["Avatar", 2009, 8.0, "Ciencia ficción"],
    ["Avengers: Endgame", 2019, 8.4, "Superhéroes"],
    ["Avatar: El camino del agua", 2022, 7.6, "Ciencia ficción"],
    ["Titanic", 1997, 7.9, "Drama"],
    ["Star Wars: El despertar de la fuerza", 2015, 7.8, "Ciencia ficción"],
    ["Avengers: Infinity War", 2018, 8.4, "Superhéroes"],
    ["Spider-Man: No Way Home", 2021, 8.2, "Superhéroes"],
    ["Jurassic World", 2015, 6.9, "Aventura"],
    ["El Rey León", 2019, 6.8, "Animación"],
    ["Top Gun: Maverick", 2022, 8.2, "Acción"],
    ["Barbie", 2023, 6.8, "Comedia"],
    ["Interestellar", 2014, 8.7, "Ciencia ficción"]
]

generos = [
    "Ciencia ficción",
    "Superhéroes",
    "Drama",
    "Aventura",
    "Animación",
    "Acción",
    "Comedia"
]


def mostrar_logo():
    print("""
██╗   ██╗██╗██████╗ ███████╗ ██████╗ ████████╗███████╗ ██████╗ █████╗
██║   ██║██║██╔══██╗██╔════╝██╔═══██╗╚══██╔══╝██╔════╝██╔════╝██╔══██╗
██║   ██║██║██║  ██║█████╗  ██║   ██║   ██║   █████╗  ██║     ███████║
╚██╗ ██╔╝██║██║  ██║██╔══╝  ██║   ██║   ██║   ██╔══╝  ██║     ██╔══██║
 ╚████╔╝ ██║██████╔╝███████╗╚██████╔╝   ██║   ███████╗╚██████╗██║  ██║
  ╚═══╝  ╚═╝╚═════╝ ╚══════╝ ╚═════╝    ╚═╝   ╚══════╝ ╚═════╝╚═╝  ╚═╝

██████╗ ██╗ ██████╗ ██╗████████╗ █████╗ ██╗
██╔══██╗██║██╔════╝ ██║╚══██╔══╝██╔══██╗██║
██║  ██║██║██║  ███╗██║   ██║   ███████║██║
██║  ██║██║██║   ██║██║   ██║   ██╔══██║██║
██████╔╝██║╚██████╔╝██║   ██║   ██║  ██║███████╗
╚═════╝ ╚═╝ ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝
""")
    print("============================================================")
    print("              SISTEMA DE VIDEOTECA DIGITAL")
    print("============================================================")


def leer_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            numero = int(input(mensaje))

            if minimo is not None and numero < minimo:
                print(f"Error: el valor debe ser mayor o igual a {minimo}.")
                continue

            if maximo is not None and numero > maximo:
                print(f"Error: el valor debe ser menor o igual a {maximo}.")
                continue

            return numero

        except ValueError:
            print("Error: debe ingresar un número entero válido.")


def leer_decimal(mensaje, minimo=None, maximo=None):
    while True:
        try:
            numero = float(input(mensaje))

            if minimo is not None and numero < minimo:
                print(f"Error: el valor debe ser mayor o igual a {minimo}.")
                continue

            if maximo is not None and numero > maximo:
                print(f"Error: el valor debe ser menor o igual a {maximo}.")
                continue

            return numero

        except ValueError:
            print("Error: debe ingresar un número válido.")


def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Ver catálogo completo")
    print("2. Buscar películas por género")
    print("3. Buscar películas por calificación mínima")
    print("4. Contar películas populares y recientes")
    print("5. Mostrar estadísticas")
    print("6. Salir")


def imprimir_tabla(lista_peliculas):
    if len(lista_peliculas) == 0:
        print("\nNo se encontraron películas con los criterios ingresados.")
        return

    print("\n" + "=" * 95)
    print(f"{'N°':<5}{'Título':<42}{'Año':<8}{'Calificación':<15}{'Género':<20}")
    print("=" * 95)

    for i, pelicula in enumerate(lista_peliculas, start=1):
        titulo = pelicula[0]
        anio = pelicula[1]
        calificacion = pelicula[2]
        genero = pelicula[3]

        print(f"{i:<5}{titulo:<42}{anio:<8}{calificacion:<15}{genero:<20}")

    print("=" * 95)


def mostrar_catalogo():
    print("\nCATÁLOGO COMPLETO DE LA VIDEOTECA")
    imprimir_tabla(peliculas)


def seleccionar_genero():
    print("\n========== GÉNEROS DISPONIBLES ==========")

    for i, genero in enumerate(generos, start=1):
        print(f"{i}. {genero}")

    opcion = leer_entero("Seleccione el género por número: ", 1, len(generos))
    return generos[opcion - 1]


def buscar_por_genero():
    genero_seleccionado = seleccionar_genero()
    resultados = []

    for pelicula in peliculas:
        if pelicula[3] == genero_seleccionado:
            resultados.append(pelicula)

    print(f"\nPelículas encontradas del género: {genero_seleccionado}")
    imprimir_tabla(resultados)


def buscar_por_calificacion():
    calificacion_minima = leer_decimal(
        "Ingrese la calificación mínima a consultar (1.0 a 10.0): ",
        1.0,
        10.0
    )

    resultados = []

    for pelicula in peliculas:
        if pelicula[2] >= calificacion_minima:
            resultados.append(pelicula)

    print(f"\nPelículas con calificación mayor o igual a {calificacion_minima}")
    imprimir_tabla(resultados)


def contar_populares_recientes(lista_peliculas, anio_limite, calificacion_minima):
    resultados = []

    for pelicula in lista_peliculas:
        anio = pelicula[1]
        calificacion = pelicula[2]

        if calificacion >= calificacion_minima and anio >= anio_limite:
            resultados.append(pelicula)

    return resultados


def consultar_populares_recientes():
    print("\n========== CONSULTA DE PELÍCULAS POPULARES Y RECIENTES ==========")

    anio_limite = leer_entero(
        "Ingrese el año mínimo de lanzamiento (1900 a 2026): ",
        1900,
        2026
    )

    calificacion_minima = leer_decimal(
        "Ingrese la calificación mínima (1.0 a 10.0): ",
        1.0,
        10.0
    )

    resultados = contar_populares_recientes(
        peliculas,
        anio_limite,
        calificacion_minima
    )

    print("\nRESULTADO DE LA CONSULTA")
    print(f"Año mínimo: {anio_limite}")
    print(f"Calificación mínima: {calificacion_minima}")
    print(f"Cantidad de títulos que cumplen ambos criterios: {len(resultados)}")

    imprimir_tabla(resultados)


def mostrar_estadisticas():
    total_peliculas = len(peliculas)
    suma_calificaciones = 0
    mejor_pelicula = peliculas[0]

    for pelicula in peliculas:
        suma_calificaciones += pelicula[2]

        if pelicula[2] > mejor_pelicula[2]:
            mejor_pelicula = pelicula

    promedio = suma_calificaciones / total_peliculas

    print("\n========== ESTADÍSTICAS DE LA VIDEOTECA ==========")
    print(f"Total de películas registradas: {total_peliculas}")
    print(f"Promedio general de calificaciones: {promedio:.2f}")
    print(f"Película mejor calificada: {mejor_pelicula[0]} ({mejor_pelicula[2]})")

    print("\nCantidad de películas por género:")
    print("-" * 45)
    print(f"{'Género':<25}{'Cantidad':<10}")
    print("-" * 45)

    for genero in generos:
        contador = 0

        for pelicula in peliculas:
            if pelicula[3] == genero:
                contador += 1

        print(f"{genero:<25}{contador:<10}")

    print("-" * 45)


def ejecutar_sistema():
    mostrar_logo()

    while True:
        mostrar_menu()
        opcion = leer_entero("Seleccione una opción (1-6): ", 1, 6)

        if opcion == 1:
            mostrar_catalogo()

        elif opcion == 2:
            buscar_por_genero()

        elif opcion == 3:
            buscar_por_calificacion()

        elif opcion == 4:
            consultar_populares_recientes()

        elif opcion == 5:
            mostrar_estadisticas()

        elif opcion == 6:
            print("\nGracias por utilizar el Sistema de Videoteca Digital.")
            break


if __name__ == "__main__":
    ejecutar_sistema()