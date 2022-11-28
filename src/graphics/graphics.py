from __future__ import annotations

from typing import Optional

import pygame
from loguru import logger


class PygameAbstraction(object):
    """Acts as an easy-to-use anchor between my code and pygame's code"""

    def __init__(self: PygameAbstraction, width: int, height: int, caption: str, fullscreen: bool = False):
        pygame.init()

        self.width: int = width
        self.height: int = height
        self.caption: str = caption
        self.image_path = 'res/images/'

        self.window: pygame.surface.Surface = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN if fullscreen else 0)

        pygame.display.set_caption(self.caption)

    # shapes

    def draw_line(self: PygameAbstraction, color: tuple[int, int, int, int], start: tuple[int, int], end: tuple[int, int], width: int = 1, surface: Optional[pygame.surface.Surface] = None) -> pygame.rect.Rect:
        """Draws a line of given width (default 1) on a surface (default main window surface)"""

        if surface is None:
            surface = self.window

        return pygame.draw.line(surface, color, start, end, width)

    def draw_lines(self: PygameAbstraction, color: tuple[int, int, int, int], points: list[tuple[int, int]], width: int = 1, closed: bool = False, surface: Optional[pygame.surface.Surface] = None) -> pygame.rect.Rect:
        """Draws multiple lines on the screen with given width (default 1) connecting all the points in the given sequence on a surface (default main window surface)"""

        if not surface:
            surface = self.window

        return pygame.draw.lines(surface, color, closed, points, width)

    def draw_circle(self: PygameAbstraction, color: tuple[int, int, int, int], center: tuple[int, int], radius: int, quadrants: int = 0b1111, width: int = 0, surface: Optional[pygame.surface.Surface] = None) -> pygame.rect.Rect:
        """Draws the specified quadrants of the circle (default 0b1111) on a surface (default main window surface)"""

        if not surface:
            surface = self.window

        new_quadrants = [bool(quadrants & 0b1000), bool(quadrants & 0b100), bool(quadrants & 0b10), bool(quadrants & 0b1)]

        return pygame.draw.circle(surface, color, center, radius, width, *new_quadrants)

    def draw_rect(self: PygameAbstraction, color: tuple[int, int, int, int], rect_x: int, rect_y: int, rect_width: int, rect_height: int, width: int = 0, surface: Optional[pygame.surface.Surface] = None) -> pygame.rect.Rect:
        """Draws a rectangle with given dimensions on a surface (default main window surface)"""

        if not surface:
            surface = self.window

        return pygame.draw.rect(surface, color, pygame.Rect(rect_x, rect_y, rect_width, rect_height), width)

    def draw_polygon(self: PygameAbstraction, color: tuple[int, int, int, int], points: list[tuple[int, int]], width: int = 0, surface: Optional[pygame.surface.Surface] = None) -> pygame.rect.Rect:
        """Draws a polygon using the given points on a surface (defualt main window surface)"""

        if not surface:
            surface = self.window

        return pygame.draw.polygon(surface, color, points, width)

    # Images

    def convert_to_pygame_image(self: PygameAbstraction, name: str) -> Optional[pygame.surface.Surface]:
        """Loads and returns a pygame image with given name"""

        try:
            image = pygame.image.load(f'{self.image_path}{name}')
        except FileNotFoundError:
            logger.error(f'Invalid image file path {self.image_path}{name}. Ignoring load request')
            return

        return image

    def blit_image(self: PygameAbstraction, pos: tuple[int, int], image_name: str, width: int = 0, height: int = 0, surface: Optional[pygame.surface.Surface] = None) -> Optional[pygame.rect.Rect]:  # type: ignore
        """Blits an image to a surface (default main window surface)"""

        if not surface:
            surface: pygame.surface.Surface = self.window

        image = self.convert_to_pygame_image(image_name)

        if not image:
            logger.error('No image file found. Ignoring blit request')
            return

        image_size = (
            width if width > 0 else int(image.get_width()),
            height if height > 0 else int(image.get_height())
        )

        image = pygame.transform.scale(image, image_size)

        return surface.blit(image, pos)