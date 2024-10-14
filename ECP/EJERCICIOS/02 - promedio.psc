//Introducir 10 números por teclado y calcular su promedio  

Algoritmo promedio
	
	suma <- 0
	Para i<-1 Hasta 10 Con Paso 1 Hacer
		Escribir Sin Saltar "Escribe un numero"
		Leer num
		suma = suma + num
	Fin Para
	
	prom <- suma / 10
	
	Escribir "El promedio es ", prom
	
FinAlgoritmo
