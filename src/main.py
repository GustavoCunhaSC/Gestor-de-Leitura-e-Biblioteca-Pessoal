

import tkinter as tk
from interface.telas import tela_inicial

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal
    tela_inicial()
    root.mainloop()

