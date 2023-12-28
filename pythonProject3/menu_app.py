def agregar_compra(lista_compras):
 compra_nueva = int(input("INGRESE MONTO DE LA COMPRA: "))
 lista_compras.append(compra_nueva)
 print("SE HA INGRESADO LA COMPRA CORRECTAMENTE.")

def mostrar_compras(lista_compras):
    if len(lista_compras) > 0:
        for idx, tarea in enumerate(lista_compras, start=1):
            print(f"{idx}. ${tarea}.00  ")
    else:
        print("NO HAY COMPRAS REALIZADAS")
def mostrar_total(lista_compras):
    total_gastado=0
    for x in lista_compras:
        total_gastado = total_gastado + x
    print(f"LA SUMA TOTAL DE LO GASTADO ES: ${total_gastado}.00")
def main():
    lista_compras = []
    while True:
     print("Menú:")
     print("1. AGREGAR COMPRA")
     print("2. MOSTRAR COMPRAS")
     print("3. MOSTRAR TOTAL GASTADO")
     print("4. SALIR")
     opcion = input("Seleccione una opción: ")

     if opcion == "1":
        agregar_compra(lista_compras)
        print("")
     elif opcion == "2":
        mostrar_compras(lista_compras)
        print("")
     elif opcion == "3":
        mostrar_total(lista_compras)
        print("")
     elif opcion == "4":
        print("FIN DEL PROGRAMA.")
        break
     else:
        print("OPCION NO VALIDA, INTENTE DE NUEVO.")
        print("")
main()