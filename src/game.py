import pygame
import math

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.triangle = pygame.image.load("assets/triangle.png")  # Load a triangle image
        self.triangle_rect = self.triangle.get_rect(center=(100, 100))  # Initial position
        self.angle = 0  # Initial angle of rotation

    def rotate_triangle(self):
        # Rotate the triangle
        self.angle += 5  # Rotation speed
        if self.angle >= 360:
            self.angle = 0
        self.triangle = pygame.transform.rotate(pygame.image.load("assets/triangle.png"), self.angle)
        self.triangle_rect = self.triangle.get_rect(center=self.triangle_rect.center)

    def update(self):
        self.rotate_triangle()  # Update the triangle’s rotation
        self.screen.blit(self.triangle, self.triangle_rect)  # Draw triangle

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
