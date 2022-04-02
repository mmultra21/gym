import numpy as np
import pytest

from gym.spaces import Box, Dict, Discrete, MultiDiscrete, Tuple
from gym.vector.utils.spaces import batch_space, iterate
from tests.vector.utils import CustomSpace, custom_spaces, spaces

expected_batch_spaces_4 = [
    Box(low=-1.0, high=1.0, shape=(4,), dtype=np.float64),
    Box(low=0.0, high=10.0, shape=(4, 1), dtype=np.float64),
    Box(
        low=np.array(
            [[-1.0, 0.0, 0.0], [-1.0, 0.0, 0.0], [-1.0, 0.0, 0.0], [-1.0, 0.0, 0.0]]
        ),
        high=np.array(
            [[1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0], [1.0, 1.0, 1.0]]
        ),
        dtype=np.float64,
    ),
    Box(
        low=np.array(
            [
                [[-1.0, 0.0], [0.0, -1.0]],
                [[-1.0, 0.0], [0.0, -1.0]],
                [[-1.0, 0.0], [0.0, -1]],
                [[-1.0, 0.0], [0.0, -1.0]],
            ]
        ),
        high=np.ones((4, 2, 2)),
        dtype=np.float64,
    ),
    Box(low=0, high=255, shape=(4,), dtype=np.uint8),
    Box(low=0, high=255, shape=(4, 32, 32, 3), dtype=np.uint8),
    MultiDiscrete([2, 2, 2, 2]),
    Box(low=-2, high=2, shape=(4,), dtype=np.int64),
    Tuple((MultiDiscrete([3, 3, 3, 3]), MultiDiscrete([5, 5, 5, 5]))),
    Tuple(
        (
            MultiDiscrete([7, 7, 7, 7]),
            Box(
                low=np.array([[0.0, -1.0], [0.0, -1.0], [0.0, -1.0], [0.0, -1]]),
                high=np.array([[1.0, 1.0], [1.0, 1.0], [1.0, 1.0], [1.0, 1.0]]),
                dtype=np.float64,
            ),
        )
    ),
    Box(
        low=np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        high=np.array([[10, 12, 16], [10, 12, 16], [10, 12, 16], [10, 12, 16]]),
        dtype=np.int64,
    ),
    Box(low=0, high=1, shape=(4, 19), dtype=np.int8),
    Dict(
        {
            "position": MultiDiscrete([23, 23, 23, 23]),
            "velocity": Box(low=0.0, high=1.0, shape=(4, 1), dtype=np.float64),
        }
    ),
    Dict(
        {
            "position": Dict(
                {
                    "x": MultiDiscrete([29, 29, 29, 29]),
                    "y": MultiDiscrete([31, 31, 31, 31]),
                }
            ),
            "velocity": Tuple(
                (
                    MultiDiscrete([37, 37, 37, 37]),
                    Box(low=0, high=255, shape=(4,), dtype=np.uint8),
                )
            ),
        }
    ),
]

expected_custom_batch_spaces_4 = [
    Tuple((CustomSpace(), CustomSpace(), CustomSpace(), CustomSpace())),
    Tuple(
        (
            Tuple((CustomSpace(), CustomSpace(), CustomSpace(), CustomSpace())),
            Box(low=0, high=255, shape=(4,), dtype=np.uint8),
        )
    ),
]


@pytest.mark.parametrize(
    "space,expected_batch_space_4",
    list(zip(spaces, expected_batch_spaces_4)),
    ids=[space.__class__.__name__ for space in spaces],
)
def test_batch_space(space, expected_batch_space_4):
    batch_space_4 = batch_space(space, n=4)
    assert batch_space_4 == expected_batch_space_4


def test_batch_space_seed():
    for space in [
        Box(0, 10, seed=123),
        Tuple([Box(0, 5, seed=123), Box(0, 3, seed=123)], seed=123),
        Dict(
            {"space-1": Box(0, 5, seed=123), "space-2": Box(0, 10, seed=123)}, seed=123
        ),
    ]:
        batched_space = batch_space(space)
        assert space.np_random == batched_space.np_random
        for _ in range(100):
            assert np.all(space.sample() == batched_space.sample())

    space = MultiDiscrete([5, 3], seed=123)
    batched_space = batch_space(space)
    assert space.np_random == batched_space.np_random
    # As type(space) == MultiDiscrete and type(batched_space) == Box
    #   the sample functions are different, therefore cannot check sample equivalence

    space = Discrete(5, seed=123)
    batched_space = batch_space(space)
    assert space.np_random == batched_space.np_random
    # As type(space) == Discrete and type(batched_space) == MultiDiscrete
    #   the sample functions are different, therefore cannot check sample equivalence


@pytest.mark.parametrize(
    "space,expected_batch_space_4",
    list(zip(custom_spaces, expected_custom_batch_spaces_4)),
    ids=[space.__class__.__name__ for space in custom_spaces],
)
def test_batch_space_custom_space(space, expected_batch_space_4):
    batch_space_4 = batch_space(space, n=4)
    assert batch_space_4 == expected_batch_space_4


@pytest.mark.parametrize(
    "space,batch_space",
    list(zip(spaces, expected_batch_spaces_4)),
    ids=[space.__class__.__name__ for space in spaces],
)
def test_iterate(space, batch_space):
    items = batch_space.sample()
    iterator = iterate(batch_space, items)
    for i, item in enumerate(iterator):
        assert item in space
    assert i == 3


@pytest.mark.parametrize(
    "space,batch_space",
    list(zip(custom_spaces, expected_custom_batch_spaces_4)),
    ids=[space.__class__.__name__ for space in custom_spaces],
)
def test_iterate_custom_space(space, batch_space):
    items = batch_space.sample()
    iterator = iterate(batch_space, items)
    for i, item in enumerate(iterator):
        assert item in space
    assert i == 3
