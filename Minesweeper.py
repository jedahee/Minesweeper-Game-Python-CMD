#OUTPUT
#0 1 2 3 4 5 6 7 8 9
#1 # # # # # # # # #
#2 # # # # # # # # #
#3 # # # # # # # # #
#4 # # # # # # # # #
#5 # # # # # # # # #
#6 # # # # # # # # #
#7 # # # # # # # # #
#8 # # # # # # # # #
#9 # # # # # # # # #

#Importar librerias
import random, os, sys, time
#el contador que va a llevar el número de bombas
bombas = 0
#le pasamos los siguientes valores
def comprobacion(tablero, tablero_2, col, fil):
    #el contador qie devolvemos...
    contador = 0
    #que intente comprobar que en cada casilla de su alrededor hay una bomba, si la hay que sume uno al contador, si no la hay que en el tablero que podemos ver en vez de imprimir "#" lo cambie por un espacio en blanco
    try:
        if tablero_2[int(fil)+1][int(col)] == False:
            contador += 1
        elif tablero_2[int(fil)+1][int(col)] == True and tablero[int(fil)+1][int(col-1)] == "#":
            tablero[int(fil)+1][int(col-1)] = " "
    except:
        pass
    try:
        if tablero_2[int(fil)+1][int(col)-1] == False:
            contador += 1
        elif tablero_2[int(fil)+1][int(col)-1] == True and tablero[int(fil)+1][int(col-1)-1] == "#":
            tablero[int(fil)+1][int(col-1)-1] = " "
    except:
        pass
    try:
        if tablero_2[int(fil)+1][int(col)+1] == False:
            contador += 1
        elif tablero_2[int(fil)+1][int(col)+1] == True and tablero[int(fil)+1][int(col-1)+1] == "#":
            tablero[int(fil)+1][int(col-1)+1] = " "
    except:
        pass
    try:
        if tablero_2[int(fil)][int(col)-1] == False:
            contador += 1
        elif tablero_2[int(fil)][int(col)-1] == True and tablero[int(fil)][int(col-1)-1] == "#":
            tablero[int(fil)][int(col-1)-1] = " "
    except:
        pass
    try:
        if tablero_2[int(fil)][int(col)+1] == False:
            contador += 1
        elif tablero_2[int(fil)][int(col)+1] == True and tablero[int(fil)][int(col-1)+1] == "#":
            tablero[int(fil)][int(col-1)+1] = " "
    except:
        pass
    try:
        if tablero_2[int(fil)-1][int(col)-1] == False:
            contador += 1
        elif tablero_2[int(fil)-1][int(col)-1] == True and tablero[int(fil)-1][int(col-1)-1] == "#":
            tablero[int(fil)-1][int(col-1)-1] = " "
    except:
        pass
    try:    
        if tablero_2[int(fil)-1][int(col)] == False:
            contador += 1
        elif tablero_2[int(fil)-1][int(col)] == True and tablero[int(fil)-1][int(col-1)] == "#":
            tablero[int(fil)-1][int(col-1)] = " "
    except:
        pass
    try:
        if tablero_2[int(fil)-1][int(col)+1] == False:
            contador += 1
        elif tablero_2[int(fil)-1][int(col)+1] == True and tablero[int(fil)-1][int(col-1)+1] == "#":
            tablero[int(fil)-1][int(col-1)+1] = " "
    except:
        pass

    #devuelve el contador
    return contador

