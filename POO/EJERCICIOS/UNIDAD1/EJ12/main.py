from GestionPartidos import GestionPartidos
from datetime import date

# Filtrar por equipo local.
# GestionPartidos.equipo_local("Zafra")

# # Ganados del equipo.
# print(GestionPartidos.ganados_equipo("Zafra"))

# # # Mostrar los partidos del año pasado como parámetro.
# GestionPartidos.partidos_anio(2019)

# # #Mostrar los partidos de una fecha pasada como parámetro.
# GestionPartidos.partidos_fecha(date.fromisoformat("20240519"))

# # #Cuenta partidos. Retorna el número de partidos de la lista.
print(GestionPartidos.num_partidos())