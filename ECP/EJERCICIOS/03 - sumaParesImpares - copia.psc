//Realizar un algoritmo que permita introducir números enteros hasta que se introduzca el número 0. 
//El programa nos debe indicar  la cantidad de números pares e impares

Algoritmo SumaNNumeros
	
	numPares <- 0
	numImpares <- 0
	
	
	Repetir
		Escribir  Sin Saltar "Ingresa un numero Positivo o Negativo"
		Leer num
		Si num % 2  == 0 Y num <> 0 Entonces
			numPares = numPares + 1
		FinSi	
		Si num % 2 <> 0 Y num <> 0 Entonces
			numImpares = numImpares + 1
		FinSi
		
	Hasta Que num = 0
	
	Escribir "Numero de Pares ", numPares
	Escribir "Numero de Impares: ", numImpares
	
FinAlgoritmo
