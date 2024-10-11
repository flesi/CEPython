from Partido import Partido
from datetime import date
class GestionPartidos:
    partidos = [
                Partido("Zafra","Medina",3,1,"RioBodion",date.fromisoformat("20240519")),
                Partido("Medina","Zafra",3,1,"RioBodion",date.fromisoformat("20240519")),
                Partido("Zafra","Medina",3,1,"RioBodion",date.fromisoformat("20240519")),
                Partido("Zafra","Medina",3,1,"RioBodion",date.fromisoformat("20190519"))
                ]
    
    @staticmethod
    def equipo_local(local):
        for partido in GestionPartidos.partidos:
            if local == partido.local:
                print(partido)

    @staticmethod
    def ganados_equipo(equipo):
        for partido in GestionPartidos.partidos:
            if equipo == partido.local & partido.goles_locales > partido.goles_visitante:
                return partido.local
            elif equipo == partido.visitante & partido.goles_visitante > partido.goles_locales:
                return partido.visitante


    @staticmethod
    def partidos_anio(anio):
        for partido in GestionPartidos.partidos:
            if anio == partido.fecha.year:
                print(partido)

    @staticmethod
    def partidos_fecha(fecha):
        for partido in GestionPartidos.partidos:
            if fecha == partido.fecha:
                print(partido)

    @staticmethod
    def agregar_partido(partido):
        GestionPartidos.partidos.append(partido)

    @staticmethod
    def num_partidos():
        return len(GestionPartidos.partidos)