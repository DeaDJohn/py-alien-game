import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """Una clase para gestionar la nave."""
    
    
    def __init__(self, ai_game):
        """Inicializa la nave y configura su posición inicial"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.setting
        
        # Carga la imagen de la nave y obtiene su rect
        self.image = pygame.image.load("images/ship.bmp")
        self.image = pygame.transform.scale(self.image, (self.settings.ship_width, self.settings.ship_height))
        self.rect = self.image.get_rect()

        
        # Coloca inicialmente cada nave nueva en el centro de la parte inferior de la pantalla
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Guarda un valor decimal para la posición horizontal de la nave
        self.x = float(self.rect.x)
        
        # bandera movimiento derecha
        self.moving_right = False
        # Bandera movimiendo izquierda
        self.moving_left = False
        
    def update(self):
        """Actualiza la posición de la nave en funcion de la bandera de movimiento."""
        # Actualiza el valor x de la nave no del rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        # actualiza el objeto rect de self.x
        self.rect.x = self.x
            
            
    def blitme(self):
        """Dibuja la nave en su ubucación inicial"""
        self.screen.blit(self.image, self.rect)
    

    def center_ship(self):
        """Centra la nave en la parte inferior de la pantalla."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        