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
