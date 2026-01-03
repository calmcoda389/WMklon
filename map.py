class Tile:
    def __init__(self, walkable: bool, buildable: bool):
        self.walkable = walkable
        self.buildable = buildable
        
class GameMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [
            [Tile(True, True) for x in range(width)]
            for y in range(height)
        ]
        
class Lane:
    # Feste Abfolge von Wegpukten
    def __init__(self, points):
        self.points = points #Liste von (x, y)