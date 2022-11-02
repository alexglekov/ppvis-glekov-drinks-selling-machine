from base.handler import ClientQueueMachineHandler
from extensions.ext2.client import ClientWithPickCount

if __name__ == '__main__':
    handler = ClientQueueMachineHandler(client_cls=ClientWithPickCount)
    handler.run()
