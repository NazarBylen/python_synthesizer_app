import pygame

pygame.mixer.pre_init(buffer=1024)
pygame.mixer.init()


def do_play(slug, key):
    pygame.mixer.music.load(f"./public/sounds/{slug}/{key}.mp3")
    pygame.mixer.music.play()

def do_playback():
    playback_sound = pygame.mixer.Sound(f"./public/sounds/playback/1.mp3")
    empty_channel = pygame.mixer.find_channel()
    empty_channel.play(playback_sound)

