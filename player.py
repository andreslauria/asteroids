import circleshape, constants, pygame, shot

class Player(circleshape.CircleShape):
    
    timer = 0
    
    def __init__(self,x,y):
        super().__init__(x,y,constants.PLAYER_RADIUS)
        self.rotation = 0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)
        
    def rotate(self,dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt
        
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer-= dt
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer >= 0:
                return
            self.shoot()
                
            
            
    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_SPEED * dt
        
    def shoot(self):
        self.timer = constants.PLAYER_SHOOT_COOLDOWN
        sh = shot.Shot(self.position.x, self.position.y)
        sh.velocity = pygame.Vector2(0,1)
        sh.velocity = sh.velocity.rotate(self.rotation)
        sh.velocity = sh.velocity * constants.PLAYER_SHOOT_SPEED
        