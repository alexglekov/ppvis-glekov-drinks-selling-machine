from base.drink_selling_machine.goods.ingredients import Item


class PreReadyDrink(Item):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'amount' in kwargs:
            self.amount: int = kwargs.pop('amount')

    def __repr__(self):
        return f'Pre ready good: {self._name}'


class CookedDrink(Item):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f'Cooked drink: {self._name}'