import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time  import sleep
from game_stats import GameStats

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

        # Crea una instancia para guardas las estadísticas del juego
        self.stats = GameStats(self)
        
        self.ship = Ship(self)
        self.bullet = pygame.sprite.Group()
        self.alien = pygame.sprite.Group()

        self._create_fleet()
        
        # Color de fondo
        self.bg_color = self.setting.bg_color
        
    
    def run_game(self):
        """Inicia el bucle principal para el juego."""
        while True:
            # Busca eventos de teclado y raton
            self._check_events()
            print(self.stats.game_active)
            if self.stats.game_active:
                # Redibuja la pantalla en cada paso por el bucle
                self.ship.update()
                self._update_bullets()
                self._update_alien()
            
            self._update_screen()
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
        self.alien.draw(self.screen)


    def _update_bullets(self):
        """Actualiza la posición de las balas y las borra si han salido de la pantalla."""
        self.bullet.update()
        #Se deshace e las balas que han esaparecido
        for bullet in self.bullet.copy():
            if bullet.rect.bottom <= 0:
                self.bullet.remove(bullet)
        # Busca balas que hayan dado a los aliens
        # Si hay, se deshace de la bala y del alien
        self._check_bullet_alien_collisions()


    def _check_bullet_alien_collisions(self):
        """Responde a las colisiones bala-alien."""
        # Retirda todas las balas y aliens que ha chocado.
        collisions = pygame.sprite.groupcollide( self.bullet, self.alien, True, True)
        if not self.alien:
            # Destruye las balas exixtentes y crea una flota nueva
            self.bullet.empty()
            self._create_fleet()


    def _update_alien(self):
        """Comprueba si la flota ha llegado al final de la pantalla."""
        self._check_fleet_edges()
        self.alien.update()

        # Busca colisiones alien-nae.
        if pygame.sprite.spritecollideany(self.ship, self.alien):
            self._ship_hit()

        # Busca si ha llegado algun alien al fondo de la pantalla.
        self._check_aliens_bottom()


    def _check_keydown_events(self,event):
        """Responde a pulsaciones de teclas"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_ESCAPE:
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


    def _create_fleet(self):
        """Crea una flota de aliens"""
        alien = Alien(self)

        alien_width, alien_height = alien.rect.size
        available_space_x = self.setting.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determina el numero de filas de aliens que caben en la pantalla.
        ship_height = self.ship.rect.height
        available_space_y = (self.setting.screen_height - (3 * alien_height) - ship_height) 
        number_rows = available_space_y // (2 * alien_height)

        if self.setting.alien_max_rows < number_rows:
            number_rows = self.setting.alien_max_rows

        # Crea la flota de aliens.
        for row_number in range(number_rows):

            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)
    
    
    def _create_alien(self, alien_number, row_number):
        """Crea un alien y lo coloca en la fila"""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.alien.add(alien)


    def _check_fleet_edges(self):
        """Responde adecuadamente sii algún alien ha llegado a un borde."""
        for alien in self.alien.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    
    def _change_fleet_direction(self):
        """Baja toda la flota y cambia su dirección."""
        for alien in self.alien.sprites():
            alien.rect.y += self.setting.fleet_drop_speed
        self.setting.fleet_direction *= -1



    def _ship_hit(self):
        """Responde al impacto de un alien en la nave."""
        if self.stats.ships_left > 0:
            #Disminuye ship_left.
            self.stats.ships_left -= 1

            # Se deshace de los aliens y balas restantes.
            self.alien.empty()
            self.bullet.empty()

            # Crea una nueva flota y centra la nave
            self._create_fleet()
            self.ship.center_ship()

            #Pausa.
            sleep(0.5)
        else:
            self.stats.game_active = False

    

    def _check_aliens_bottom(self):
        """Comprueba si algún alien ha llegado al fondo de la pantalla."""
        screen_rect = self.screen.get_rect()
        for alien in self.alien.sprites():
            if  alien.rect.bottom >= screen_rect.bottom:
                # Trata esto como si la nave hubise sido alcanzada
                self._ship_hit()

if __name__ == '__main__':
    # Hace una instancia al juego y lo ejecuta
    ai = AlienInvasion()
    ai.run_game()