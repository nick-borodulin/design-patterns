import pytest
from design_patterns.structural.bridge import (
    IconWindow,
    LinuxWindowImplementation,
    MacOSWindowImplementation,
    TextBox,
)


@pytest.mark.parametrize(
    "window,expected_result",
    [
        (
            TextBox(MacOSWindowImplementation()),
            "mac_os_draw_line" * 4 + "mac_os_draw_text",
        ),
        (IconWindow(MacOSWindowImplementation()), "mac_os_draw_line" * 4),
    ],
)
def test_mac_os_windows(window: TextBox | IconWindow, expected_result: str) -> None:
    assert window.draw() == expected_result


@pytest.mark.parametrize(
    "window,expected_result",
    [
        (
            TextBox(LinuxWindowImplementation()),
            "linux_draw_line" * 4 + "linux_draw_text",
        ),
        (IconWindow(LinuxWindowImplementation()), "linux_draw_line" * 4),
    ],
)
def text_linux_windows(window: TextBox | IconWindow, expected_result: str) -> None:
    assert window.draw() == expected_result
