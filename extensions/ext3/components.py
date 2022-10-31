import asyncio
import random

from drink_selling_machine.components_part.components import IngredientOperator


class IngredientOperatorWithMistake(IngredientOperator):
    async def _operate_ingredient(self):
        await asyncio.sleep(self._current_receipt['time'])
        mistake = random.randrange(0, 10)
        if mistake > -1:
            return self._current_ingredient, False
        else:
            return self._current_ingredient, True
