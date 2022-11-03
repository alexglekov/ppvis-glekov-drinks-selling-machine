import time

from base.client.client import Client
from base.config.settings import CLIENT_GENERATION_DELTA
from base.drink_selling_machine.drink_selling_machine import DrinkSellingMachine


class ClientQueueMachineHandler:
    def __init__(self, **kwargs):
        self._machine_class = kwargs.pop('machine_cls', DrinkSellingMachine)
        self._client_class = kwargs.pop('client_cls', Client)
        self._machine = self._machine_class(**kwargs)
        self._init_kwargs = kwargs
        self._current_client = None
        self._client_generation_delta = CLIENT_GENERATION_DELTA

    def run(self):
        while self._machine.is_available():
            self._create_client(**self._init_kwargs)
            self._current_client.order_drink(self._machine)
            time.sleep(self._client_generation_delta)

    def _create_client(self, **kwargs):
        self._current_client = self._client_class(**kwargs)
