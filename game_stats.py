class GameStats:
    """Sigue las estadísticas de Alien Invasion."""

    def __init__(self, ai_game):
        """Inicializa las estadísticas."""
        self.settings = ai_game.setting
        self.reset_stats()

        # Inicia Alien Invasion en estado inactivo.
        self.game_active = False

         # La puntuación mas alta no debería restablecerse nunca.
        self.high_score = 0

    def reset_stats(self):
        """Inicializa las estadísticas que se pueden resetear en el juego."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
