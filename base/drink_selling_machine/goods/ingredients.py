class Item:
    def __init__(self, name=''):
        self._name: str = name

    @property
    def name(self):
        return self._name


class Ingredient(Item):
    def __init__(self, name='', amount=0):
        super().__init__(name=name)
        self.amount: int = amount
