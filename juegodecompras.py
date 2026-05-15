import time


def tiendaGamer(nombre, precio, descuento):

    # Descuento
    rebaja = precio * descuento / 100

    # Precio final con descuento
    final = precio - rebaja
    print(f"\n\nEl precio original de la tarjeta de video: {nombre} es de ${precio}")
    print(f"Con un descuento del {descuento}%, el precio final es de: ${final}")



while True:

    entrada = input("Presiona « x » para continuar (o escribe « salir » para finalizar): ")

    if entrada == "salir":
        print("Fin del programa")
        break
    elif entrada == "x":


        tiendaGamer("\n1) NVIDIA GeForce RTX 4090", 1599, 20)
        tiendaGamer("\n2) AMD Radeon RX 7900 XTX", 999, 15)
        tiendaGamer("\n3) NVIDIA GeForce RTX 4080", 1199, 10)
    
        compra = (input("\nSí desea comprar un producto disponible, ingrese el numero correspodiente al producto: "))
        if compra == "1":
                print("Realizando compra")
                time.sleep(1)
                print("Compra realizada con exito")
                break
            
        elif compra == "2":
                 print("Realizando compra")
                 time.sleep(1)
                 print("Compra realizada con exito")
                 break
            
        elif compra == "3":
                 print("Realizando compra")
                 time.sleep(1)
                 print("Compra realizada con exito")
                 break
            
        else:
            print("Número de producto inválido. Ingrese el numero correcto del producto: ")
            continue

    else:
        print("ERROR 404, ejecute nuevamente el programa.")
        break
