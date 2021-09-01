from ethtx.events.observer.event_publisher import EventSubject
from ethtx.events.observer.event_subscribers import (
    ABIEventObserver,
    SemanticsEventObserver,
    GlobalEventObserver,
)

if __name__ == "__main__":
    s = EventSubject()
    a = ABIEventObserver()
    sem = SemanticsEventObserver()
    g = GlobalEventObserver()
    s.attach([ABIEventObserver(), SemanticsEventObserver(), GlobalEventObserver()])
    print(22, s._observers)
    s.set_event_state("abi")
    s.notify_start()
    print(555, s.current_event_state)
    s.set_event_state("global")
    print(555, s.current_event_state)
    s.notify_start()
    print(333, s._observers[0].event)
    print(444, s._observers[2].event)
    print(555, s.current_event_state)
    s.set_event_state("abi")
    s.notify_end()
    s.set_event_state("global")
    s.notify_end()
    print(66, s._observers[0].event)
    print(77, s._observers[1].event)
