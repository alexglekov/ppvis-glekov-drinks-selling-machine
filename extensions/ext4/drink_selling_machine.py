from drink_selling_machine.drink_selling_machine import DrinkSellingMachine


class DrinkSellingMachineWithStats(DrinkSellingMachine):
    def __init__(self):
        super().__init__()
        self._stats = {'drink_stats': {drink_name: 0 for drink_name in self.get_menu()},
                       'client_stats': 0}

    def get_menu(self):
        self._stats['client_stats'] += 1
        res = super().get_menu()
        return res

    def make_order(self, ordered_position):
        res = super().make_order(ordered_position)
        if res:
            self._stats['drink_stats'][ordered_position.name] += 1
        return res
