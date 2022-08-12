class Settings:
    # Una clase para guardar toda la configuracion del juego
    
    def __init__(self) :
        # inicializa la configuración del juego
        self.screen_width = 1200
        self.screen_height = 640
        self.bg_color = (230, 230, 230)
        
        # Configuración de la nave
        self.ship_speed = 1.5