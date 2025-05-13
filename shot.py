import circleshape, constants, pygame

class Shot(circleshape.CircleShape):
    def __init__(self, x, y):
         super().__init__(x,y,constants.SHOT_RADIUS)
         self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position,constants.SHOT_RADIUS, 2)
    
    def update(self,dt):
        self.position += self.velocity*dt