from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pygame
    from graphics.graphics import PygameAbstraction
    from level_editor import Editor

from graphics.surface import Surface 
from graphics.screens import Screen
from graphics.stacks import Stack
from graphics.layers import Layer
from graphics.constants import RESOLUTION


class LevelEditorScreen(Screen):

    def __init__(self, pygame_access: PygameAbstraction) -> None:
        self.pygame_access: PygameAbstraction = pygame_access
        self.surface: Surface = Surface(RESOLUTION, [0,0])
        self.layers: Stack[Layer] = Stack[Layer]()

    def clear(self):
        self.surface.fill((0,0,0,0))

    def handle_events(self, events: list[pygame.event.Event]) -> None:
        pass

    def render(self, editor: Editor) -> None:
        self.pygame_access.draw_circle((255,255,255,255), tuple([x//2 for x in RESOLUTION]), 100, surface=self.surface)