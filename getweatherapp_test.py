import pytest
import getweatherapp
from typing import Any

def test_getweather_with_monkey_patch(monkeypatch:pytest.MonkeyPatch):
    def fake_get(url: str, params: dict[str, Any]) -> any:
        class FakeResponse:
            def raise_for_status(self) -> None: pass
            def json(self) -> dict[str, Any]:
                return {"final": {"temp_celsius": 19}}
        return FakeResponse()

    monkeypatch.setattr("requests.get", fake_get)
    service = getweatherapp.Getweather(api_key="fake-key")
    temp = service.get_temperature("Denver")
    assert temp == 19