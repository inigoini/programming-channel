#!/usr/bin/env python3

import os
import pygame

# Inits pygame engine
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

#surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
surface = pygame.display.set_mode((400, 400))

# Set dark background
background = pygame.Surface(surface.get_size())
background.fill((20, 20, 20))

layer = pygame.sprite.LayeredDirty()
layer.clear(surface, background)

mario_source = pygame.image.load(os.path.join('assets', 'mario.png')).convert()

mario = pygame.sprite.DirtySprite()
mario.image = mario_source
mario.image.set_colorkey((255, 0, 255))
mario.rect = pygame.Rect(0, 0, 64, 96)

layer.add(mario)

fps = 40
clock = pygame.time.Clock()
running = True

# Main game loop
while running:

	# Manages events
	events = pygame.event.get()
	for event in events:
		keys = pygame.key.get_pressed()
		if event.type == pygame.QUIT:
			running = False

	# Adds logic
	#update()

	# Paints screen
	rects = layer.draw(surface)
	pygame.display.update(rects)

	# Waits, frames per second
	clock.tick(fps)

pygame.mixer.quit()
pygame.quit()
