from ethtx.events.observer.observer_abc import Observer


class GlobalEventObserver(Observer):
    def update(self, observable) -> None:
        pass


class ABIEventObserver(Observer):
    def update(self, observable) -> None:
        pass


class SemanticEventObserver(Observer):
    def update(self, observable) -> None:
        pass
