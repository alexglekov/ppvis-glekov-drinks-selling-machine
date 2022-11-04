import time

from base.config.settings import RECEIPTS


class IngredientOperator:
    def __init__(self, name='', ingredients=None):
        self.__name = name
        self.__binded_ingredients = ingredients
        self._current_receipt = None
        self._current_ingredient = None

    def operate_ingredient(self):
        res = self._operate_ingredient()
        self._clean_receipt_ingredient_slot()
        return res

    def pass_receipt_ingredient(self, receipt: str, ingredient: str):
        if RECEIPTS[receipt][ingredient]['component'] == self.__name and \
                ingredient in self.__binded_ingredients:
            self._current_receipt = RECEIPTS[receipt][ingredient]
            self._current_ingredient = ingredient
        else:
            return False

    @property
    def name(self):
        return self.__name

    def _operate_ingredient(self):
        if self._current_receipt is not None:
            time.sleep(self._current_receipt['time'])
            return self._current_ingredient, True

    def _clean_receipt_ingredient_slot(self):
        self._current_receipt = None
        self._current_ingredient = None
