class Partido:
    def __init__(self,local,visitante,goles_local,goles_visitante,campeonato,fecha):
        self.local = local
        self.visitante = visitante
        self.goles_locales = goles_local
        self.goles_visitante = goles_visitante
        self.campeonato = campeonato
        self.fecha = fecha

    def __str__(self):
        return f"LOCAL: {self.local} | GOLES: {self.goles_locales} - {self.goles_visitante} | CAMPEONATO: {self.campeonato} | FECHA: {self.fecha}"

