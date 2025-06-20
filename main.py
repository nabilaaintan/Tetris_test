import pygame ,sys
from game import Game 
from colors import Colors


def handle_touch_input(game, x, y, screen):
    print("Touch at:", x, y)
    if game.game_over:
       game.reset()
    else:
        if y < screen.get_height() * 0.3:
            game.rotate()
        elif y > screen.get_height() * 0.7:
            game.move_down()
            game.update_score(0, 1)
        elif x < screen.get_width() * 0.3:
            game.move_left()
        elif x > screen.get_width() * 0.7:
            game.move_right()

pygame.init()
title_font = pygame.font.Font(None, 47)
score_surface = title_font.render("Score:", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("Game Over!", True, Colors.white)

score_rect = pygame.Rect(320,55,170,60)
next_rect = pygame.Rect(320,215,170,180)

screen = pygame.display.set_mode((320,640))
pygame.display.set_caption("Tetris Game")
game_over_rect = game_over_surface.get_rect()
game_over_rect.centerx = screen.get_width() // 2
game_over_rect.top = 250


clock = pygame.time.Clock()

game = Game()

GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)


while True: 
        for  event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if game.game_over == True:
                    game.game_over == False
                    game.reset()
                if event.key == pygame.K_LEFT and game.game_over == False:
                    game.move_left()
                if event.key == pygame.K_RIGHT and game.game_over == False:
                    game.move_right()
                if event.key == pygame.K_DOWN and game.game_over == False:
                    game.move_down()
                    game.update_score(0,1)
                if event.key == pygame.K_UP and game.game_over == False:
                    game.rotate()
            if event.type == pygame.FINGERDOWN:
                x = event.x * screen.get_width()
                y = event.y * screen.get_height()
                handle_touch_input(game, x, y, screen)

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                handle_touch_input(game, x, y, screen)
            if event.type == GAME_UPDATE and game.game_over == False:
                game.move_down()

        #Drawing
        score_value_surface = title_font.render(str(game.score), True, Colors.white)
        screen.fill(Colors.pink)
        screen.blit(score_surface, (220,10))
        screen.blit(next_surface, (375,180,50,50))
        screen.blit(score_value_surface,(220,40))
    
         game.draw(screen)

        if game.game_over == True:
          screen.blit(game_over_surface, game_over_rect)


        pygame.display.update()
        clock.tick(60)
