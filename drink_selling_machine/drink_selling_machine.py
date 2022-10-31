import asyncio
import copy
import datetime
import time

from core.tools import get_class
from .config.settings import RECEIPTS, STORAGES, COMPONENTS, MACHINE
from core.interfaces import IOrderable
from .ingredients_part.ingredients import CookedDrink


class DrinkSellingMachine(IOrderable):
    def __init__(self, *args, **kwargs):
        self.__components = {
            name: get_class(COMPONENTS[name]['class'])(name=name, ingredients=COMPONENTS[name]['ingredients']) for name
            in COMPONENTS}
        self.__storages = {name: get_class(STORAGES[name]['class'])(name=name) for name in STORAGES}
        self.__receipts = copy.deepcopy(RECEIPTS)
        self.__work_start = datetime.datetime.now()
        self.__work_delta = datetime.timedelta(seconds=MACHINE['work_delta'])

    def _get_receipt(self, required_drink, *args, **kwargs):
        receipt = {required_drink: copy.deepcopy(self.__receipts[required_drink])}
        return receipt

    def is_available(self):
        if datetime.datetime.now() > (self.__work_start + self.__work_delta):
            return False
        else:
            return True

    def _execute_receipt(self, receipt, required_drink, *args, **kwargs):
        # storage = self.__storages['Ingredients storage']
        result_list = {stage: False for stage in receipt[required_drink]}
        required_components = {stage: receipt[required_drink][stage]['component'] for stage in
                               receipt[required_drink]}
        required_ingredients = {key: False for key in receipt[required_drink]}
        ingr_check = True
        while False in result_list.values():
            ingr_check = self._get_required_ingredients(receipt[required_drink], required_ingredients)
            if ingr_check is False:
                break
            for stage in required_components:
                self.__components[required_components[stage]].pass_receipt_ingredient(required_drink, stage)
            loop = asyncio.get_event_loop()
            result = loop.run_until_complete(self._trigger_operations(required_components))
            result_list = dict(result)
            vals_to_del = []
            for ingr in result_list:
                if result_list[ingr]:
                    # del result_list[ingr]
                    del required_components[ingr]
                    vals_to_del.append(ingr)
            for val in vals_to_del:
                del result_list[val]
        if False in result_list.values():
            return False
        else:
            return CookedDrink(name=required_drink)

    def _get_required_ingredients(self, receipt, prev_extraction_info):
        for stage in prev_extraction_info:
            if prev_extraction_info[stage]:
                del prev_extraction_info[stage]
            else:
                pass
        s = self.__storages['Ingredients storage'].get_receipt_ingredients(prev_extraction_info, receipt)
        return s

    async def _trigger_operations(self, req_comps):
        my_list = []
        for comp in req_comps:
            my_list.append(asyncio.create_task(self.__components[req_comps[comp]].operate_ingredient()))
        result = await asyncio.gather(*my_list, return_exceptions=False)
        return result

    def _execute_order(self, required_drink):
        poss = self._check_order_possibility(required_drink)
        if poss:
            if required_drink not in self.__receipts:
                res = self._get_pre_ready_good(required_drink)
            else:
                receipt = self._get_receipt(required_drink)
                res = self._execute_receipt(receipt, required_drink)
            return res
        else:
            return False

    def make_order(self, ordered_position):
        res = self._execute_order(ordered_position)
        if res is not False:
            return res
        else:
            return False

    def is_position_avaliable(self, position):
        res = self._check_order_possibility(position)
        return res

    def _check_order_possibility(self, order):
        if order in self.__storages['Pre-ready goods fridge']:
            if self.__storages['Pre-ready goods fridge'].check_stored_item(order, 1):
                return True
            else:
                return False
        elif order in self.__receipts:
            ingred_cur_state = self.__storages['Ingredients storage'].get_current_state()
            for ingred in self.__receipts[order]:
                if self.__receipts[order][ingred]['amount'] > ingred_cur_state[ingred]:
                    return False
                else:
                    pass
            return True
        else:
            return False

    def _get_pre_ready_good(self, name):
        result = self.__storages['Pre-ready goods fridge'].get_element(name, 1)
        return result

    def get_menu(self):
        return list(list(self.__receipts.keys()) + list(self.__storages['Pre-ready goods fridge'].get_current_state().keys()))
