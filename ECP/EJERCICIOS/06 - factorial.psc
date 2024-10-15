//Calcular el factorial de un número introducido por teclado

Algoritmo factorial
	Escribir Sin Saltar "Introduce un numero: " 
	Leer num
	miFactorial = 1
	Para i<- 1 Hasta num Con Paso 1 Hacer
		miFactorial = miFactorial * i
	Fin Para
	
	Escribir "El factorial de ", num, " es= ", miFactorial
	
FinAlgoritmo
