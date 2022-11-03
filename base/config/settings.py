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
        }
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
    }
}
STORAGES = {
        'Ingredients storage': {
            'contents': INGREDIENTS['list'].keys()
        },
        'Pre-ready goods fridge': {
            'contents': PRE_READY_GOODS['list'].keys()
        },
}

COMPONENTS = {
        'Cappuccinator': {
            'ingredients': ['milk']
        },
        'Bean grinder': {
            'ingredients': ['coffee_beans']
        },
        'Dozator': {
            'ingredients': ['syrup']
        },
        'Boiler': {
            'ingredients': ['milk']
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
    'possible_wait_time': 30
}

MACHINE = {
    'work_delta': 60
}

CLIENT_GENERATION_DELTA = 5