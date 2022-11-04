from base.handler import ClientQueueMachineHandler


class ClientQueueMachineHandlerWithStats(ClientQueueMachineHandler):
    def __init__(self, machine_cls=None, client_cls=None, component_cls=None):
        super().__init__(machine_cls=machine_cls, client_cls=client_cls, component_cls=component_cls)

    def run(self):
        super().run()
        self._machine.print_statistics()