import json
import os
import time

from qbubbles.events import PreInitializeEvent, PostInitializeEvent, InitializeEvent
from qbubbles.resources import ModelLoader, Resources
from qbubbles.modloader import Addon, AddonSkeleton
from qbubbles.registry import Registry

from impossiblemode.globals import MODID, MODNAME, VERSION
from impossiblemode.init.gameMapsInit import initaddon_gamemaps


@Addon(modid=MODID, name=MODNAME, version=VERSION)
class ImpossibleModeAddon(AddonSkeleton):
    def __init__(self):
        print(f"Loaded addon {self.modID}")
        PreInitializeEvent.bind(self.pre_initialize)
        InitializeEvent.bind(self.initialize)
        PostInitializeEvent.bind(self.post_initialize)

    def pre_initialize(self, evt: PreInitializeEvent):
        print(f"Pre initialized addon {self.modID}")

    def initialize(self, evt: InitializeEvent):
        initaddon_gamemaps()
        print(f"Initialized addon {self.modID}")

    def post_initialize(self, evt: PostInitializeEvent):
        print(f"Post initialized addon {self.modID}")


print(os.listdir(".."))
