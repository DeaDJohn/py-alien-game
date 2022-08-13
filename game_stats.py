class GameStats:
    """Sigue las estadísticas de Alien Invasion."""

    def __init__(self, ai_game):
        """Inicializa las estadísticas."""
        self.settings = ai_game.setting
        self.reset_stats()

        # Inicia Alien Invasion en estado activo.
        self.game_active = True

    def reset_stats(self):
        """Inicializa las estadísticas que se pueden resetear en el juego."""
        self.ships_left = self.settings.ship_limit
