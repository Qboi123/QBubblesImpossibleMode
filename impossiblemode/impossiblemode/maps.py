from typing import Tuple

from qbubbles.bubbleSystem import BubbleSystem
from qbubbles.bubbles import BubbleObject, DamageBubble, Bubble
from qbubbles.events import UpdateEvent
from qbubbles.maps import ClassicMap
from qbubbles.registry import Registry


class ImpossibleModeMap(ClassicMap):
    def __init__(self):
        super(ImpossibleModeMap, self).__init__()

        self.set_uname("impossiblemode_map")
        Registry.gameData["language"]["gamemap.impossiblemode_map.name"] = "Impossible Mode"

    def get_random_bubble(self) -> Tuple[BubbleObject, float, float]:
        bubble: Bubble = BubbleSystem.random(self.randoms["qbubbles:bubble_system"][0])
        bubble = DamageBubble()
        radius = self.randoms["qbubbles:bubble_radius"][0].randint(bubble.minRadius, bubble.maxRadius)
        speed = self.randoms["qbubbles:bubble_speed"][0].randint(bubble.minSpeed, bubble.maxSpeed)

        max_health = 1
        if hasattr(bubble, "maxHealth"):
            max_health = bubble.maxHealth

        return BubbleObject(bubble, max_health), radius, speed
