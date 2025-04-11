class Level:
    def __init__(self, grid_size=6):
        self.grid_size = grid_size
        self.obstacles = []  # List to hold obstacle positions
        self.goal = (5, 5)  # Target position

    def add_obstacle(self, x, y):
        self.obstacles.append((x, y))

    def draw(self, screen):
        # Draw the grid and obstacles
        for x in range(self.grid_size):
            for y in range(self.grid_size):
                pygame.draw.rect(screen, (200, 200, 200), pygame.Rect(x * 100, y * 100, 100, 100), 1)
        for obstacle in self.obstacles:
            pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(obstacle[0] * 100, obstacle[1] * 100, 100, 100))
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(self.goal[0] * 100, self.goal[1] * 100, 100, 100))  # Goal

