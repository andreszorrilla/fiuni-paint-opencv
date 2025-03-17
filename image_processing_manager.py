import numpy as np
import cv2

class ImageProcessingManager():
    """
    Esta clase maneja la implementación de los procesos internos del Editor de Imágenes.

    Desarrollado por:
    """

    # Dimensiones por defecto de las imágenes
    DEFAULT_WIDTH = 512
    DEFAULT_HEIGHT = 512

    def __init__(self):
        """
        Constructor de la clase.
        Inicializa la pila de imágenes con una imagen en blanco y
        una lista para almacenar líneas dibujadas.
        """
        super(ImageProcessingManager, self).__init__()

        # Por defecto, creamos una imagen blanca de tamaño DEFAULT_WIDTH x DEFAULT_HEIGHT.
        initial_matrix = np.ones((self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT, 3), np.uint8) * 255
        
        # Pila de imágenes
        self.stack_images = [initial_matrix]
        
        # Pila de líneas/puntos dibujados
        self.stack_lines = []

    def rgb_to_hex(self, rgb):
        """
        Convierte un color RGB en un código hexadecimal.
        
        Parámetros:
        - rgb (tuple): Tupla con tres valores (R, G, B) en el rango de 0 a 255.

        Retorna:
        - str: Representación hexadecimal del color.

        Fuente: https://www.codespeedy.com/convert-rgb-to-hex-color-code-in-python/
        """
        return '%02x%02x%02x' % rgb

    def last_image(self):
        """
        NO ALTERAR ESTA FUNCIÓN.
        
        Obtiene la última imagen almacenada en la pila.
        
        Retorna:
        - numpy.ndarray: Última imagen almacenada.
        """
        return self.stack_images[-1]

    def can_undo(self):
        """
        NO ALTERAR ESTA FUNCIÓN.
        
        Verifica si se puede deshacer la última acción.
        Se puede deshacer si hay más de una imagen en la pila.

        Retorna:
        - bool: True si hay más de una imagen en la pila, False en caso contrario.
        """
        return len(self.stack_images) > 1

    def has_changes(self):
        """
        NO ALTERAR ESTA FUNCIÓN.
        
        Determina si hay cambios en la imagen, es decir,
        si la pila contiene más de una imagen.

        Retorna:
        - bool: True si hay más de una imagen en la pila, False en caso contrario.
        """
        return len(self.stack_images) > 1

    def add_image(self, image_path):
        """
        Carga una imagen desde el sistema de archivos, la redimensiona
        a las dimensiones por defecto y la almacena en la pila.

        Parámetros:
        - image_path (str): Ruta del archivo de imagen.

        Observaciones:
        - Antes de cargar una nueva imagen, se deben vaciar las colecciones
          de imágenes y líneas dibujadas.
        """
        pass

    def save_image(self, filename):
        """
        Guarda la última imagen de la pila en un archivo.

        Parámetros:
        - filename (str): Nombre del archivo donde se guardará la imagen.
        """
        pass

    def undo_changes(self):
        """
        Deshace el último cambio eliminando la última imagen de la pila.
        """
        pass

    def save_points(self, x1, y1, x2, y2, line_width, color):
        """
        Guarda la información de los puntos de una línea en la pila de líneas.

        Parámetros:
        - x1, y1 (int): Coordenadas del punto inicial de la línea.
        - x2, y2 (int): Coordenadas del punto final de la línea.
        - line_width (int): Grosor de la línea.
        - color (tuple): Color de la línea en formato RGB.
        """
        pass

    def add_lines_to_image(self):
        """
        Dibuja todas las líneas almacenadas en la pila sobre una imagen nueva.
        Luego, la imagen resultante se guarda en la pila.

        Pasos:
        1. Crear una nueva matriz de imagen.
        2. Dibujar cada línea almacenada en `self.stack_lines` usando `cv2.line`.
        3. Agregar la imagen con líneas a `self.stack_images`.
        4. Limpiar `self.stack_lines`.

        Ayudas:
        - Documentación de `cv2.line`: https://docs.opencv.org/4.x/dc/da5/tutorial_py_drawing.html
        - Usar `rgb_to_hex` para convertir colores si es necesario.
        """
        pass

    def black_and_white_image(self):
        """
        Convierte la última imagen de la pila a escala de grises y la almacena.

        Retorna:
        - numpy.ndarray: Imagen procesada en blanco y negro.
        """
        last = self.stack_images[-1].copy()
        return last

    def negative_image(self):
        """
        Calcula el negativo de la última imagen y la almacena.

        Retorna:
        - numpy.ndarray: Imagen procesada en negativo.
        """
        last = self.stack_images[-1].copy()
        return last

    def global_equalization_image(self):
        """
        Aplica ecualización global del histograma a la última imagen y la almacena.

        Retorna:
        - numpy.ndarray: Imagen ecualizada globalmente.
        """
        last = self.stack_images[-1].copy()
        return last

    def CLAHE_equalization_image(self, grid=(8, 8), clipLimit=2.0):
        """
        Aplica ecualización adaptativa con contraste limitado (CLAHE)
        a la última imagen y la almacena.

        Parámetros:
        - grid (tuple): Tamaño de la grilla utilizada para el procesamiento.
        - clipLimit (float): Límite de contraste.

        Retorna:
        - numpy.ndarray: Imagen ecualizada con CLAHE.
        """
        last = self.stack_images[-1].copy()
        return last

    def contrast_and_brightness_processing_image(self, alpha, beta):
        """
        Ajusta el contraste y brillo de la última imagen y la almacena.

        Parámetros:
        - alpha (float): Factor de escala para el contraste.
        - beta (float): Valor sumado a los píxeles para ajustar el brillo.

        Retorna:
        - numpy.ndarray: Imagen con ajuste de contraste y brillo.

        Referencias:
        - Szeliski, R. (2010). "Computer Vision: Algorithms and Applications". Página 103.
        - OpenCV: https://docs.opencv.org/3.4/d3/dc1/tutorial_basic_linear_transform.html
        - Función `convertScaleAbs`: 
          https://docs.opencv.org/2.4/modules/core/doc/operations_on_arrays.html#convertscaleabs
        """
        last = self.stack_images[-1].copy()
        return last
