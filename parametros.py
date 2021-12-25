import os

# Parámetros iniciales de las ventanas
GEOMETRY_ARGS = (420, 70, 600, 600)
TITULO = 'Anime Image Generator'
COLOR_FONDO = '#555A61'
ESTILO_BOTON = ('QPushButton{'
    f'background-color : {COLOR_FONDO};'
    'border : none;'
    'height : 40px;'
    'padding-left : 20px;'
    'padding-right : 20px;'
    '}'
    'QPushButton::hover{'
    'background-color : #3b4045;'
    'border : 1px solid #3b4045;'
    'border-top-left-radius : 15px;'
    'border-top-right-radius : 15px;'
    'border-bottom-left-radius : 15px;'
    'border-bottom-right-radius : 15px;'
    '}'
    )

ESTILO_COMBOBOX = ('background-color : white;'
    'border : 1.5px solid black;'
    )

# Ventana inicial
STR_HEADER_INICIO = '¡Bienvenido/a a Anime Image Generator!'
STR_DESCRIPCION_INICIO = ('Esta es una pequeña aplicación en la que podrás ver y descargar imágenes'
    ' de personajes de Anime bajo alguna de las categorías disponibles. Para más información, te '
    'invito a visitar el repositorio de GitHub de Anime Image Generator en '
    'https://github.com/valentin-diaz/Anime-images-generator'
    )

# Ventana de selección
STR_HEADER_SELECCION = 'Menú de Selección'
STR_DESCRIPCION_SELECCION = ('A continuación, indica el tipo y categoría de imagen que quieres '
    'obtener: '
    )

TIPOS = [
    'SFW',
    'NSFW'
]

CATEGORIAS_SFW = [
    'waifu',
    'neko',
    'shinobu',
    'megumin',
    'bully',
    'cuddle',
    'cry',
    'hug',
    'awoo',
    'kiss',
    'lick',
    'pat',
    'smug',
    'bonk',
    'yeet',
    'blush',
    'smile',
    'wave',
    'highfive',
    'handhold',
    'nom',
    'bite',
    'glomp',
    'slap',
    'kill',
    'kick',
    'happy',
    'wink',
    'poke',
    'dance',
    'cringe'
]

CATEGORIAS_NSFW = [
    'waifu',
    'neko',
    'trap',
    'blowjob'
]

MENSAJE_HELP = '''SFW --> Safe for Work
NSFW --> Not Safe for Work (las imágenes pueden ser explícitas)'''

# Menú principal
STR_HEADER_PRINCIPAL = 'Menú Principal'
STR_DESCRIPCION_PRINCIPAL = 'Imagen generada: '

SIZE_IMAGEN = (400, 275)

# Rutas
RUTA_HELP = os.path.join('frontend', 'assets', 'help.png')