from turtle import speed
import pygame

class Player:
    position = pygame.Vector2()
    position.xy = 1130, 666
    speed = pygame.Vector2()
    speed = 0.06
    acceleration = 0
    sprite = pygame.image.load('sprites/player.png')