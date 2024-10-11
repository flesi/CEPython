from Vehiculo import Vehiculo

v1 = Vehiculo("Ford","Focus",2010,5000)
v2 = Vehiculo("Reanault","Megane",2016,7000)


print(f"""
        Vehiculo1:         
        Marca:  {v1.marca}  
        Modelo: {v1.modelo}  
        Año:    {v1.anio}    
        Precio: {v1.precio}
""" )


print(f"""
        Vehiculo2:         
        Marca:  {v2.marca}  
        Modelo: {v2.modelo}  
        Año:    {v2.anio}    
        Precio: {v2.precio}
""" )