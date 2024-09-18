from design_patterns.behavioral.observer import Clock, Timer

def test_observer() -> None:
    timer = Timer(0.1)
    clock = Clock(timer=timer)
    assert timer._observers == [clock]
    assert not clock.timer_went_off
    timer.start()
    assert clock.timer_went_off
    timer.detach_observer(clock)
    assert timer._observers == []
