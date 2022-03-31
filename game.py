import random
from ball import Ball
from functions import *
from player import Player
from pygame.locals import *
from pygame import *

white = (255,255,255)
black = (0,0,0)

pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("theme.wav") 
pygame.mixer.music.play(-1,0.0)

screen = pygame.display.set_mode([500, 500])
pygame.display.set_caption("OUR GAME")

paddleA = Player((255,255,255), 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 250

paddleB = Player((255,255,255), 10, 100)
paddleB.rect.x = 470
paddleB.rect.y = 250

ball = Ball((255,255,255), 20, 20)
ball.rect.x = 250
ball.rect.y = 250

sprites_list = pygame.sprite.Group()
sprites_list.add(paddleA)
sprites_list.add(paddleB)
sprites_list.add(ball)

def gameLoop():
  scoreA = 0
  scoreB = 0
  clock = pygame.time.Clock()
  check = True

  while check:
    keys = key.get_pressed()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        check = False

      elif event.type == pygame.KEYDOWN:
        if (event.key == pygame.K_x):
          check = False
        if (event.key == pygame.K_p):
          paused(True, screen, clock)
    if (keys[K_w]):
        paddleA.moveUp()
        
    if (keys[K_s]):
        paddleA.moveDown()

    if keys[K_DOWN]:
        paddleB.moveDown()
        
    if keys[K_UP]:
        paddleB.moveUp()

    if (ball.rect.x >= 500):
      scoreA += 1
      ball.rect.x = 420
      ball.rect.y = random.randint(0, 300)
      ball.velocity[0] = -ball.velocity[0]
    
    if (ball.rect.x <= -1):
      scoreB += 1
      ball.rect.x = 55
      ball.rect.y = random.randint(0, 300)
      ball.velocity[0] = -ball.velocity[0]
    
    if (ball.rect.y > 475 or ball.rect.y < 0):
      ball.velocity[1] = -ball.velocity[1]
    
    if (pygame.sprite.collide_mask(ball, paddleA)):
      ball.velocity[0] *= -1
      ball.rect.x = paddleA.rect.right
      ball.velocity[1] = random.randint(-8, 8)
    
    if (pygame.sprite.collide_mask(ball, paddleB)):
      ball.velocity[0] *= -1
      ball.rect.right = paddleB.rect.x
      ball.velocity[1] = random.randint(-8, 8)

    sprites_list.update()
    screen.fill((0,0,0))
    sprites_list.draw(screen)

    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, (255,255,255))
    screen.blit(text, (150,10))
    text = font.render(str(scoreB), 1, (255,255,255))
    screen.blit(text, (350,10))

    if (win(scoreA, scoreB, screen, False) == True):
      gameLoop()
    
    else:
      pygame.quit()

    pygame.display.flip()
    clock.tick(60)

gameLoop()