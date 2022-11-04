from base.drink_selling_machine.drink_selling_machine import DrinkSellingMachine


class DrinkSellingMachineWithStats(DrinkSellingMachine):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._stats = {'drink_stats': {drink_name: 0 for drink_name in super().get_menu()},
                       'client_stats': 0}

    def get_menu(self):
        self._stats['client_stats'] = self._stats['client_stats'] + 1
        res = super().get_menu()
        return res

    def make_order(self, ordered_position):
        res = super().make_order(ordered_position)
        if res:
            self._stats['drink_stats'][ordered_position] += 1
        return res

    def print_statistics(self):
        print('Sold drinks:')
        for i in self._stats['drink_stats']:
            s = self._stats['drink_stats'][i]
            print(f'Drink name: {i}, amount of sold positions: {s}')
        k = self._stats['client_stats']
        print(f'Amount of clients: {k}')
