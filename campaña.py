from anuncio import Anuncio, Video, Display, Social  
from error import LargoExcedidoError  

# Definimos la clase Campaña
class Campaña:
    def __init__(self, nombre, fecha_inicio, fecha_termino, anuncios_info):
        # Inicializamos las propiedades de la campaña
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self._anuncios = self._crear_anuncios(anuncios_info)

    # Definimos el getter y setter para la propiedad 'nombre'
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if len(value) > 250:
            raise LargoExcedidoError("El nombre supera los 250 caracteres.")
        self._nombre = value

    # Definimos el getter para la propiedad 'anuncios'
    @property
    def anuncios(self):
        return self._anuncios

    # Método privado para crear anuncios
    def _crear_anuncios(self, anuncios_info):
        anuncios = []
        for info in anuncios_info:
            tipo = info.pop("tipo")
            if tipo == "Video":
                anuncios.append(Video(**info))
            elif tipo == "Display":
                anuncios.append(Display(**info))
            elif tipo == "Social":
                anuncios.append(Social(**info))
        return anuncios

    # Método para convertir la campaña a una cadena de texto
    def __str__(self):
        tipos = {"Video": 0, "Display": 0, "Social": 0}
        for anuncio in self._anuncios:
            tipos[anuncio.FORMATO] += 1
        return f"Nombre de la campaña: {self.nombre}\nAnuncios: {tipos['Video']} Video, {tipos['Display']} Display, {tipos['Social']} Social"
