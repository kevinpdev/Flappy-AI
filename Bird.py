# represents Bird object that is instantiated each round
# each Bird has their own "brain" which is a NeuralNetwork Object
import pygame
import Constants
from NeuralNetwork import NeuralNetwork


class Bird:
    def __init__(self, parent1, parent2):
        # asexual reproduction, exact clone
        if parent1 != 'None' and parent2 == 'None':
            # all birds start out in same position
            self.x = 100
            self.y = 200
            # width and height need to be adjusted to whatever the dimensions of the picture are
            self.width = 50
            self.height = 34
            self.image = pygame.image.load('images/clone.png')

            self.gravity = Constants.GRAVITY
            self.acceleration = 0
            self.score = 0
            # Game won't draw the bird if it is dead
            self.dead = False

            # Neural network variables
            self.brain = parent1.brain
            self.horizontal_distance = 0  # right edge of closest obstacle - self.x
            self.vertical_distance = 0  # bottom edge of top rectangle of closest obstacle - self.y
            self.ground_distance = 0
            self.velocity = 0
            self.fitness = 0  # total traveled distance - horzontal distance
        else:
            # all birds start out in same position
            self.x = 100
            self.y = 200
            # width and height need to be adjusted to whatever the dimensions of the picture are
            self.width = 50
            self.height = 34

            # image
            if parent1 == 'None' and parent2 == 'None':
                self.image = pygame.image.load('images/bird.png')
            else:
                self.image = pygame.image.load('images/child.png')

            # initialize bird variables
            self.gravity = Constants.GRAVITY
            self.acceleration = 0
            self.score = 0

            # Game won't draw the bird if it is dead
            self.dead = False
            # brain is it's Neural Network, every bird has its own Neural network
            self.brain = NeuralNetwork(parent1, parent2)
            self.horizontal_distance = 0         # right edge of closest obstacle - self.x
            self.vertical_distance = 0           # bottom edge of top rectangle of closest obstacle - self.y
            self.ground_distance = 0
            self.velocity = 0
            self.fitness = 0                     # total traveled distance - horizontal distance

    # simulates a bird jumping
    def jump(self):
        self.acceleration = Constants.BIRD_JUMP_ACCELERATION

    # simulates the bird's physics with acceleration and velocity variables
    def update_position(self):
        self.acceleration += Constants.BIRD_ACCELERATION_DOWN
        self.velocity = self.gravity + self.acceleration
        self.y += self.velocity

    # the fitness(objective) function is simply the birds distance
    # the birds that travel farther will have a higher fitness score
    def update_fitness(self, bird_distance):
        self.fitness += bird_distance

    # resets different attributes when copying bird to new population
    def reset(self):
        self.horizontal_distance = 0  # right edge of closest obstacle - self.x
        self.vertical_distance = 0  # bottom edge of top rectangle of closest obstacle - self.y
        self.ground_distance = 0
        self.velocity = 0
        self.fitness = 0  # total traveled distance - horzontal distance
        self.dead = False
        self.acceleration = 0
        self.score = 0

    # returns the closest obstacle to the bird
    @staticmethod
    def get_closest_obstacle(game, bird):
        for obstacle in reversed(game.obstacles):
            if bird.x < obstacle.right_edge:
                return obstacle

    # updates the distances from the bird to the closest obstacle and the ground
    @staticmethod
    def update_distances(game, bird):
        closest_obstacle = bird.get_closest_obstacle(game, bird)
        bird.horizontal_distance = closest_obstacle.right_edge - bird.x
        bird.vertical_distance = bird.y - closest_obstacle.top_rect.height
        bird.ground_distance = Constants.SCREEN_HEIGHT - (bird.y + bird.height)
