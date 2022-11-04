from base.config.settings import PRE_READY_GOODS, INGREDIENTS
from base.drink_selling_machine.goods.drinks import PreReadyDrink
from base.drink_selling_machine.goods.ingredients import Ingredient


class Storage:
    def __init__(self, name=''):
        self.__name = name
        self._stored_items = None

    def check_stored_item(self, name: str, amount):
        if self._stored_items[name].amount >= amount:
            return True
        else:
            return False

    def get_current_state(self):
        s = {key: self._stored_items[key].amount for key in self._stored_items.keys()}
        return s

    def __contains__(self, item):
        if item in self._stored_items:
            return True
        else:
            return False


class IngredientStorage(Storage):
    def __init__(self, name=''):
        super(IngredientStorage, self).__init__(name=name)
        self._stored_items = {name: Ingredient(name=name, **INGREDIENTS['list'][name])
                              for name in INGREDIENTS['list']}

    def get_receipt_ingredients(self, ingredients, receipt):
        current_state = self.get_current_state()
        poss = True
        for ingr in ingredients:
            if receipt[ingr]['amount'] > current_state[ingr]:
                poss = False
                break
        if not poss:
            return False
        else:
            pass
        for ingr in ingredients:
            self._stored_items[ingr].amount -= receipt[ingr]['amount']
        ingr_dict = {stage: False for stage in ingredients}
        return ingr_dict


class PreReadyGoodsStorage(Storage):
    def __init__(self, name=''):
        super(PreReadyGoodsStorage, self).__init__(name=name)
        self._stored_items = {name: PreReadyDrink(name=name, **PRE_READY_GOODS['list'][name])
                              for name in PRE_READY_GOODS['list']}

    def get_element(self, name, amount):
        if self._stored_items[name].amount >= amount:
            self._stored_items[name].amount -= amount
            return PreReadyDrink(name=name)
        else:
            return False
