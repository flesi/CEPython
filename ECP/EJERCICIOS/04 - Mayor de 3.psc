//Introducir 3 números por teclado. Decir cual es el mayor de todos ellos

Algoritmo MayorDeTres
	
	Escribir  Sin Saltar "Escribe el primer numero: "
	Leer num1
	Escribir  Sin Saltar "Escribe el segundo numero: "
	Leer num2
	Escribir  Sin Saltar "Escribe el tercer numero: "
	Leer num3
	
	Si num1 > num2 Y num1 > num3 Entonces
		numMayor = num1		
	FinSi	
	Si num2 > num1 Y num2 > num3 Entonces
		numMayor = num2	
	FinSi	
	Si num3 > num2 Y num3 > num1 Entonces
		numMayor = num3
	FinSi	
	
	Escribir "El numero mayor es: ", numMayor
	
FinAlgoritmo
