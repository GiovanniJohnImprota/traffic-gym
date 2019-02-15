import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Acosta-v0',
    entry_point='traffic_gym.envs:AcostaEnv'
)
