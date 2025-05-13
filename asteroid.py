import circleshape, constants, pygame, random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
         super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position,self.radius, 2)
    
    def update(self,dt):
        self.position += self.velocity*dt
    
    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        rand_angle = random.uniform(20,50)
        vect_1 = self.velocity.rotate(rand_angle)
        vect_2 = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        a1 = Asteroid(self.position.x,self.position.y,new_radius)
        a2 = Asteroid(self.position.x,self.position.y,new_radius)
        a1.velocity = vect_1 * 1.2
        a2.velocity = vect_2 * 1.2

        