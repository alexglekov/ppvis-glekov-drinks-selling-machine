# from core.exceptions import IncorrectMachineSetup
# from core.tools import get_class
# from drink_selling_machine.config.settings import STORAGES, COMPONENTS
# from drink_selling_machine.drink_selling_machine import ISettable
#
#
# class BaseSetter:
#     _block_methods_to_execute = []
#
#     def set_machine(self, machine: ISettable):
#         for block_method in BaseSetter._block_methods_to_execute:
#             if block_method[0] not in machine.get_block_list():
#                 raise IncorrectMachineSetup()
#             else:
#                 block = machine.get_block_slot(block_method[0])[block_method[0]]
#                 block_method[1](block)
#
#
# class MachineSetter(BaseSetter):
#     __storages = {key: get_class(STORAGES[key]['class']) for key in STORAGES}
#     __components = {key: get_class(COMPONENTS[key]['class']) for key in COMPONENTS}
#
#     def __set_components(self, **kwargs):
#         kwargs['components'] = {key: MachineSetter.__components[key]() for key in MachineSetter.__components}
#
#     def __set_storages(self, **kwargs):
#         kwargs['storages'] = {key: MachineSetter.__storages[key]() for key in MachineSetter.__storages}
#
#     _block_methods_to_execute = [('components', __set_components), ('storages', __set_storages)]
