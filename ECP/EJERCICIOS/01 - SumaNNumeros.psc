// Realizar un Algoritmo hasta que introduzcamos el número 0. 
//El programa nos debe devolver la suma n números positivos y la cantidad de números negativos 

Algoritmo SumaNNumeros
	numPositivos <- 0
	numNegativos <- 0
	
	
	Repetir
		Escribir  Sin Saltar "Ingresa un numero Positivo o Negativo"
		Leer num
		Si num > 0 Entonces
			numPositivos = numPositivos + 1
		FinSi
		
		Si num < 0 Entonces
			numNegativos = numNegativos + 1
		FinSi
		
	Hasta Que num = 0
	
	Escribir "Numero de Positivos ", numPositivos
	Escribir "Numero de Negativos ", numNegativos
	
FinAlgoritmo
