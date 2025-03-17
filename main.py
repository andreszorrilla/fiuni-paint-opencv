"""
Paint Window Manager

Una aplicación simple de procesamiento de imágenes utilizando OpenCV.

Autor: Andres Zorrilla
Última modificación: Marzo 2025
"""

import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Frame, Button, Entry, Style, Label
from tkinter.colorchooser import askcolor

from menu_bar import MenuBar
from menu_paint_buttons import MenuPaintButtonGroup, EnhancementButtonGroup, MenuAction
from image_processing_manager import ImageProcessingManager
from paint_board import PaintBoard


def setup_ui(root):
  """Configura los componentes de la interfaz gráfica."""
  
  img_processing_manager = ImageProcessingManager()
  canvas = PaintBoard(root, bg='white', width=512, height=512)

  # Configuración de los menús y herramientas
  menubar = MenuBar(root, canvas, img_processing_manager)
  paint_buttons = MenuPaintButtonGroup(root, canvas, img_processing_manager)
  enhancement_buttons = EnhancementButtonGroup(root, canvas, img_processing_manager)
  menu_action = MenuAction(root, canvas, img_processing_manager)

  # Ubicación de los elementos en la ventana
  menu_action.grid(row=0, column=1, sticky=tk.N)
  paint_buttons.grid(row=1, column=0, sticky=tk.N)
  canvas.grid(row=1, column=1, columnspan=5, sticky=tk.N)
  enhancement_buttons.grid(row=1, column=6, columnspan=5, sticky=tk.N)

  return root


def main():
  """Inicializa la ventana principal y ejecuta la aplicación."""
  
  root = tk.Tk()
  root.title("Paint Window Manager")  # Título de la ventana
  setup_ui(root)
  root.mainloop()


if __name__ == "__main__":
  main()
