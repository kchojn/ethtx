from ethtx.events.observer.event_publisher import EventSubject
from ethtx.events.observer.observer_abc import Observer


class GlobalEventObserver(Observer):
    def update(self, subject: EventSubject, *args, **kwargs) -> None:
        if (
            not subject.current_event_state
            or subject.current_event_state.lower() == "global"
        ):
            pass


class ABIEventObserver(Observer):
    def update(self, subject: EventSubject, *args, **kwargs) -> None:
        if subject.current_event_state and subject.current_event_state.lower() == "abi":
            pass


class SemanticsEventObserver(Observer):
    def update(self, subject: EventSubject, *args, **kwargs) -> None:
        if (
            subject.current_event_state
            and subject.current_event_state.lower() == "semantics"
        ):
            pass
