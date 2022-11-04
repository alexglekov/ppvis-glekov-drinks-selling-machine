import random

from base.client.client import Client
from base.abstract.interfaces import IOrderable


class ClientWithPickCount(Client):
    def __init__(self):
        super().__init__()
        self._pick_count = 0

    def _pick_drink(self, machine: IOrderable):
        menu = machine.get_menu()
        while self._pick_count < 2:
            print(f'Client is picking drink: try no. {self._pick_count + 1}')
            self._chosen_drink = random.choice(menu)
            print(f'Chosen drink: {self._chosen_drink}')
            if machine.is_position_avaliable(self._chosen_drink):
                print("Chosen drink is available, proceeding to the next step")
                return True
            else:
                print('Chosen drink is unavailable')
                self._pick_count += 1
        else:
            print("Client\'s amount of picks is over")
        return False
