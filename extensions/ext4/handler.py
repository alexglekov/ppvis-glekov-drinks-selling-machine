from base.handler import ClientQueueMachineHandler


class ClientQueueMachineHandlerWithStats(ClientQueueMachineHandler):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def run(self):
        super().run()
        self._machine.print_statistics()