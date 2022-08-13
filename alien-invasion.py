import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion :
    """Clase general para gestionar los recursos y el comportamiento del juego."""
    
    def __init__(self) :
        """Inicializa el juego y crea los recursos"""
        pygame.init()
        self.setting = Settings()
                
        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.setting.screen_height = self.screen.get_rect().height
        self.setting.screen_width = self.screen.get_rect().width
        pygame.display.set_caption("Alien invasion")
        
        self.ship = Ship(self)
        self.bullet = pygame.sprite.Group()
        
        # Color de fondo
        self.bg_color = self.setting.bg_color
        
    
    def run_game(self):
        """Inicia el bucle principal para el juego."""
        while True:
            # Busca eventos de teclado y raton
            self._check_events()
            # Redibuja la pantalla en cada paso por el bucle
            self._update_screen()
            self.ship.update()
            self.bullet.update()

            # Se deshace de las balas que han salido de la pantalla.
            for bullet in self.bullet.copy():
                if bullet.rect.bottom <= 0:
                    self.bullet.remove(bullet)
            
            # Hace visible la ultima pantalla dibujada
            pygame.display.flip()


    def _check_events(self):
        """Responde a los eventos de teclado y raton."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
                
    def _update_screen(self):
        """Actializa las imágenes de la pantalla y cambia la pantalla nueva."""
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullet.sprites():
            bullet.draw_bullet()


    def _check_keydown_events(self,event):
        """Responde a pulsaciones de teclas"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_events(self, event):
        """Responde a la liberación de las teclas"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False 


    def _fire_bullet(self):
        """Dispara una bala si no hay otra bala en la pantalla"""
        if len(self.bullet) < self.setting.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullet.add(new_bullet)


if __name__ == '__main__':
    # Hace una instancia al juego y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()