from drink_selling_machine.components_part.components import IngredientOperator


class IngredientOperatorWithSpeed(IngredientOperator):
    def __init__(self, **kwargs):
        super().__init__()
        self.__operation_speed = 1

    async def _operate_ingredient(self):
        self._current_receipt['time'] *= self.__operation_speed
        ret_val = await super()._operate_ingredient()
        return ret_val
