"""
Top-down car dynamics simulation.

Some ideas are taken from this great tutorial http://www.iforce2d.net/b2dtut/top-down-car by Chris Campbell.
This simulation is a bit more detailed, with wheels rotation.

Created by Oleg Klimov. Licensed on the same terms as the rest of OpenAI Gym.
"""

import numpy as np
import math
import Box2D
from Box2D.b2 import (
    edgeShape,
    circleShape,
    fixtureDef,
    polygonShape,
    revoluteJointDef,
    contactListener,
    shape,
)

MASK_POLY1 = [(-1, +0.5), (+1, +0.5), (+1, -0.5), (-1, -0.5)]


class Mask:
    def __init__(self, world, init_angle, init_x, init_y, size=2.5):
        self.world = world
        self.size = size
        self.hull = self.world.CreateStaticBody(
            position=(init_x, init_y),
            angle=init_angle,
            fixtures=[
                fixtureDef(
                    shape=polygonShape(
                        vertices=[(x * self.size, y * self.size) for x, y in MASK_POLY1]
                    ),
                    groupIndex=2,
                    categoryBits=0x0004,
                    maskBits=0x002,
                )
            ]
        )
        self.hull.color = (0.8, 0.2, 0.8)

    def move(self, velocity):
        self.hull.linearVelocity = (velocity[0], velocity[1])

    def draw(self, viewer):
        for f in self.hull.fixtures:
            trans = f.body.transform
            path = [trans * v for v in f.shape.vertices]
            viewer.draw_polygon(path, color=self.hull.color)

    def destroy(self):
        self.world.DestroyBody(self.hull)
        self.hull = None