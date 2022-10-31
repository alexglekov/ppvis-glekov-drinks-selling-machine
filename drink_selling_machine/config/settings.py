INGREDIENTS = {
    'list':
        {
            'milk':
                {
                    'amount': 600,
                },
            'coffee_beans':
                {
                    'amount': 100,
                },
            'syrup':
                {
                    'amount': 200,
                },
        },
    'class': ('drink_selling_machine.ingredients_part.ingredients', 'Ingredient')
}
PRE_READY_GOODS = {
    'list': {
        'cola': {
            'amount': 10
        },
        'fanta': {
            'amount': 10
        },
        'sprite': {
            'amount': 10
        }
    },
    'class': ('drink_selling_machine.ingredients_part.ingredients', 'PreReadyGood')
}
STORAGES = {
        'Ingredients storage': {
            'contents': INGREDIENTS['list'].keys(),
            'class': ('drink_selling_machine.components_part.storages', 'IngredientStorage')
        },
        'Pre-ready goods fridge': {
            'contents': PRE_READY_GOODS['list'].keys(),
            'class': ('drink_selling_machine.components_part.storages', 'PreReadyGoodsStorage')
        },
}

COMPONENTS = {
        'Cappuccinator': {
            'ingredients': ['milk'],
            'class': ('drink_selling_machine.components_part.components', 'IngredientOperator')
        },
        'Bean grinder': {
            'ingredients': ['coffee_beans'],
            'class': ('drink_selling_machine.components_part.components', 'IngredientOperator')
        },
        'Dozator': {
            'ingredients': ['syrup'],
            'class': ('drink_selling_machine.components_part.components', 'IngredientOperator')
        },
        'Boiler': {
            'ingredients': ['milk'],
            'class': ('drink_selling_machine.components_part.components', 'IngredientOperator')
        }
}

RECEIPTS = {
    "cappuccino": {
        "milk": {
            "component": "Cappuccinator",
            "time": 5,
            "amount": 150
        },
        "coffee_beans": {
            "component": "Bean grinder",
            "time": 5,
            "amount": 10
        },
        "syrup": {
            "component": "Dozator",
            "time": 1,
            "amount": 50
        },
    },
    "latte": {
        "milk": {
            "component": "Boiler",
            "time": 5,
            "amount": 250
        },
        "coffee_beans": {
            "component": "Bean grinder",
            "time": 3,
            "amount": 5
        },
        "syrup": {
            "component": "Dozator",
            "time": 1,
            "amount": 50
        },
    },
    "espresso": {
        "coffee_beans": {
            "component": "Bean grinder",
            "amount": 3,
            "time": 20
        },
    }
}
CLIENT = {
    'class': ('client.client', 'Client'),
    'possible_wait_time': 20
}

MACHINE = {
    'class': ('drink_selling_machine.drink_selling_machine', 'DrinkSellingMachine'),
    'work_delta': 10
}

CLIENT_GENERATION_DELTA = 5