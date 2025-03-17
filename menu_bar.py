"""
Menu Bar

Este módulo define la barra de menú para la aplicación de procesamiento de imágenes.

Autor: Andres Zorrilla
Última modificación: Marzo 2020
"""

# Importaciones necesarias para la interfaz gráfica
from tkinter import filedialog, messagebox
import tkinter as tk
from file_manager import FileManager


class MenuBar(tk.Menu):
  """Clase que define la barra de menú de la aplicación."""

  def __init__(self, root, canvas, img_processing_manager):
    """
    Inicializa la barra de menú.

    Parámetros:
    - root: Ventana principal de la aplicación.
    - canvas: Lienzo donde se mostrarán las imágenes.
    - img_processing_manager: Gestor de procesamiento de imágenes.
    """
    super(MenuBar, self).__init__()
    self.root = root
    self.canvas = canvas
    self.img_processing_manager = img_processing_manager
    self.init_menu()

  def init_menu(self):
    """Configura los menús de la aplicación."""
    self.root.config(menu=self)

    # Menú Archivo
    filemenu = tk.Menu(self, tearoff=0)
    filemenu.add_command(label="Nuevo")
    filemenu.add_command(label="Abrir", command=self.upload_image)
    filemenu.add_command(label="Guardar", command=self.save_image)
    filemenu.add_command(label="Cerrar")
    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=self.quit)

    # Menú Editar
    editmenu = tk.Menu(self, tearoff=0)
    editmenu.add_command(label="Deshacer")

    # Menú Ayuda
    helpmenu = tk.Menu(self, tearoff=0)
    helpmenu.add_command(label="Ayuda")
    helpmenu.add_separator()
    helpmenu.add_command(label="Acerca de...")

    # Agregar los menús a la barra
    self.add_cascade(label="Archivo", menu=filemenu)
    self.add_cascade(label="Editar", menu=editmenu)
    self.add_cascade(label="Ayuda", menu=helpmenu)

  def upload_image(self):
    """Carga una imagen en la aplicación."""
    FileManager.upload_image(self.root, self.canvas, self.img_processing_manager)

  def save_image(self):
    """Guarda la imagen procesada."""
    FileManager.save_image(self.root, self.canvas, self.img_processing_manager)

  def quit(self):
    """Cierra la aplicación."""
    FileManager.quit(self.root, self.canvas)
