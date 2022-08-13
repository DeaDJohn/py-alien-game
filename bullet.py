import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Una clase para gestionar las balas disparadas desde la nave."""

    def __init__(self , ai_game):
        """Crea un objeto para la baja en la posición actual de la nave."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.setting
        self.color = self.settings.bullet_color
        
        # Crea una bala en la posición actual de la nave.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Almacena la posición de la bala como un decimal.
        self.y = float(self.rect.y)

    def update(self):
        """Mueve la bala hacia arriba."""
        # Actualiza la posición de la bala en el eje y.
        self.y -= self.settings.bullet_speed
        # Actualiza la posición de la bala.
        self.rect.y = self.y

    def draw_bullet(self):
        """Dibuja la bala en la pantalla."""
        pygame.draw.rect(self.screen, self.color, self.rect)