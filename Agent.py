import random
import time

import torch
import torch.nn as nn
import torch.optim as optim

from Model import LinearQNet

class Agent:

    def __init__(self, game_objects):
        self.game_objects = game_objects
        self.model = LinearQNet(8, 512, 4)

        self.lr = 0.001
        self.gamma = 0.9
        self.optimizer = optim.Adam(self.model.parameters(), lr=self.lr)
        self.criterion = nn.MSELoss()

        self.game_times = 0

    def run(self):
        # get old state
        state_old = self.get_state()
        # get action
        final_move = self.get_action(state_old)
        # play step
        reward = self.play_step(final_move)
        # get new state
        state_new = self.get_state()
        # train short memory
        self.train_short_memory(state_old, state_new, final_move, reward)
        # increase attribute
        self.game_times += 0.1

    def train_short_memory(self, state_old, state_new, final_move, reward):
        state_old = torch.tensor(state_old, dtype=torch.float)
        state_new = torch.tensor(state_new, dtype=torch.float)
        final_move = torch.tensor(final_move, dtype=torch.long)
        reward = torch.tensor(reward, dtype=torch.float)

        pred_old = self.model(state_old)
        target = pred_old.clone()

        Q_new = reward + self.gamma * torch.max(self.model(state_new))
        target[torch.argmax(final_move).item()] = Q_new

        self.optimizer.zero_grad()
        loss = self.criterion(target, pred_old)
        loss.backward()

        self.optimizer.step()

    def get_action(self, state):
        # random moves: tradeoff exploration / exploitation
        final_move = [0, 0, 0, 0]
        if random.randint(0, 100) < max((80 - self.game_times), 20):
            index = random.choice([0, 1, 2, 3])
        else:
            state_0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state_0)
            index = torch.argmax(prediction).item()

        final_move[index] += 1

        return final_move

    def play_step(self, final_move):
        four_dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        for i in range(len(final_move)):
            if final_move[i] == 1:
                x, y = four_dir[i]

        new_x, new_y = self.game_objects.player[0] + x, self.game_objects.player[1] + y
        reward = 0

        if self.game_objects.object[new_x][new_y] == 2: # wall wall
            reward = -100
        elif self.game_objects.object[new_x][new_y] == 1: # space
            self.game_objects.player = [new_x, new_y]
            reward = +1
        elif self.game_objects.object[new_x][new_y] == 5: # end_point
            self.game_objects.player = [new_x, new_y]
            reward = +1000

        return reward

    def get_state(self):
        player_x, player_y = self.game_objects.player
        state = [
            # player's x
            player_x,
            # player's y
            player_y,
            # end_point's x
            self.game_objects.end_point[0],
            # end_point's y
            self.game_objects.end_point[1],
            # player's up is wall
            self.game_objects.object[player_x - 1][player_y] == 2,
            # player's down is wall
            self.game_objects.object[player_x + 1][player_y] == 2,
            # player's left is wall
            self.game_objects.object[player_x][player_y - 1] == 2,
            # player's right is wall
            self.game_objects.object[player_x][player_y + 1] == 2
        ]

        return state