
from .user_authentication import User

class Newsletter:
    def __init__(self) -> None:
        self.__subscribers = []

    def subscribe(self, subscriber: User):
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber: User):
        self.__subscribers.remove(subscriber)

    def notify_subscribers(self, vehicles):
        for subscriber in self.__subscribers:
            subscriber.update(vehicles)

