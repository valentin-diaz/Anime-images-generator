# Generador de imágenes de Anime

Esta es una pequeño proyecto que consiste en una aplicación que genera imágenes aleatorias de personajes de Anime, utilizando la API waifu.pics (https://waifu.pics/).

### Objetivos :clipboard:

- Aplicar y ejercitar el uso de interfaces gráficas mediante ```PyQt5```
- Realizar un uso práctico de la librería ```requests```, implementándola en una pequeña aplicación tangible

### Funcionamiento :gear:
El programa está escrito en Python, utilizando ```PyQt5``` para la inerfaz gráfica y ```requests``` para las solicitudes HTTP. Consta de una ventana de bienvenida, un menú de selección en el que es posible elegir un tipo y una categoría de imagen (que se encuentran en la documentación de la API), y el menú principal. En este último, es posible ver una visualización de la imagen obtenida, y decidir entre guardarla en el dispositivo o descartarla y obtener una nueva imagen en la misma categoría. También es posible volver al menú anterior y seleccionar un nuevo tipo y una nueva categoría. Para ejecutar el programa basta con descargar el repositorio y ejecutar el archivo ```main.py```.

### Librerías :books:
- ```PyQt5```
- ```requests```
- ```sys```
- ```os```
  
### Desafíos a futuro
- [ ] Mejorar el diseño gráfico de las interfaces
- [ ] Añadir una ventana de advertencia al seleccionar la categoría NSFW
- [ ] Mejorar la modularización de algunos parámetros (e.g. los nombres de las fuentes están *hardcodeadas*)