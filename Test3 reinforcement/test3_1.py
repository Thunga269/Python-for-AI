import random

import gym
import numpy as np


env = gym.make("Taxi-v3", render_mode="ansi").env

state_size = env.observation_space.n
action_size = env.action_space.n
qtable = np.zeros((state_size, action_size))


learning_rate = 0.9
discount_rate = 0.8
epsilon = 1.0
decay_rate = 0.005


num_episodes = 10000
max_steps = 99  

max_reward = -10000
max_step = 100

for episode in range(num_episodes):

    state = env.reset()[0]
    done = False
    penaltys, rewards, epoch = 0, 0, 0
    for s in range(max_steps):

        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(qtable[state, 🙂)

        new_state, reward, done, info, _ = env.step(action)
        rewards += reward
        if reward == -10:
            penaltys += 1
        qtable[state, action] = qtable[state, action] + learning_rate * (
                reward + discount_rate * np.max(qtable[new_state, 🙂) - qtable[state, action])

        state = new_state
        epoch += 1
        if rewards > max_reward and epoch < max_steps and penaltys == 0:
            max_reward = rewards
            np.save('q_table.npy', qtable)
        if done == True:
            break
    print("Penalty {} Reward {} Epoch {}".format(penaltys, rewards, epoch))
    epsilon = np.exp(-decay_rate * episode)

print("Training finished.\n")