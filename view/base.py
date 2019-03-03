from abc import abstractmethod, ABCMeta


class BaseView(metaclass=ABCMeta):
    @abstractmethod
    def output(self):
        pass
