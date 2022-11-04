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

