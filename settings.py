class Settings:
    # Una clase para guardar toda la configuracion del juego
    
    def __init__(self) :
        # inicializa la configuración del juego
        self.screen_width = 1200
        self.screen_height = 640
        self.bg_color = (230, 230, 230)
        
        # Configuración de la nave
        self.ship_limit = 3
        self.ship_width = 100
        self.ship_height = 100


        # Configuración de la bala
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 50

        #configuración del alien
        self.fleet_drop_speed = 10
        self.alien_max_rows = 5
        self.alien_width = 100
        self.alien_height = 100

        #Rapidez con la que se acelera el juego
        self.speedup_scale = 1.1

        # Rapidez que aumenta el valor de los puntos de los aliens
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    
    def initialize_dynamic_settings(self):
        # inicializa las configuraciones que cambian con el tiempo
        self.ship_speed = 5.0
        self.bullet_speed = 10.0
        self.alien_speed = 5.0
        # fleet_direction = 1 representa derecha; -1 representa izquierda
        self.fleet_direction = 1
        self.alien_points = 50
        # puntuación
        self.alien_points = 50

    def increase_speed(self):
        """Incrementa las cofiguraciones de velocidad."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
