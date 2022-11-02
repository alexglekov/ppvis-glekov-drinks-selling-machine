from extensions.ext4.drink_selling_machine import DrinkSellingMachineWithStats
from extensions.ext4.handler import ClientQueueMachineHandlerWithStats

if __name__ == '__main__':
    handler = ClientQueueMachineHandlerWithStats(machine_cls=DrinkSellingMachineWithStats)
    handler.run()
