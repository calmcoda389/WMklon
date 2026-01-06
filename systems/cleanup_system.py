class CleanupSystem:
    def __init__(self, units, on_unit_leak):
        self.units = units
        self.on_unit_leak = on_unit_leak

    def update(self):
        alive_units = []

        for unit in self.units:
            if not unit.alive:
                continue

            if unit.path_index >= len(unit.lane.points):
                self.on_unit_leak()
                continue

            alive_units.append(unit)

        self.units[:] = alive_units