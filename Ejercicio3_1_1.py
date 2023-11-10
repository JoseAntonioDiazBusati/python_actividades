"""
Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
"""
def AsignaturasTotales():
    asignatura=("Matematicas","Fisica","Quimica","Historia","Lengua")
    return asignatura

def main():
    asignatura=AsignaturasTotales()
    for tema in asignatura:
        print(tema)

if __name__=="__main__":
    main()