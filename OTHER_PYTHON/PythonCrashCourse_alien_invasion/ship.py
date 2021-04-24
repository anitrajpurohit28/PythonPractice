import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rectangle.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag
        self.move_right = False
        self.move_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # update the ship's x value, not the rect.
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.move_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object for self.x
        self.rect.x = self.x
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
