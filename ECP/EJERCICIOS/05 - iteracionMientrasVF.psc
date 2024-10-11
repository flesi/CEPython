Algoritmo iteracionMientrasVF
	
	salir = Falso
	suma = 0
	Mientras  salir = Falso Hacer
		Escribir Sin Saltar "Inserta un número: "
		Leer numEntero
		suma = suma + numEntero
		si suma > 20 Entonces
			salir = Verdadero
		FinSi
	FinMientras
	Escribir  "La suma es: ", suma
	Escribir  "Final del algoritmo"
	
FinAlgoritmo
