import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('ex021 Tocando um Mp3.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()


