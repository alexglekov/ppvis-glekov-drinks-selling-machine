import datetime
import random

from base.config.settings import CLIENT
from base.drink_selling_machine.drink_selling_machine import IOrderable


class Client:
    def __init__(self):
        self._possible_wait_time = datetime.timedelta(seconds=CLIENT['possible_wait_time'])
        self._chosen_drink = None
        self._received_drink = None
        self._order_time = None

    def order_drink(self, machine):
        pick_try = self._pick_drink(machine)
        if pick_try:
            self._order_time = datetime.datetime.now()
            print(f'Order execution is starting, ordered drink is {self._chosen_drink}')
            order_try = self._order_drink(machine)
            if order_try:
                if datetime.datetime.now() <= self._order_time + self._possible_wait_time:
                    self._received_drink = order_try
                    print(f"Order executed successfully, received drink is {self._received_drink}, client is leaving")
                    return True
                else:
                    print(f'Order has been executed for too long, client left')
                    return False
            else:
                print(f"Order execution failed, client is leaving")
                return False
        else:
            print('Drink chosen by client is unavailable, client is leaving')
            return False

    @property
    def received_drink(self):
        return self._received_drink

    def _pick_drink(self, machine: IOrderable):
        menu = machine.get_menu()
        print('Client is picking drink')
        self._chosen_drink = random.choice(menu)
        print(f'Chosen drink: {self._chosen_drink}')
        if machine.is_position_avaliable(self._chosen_drink):
            print("Chosen drink is available, proceeding to the next step")
            return True
        else:
            print('Chosen drink is unavailable')
            return False

    def _order_drink(self, drink_selling_machine: IOrderable):
        order_try = drink_selling_machine.make_order(self._chosen_drink)
        return order_try
