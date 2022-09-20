import pygame, sys, time, random
from pygame.locals import *
from player import Player


def main():

    #Inicializa as libs
    pygame.init()
    pygame.font.init()

    #cores
    white = (255, 255, 255)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    black = (0, 0, 0)   

    player = Player()
    player_sprite = Player.sprite

    x = player.position.x
    y = player.position.y

    speed = player.speed
    acceleration = player.acceleration

    font = pygame.font.Font("freesansbold.ttf", 32)

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    while True:

        screen.fill(black)

        y += -speed
        x += acceleration

        instruções = font.render('''S para adicionar aceleração á direita, D para á esquerda, W para aumentar a velocidade, S para diminuir a velocidade. Utilize a virgula para sair''', False, white)

        velocidade = font.render(f"velocidade: {round(speed, 2)}", False, white)
        posição_x =  font.render(f"A posição X é: {round(x, 2)}", False, white)
        posição_y =  font.render(f"A posição y é: {round(y, 2)}", False, white)
        aceleração = font.render(f"aceleração: {round(acceleration, 2)}", False, white)

        screen.blit(instruções, (0, 13))
        screen.blit(velocidade, (0, 100))
        screen.blit(aceleração, (0, 150))
        screen.blit(posição_x,  (0, 200))
        screen.blit(posição_y,  (0, 250))
        screen.blit(player_sprite, (x, y))

        for event in pygame.event.get():

            if event.type == pygame.KEYUP:
                if event.key == K_a:
                    acceleration += -0.1
                    
            if event.type == pygame.KEYUP:
                if event.key == K_d:
                    acceleration += 0.1

            if event.type == pygame.KEYUP:
                if event.key == K_s:
                    speed -= 0.03

            if event.type == pygame.KEYUP:
                 if event.key == K_w:
                     speed += 0.03

            if event.type == pygame.KEYUP:
                if event.key == K_COMMA:
                     pygame.quit()
                     sys.exit()

        pygame.display.update()


if __name__ == '__main__':
 main()