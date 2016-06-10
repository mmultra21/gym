import logging
import os

import numpy as np

from doom_py import DoomGame, Mode, Button, GameVariable, ScreenFormat, ScreenResolution, Loader
from gym import spaces
from gym.envs.doom import doom_env

logger = logging.getLogger(__name__)

class DoomMyWayHomeEnv(doom_env.DoomEnv):
    """
    ------------ Training Mission 6 - My Way Home ------------
    This map is designed to improve navigational skills. It is a series of
    interconnected rooms and 1 corridor with a dead end. Each room
    has a separate color. There is a green vest in one of the room.
    The vest is always in the same room. Player must find the vest.

    Allowed actions:
        [13] - MOVE_FORWARD                     - Move forward - Values 0 or 1
        [14] - TURN_RIGHT                       - Turn right - Values 0 or 1
        [15] - TURN_LEFT                        - Turn left - Values 0 or 1
    Note: see controls.md for details

    Rewards:
        +  1    - Finding the vest
        -0.0001 - Several times per second - Find the vest quick!

    Goal: 0.50 point
        Find the vest

    Mode:
        - env.mode can be 'fast' or 'normal' (e.g. env.mode = 'fast')
        - 'fast' (default) will run as fast as possible (~75 fps) (best for simulation, harder for human to watch)
        - 'normal' will run at roughly 30 fps (easier for human to watch)

    Ends when:
        - Vest is found
        - Timeout (2 minutes - 4,200 frames)

    Actions:
    Either of
        1) action = [0, 1, 0]       # Recommended
            where parameter #1 is MOVE_FORWARD (0 or 1)
            where parameter #2 is TURN_RIGHT (0 or 1)
            where parameter #3 is TURN_LEFT (0 or 1)
        or
        2) actions = [0] * 43       # To train for the Deathmatch level
           actions[13] = 0      # MOVE_FORWARD
           actions[14] = 1      # TURN_RIGHT
           actions[15] = 0      # TURN_LEFT
    -----------------------------------------------------
    """
    def __init__(self):
        super(DoomMyWayHomeEnv, self).__init__()
        package_directory = os.path.dirname(os.path.abspath(__file__))
        self.loader = Loader()
        self.game = DoomGame()
        self.game.load_config(os.path.join(package_directory, 'assets/my_way_home.cfg'))
        self.game.set_vizdoom_path(self.loader.get_vizdoom_path())
        self.game.set_doom_game_path(self.loader.get_freedoom_path())
        self.game.set_doom_scenario_path(self.loader.get_scenario_path('my_way_home.wad'))
        self.screen_height = 480                    # Must match .cfg file
        self.screen_width = 640                     # Must match .cfg file
        self.game.set_window_visible(False)
        self.viewer = None
        self.game.init()
        self.game.new_episode()

        # 3 allowed actions [13, 14, 15] (must match .cfg file)
        self.action_space = spaces.HighLow(np.matrix([[0, 1, 0]] * 38 + [[-10, 10, 0]] * 2 + [[-100, 100, 0]] * 3))
        self.observation_space = spaces.Box(low=0, high=255, shape=(self.screen_height, self.screen_width, 3))
        self.action_space.allowed_actions = [13, 14, 15]

        self._seed()
