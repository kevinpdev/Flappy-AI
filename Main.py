# Main File
# Runs the Flappy Bird AI simulation
import Graphics
from Rectangle import *
from Game import Game
import pygame
from Bird import Bird
import Population
import Stats


pygame.init()
screen = pygame.display.set_mode((Constants.SCREEN_WIDTH, Constants.SCREEN_HEIGHT))

file = 1
while file <= 10:
    # make first population
    birds_for_generation = [Bird('None', 'None') for i in range(Constants.NUM_START_BIRDS)]

    out_file = open('stats' + str(file) + '.csv', 'w')
    out_file.write('fitness, generation, highest round\n')
    # load starting graphics that don't need to be reloaded
    # Graphics.load_static_gfx()
    # loops the whole simulation
    done = 0
    Stats.generation = 0
    while done < 30:
        game = Game(birds_for_generation)
        done_generation = False

        # loops each generation
        while not done_generation:
            screen.fill(Constants.WHITE)
            game.update_obstacles()
            game.draw_game(screen)
            Graphics.draw_stats(screen)
            Graphics.draw_key(screen)
            # game.check_actions returns True if all the birds are dead
            if game.check_actions(game.birds):
                done_generation = True

            # pygame specific functions
            pygame.display.update()
            pygame.display.flip()

            # check to quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Reached quit in check_actions function, quitting now...")
                    exit(0)

        # update statistics and make a new population by mutation and crossover
        Stats.generation += 1
        birds_for_generation = Population.update_generation(birds_for_generation, out_file)
        done += 1
    file += 1

