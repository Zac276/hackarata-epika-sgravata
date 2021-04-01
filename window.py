import PySimpleGUI as sg

class window:
    def __init__(self, title, layout, margins):
        self.title = title
        self.layout = layout
        self.margins = margins
    
    def create(self):
        sg.Window(title = self.title, layout = self.layout, margins = self.margins).read()

# win = window("prova", 
#     [
#         [sg.Text("provafgk")],
#         [sg.Button("OK")]
#     ], 
#     (100, 200)
#  )
# win.create()