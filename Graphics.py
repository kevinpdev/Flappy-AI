# The Graphics class contains functions for drawing
# using the PyGame Graphics Library
import pygame
import Constants
import Stats


def draw_background(surface):
    bg_image = pygame.image.load('images/background.png')
    surface.blit(bg_image, (0, 0))


# draws a bird, pos is in form (x, y, width, height)
def draw_bird(bird, surface, color):
    surface.blit(bird.image, (bird.x, bird.y))


def draw_obstacle(surface, obstacle):
    pygame.draw.rect(surface, Constants.WHITE, obstacle.top_rect.pos, Constants.RECTANGLE_THICKNESS)
    pygame.draw.rect(surface, Constants.WHITE, obstacle.bottom_rect.pos, Constants.RECTANGLE_THICKNESS)


def draw_stats(surface):
    pygame.draw.rect(surface, (10, 10, 10), (0, 0, Constants.SCREEN_WIDTH, 60))
    my_font = pygame.font.Font('images/mario.ttf', 20)
    # draw score
    score_surface = my_font.render("Score: " + str(Stats.current_score), False, (250, 250, 250))
    surface.blit(score_surface, (10, 10))
    # draw generation
    generation_surface = my_font.render("Generation: " + str(Stats.generation), False, (250, 250, 250))
    surface.blit(generation_surface, (10, 30))
    # draw title
    title_font = pygame.font.Font('images/mario.ttf', 50)
    generation_surface = title_font.render("Flappy AI", False, (250, 250, 250))
    surface.blit(generation_surface, (Constants.SCREEN_WIDTH / 2 - 160, 10))
    # draw highest score
    score_surface = my_font.render("Highest Score: " + str(Stats.highest_score), False, (250, 250, 250))
    surface.blit(score_surface, (Constants.SCREEN_WIDTH - 220, 10))
    #draw number alive
    score_surface = my_font.render("Alive: " + str(Stats.num_alive) + " / " + str(Constants.NUM_START_BIRDS), False, (250, 250, 250))
    surface.blit(score_surface, (Constants.SCREEN_WIDTH - 220, 30))


def draw_key(surface):
    pygame.draw.rect(surface, (10, 10, 10), (0, 60, Constants.SCREEN_WIDTH, 40))
    my_font = pygame.font.Font('images/mario.ttf', 20)
    # draw start bird
    bird_image = pygame.image.load('images/bird.png')
    surface.blit(bird_image, (10, 60))
    text_surface = my_font.render(": Random", False, (250, 250, 250))
    surface.blit(text_surface, (60, 70))
    # draw child bird
    bird_image = pygame.image.load('images/child.png')
    surface.blit(bird_image, (210, 60))
    text_surface = my_font.render(": Child", False, (250, 250, 250))
    surface.blit(text_surface, (260, 70))
    # draw mutant bird
    bird_image = pygame.image.load('images/mutant.png')
    surface.blit(bird_image, (410, 60))
    text_surface = my_font.render(": Mutant", False, (250, 250, 250))
    surface.blit(text_surface, (460, 70))
    # draw clone bird
    bird_image = pygame.image.load('images/clone.png')
    surface.blit(bird_image, (610, 60))
    text_surface = my_font.render(": Clone", False, (250, 250, 250))
    surface.blit(text_surface, (660, 70))


