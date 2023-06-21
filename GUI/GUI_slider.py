'''
CLASE SLIDER
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=invalid-name


from gui_widget import * 

class Slider(Widget):

    def __init_(self):
        pass

    def close(self):
        self.active = False

    def verificar_dialog_result(self):
        return self.hijo == None or self.hijo.dialog_result != None

    def render(self):
        pass

    def update(self, lista_eventos):
        pass