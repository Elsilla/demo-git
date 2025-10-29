def ingresar_datos():
    nombre = str(input("Indique su nombre: "))
    cargo = str(input("Indique su cargo: "))
    edad = int(input("Ingrese su edad: "))
    sueldo = float(input("Ingrese su sueldo: "))
    porcentaje = float(input("Ingrese el porcentaje de bono: "))
    return nombre, cargo, edad, sueldo, porcentaje

def menu():
    print("1. Ingresar datos del empleado")
    print("2. Calcular bono")
    print("3. Mostrar resumen")
    print("4. Salir")
# bono.py

def calcular_bono(sueldo, porcentaje):
    bono = sueldo * (porcentaje / 100)
    total = sueldo + bono
    return total

def mostrar_resumen(nombre, edad, cargo, total):

    #  imprime los datos del empleado y su sueldo con bono.
    print("Resumen del empleado:")
    print("Nombre:", nombre)
    print("Edad:", edad)
    print("Cargo:", cargo)
    print("Sueldo total con bono: ", total)

def mostrar_menu():
    """Muestra el menú de opciones."""
    print("\n--- Menú de Opciones del Sistema de Empleados ---")
    print("1. Ingresar datos del empleado")
    print("2. Calcular bono")
    print("3. Mostrar resumen")
    print("4. Salir")
    print("--------------------------------------------------")

def main():
    """Función principal del programa."""
    
    ejecutando = True 
    
    while ejecutando:
        mostrar_menu()
        
        
        opcion = input("Ingrese el número de la opción deseada (1-4): ")
        
        try:
            opcion = int(opcion)
        except ValueError:
            print("*Error*: Por favor, ingrese un número válido.")
            continue 

        if opcion == 1:
            print("\n*Opción 1 seleccionada*: Datos del empleado...")
            
        elif opcion == 2:
            print("\n*Opción 2 seleccionada*: calcular el bono...")
            
        elif opcion == 3:
            print("\n*Opción 3 seleccionada*: mostrar el resumen...")
            
        elif opcion == 4:
            print("\n*Opción 4 seleccionada*: Saliendo del sistema. ¡Hasta pronto! 👋")
            ejecutando = False 
            
        else:
        
            print(f"\n*Error*: Opción '{opcion}' no válida. Por favor, elija una opción entre 1 y 4.")

main()

