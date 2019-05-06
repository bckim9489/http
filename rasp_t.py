import pygame

music_file = "./Side_Right.wav"

freq = 24000
bitsize = -16
channels = 1
buffer = 2048

pygame.mixer.init(freq, bitsize, channels, buffer)
pygame.mixer.music.load(music_file)
pygame.mixer.music.play()
clock = pygame.time.Clock()

while pygame.mixer.music.get_busy():
	clock.tick(30)
pygame.mixer.quit()
