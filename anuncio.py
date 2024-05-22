from error import SubTipoInvalidoError  # Importamos la excepción personalizada para subtipos inválidos

# Definimos la clase base Anuncio
class Anuncio:
    def __init__(self, ancho, alto, url_archivo, url_clic, sub_tipo):
        # Inicializamos las propiedades del anuncio
        self.ancho = ancho if ancho > 0 else 1
        self.alto = alto if alto > 0 else 1
        self.url_archivo = url_archivo
        self.url_clic = url_clic
        self.sub_tipo = sub_tipo

    # Definimos el getter y setter para la propiedad 'ancho'
    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, value):
        self._ancho = value if value > 0 else 1

    # Definimos el getter y setter para la propiedad 'alto'
    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, value):
        self._alto = value if value > 0 else 1

    # Definimos el getter y setter para la propiedad 'url_archivo'
    @property
    def url_archivo(self):
        return self._url_archivo

    @url_archivo.setter
    def url_archivo(self, value):
        self._url_archivo = value

    # Definimos el getter y setter para la propiedad 'url_clic'
    @property
    def url_clic(self):
        return self._url_clic

    @url_clic.setter
    def url_clic(self, value):
        self._url_clic = value

    # Definimos el getter y setter para la propiedad 'sub_tipo'
    @property
    def sub_tipo(self):
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, value):
        # Verificamos si el subtipo es válido
        if value not in self.SUB_TIPOS:
            raise SubTipoInvalidoError("Subtipo inválido.")
        self._sub_tipo = value

    # Método estático para mostrar los formatos de anuncios disponibles
    @staticmethod
    def mostrar_formatos():
        for cls in Anuncio.__subclasses__():
            print(f"FORMATO: {cls.FORMATO}")
            for subtype in cls.SUB_TIPOS:
                print(f"- {subtype}")

# Definimos la clase Video que hereda de Anuncio
class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, url_archivo, url_clic, sub_tipo, duracion):
        super().__init__(1, 1, url_archivo, url_clic, sub_tipo)
        self.duracion = duracion if duracion > 0 else 5

    # Método para comprimir anuncios de video (aún no implementado)
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    # Método para redimensionar anuncios de video (aún no implementado)
    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")

# Definimos la clase Display que hereda de Anuncio
class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    # Método para comprimir anuncios de display (aún no implementado)
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    # Método para redimensionar anuncios de display (aún no implementado)
    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

# Definimos la clase Social que hereda de Anuncio
class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    # Método para comprimir anuncios de redes sociales (aún no implementado)
    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    # Método para redimensionar anuncios de redes sociales (aún no implementado)
    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")
