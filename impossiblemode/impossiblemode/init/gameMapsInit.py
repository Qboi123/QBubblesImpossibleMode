from qbubbles.registry import Registry

from impossiblemode.maps import ImpossibleModeMap


def initaddon_gamemaps():
    Registry.register_gamemap(ImpossibleModeMap().get_uname(), ImpossibleModeMap())
