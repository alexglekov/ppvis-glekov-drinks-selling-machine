from abc import ABC, abstractmethod


class IOrderable(ABC):
    @abstractmethod
    def get_menu(self):
        ...

    @abstractmethod
    def make_order(self, ordered_position):
        ...

    @abstractmethod
    def is_position_avaliable(self, position):
        ...

class ISettable(ABC):
    @abstractmethod
    def get_block_list(self):
        ...

    @abstractmethod
    def get_block_slot(self, block_name):
        ...

