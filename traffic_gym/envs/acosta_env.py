import random

import gym


class AcostaEnv(gym.Env):
    def __init__(self):
        super(AcostaEnv, self).__init__()

        self.action_space = NotImplemented
        self.observation_space = NotImplemented

    @property
    def observation(self):
        raise NotImplementedError

    def step(self, actions):
        raise NotImplementedError

    def reset(self):
        return self.observation

    def render(self, mode='human'):
        raise NotImplementedError

    def close(self):
        raise NotImplementedError

    def seed(self, seed):
        random.seed(seed)
