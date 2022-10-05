from logging import root
from random import randint
from tkinter import *;
def jugar():
	if __name__ == '__main__':
		matriz = [[str() for ind0 in range(11)] for ind1 in range(12)]
		letras = [str() for ind0 in range(26)]
		letras[0] = "A"
		letras[1] = "B"
		letras[2] = "C"
		letras[3] = "D"
		letras[4] = "E"
		letras[5] = "F"
		letras[6] = "G"
		letras[7] = "H"
		letras[8] = "I"
		letras[9] = "J"
		letras[10] = "K"
		letras[11] = "L"
		letras[12] = "M"
		letras[13] = "N"
		letras[14] = "O"
		letras[15] = "P"
		letras[16] = "Q"
		letras[17] = "R"
		letras[18] = "S"
		letras[19] = "T"
		letras[20] = "U"
		letras[21] = "V"
		letras[22] = "W"
		letras[23] = "X"
		letras[24] = "Y"
		letras[25] = "Z"
		for i in range(1,13):
			for j in range(1,12):
				l = randint(0,24)+1
				x = letras[l-1]
				matriz[i-1][j-1] = x
		matriz[1][0] = "P"
		matriz[1][1] = "A"
		matriz[1][2] = "L"
		matriz[1][3] = "A"
		matriz[2][4] = "V"
		matriz[2][5] = "I"
		matriz[2][6] = "V"
		matriz[2][7] = "I"
		matriz[2][8] = "R"
		matriz[3][1] = "E"
		matriz[3][5] = "M"
		matriz[3][6] = "E"
		matriz[3][7] = "S"
		matriz[3][8] = "A"
		matriz[4][0] = "C"
		matriz[5][0] = "A"
		matriz[6][0] = "M"
		matriz[7][0] = "I"
		matriz[8][0] = "N"
		matriz[9][0] = "A"
		matriz[10][0] = "R"
		matriz[4][1] = "D"
		matriz[4][2] = "B"
		matriz[4][3] = "O"
		matriz[4][4] = "T"
		matriz[4][5] = "E"
		matriz[4][8] = "U"

		matriz[5][2] = "S"
		matriz[5][4] = "R"
		matriz[5][7] = "J"
		matriz[4][10] = "F"
		matriz[5][10] = "E"
		matriz[6][10] = "O"
		matriz[6][1] = "A"
		matriz[6][2] = "L"
		matriz[6][3] = "O"
		matriz[6][5] = "N"
		matriz[6][7] = "R"
		matriz[6][8] = "U"
		matriz[7][2] = "J"
		matriz[7][6] = "A"
		matriz[7][7] = "A"
		matriz[8][7] = "N"
		matriz[8][8] = "N"
		matriz[7][2] = "C"
		matriz[8][2] = "A"
		matriz[9][2] = "S"
		matriz[10][2] = "A"
		matriz[9][3] = "C"
		matriz[9][4] = "A"
		matriz[9][5] = "S"
		matriz[9][6] = "N"
		matriz[9][7] = "A"
		matriz[9][8] = "D"
		matriz[9][9] = "A"
		matriz[9][10] = "R"
		matriz[10][6] = "L"
		matriz[10][7] = "I"
		matriz[10][8] = "N"
		matriz[10][9] = "D"
		matriz[10][10] = "O"
		matriz[11][3] = "A"
		matriz[11][5]="C"
		matriz[11][6] = "O"
		matriz[11][7] = "R"
		matriz[11][8] = "R"
		matriz[11][9] = "E"
		matriz[11][10] = "R"
		for i in range(1,13):
			print(matriz[i-1][0]," ",matriz[i-1][1]," ",matriz[i-1][2]," ",matriz[i-1][3]," ",matriz[i-1][4]," ",matriz[i-1][5]," ",matriz[i-1][6]," ",matriz[i-1][7]," ",matriz[i-1][8]," ",matriz[i-1][9]," ",matriz[i-1][10])
		print("               ")
		print("""LISTA DE AUTOAYUDA PARA BUSCAR LAS PALABRAS...:\nVerbos:\n -nadar -mezclar -vivir  -buscar -correr  -caminar -reir -leer -mirar -saludar
		\nSustantivos:\n-pala -termo -mesa -mate -casa -pizzara -bote -cargador -proyector -silla
		\nAdjetivos:\n-fuerte -malo -alto -feo -lindo -sencillo -gris -blanco -rapido -lento
		""")
		
		
		aciertopalabras = 0
		print("BIENVENIDO AL JUEGO SOPA DE LETRAS!\nBUSCAR 4 VERBOS,4 SUSTANTIVOS Y 3 ADEJETIVOS ESCONDIDOS EN LA SOPA DE LETRA!!!")
		print("MIRAR LA LISTA DE AUTOAYUDA.....")
		print()
		print("PARA SALIR DEL JUEGO ESCRIBA LA SIGUIENTE PALABRA: 'salir'")
		print()
		while True:
			palabra = input("Ingrese la palabra encontrada: ")
			if palabra == "pala":
				aciertopalabras +=1
				print()
				print(f"Ya tienes {aciertopalabras} acierto, felicidades!")
				print()
				print("Sigue buscando màs palabras.....")
			elif palabra == "vivir":
				aciertopalabras +=1
				print()
				print(f"Ya tienes {aciertopalabras} aciertos, felicidades!")
				print()
				print("Sigue buscando màs palabras.....")
			elif palabra == "mesa":
				aciertopalabras +=1
				print()
				print(f"Ya tienes {aciertopalabras} aciertos, felicidades!")
				print()
				print("Sigue buscando màs palabras.....")
			elif palabra == "caminar":
				aciertopalabras +=1
				print()
				print(f"Ya tienes {aciertopalabras} aciertos, felicidades!")
				print()
				print("Sigue buscando màs palabras.....")
			elif palabra == "bote":
				aciertopalabras +=1
				print()
				print(f"Ya tienes {aciertopalabras} aciertos, felicidades!")
				print()
				print("Sigue buscando màs palabras.....")
			elif palabra == "feo":
				aciertopalabras +=1
				print()
				print(f"Ya tienes {aciertopalabras} aciertos, felicidades!")
				print()
				print("Sigue buscando màs palabras.....")
			elif palabra == "casa":
				aciertopalabras +=1
				print()
				print(f"Ya tienes {aciertopalabras} aciertos, felicidades!")
				print()
				print("Sigue buscando màs palabras.....")
			elif palabra == "nadar":
				aciertopalabras +=1
				print()
				print(f"Ya tienes {aciertopalabras} aciertos, felicidades!")
				print()
				print("Sigue buscando màs palabras.....")
			elif palabra == "lindo":
				aciertopalabras +=1
				print()
				print(f"Ya tienes {aciertopalabras} aciertos, felicidades!")
				print()
				print("Sigue buscando màs palabras.....")
			elif palabra == "correr":
				aciertopalabras +=1
				print()
				print(f"Ya tienes {aciertopalabras} aciertos, felicidades!")
				print()
				print("Sigue buscando màs palabras.....")
			elif palabra == "malo":
				aciertopalabras +=1
				print()
				print(f"Ya tienes {aciertopalabras} aciertos, felicidades!")
				print()
				print("Sigue buscando màs palabras.....")
		
			elif palabra == "salir":
				break
			else:
				print("La palabra no se encuentra en la sopa de letra!, sigue buscando")
			
		
			
		    
	    
		print()
		print()
		print(f"LA CANTIDAD DE PALABRAS ACERTADAS FUERON: {aciertopalabras}")
		print()
		print("SI LA CANTIDAD  DE PALABRA ACERTADA ES 11,'FELICIDADES HAS GANADO',sino sigue BUSCANDO..... ")
		print()
		print("FIN DEL JUEGO!")
		print()
		print("GRACIAS POR PARTICIPAR... Si quieres seguir jugando,selecciona 1 OPCION JUGAR.....")
	
		

print()
print()
while True:
            print("""\t.:///////////////SOPA DE LETRA//////////////////:
			
			1.JUGAR
			2.SALIR


	///////////////////////////////////////////////////////////""")
          
            opcion=int(input("INGRESE UNA OPCION: "))
            if opcion==1:
                jugar()

            elif opcion==2:
                break
            else:
                print("ERROR")