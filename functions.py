import pygame
#import gameLoop

def paused(pause, screen, clock):

    font = pygame.font.Font(None, 74)
    text = font.render("PAUSED", 1, (255,255,255))
    screen.blit(text, (150,250))

    while (pause):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
              if event.key == pygame.K_p:
                  screen.fill((255,255,255))
                  pause = False
              
              if event.key == pygame.K_ESCAPE:
                  pause = False
        
        pygame.display.update()
        clock.tick(60)

def win(scoreA, scoreB, screen, winner_check):
    font = pygame.font.Font(None, 74)
    
    if (scoreA == 10):
        text = font.render("Player One Wins", 1, (255,255,255))
        screen.blit(text, (50,250))
        winner_check = True
    
    if (scoreB == 10):
        text = font.render("Player Two Wins", 1, (255,255,255))
        screen.blit(text, (50,250))
        winner_check = True

    while (winner_check):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                winner_check = False
                return False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    return True
                    
        pygame.display.flip()
