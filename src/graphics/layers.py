from __future__ import annotations

from typing import TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    import pygame
    from graphics.screens import Screen
    from level_editor import Editor

from loguru import logger


class Layer(ABC):    

    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def handle_events(self, events: list[pygame.event.Event]) -> None:
        pass
    
    @abstractmethod
    def render(self, screen: Screen, editor: Editor) -> None:
        pass