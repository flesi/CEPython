from Partido import Partido
from datetime import date
class GestionPartidos:
    partidos = [
                Partido("Zafra","Medina",3,1,"RioBodion",date.fromisoformat("20240519")),
                Partido("Medina","Zafra",2,4,"RioBodion",date.fromisoformat("20240519")),
                Partido("Zafra","Medina",2,4,"RioBodion",date.fromisoformat("20240519")),
                Partido("Zafra","Medina",2,4,"RioBodion",date.fromisoformat("20190519"))
                ]
    
    @classmethod
    def equipo_local(cls,local):
        for partido in cls.partidos:
            if partido.local == local:
                print(partido)

    @classmethod
    def ganados_equipo(cls,equipo):
        # GestionPartidos.partidos[0].local = "MADRID"
        for partido in cls.partidos:
            if equipo == partido.local and partido.goles_locales > partido.goles_visitante:
                return partido
            elif equipo == partido.visitante and partido.goles_visitante > partido.goles_locales:
                return partido


    @classmethod
    def partidos_anio(cls,anio):
        for partido in cls.partidos:
            if anio == partido.fecha.year:
                print(partido)

    @classmethod
    def partidos_fecha(cls,fecha):
        for partido in cls.partidos:
            if fecha == partido.fecha:
                print(partido)

    @classmethod
    def agregar_partido(cls,partido):
        cls.partidos.append(partido)

    @classmethod
    def num_partidos(cls):
        return len(cls.partidos)