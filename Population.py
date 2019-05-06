# Population class contains functions that control the
# operations and updating on the bird population. This includes how likely
# certain birds are to reproduce and mutate
from Bird import Bird
import random
import Constants
import pygame
import Stats
from statistics import mean


# simulates a generation change, keep 5 winners, make 5 random children from those winners, mutate 2 of the chidlren
def update_generation(prev_gen, csv_file):
    # sort previous generation by the most fit birds first
    prev_gen.sort(key=lambda x: x.fitness, reverse=True)

    # print scores
    fitness_scores = []
    for bird in prev_gen:
        # print(bird.fitness, end=' ')
        fitness_scores.append(bird.fitness)

    #print('fitness: ', mean(fitness_scores), ' generation: ', Stats.generation, 'highest round: ', Stats.prev_population_score)
    #csv_file.write(str(mean(fitness_scores)) + ', ' + str(Stats.generation) + ', ' + str(Stats.prev_population_score) + '\n')
    # append to new gen
    new_gen = []
    # best gets 5 duplicates, 50% mutated
    for i in range(0, 5):
        new_gen.append(Bird(prev_gen[0], 'None'))
        new_gen[-1].reset()
    # 45 clones, 50% mutated
    for i in range(5, Constants.NUM_START_BIRDS // 6):
        new_gen.append(Bird(prev_gen[i], 'None'))
        new_gen[-1].reset()

    # 50 children of just top population
    for i in range(Constants.NUM_START_BIRDS // 6, Constants.NUM_START_BIRDS // 4):
        new_gen.append(Bird(prev_gen[random.randint(0, 5)], prev_gen[random.randint(0, 10)]))
        new_gen[-1].reset()
    # 50 children of just top population
    for i in range(Constants.NUM_START_BIRDS // 4, Constants.NUM_START_BIRDS // 4 * 3):
        new_gen.append(Bird(prev_gen[random.randint(0, 5)], prev_gen[random.randint(0, 50)]))
        new_gen[-1].reset()
    # more children of general population
    for i in range(Constants.NUM_START_BIRDS // 4 * 3, Constants.NUM_START_BIRDS):
        new_gen.append(Bird(prev_gen[random.randint(0, 50)], prev_gen[random.randint(50, Constants.NUM_START_BIRDS - 1)]))

    for bird in new_gen:
        if random.randint(0, 100) < 30:
            bird.brain.mutate()
            bird.image = pygame.image.load('images/mutant.png')  # change mutated birds image to mutant

    return new_gen
