  # Versión simple usando variables, condicionales, input y ciclos
estudiantes = 5
suma = 0.0
mejor_nombre = ""
mejor_cal = -1.0
peor_nombre = ""
peor_cal = 6.0

for i in range(estudiantes):
    print("\n--- Estudiante " + str(i+1) + " ---")
    nombre = input("Nombre: ").strip()
    while nombre == "":
        print("Nombre inválido. Intenta de nuevo.")
        nombre = input("Nombre: ").strip()

    # Validar edad (entero entre 5 y 100)
    while True:
        edad_str = input("Edad (5-100): ")
        if edad_str.isdigit():
            edad = int(edad_str)
            if 5 <= edad <= 100:
                break
            else:
                print("Edad inválida. Debe estar entre 5 y 100.")
        else:
            print("Ingresa un número entero para la edad.")

    # Validar calificación (número entre 0 y 5)
    while True:
        cal_str = input("Calificación (0-5): ")
        # permitir números con punto (ej. 4.5)
        try:
            cal = float(cal_str.replace(',','.'))
            if 0.0 <= cal <= 5.0:
                break
            else:
                print("Calificación inválida. Debe estar entre 0 y 5.")
        except:
            print("Ingresa un número para la calificación.")

    suma = suma + cal

    if cal > mejor_cal:
        mejor_cal = cal
        mejor_nombre = nombre
    if cal < peor_cal:
        peor_cal = cal
        peor_nombre = nombre

promedio = suma / estudiantes

print("\nResultados:")
print("Mejor calificación: " + mejor_nombre + " -> " + str(mejor_cal))
print("Peor calificación: " + peor_nombre + " -> " + str(peor_cal))
print("Calificación promedio: " + str(round(promedio,2)))

