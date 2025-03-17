import numpy as np
import cv2

class PaintTools:
    """
    Esta clase maneja las herramientas de dibujo del editor de imágenes.
    """

    def __init__(self, default_width=512, default_height=512):
        """
        Inicializa la estructura con una imagen en blanco y las listas necesarias.
        """
        self.DEFAULT_WIDTH = default_width
        self.DEFAULT_HEIGHT = default_height
        
        # Imagen inicial en blanco
        initial_matrix = np.ones((self.DEFAULT_WIDTH, self.DEFAULT_HEIGHT, 3), np.uint8) * 255
        
        # Pilas de imágenes y líneas
        self.stack_images = [initial_matrix]
        self.stack_lines = []

    def save_points(self, x1, y1, x2, y2, line_width, color):
        """
        Guarda la información de una línea en la pila de líneas.
        """
        pass

    def add_lines_to_image(self):
        """
        Dibuja todas las líneas almacenadas en la pila sobre la imagen actual.
        Guarda la imagen modificada en la pila de imágenes.
        """
        pass

    def add_image(self, image_path):
        """
        Carga una imagen desde un archivo, la redimensiona y la agrega a la pila de imágenes.
        Se eliminan los elementos previos en las pilas de imágenes y líneas.
        """
        pass

    def save_image(self, filename):
        """
        Guarda la imagen actual en el archivo especificado.
        """
        pass

    def undo_changes(self):
        """
        Elimina la última imagen agregada si hay más de una en la pila.
        """
        pass


class ImageFilters:
    """
    Esta clase maneja los filtros y mejoras de imágenes.
    """

    def __init__(self, stack_images):
        """
        Recibe la pila de imágenes desde PaintTools.
        """
        self.stack_images = stack_images

    def black_and_white_image(self):
        """
        Convierte la última imagen a blanco y negro y la guarda en la pila.
        Retorna la imagen procesada.
        """
        last = self.stack_images[-1].copy()
        return last

    def negative_image(self):
        """
        Convierte la última imagen a negativo y la guarda en la pila.
        Retorna la imagen procesada.
        """
        last = self.stack_images[-1].copy()
        return last

    def global_equalization_image(self):
        """
        Aplica ecualización global de histograma a la última imagen.
        Guarda la imagen en la pila y la retorna.
        """
        last = self.stack_images[-1].copy()
        return last

    def CLAHE_equalization_image(self, grid=(8, 8), clipLimit=2.0):
        """
        Aplica ecualización adaptativa (CLAHE) a la última imagen.
        Guarda la imagen en la pila y la retorna.
        """
        last = self.stack_images[-1].copy()
        return last

    def contrast_and_brightness_processing_image(self, alpha, beta):
        """
        Ajusta el contraste y brillo de la última imagen según los parámetros alpha y beta.
        Guarda la imagen en la pila y la retorna.
        """
        last = self.stack_images[-1].copy()
        return last


class ImageProcessingManager:
    """
    Clase principal que coordina las herramientas de dibujo (PaintTools)
    y los filtros de imagen (ImageFilters).
    """

    def __init__(self):
        """
        Inicializa el sistema con PaintTools e ImageFilters.
        """
        self.paint_tools = PaintTools()
        self.image_filters = ImageFilters(self.paint_tools.stack_images)

    def last_image(self):
        """
        NO ALTERAR ESTA FUNCIÓN.
        Retorna la última imagen de la pila.
        """
        return self.paint_tools.stack_images[-1]

    def can_undo(self):
        """
        NO ALTERAR ESTA FUNCIÓN.
        Verifica si es posible deshacer cambios en la pila de imágenes.
        """
        return len(self.paint_tools.stack_images) > 1

    def has_changes(self):
        """
        NO ALTERAR ESTA FUNCIÓN.
        Verifica si existen cambios en la pila de imágenes.
        """
        return len(self.paint_tools.stack_images) > 1

    # Métodos delegados a PaintTools
    def save_points(self, x1, y1, x2, y2, line_width, color):
        return self.paint_tools.save_points(x1, y1, x2, y2, line_width, color)

    def add_lines_to_image(self):
        return self.paint_tools.add_lines_to_image()

    def add_image(self, image_path):
        return self.paint_tools.add_image(image_path)

    def save_image(self, filename):
        return self.paint_tools.save_image(filename)

    def undo_changes(self):
        return self.paint_tools.undo_changes()

    # Métodos delegados a ImageFilters
    def black_and_white_image(self):
        return self.image_filters.black_and_white_image()

    def negative_image(self):
        return self.image_filters.negative_image()

    def global_equalization_image(self):
        return self.image_filters.global_equalization_image()

    def CLAHE_equalization_image(self, grid=(8, 8), clipLimit=2.0):
        return self.image_filters.CLAHE_equalization_image(grid, clipLimit)

    def contrast_and_brightness_processing_image(self, alpha, beta):
        return self.image_filters.contrast_and_brightness_processing_image(alpha, beta)
