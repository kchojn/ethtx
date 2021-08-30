from ethtx.events.observer.event_publisher import EventSubject
from ethtx.events.observer.observer_abc import Observer


class GlobalEventObserver(Observer):
    def update(self, subject: EventSubject) -> None:
        if (
            subject.current_event_state.lower() == "global"
            or not subject.current_event_state
        ):
            pass


class ABIEventObserver(Observer):
    def update(self, subject: EventSubject) -> None:
        if (
            subject.current_event_state.lower() == "abi"
            or not subject.current_event_state
        ):
            pass


class SemanticsEventObserver(Observer):
    def update(self, subject: EventSubject) -> None:
        if (
            subject.current_event_state.lower() == "semantics"
            or not subject.current_event_state
        ):
            pass
