import pygame ,sys
from game import Game
from colors import Colors

pygame.init()
title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("Game Over", True, Colors.white)

score_rect = pygame.Rect(320,55,170,60)
next_rect = pygame.Rect(320,215,170,180)

screen = pygame.display.set_mode((320,640))
pygame.display.set_caption("Tetris Game")

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
            if event.type == GAME_UPDATE and game.game_over == False:
                game.move_down()

        #Drawing
        score_value_surface = title_font.render(str(game.score), True, Colors.white)
        screen.fill(Colors.pink)
        screen.blit(score_surface, (10,5))
        screen.blit(next_surface, (375,180,50,50))
        screen.blit(score_value_surface,(10,40))

        if game.game_over == True:
          screen.blit(game_over_surface, (10,400))
        
        game.draw(screen)


        pygame.display.update()
        clock.tick(60)
        def main():
                if __name__ == "__main__":
                  main()
