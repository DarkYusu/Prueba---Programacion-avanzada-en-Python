from campaña import Campaña  # Importamos la clase Campaña
from error import SubTipoInvalidoError, LargoExcedidoError  # Importamos las excepciones

def main():
    # Información inicial de los anuncios
    anuncios_info = [
        {"tipo": "Video", "url_archivo": "video.mp4", "url_clic": "http://example.com", "sub_tipo": "instream", "duracion": 10}
    ]
    # Creamos una nueva campaña
    campaña = Campaña("Campaña 1", "2024-05-01", "2024-06-01", anuncios_info)
    
    try:
        # Solicitamos al usuario que ingrese un nuevo nombre para la campaña
        nuevo_nombre = input("Ingrese el nuevo nombre de la campaña: ")
        campaña.nombre = nuevo_nombre
        
        # Solicitamos al usuario que ingrese un nuevo subtipo para el anuncio
        nuevo_subtipo = input("Ingrese el nuevo subtipo del anuncio: ")
        campaña.anuncios[0].sub_tipo = nuevo_subtipo

    except (SubTipoInvalidoError, LargoExcedidoError) as e:
        # Si ocurre una excepción, registramos el error en un archivo de log
        with open("error.log", "a") as file:
            file.write(f"{str(e)}\n")
    
    # Imprimimos la información de la campaña
    print(campaña)

if __name__ == "__main__":
    main()
