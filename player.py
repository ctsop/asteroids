from circleshape import *
from shot import *
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN, WHITE
class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)

        self.rotation = 0
        self.timer = 0
        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    

    def draw(self, screen):
        pygame.draw.polygon(screen, WHITE, self.triangle(), 2)

    
    def rotate(self, dt, direction):
        self.rotation += PLAYER_TURN_SPEED * dt * direction


    def move(self, dt, direction):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction

    def shoot(self):
        if self.timer > 0:
            return
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = (pygame.Vector2(0, 1).rotate(self.rotation)) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN
        

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt
        self.timer = max(self.timer, 0)

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(dt, -1)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt, 1)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt, 1)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(dt, -1)
        if keys[pygame.K_SPACE]:
            self.shoot()