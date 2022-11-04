from base.handler import ClientQueueMachineHandler
from extensions.ext1.components import IngredientOperatorWithSpeed

if __name__ == '__main__':
    handler = ClientQueueMachineHandler(component_cls=IngredientOperatorWithSpeed)
    handler.run()
