from base.drink_selling_machine.goods.ingredients import Item


class PreReadyDrink(Item):
    def __init__(self, name='', amount=None):
        super().__init__(name=name)
        if amount is not None:
            self.amount: int = amount

    def __repr__(self):
        return f'Pre ready good: {self._name}'


class CookedDrink(Item):
    def __init__(self, name=''):
        super().__init__(name=name)

    def __repr__(self):
        return f'Cooked drink: {self._name}'