from base.handler import ClientQueueMachineHandler
from extensions.ext3.components import IngredientOperatorWithMistake

if __name__ == '__main__':
    handler = ClientQueueMachineHandler(component_cls=IngredientOperatorWithMistake)
    handler.run()
