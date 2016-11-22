# EXPERIMENTAL: all may be removed soon

from gym.benchmarks import scoring
from gym.benchmarks.registration import benchmark_spec, register_benchmark, registry  # imports used elsewhere

register_benchmark(
    id='Atari7Pixel-v0',
    scorer=scoring.ClipTo01ThenAverage(),
    name='Atari7Pixel',
    description='7 Atari games, with pixel observations',
    tasks=[
        {'env_id': 'BeamRider-v0',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'Breakout-v0',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'Enduro-v0',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'Pong-v0',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'Qbert-v0',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'Seaquest-v0',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'SpaceInvaders-v0',
         'trials': 1,
         'max_timesteps': 10000000,
        }
    ])

register_benchmark(
    id='Atari7PixelDeterministic-v0',
    scorer=scoring.ClipTo01ThenAverage(),
    name='Atari7PixelDeterministic',
    description='7 Atari games, with pixel observations',
    tasks=[
        {'env_id': 'BeamRiderDeterministic-v0',
         'trials': 2,
         'max_timesteps': 25000000,
        },
        {'env_id': 'BreakoutDeterministic-v0',
         'trials': 2,
         'max_timesteps': 25000000,
        },
        {'env_id': 'EnduroDeterministic-v0',
         'trials': 2,
         'max_timesteps': 25000000,
        },
        {'env_id': 'PongDeterministic-v0',
         'trials': 2,
         'max_timesteps': 25000000,
        },
        {'env_id': 'QbertDeterministic-v0',
         'trials': 2,
         'max_timesteps': 25000000,
        },
        {'env_id': 'SeaquestDeterministic-v0',
         'trials': 2,
         'max_timesteps': 25000000,
        },
        {'env_id': 'SpaceInvadersDeterministic-v0',
         'trials': 2,
         'max_timesteps': 25000000,
        }
    ])

register_benchmark(
    id='Atari7Pixel-v3',
    scorer=scoring.ClipTo01ThenAverage(),
    name='Atari7Pixel',
    description='7 Atari games, with pixel observations',
    tasks=[
        {'env_id': 'BeamRider-v3',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'Breakout-v3',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'Enduro-v3',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'Pong-v3',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'Qbert-v3',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'Seaquest-v3',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'SpaceInvaders-v3',
         'trials': 1,
         'max_timesteps': 10000000,
        }
    ])

register_benchmark(
    id='Atari7Ram-v0',
    name='Atari7Ram',
    description='7 Atari games, with RAM observations',
    scorer=scoring.ClipTo01ThenAverage(),
    tasks=[
        {'env_id': 'BeamRider-ram-v0',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'Breakout-ram-v0',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'Enduro-ram-v0',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'Pong-ram-v0',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'Qbert-ram-v0',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'Seaquest-ram-v0',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'SpaceInvaders-ram-v0',
         'trials': 1,
         'max_timesteps': 10000000,
        },
    ])

register_benchmark(
    id='Atari7Ram-v3',
    name='Atari7Ram',
    description='7 Atari games, with RAM observations',
    scorer=scoring.ClipTo01ThenAverage(),
    tasks=[
        {'env_id': 'BeamRider-ram-v3',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'Breakout-ram-v3',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'Enduro-ram-v3',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'Pong-ram-v3',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'Qbert-ram-v3',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'Seaquest-ram-v3',
         'trials': 1,
         'max_timesteps': 10000000,
        },
        {'env_id': 'SpaceInvaders-ram-v3',
         'trials': 1,
         'max_timesteps': 10000000,
        },
    ])

register_benchmark(
    id='ClassicControl2-v0',
    name='ClassicControl2',
    description='Simple classic control benchmark',
    scorer=scoring.ClipTo01ThenAverage(),
    tasks=[
        {'env_id': 'CartPole-v0',
         'trials': 1,
         'max_timesteps': 2000,
        },
        {'env_id': 'Pendulum-v0',
         'trials': 1,
         'max_timesteps': 1000,
        },
    ])

### Autogenerated by tinkerbell.benchmark.convert_benchmark.py

register_benchmark(
    id='Mujoco10M-v0',
    name='Mujoco10M',
    description='Mujoco benchmark with 10M steps',
    scorer=scoring.ClipTo01ThenAverage(),
    tasks=[
        {'env_id': 'Ant-v1',
         'trials': 1,
         'max_timesteps': 1000000,
        },
        {'env_id': 'Hopper-v1',
         'trials': 1,
         'max_timesteps': 1000000,
        },
        {'env_id': 'Humanoid-v1',
         'trials': 1,
         'max_timesteps': 1000000,
        },
        {'env_id': 'HumanoidStandup-v1',
         'trials': 1,
         'max_timesteps': 1000000,
        },
        {'env_id': 'Walker2d-v1',
         'trials': 1,
         'max_timesteps': 1000000,
        }
    ])

register_benchmark(
    id='Mujoco1M-v0',
    name='Mujoco1M',
    description='Mujoco benchmark with 1M steps',
    scorer=scoring.ClipTo01ThenAverage(),
    tasks=[
        {'env_id': 'HalfCheetah-v1',
         'trials': 3,
         'max_timesteps': 1000000,
        },
        {'env_id': 'Hopper-v1',
         'trials': 3,
         'max_timesteps': 1000000,
        },
        {'env_id': 'InvertedDoublePendulum-v1',
         'trials': 3,
         'max_timesteps': 1000000,
        },
        {'env_id': 'InvertedPendulum-v1',
         'trials': 3,
         'max_timesteps': 1000000,
        },
        {'env_id': 'Reacher-v1',
         'trials': 3,
         'max_timesteps': 1000000,
        },
        {'env_id': 'Swimmer-v1',
         'trials': 3,
         'max_timesteps': 1000000,
        },
        {'env_id': 'Walker2d-v1',
         'trials': 3,
         'max_timesteps': 1000000,
        }
    ])

bandit_tasks = []
for n_arms in [5, 10, 50]:
    for n_episodes in [10, 100, 500]:
        bandit_tasks.append({
            'env_id': 'BernoulliBandit-{k}.arms-{n}.episodes-v0'.format(k=n_arms, n=n_episodes),
            'trials': 1,
            'max_timesteps': 10 ** 9,
            'reward_floor': 0,
            'reward_ceiling': n_episodes,
        })

register_benchmark(
    id='BernoulliBandit-v0',
    name='BernoulliBandit',
    description='Multi-armed Bernoulli bandits',
    scorer=scoring.ClipTo01ThenAverage(num_episodes=1000),
    tasks=bandit_tasks
)

tabular_mdp_tasks = []
for n_states in [10]:
    for n_actions in [5]:
        for episode_length in [10]:
            for n_episodes in [10, 25, 50, 75, 100]:
                tabular_mdp_tasks.append({
                    'env_id': 'RandomTabularMDP-{s}.states-{a}.actions-{t}.timesteps-{n}.episodes-v0'.format(
                        s=n_states, a=n_actions, t=episode_length, n=n_episodes,
                    ),
                    'trials': 1,
                    'max_timesteps': 10 ** 9,
                    'reward_floor': 0,
                    'reward_ceiling': episode_length * n_episodes * 2,
                })

register_benchmark(
    id='RandomTabularMDP-v0',
    name='RandomTabularMDP',
    description='Random tabular MDPs',
    scorer=scoring.ClipTo01ThenAverage(num_episodes=1000),
    tasks=tabular_mdp_tasks
)
