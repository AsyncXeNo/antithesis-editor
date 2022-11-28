from __future__ import annotations

import sys
import warnings
from typing import TYPE_CHECKING

import pygame
from loguru import logger

from graphics.stacks import Stack
from graphics.screens import Screen
from graphics.graphics import PygameAbstraction
from graphics.constants import RESOLUTION
from screens.level_editor_screen import LevelEditorScreen

warnings.filterwarnings("ignore")
event_logger_format: str = "<g>{time:YYYY-MM-DD HH:mm:ss}</g> <c>{name}</c> <magenta>>></magenta> <lvl>{message}</lvl>"
logger.remove()
logger.add(sink='logs/app.log', mode='w', level="DEBUG", format=event_logger_format, diagnose=False)
logger.add(sink=sys.stdout, colorize=True, level="DEBUG", format=event_logger_format, diagnose=False)


class Editor(object):
    """Editor for antithesis"""

    def __init__(self) -> None:
        self.pygame_abs: PygameAbstraction = PygameAbstraction(*RESOLUTION, 'Antithesis Editor', fullscreen=False)
        self.screens: Stack[Screen] = Stack[Screen]()
        self.running: bool = True
        self.mainloop()

    def events_handler(self) -> None:
        """Events handler of the editor"""

        events = pygame.event.get()
        
        for event in events:
            if event.type == pygame.QUIT:  
                
                # TODO: push confirmation screen
                # self.screens.push(ConfirmationScreen()) ??

                pygame.quit()
                self.running = False
                return
                
        self.screens.get_top().handle_events(events)
        
    def graphics_handler(self) -> None:
        """Graphics handler of the editor"""

        self.pygame_abs.window.fill(pygame.Color('black'))
        
        for name, screen in self.screens:
            screen.clear()
            screen.render(self)
            self.pygame_abs.window.blit(screen.surface, (0,0))

        pygame.display.update()

    def mainloop(self) -> None:
        """Main loop of the editor"""

        self.screens.push(LevelEditorScreen(self.pygame_abs), 'Main')

        while self.running:
            self.graphics_handler()
            self.events_handler()
    