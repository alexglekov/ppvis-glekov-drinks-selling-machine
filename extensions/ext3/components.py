import random
import time

from base.drink_selling_machine.machine_elements.components import IngredientOperator


class IngredientOperatorWithMistake(IngredientOperator):
    def _operate_ingredient(self):
        time.sleep(self._current_receipt['time'])
        mistake = random.randrange(0, 10)
        if mistake > -1:
            print(f'Component {self.name} crushed, retrying')
            return self._current_ingredient, False
        else:
            print(f'Component {self.name} worked properly, proceeding to the next step')
            return self._current_ingredient, True
