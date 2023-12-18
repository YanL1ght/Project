import pygame
import typing


class Entity():
    def __init__(self, health, pos: list, size: typing.Tuple, v: list, mass):
        self.v = v
        self.position = pos
        self.MAX_HEALTH = health
        self.cur_health = health
        self.MASS = mass
        self.size = size # tuple(width, hight)
        self.is_in_air = True

    def render(self, screen): # куча проверок. Физика, состояние здоровья, скорость
        # Гравитация
        if self.in_air:
            self.speed[1] += 10
        else:
            self.speed[1] = 0

        self.position = [self.position[0] + self.speed[0] / fps, self.position[1] + self.speed[1] / fps]
        rect = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        pygame.draw.rect(screen, pygame.Color('White'), rect=rect)
    
    @property
    def speed(self):
        return self.v

    @speed.setter
    def speed(self, v):
        self.v = v
    
    @property
    def health(self):
        return self.cur_health
    
    @health.setter
    def health(self, new_health):
        self.cur_health = new_health

    @property
    def position(self):
        return self.pos
    
    @position.setter
    def position(self, coords):
        self.pos = coords

    def get_hitbox(self):
        hitbox = pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
        return hitbox
    
    @property
    def in_air(self):
        return self.is_in_air

    @in_air.setter
    def in_air(self, state):
        self.is_in_air = state #Bool
    

if __name__ == '__main__':
    pygame.init()
    size = width, height = 500, 500
    screen = pygame.display.set_mode(size)
    test_entity = Entity(10, [0, 0], (50, 50), [0, 0], 1)
    # test_entity2 = Entity(10, [100, 0], (50, 50), [0, 0], 1)
    platforms = [pygame.Rect(0, 495, 500, 5), pygame.Rect(300, 440, 300, 100)]
    # entities = [test_entity2]
    print(test_entity.speed)
    # print(test_entity2.position)
    fps = 60
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # test_entity.speed[0] += 100
                test_entity.position[1] -= 100
                # test_entity.speed[1] += 100
        screen.fill((0, 0, 0))
        hitboxes = []
        # for entity in entities:
            # hitboxes.append(entity.get_hitbox())
        collided_platforms = test_entity.get_hitbox().collidelistall(platforms)

        if test_entity.get_hitbox().collidelistall(hitboxes):
            test_entity.speed[0] = 0
            test_entity.speed[1] = 0
        elif collided_platforms:
            for collided_index in collided_platforms:
                platform = platforms[collided_index]
                right_side = test_entity.position[0] + test_entity.size[0]
                left_side = test_entity.position[0]
                top_side = test_entity.position[1]
                bottom_side = test_entity.position[1] + test_entity.size[1]
                
                if platform.top <= bottom_side and platform.bottom >= top_side:
                    modifier = abs(bottom_side - platform.top)
                    test_entity.position[1] -= modifier - 1
                    test_entity.in_air = False
                
                if platform.right >= left_side and platform.left >= right_side:
                    modifier = abs(left_side - platform.right)
                    test_entity.position[0] += modifier
                    test_entity.speed[0] = 0
                if platform.left <= right_side and platform.right <= left_side:
                    modifier = abs(right_side - platform.left)
                    test_entity.position[0] -= modifier 
                    test_entity.speed[0] = 0
                if platform.bottom >= top_side and platform.top >= bottom_side:
                    modifier = abs(top_side - platform.bottom)
                    test_entity.position[1] += modifier
                    test_entity.speed[1] = 0
        else:
            test_entity.is_in_air = True

        
        for platform in platforms:
            pygame.draw.rect(screen, pygame.Color('blue'), platform)
        test_entity.render(screen)
        # test_entity2.render(screen)
        clock.tick(fps)
        pygame.display.flip()
        
    pygame.quit()
