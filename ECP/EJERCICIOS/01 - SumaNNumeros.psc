// Realizar un Algoritmo hasta que introduzcamos el n�mero 0. 
//El programa nos debe devolver la suma n n�meros positivos y la cantidad de n�meros negativos 

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
