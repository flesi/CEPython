//Realiza un algoritmo para determinar cuánto cuanto tiene que pagar finalmente una persona por un artículo equis, 
//considerando que tiene un descuento de 20%, y debe pagar 10% de IVA. Debe mostrar el precio con descuento y el precio final.

Algoritmo descuento
	
	Escribir Sin Saltar "Introduce el precio del producto"
	Leer precio
	
	precioDescuento = precio - (precio * 20 / 100)
	precioIVA = precioDescuento + (precio * 10 / 100)
	
	Escribir precioIVA
	
FinAlgoritmo
