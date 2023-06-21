'''
CLASE TEXTBOX
'''

# pylint: disable=missing-function-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=unused-wildcard-import
# pylint: disable=wildcard-import

import unicodedata
import pygame
from pygame.locals import *
from gui_widget import *

FPS = 18


class TextBox(Widget):
    def __init__(
            self, screen, master_x, master_y, x, y, w, h,
            bg_color, selecter_bg_color, border_color, selected_border_color, border_size,
            font, font_size, font_color
    ):

        super().__init__(screen, x, y, w, h, bg_color, border_color, border_size)

        pygame.font.init()  # llamo para que no pinche
        self._default_bg_color = bg_color
        self._default_border_color = border_color
        self._selected_bg_color = selecter_bg_color
        self._selected_border_color = selected_border_color
        self._text = ""
        self._font = pygame.font.SysFont(font, font_size)
        self._font_color = font_color
        self._master_x = master_x
        self._master_y = master_y

        self.is_selected = False

        self.render()

    def get_text(self):
        return self._text

    def set_text(self, text):
        self._text = text
        self.render()

    def render(self):
        image_text = self._font.render(
            self._text, True, self._font_color, self._bg_color)
        # Superficie que se adapte a la del
        self._slave = pygame.surface.Surface((self._w, self._h))

        self.slave_rect_x = self._x
        self.slave_rect_y = self._y
        self.slave_rect_collide = pygame.Rect(self.slave_rect)

        self._slave.fill(self._bg_color)

        media_texto_horizontal = image_text.get_width() / 2
        media_texto_vertical = image_text.get_height() / 2

        media_horizontal = self._w / 2
        media_vertical = self._h / 2

        diferencia_horizontal = media_horizontal - media_texto_horizontal
        diferencia_vertical = media_vertical - media_texto_vertical

        self._slave.blit(
            image_text, (diferencia_horizontal, diferencia_vertical))

    def update(self, lista_eventos):

        for evento in lista_eventos:

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if self.slave_rect_collide.collidepoint(evento.pos):
                    self._bg_color = self._selected_bg_color
                    self._border_color = self._selected_border_color
                    self.is_selected = True
                else:
                    self._bg_color = self._default_bg_color
                    self._border_color = self._default_border_color
                    self.is_selected = False
                self.render()
            elif self.is_selected and evento.type == pygame.KEYDOWN:
                character = evento.unicode
                if evento.key == pygame.K_BACKSPACE:
                    self._text = self._text[:-1]
                elif len(character) == 1 and unicodedata.category(character)[0] != 'C':
                    self_text += character
                self.render()
        self.draw()
