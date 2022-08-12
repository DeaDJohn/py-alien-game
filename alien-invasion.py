import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion :
    """Clase general para gestionar los recursos y el comportamiento del juego."""
    
    def __init__(self) :
        """Inicializa el juego y crea los recursos"""
        pygame.init()
        self.setting = Settings()
                
        self.screen = pygame.display.set_mode((self.setting.screen_width, self.setting.screen_height))
        pygame.display.set_caption("Alien invasion")
        
        self.ship = Ship(self)
        
        # Color de fondo
        self.bg_color = self.setting.bg_color
        
    
    def run_game(self):
        """Inicia el bucle principal para el juego."""
        while True:
            # Busca eventos de teclado y raton
            self._check_events()
            # Redibuja la pantalla en cada paso por el bucle
            self._update_screen()
            
            # Hace visible la ultima pantalla dibujada
            pygame.display.flip()
            
    def _check_events(self):
        """Responde a los eventos de teclado y raton."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.rect.x += 1
                
    def _update_screen(self):
        """Actializa las imágenes de la pantalla y cambia la pantalla nueva."""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        
if __name__ == '__main__':
    # Hace una instancia al juego y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()