import random, pygame, sys
from src.states.BaseState import BaseState
from src.constants import *
from src.Dependency import *
import src.CommonRender as CommonRender
from src.PowerUp import PowerUp
from src.constants import PADDLE_SPEED

class PlayState(BaseState):
    def __init__(self):
        super(PlayState, self).__init__()
        self.paused = False
        self.powerups = []

    def Enter(self, params):
        self.paddle = params['paddle']
        self.bricks = params['bricks']
        self.health = params['health']
        self.score = params['score']
        self.high_scores = params['high_scores']
        self.ball = params['ball']
        self.level = params['level']

        self.recover_points = 5000

        self.ball.dx = random.randint(-600, 600)
        self.ball.dy = random.randint(-180, -150)

    def Exit(self):
        pass

    def update(self, dt, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
                    gSounds['pause'].play()

        if self.paused:
            return

        self.paddle.update(dt)
        self.ball.update(dt)

        if self.ball.Collides(self.paddle):
            self.ball.rect.y = self.paddle.rect.y - 24
            self.ball.dy = -self.ball.dy

            if self.ball.rect.x + self.ball.rect.width < self.paddle.rect.x + (self.paddle.width / 2) and self.paddle.dx < 0:
                self.ball.dx = -150 + -(8 * (self.paddle.rect.x + self.paddle.width / 2 - self.ball.rect.x))
            elif self.ball.rect.x > self.paddle.rect.x + (self.paddle.width / 2) and self.paddle.dx > 0:
                self.ball.dx = 150 + (8 * abs(self.paddle.rect.x + self.paddle.width / 2 - self.ball.rect.x))

            gSounds['paddle-hit'].play()

        for k, brick in enumerate(self.bricks):
            if brick.alive and self.ball.Collides(brick):
                self.score = self.score + (brick.tier * 200 + brick.color * 50)
                brick.Hit(self.powerups)

                if random.random() < 0.3:
                    powerup_type = random.randint(1, len(powerup_image_list))
                    self.powerups.append(PowerUp(brick.rect.x, brick.rect.y, powerup_type))

                if self.CheckVictory():
                    gSounds['victory'].play()
                    g_state_manager.Change('victory', {
                        'level': self.level,
                        'paddle': self.paddle,
                        'health': self.health,
                        'score': self.score,
                        'high_scores': self.high_scores,
                        'ball': self.ball,
                        'recover_points': self.recover_points
                    })

                if self.ball.rect.x + 6 < brick.rect.x and self.ball.dx > 0:
                    self.ball.dx = -self.ball.dx
                    self.ball.rect.x = brick.rect.x - 24
                elif self.ball.rect.x + 18 > brick.rect.x + brick.width and self.ball.dx < 0:
                    self.ball.dx = -self.ball.dx
                    self.ball.rect.x = brick.rect.x + 96
                elif self.ball.rect.y < brick.rect.y:
                    self.ball.dy = -self.ball.dy
                    self.ball.rect.y = brick.rect.y - 24
                else:
                    self.ball.dy = -self.ball.dy
                    self.ball.rect.y = brick.rect.y + 48

                if abs(self.ball.dy) < 450:
                    self.ball.dy = self.ball.dy * 1.02
                break

        if self.ball.rect.y >= HEIGHT:
            self.health -= 1
            gSounds['hurt'].play()

            if self.health == 0:
                g_state_manager.Change('game-over', {
                    'score': self.score,
                    'high_scores': self.high_scores
                })
            else:
                g_state_manager.Change('serve', {
                    'level': self.level,
                    'paddle': self.paddle,
                    'bricks': self.bricks,
                    'health': self.health,
                    'score': self.score,
                    'high_scores': self.high_scores,
                    'recover_points': self.recover_points
                })

        for powerup in self.powerups:
            powerup.update(dt)
            if powerup.alive and self.paddle.rect.colliderect(powerup.rect):
                self.ApplyPowerUp(powerup)
                powerup.alive = False

        self.powerups = [p for p in self.powerups if p.alive]

    def render(self, screen):
        for brick in self.bricks:
            brick.render(screen)

        self.paddle.render(screen)
        self.ball.render(screen)

        CommonRender.RenderScore(screen, self.score)
        CommonRender.RenderHealth(screen, self.health)

        for powerup in self.powerups:
            powerup.render(screen)

        if self.paused:
            t_pause = gFonts['large'].render("PAUSED", False, (255, 255, 255))
            rect = t_pause.get_rect(center=(WIDTH/2, HEIGHT/2))
            screen.blit(t_pause, rect)

    def ApplyPowerUp(self, powerup):
        if powerup.type == 2:
            self.ball.dx *= 1.2  
            self.ball.dy *= 1.2  

        elif powerup.type == 1:
            self.health = min(3, self.health + 1)
            
        elif powerup.type == 3:  

            self.paddle.dx *= 0.8  

    def CheckVictory(self):
        for brick in self.bricks:
            if brick.alive:
                return False
        return True