from base.drink_selling_machine.machine_elements.components import IngredientOperator


class IngredientOperatorWithSpeed(IngredientOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__operation_speed = 1

    def _operate_ingredient(self):
        self._current_receipt['time'] /= self.__operation_speed
        ret_val = super()._operate_ingredient()
        return ret_val