#el tablero2 es el tablero que estará de fondo con sus respectivos True(sitio donde no hay bomba) y False(sitio donde hay bomba)
def tablero2(bombas, tablero):
    #El contador que guardará el numero de bombas que hemos "capturado"
    contador_ganar = 0
    #Generamos todo el tablero con True
    tablero_2 = [[True for i in range(10)] for j in range(10)]
    #Aleatoriamente posicionamos las bombas en el tablero(False)
    for i in range(10):
        for j in range(9):
            if bombas >= 12: #Si se generan mas de 12 bombas el bucle se rompe
                    break
            #Hay un 32% de probabilidades de que se genere una bomba en una casilla, esta casilla no puede tener indice 0 en x ni en y porque todo en indice 0 en x y en y esta reservador para el índice del tablero
            if random.randint(0, 100) < 32 and i != 0 and j != 0:
                tablero_2[j][i] = False #Se le asigna False donde haya una bomba
                bombas += 1 #se suma 1 a bombas
            else:
                pass

    #bucle del juego
    while True:
        #Si capturamos las 12 bombas generadas significa que hemos ganado
        if contador_ganar >= 12:
            #Decoración...
            ganar = "¡HAS GANADO! C:"
            for i in range(5):
                print(ganar.lower())
                time.sleep(0.2)
                os.system("cls")
                print(ganar.upper())
                time.sleep(0.2)
                os.system("cls")
            sys.exit()

        #Inicializamos fila y columna(y, x)
        fil = 0
        col = 0

        print("""
        1) Marcar casilla sin bomba
        2) Marcar casilla bomba (Elige esta opción si quieres desmarcar una casilla ya marcada)
        """)

        opc = input("(elije entre 1 o 2) >> ")
        opc = int(opc)
        os.system("cls")
        #Pedimos x,y
        fil = int(fil)
        col = int(col)
        #Control para que x e y no puedan salirse del rango de la tabla
        while fil < 1 or fil > 9 or col < 1 or col > 9:  
            fil = int(input("fila >> "))
            if fil < 1 or fil > 9:
                print("MIN - 1")
                print("MAX - 9")
            col = int(input("columna >> "))
            if col < 1 or col > 9:
                print("MIN - 1")
                print("MAX - 9")
        #Si se ha elegido la opcion 1...
        if opc == 1:
            #Y el la posicion dada es justo donde hay una bomba has perdido...
            #Este bloque de código nos imprime como ha quedado el tablero que nosotros vemos antes de salirse del programa
            if tablero_2[int(fil)][int(col)] == False:
                tablero[fil][col-1] = "*"
                for a in range(10):
                    print(a, end=" ")
                    for b in range(9):
                        if a == 0:
                            print(b+1, end=" ")
                        else:
                            print(tablero[a][b], end=" ")
                    print("")
                #Decoración...
                perder = "PERDISTE... :C"
                for i in range(5):
                    print(perder.lower())
                    time.sleep(0.2)
                    os.system("cls")
                    print(perder.upper())
                    time.sleep(0.2)
                    os.system("cls")
                sys.exit()
            #pero si no...
            elif tablero_2[int(fil)][int(col)] == True:
                #que se añada a un contador el número de bombas que hay alrededor de esa posicion
                contador = comprobacion(tablero, tablero_2, col, fil)
                #Y que la posicion dada sea igual al contador (a la columna se le resta 1 porque el indice de nuestro tablero en columnas(x) es 8)
                tablero[fil][col-1] = contador
                #Imprime el tablero...
                os.system("cls")
                for a in range(10):
                    print(a, end=" ")
                    for b in range(9):
                        if a == 0:
                            print(b+1, end=" ")
                        else:
                            print(tablero[a][b], end=" ")
                    print("")
        #si la opcion elegida es 2(para capturar una bomba)
        elif opc == 2:
            #si la posicion dada para capturar la bomba en el tablero que nosotros no podemos ver es cierta y en el tablero que nosotros si podemos ver es igual a "#" 
            if tablero_2[fil][col] == False and tablero[fil][col-1] == "#":
                contador_ganar += 1 #Como ha capturado la bomba se le suma uno al contador de bombas capturadas
                tablero[fil][col-1] = "+" #Para saber que ha sido capturada en el tablero que nosotros podemos ver se cambia "#" por "+"
            #sino, si en el tablero que podemos ver la posicion dada es igual a "+"
            elif tablero_2[fil][col] == False and tablero[fil][col-1] == "+":
                contador_ganar -= 1 #se desmarca la posicion marcada y se resta uno a contador_ganar
                tablero[fil][col-1] = "#" #se vuelve a imprimir "#"
            #Aquí si se marca una posicion para capturar una bomba y falla, es decir, que no hay bomba
            elif tablero_2[fil][col] == True and tablero[fil][col-1] == "#":
                tablero[fil][col-1] = "+" #Que solo imprima "+" en la posicion dada
            elif tablero_2[fil][col] == True and tablero[fil][col-1] == "+":
                tablero[fil][col-1] = "#" #Si se quiere desmarcar lo marcado que se vuelva a imprimir "#"
            #Imprimir el tablero
            for a in range(10):
                print(a, end=" ")
                for b in range(9):
                    if a == 0:
                        print(b+1, end=" ")
                    else:
                        print(tablero[a][b], end=" ")
                print("")

        else:
            print("Elige una opcion correcta...")
            
print("")
#Decoracion...
buscaminas = "Bienvenidos al buscaminas realizado por Jesús Daza"
buscaminas_aux = ""
for letra in buscaminas:
    buscaminas_aux += letra.upper()
    print(buscaminas_aux)
    buscaminas_aux = buscaminas_aux.lower()
    time.sleep(0.075)
    os.system("cls")
#generacion del tablero que nosotros vamos a ver
tablero = [["#" for i in range(10)] for j in range(10)]
#Aquí estamos imprimiendo la tabla con su respectivo indice
for a in range(10):
    print(a, end=" ")
    for b in range(9):
        if a == 0:
            print(b+1, end=" ")
        else:
            print(tablero[a][b], end=" ")
    print("")
#llamamos la funcion tablero2 pasandole como valores el numero de bombas y el tablero que nosotros vamos a ver
tablero2(bombas, tablero)