import time

from base.client.client import Client
from base.core.tools import get_class
from base.drink_selling_machine.config.settings import MACHINE, CLIENT, CLIENT_GENERATION_DELTA
from base.drink_selling_machine.drink_selling_machine import DrinkSellingMachine


class ClientQueueMachineHandler:
    _machine_class = DrinkSellingMachine
    _client_class = Client

    def __init__(self, **kwargs):
        if 'client_cls' in kwargs:
            ClientQueueMachineHandler._machine_class = kwargs.pop('machine_cls')
        if 'machine_cls' in kwargs:
            ClientQueueMachineHandler._machine_class = kwargs.pop('machine_cls')
        self._machine = self._machine_class(**kwargs)
        self._init_kwargs = kwargs
        self._current_client = None
        self._client_generation_delta = CLIENT_GENERATION_DELTA

    def _create_client(self, **kwargs):
        self._current_client = self._client_class(**kwargs)

    def run(self):
        while self._machine.is_available():
            self._create_client(**self._init_kwargs)
            self._current_client.order_drink(self._machine)
            time.sleep(self._client_generation_delta)
