from ethtx.events.models.abi import ABIModel
from ethtx.events.models.semantic import SemanticModel
from ethtx.events.models.transaction import TransactionModel
from ethtx.events.observer.event_publisher import EventSubject
from ethtx.events.observer.observer_abc import Observer


class GlobalEventObserver(Observer):
    event: TransactionModel = TransactionModel()

    def update(self, subject: EventSubject, *args, **kwargs) -> None:
        if (
            not subject.current_event_state
            or subject.current_event_state.lower() == "global"
        ):
            if "starts" in kwargs:
                self.event.starts = kwargs["starts"]
            if "ends" in kwargs:
                self.event.starts = kwargs["ends"]


class ABIEventObserver(Observer):
    event: ABIModel = ABIModel()

    def update(self, subject: EventSubject, *args, **kwargs) -> None:
        if subject.current_event_state and subject.current_event_state.lower() == "abi":
            if "starts" in kwargs:
                self.event.starts = kwargs["starts"]
            if "ends" in kwargs:
                self.event.starts = kwargs["ends"]


class SemanticsEventObserver(Observer):
    event: SemanticModel = SemanticModel()

    def update(self, subject: EventSubject, *args, **kwargs) -> None:
        if (
            subject.current_event_state
            and subject.current_event_state.lower() == "semantics"
        ):
            if "starts" in kwargs:
                self.event.starts = kwargs["starts"]
            if "ends" in kwargs:
                self.event.starts = kwargs["ends"]
