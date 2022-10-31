import abc

from core.exceptions import InpropriateState


class Item:
    def __init__(self, *args, **kwargs):
        self._name: str = kwargs.pop('name')

    @property
    def name(self):
        return self._name


class Ingredient(Item):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.amount: int = kwargs.pop('amount')


class PreReadyGood(Item):
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