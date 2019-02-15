import gym
import pytest

import traffic_gym


@pytest.fixture()
def env():
    env = gym.make('Acosta-v0')
    env.seed(42)
    return env


def test_step(env):
    with pytest.raises(NotImplementedError):
        env.step(0)


def test_reset(env):
    with pytest.raises(NotImplementedError):
        env.reset()


def test_render(env):
    with pytest.raises(NotImplementedError):
        env.render()


def test_close(env):
    with pytest.raises(NotImplementedError):
        env.close()
