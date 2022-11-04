import time

from base.client.client import Client
from base.config.settings import CLIENT_GENERATION_DELTA
from base.drink_selling_machine.drink_selling_machine import DrinkSellingMachine


class ClientQueueMachineHandler:
    def __init__(self, machine_cls=None, client_cls=None, component_cls=None):
        self._machine_class = machine_cls or DrinkSellingMachine
        self._client_class = client_cls or Client
        self._machine = self._machine_class(component_cls=component_cls)
        self._current_client = None
        self._client_generation_delta = CLIENT_GENERATION_DELTA

    def run(self):
        while self._machine.is_available():
            self._create_client()
            self._current_client.order_drink(self._machine)
            time.sleep(self._client_generation_delta)

    def _create_client(self):
        self._current_client = self._client_class()
