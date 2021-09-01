from ethtx.events.models.abi import ABIModel
from ethtx.events.models.semantic import SemanticModel
from ethtx.events.models.transaction import TransactionModel, FullTransactionModel
from ethtx.events.observer.event_publisher import EventSubject
from ethtx.events.observer.observer_abc import Observer


class GlobalEventObserver(Observer):
    event: FullTransactionModel = FullTransactionModel()

    def update(self, subject: EventSubject, *args, **kwargs) -> None:
        if (
            subject.current_event_state
            and subject.current_event_state.lower() == "global"
        ):
            if "hash" in kwargs:
                self.event.hash = kwargs["hash"]


class TransactionEventObserver(Observer):
    event: TransactionModel = TransactionModel()

    def update(self, subject: EventSubject, *args, **kwargs) -> None:
        if (
            not subject.current_event_state
            or subject.current_event_state.lower() == "transaction"
        ):
            if "starts" in kwargs:
                self.event.starts = kwargs["starts"]
            if "ends" in kwargs:
                self.event.ends = kwargs["ends"]
            if "address_semantics" in kwargs:
                self.event.meta.address_semantics.append(kwargs["address_semantics"])
            if "signature_semantics" in kwargs:
                self.event.meta.signature_semantics.append(
                    kwargs["signature_semantics"]
                )
            if "exception" in kwargs:
                self.event.exception = kwargs["exception"]
            if "message" in kwargs:
                self.event.message = kwargs["message"]


class ABIEventObserver(Observer):
    event: ABIModel = ABIModel()

    def update(self, subject: EventSubject, *args, **kwargs) -> None:
        if subject.current_event_state and subject.current_event_state.lower() == "abi":
            if "starts" in kwargs:
                self.event.starts = kwargs["starts"]
            if "ends" in kwargs:
                self.event.ends = kwargs["ends"]
            if "exception" in kwargs:
                self.event.exception = kwargs["exception"]
            if "message" in kwargs:
                self.event.message = kwargs["message"]


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
                self.event.ends = kwargs["ends"]
            if "exception" in kwargs:
                self.event.exception = kwargs["exception"]
            if "message" in kwargs:
                self.event.message = kwargs["message"]
