# The game controls the simulation of multiple bird populations
# being created and evolving including the score and data structures that store
# the bird objects and information on whether they are alive or dead
from Rectangle import *
from collections import deque
import Graphics
import numpy as np
import Stats


class Game:
    def __init__(self, bird_list):
        # initialize birds
        self.birds = bird_list
        self.obstacles = deque()               # use deck for obstacles because of frequent popping
        self.obstacles.appendleft(Obstacle())
        self.score = 0
        self.bird_distance = 0                 # distance is stored here because bird doesnt actually move
        Stats.num_alive = len(self.birds)

    # updates the data structures the obstacles are stored in
    def update_obstacles(self):
        if Constants.SCREEN_WIDTH - self.obstacles[0].right_edge > 200:
            self.obstacles.appendleft(Obstacle())
        if self.obstacles[-1].right_edge < 0:
            self.obstacles.pop()
            self.score += 1

    # updates and uses the Graphics class to draw the game objects
    def draw_game(self, screen):
        # draw background
        Graphics.draw_background(screen)
        # draw all birds and update their position
        for bird in self.birds:
            if not bird.dead:
                Graphics.draw_bird(bird, screen, Constants.WHITE)
                bird.update_position()
                bird.update_distances(self, bird)
                # check if each individual bird is colliding with obstacles
                for obstacle in self.obstacles:
                    if Game.colliding(bird, obstacle):
                        bird.dead = True
                        Stats.num_alive -= 1
                        bird.update_fitness(self.bird_distance)

        # update obstacle positions
        for obstacle in self.obstacles:
            Graphics.draw_obstacle(screen, obstacle)
            obstacle.update_position(self)
            self.bird_distance += 1

        # update score
        Stats.current_score = self.score

    # checks game actions such as if the birds are dead
    def check_actions(self, birds):
        # check if all birds are dead
        all_birds_dead = True
        for bird in birds:
            # feed in inputs to each birds brain and it will decide what to do
            nn_in = np.array([bird.horizontal_distance, bird.vertical_distance, bird.ground_distance, bird.velocity])
            normalized = (nn_in - min(nn_in))/(max(nn_in)-min(nn_in))
            nn_out = bird.brain.query(normalized)
            if nn_out > 0.5:            # else do nothing
                bird.jump()
            if not bird.dead:
                all_birds_dead = False

        # update highest score before this game ends
        if self.score > Stats.highest_score:
            Stats.highest_score = self.score
        else:
            Stats.prev_population_score = self.score
        return all_birds_dead

    # returns true if the given bird and obstacle are colliding, false otherwise
    @staticmethod
    def colliding(bird, obstacle):
        if bird.dead:
            return False
        if bird.y + bird.height > Constants.SCREEN_HEIGHT or bird.y < 0:
            return True

        horizontal_col = False     # whether objects are colliding horizontally
        vertical_col = False       # whether objects are colliding vertically
        if bird.x + bird.width > obstacle.left_edge and bird.x < obstacle.right_edge:
            horizontal_col = True
        if bird.y < obstacle.top_rect.y + obstacle.top_rect.height or bird.y + bird.height > obstacle.bottom_rect.y:
            vertical_col = True
        if horizontal_col and vertical_col:
            return True
        else:
            return False

