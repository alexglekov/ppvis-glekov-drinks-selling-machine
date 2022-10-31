import asyncio
import random
from core.exceptions import IncorrectReceiptIngredient
from drink_selling_machine.config.settings import RECEIPTS


class IngredientOperator:
    def __init__(self, **kwargs):
        self.__name = kwargs.pop('name')
        self.__binded_ingredients = kwargs.pop('ingredients')
        self._current_receipt = None
        self._current_ingredient = None

    async def operate_ingredient(self):
        res = await self._operate_ingredient()
        self._clean_receipt_ingredient_slot()
        return res

    async def _operate_ingredient(self):
        if self._current_receipt is not None:
            await asyncio.sleep(self._current_receipt['time'])
            return self._current_ingredient, True

    def pass_receipt_ingredient(self, receipt: str, ingredient: str):
        if RECEIPTS[receipt][ingredient]['component'] == self.__name and \
                ingredient in self.__binded_ingredients:
            self._current_receipt = RECEIPTS[receipt][ingredient]
            self._current_ingredient = ingredient
        else:
            raise IncorrectReceiptIngredient()

    def _clean_receipt_ingredient_slot(self):
        self._current_receipt = None
        self._current_ingredient = None

    @property
    def name(self):
        return self.__name