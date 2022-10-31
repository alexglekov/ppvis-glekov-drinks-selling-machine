import time

from core.tools import get_class
from drink_selling_machine.config.settings import MACHINE, CLIENT, CLIENT_GENERATION_DELTA


class ClientQueueMachineHandler:
    _machine_class = get_class(MACHINE['class'])
    _client_class = get_class(CLIENT['class'])

    def __init__(self):
        self.__machine = self._machine_class()
        self._current_client = None
        self._client_generation_delta = CLIENT_GENERATION_DELTA

    def _create_client(self):
        self._current_client = self._client_class()

    def run(self):
        while self.__machine.is_available():
            self._create_client()
            self._current_client.order_drink(self.__machine)
            time.sleep(self._client_generation_delta)
