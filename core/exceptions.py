class MyException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message


class NoRequiredIngridients(MyException):
    def __init__(self, message='Not enough ingridients for requested drink'):
        super().__init__(message)


class DrinkCantBeMade(MyException):
    def __init__(self, message='Requested drink cant be made'):
        super().__init__(message)


class ComponentCrushed(MyException):
    def __init__(self, message='One of components failed during its operation'):
        super().__init__(message)


class OperationFailed(MyException):
    def __init__(self, operation):
        super().__init__(f'{operation} failed')


class InpropriateState(MyException):
    def __init__(self, message='Inpropriate state was set for component'):
        super().__init__(message)


class IncorrectMachineSetup(MyException):
    def __init__(self, message='Actual block of machine don\'t match configuration from settings.py'):
        super().__init__(message)


class IncorrectReceiptIngredient(MyException):
    def __init__(self, message='Passed receipt ingredient don\'t match current component'):
        super().__init__(message)


class IngredientOperationFailed(MyException):
    def __init__(self, message='Error occurred during operation'):
        super().__init__(message)
