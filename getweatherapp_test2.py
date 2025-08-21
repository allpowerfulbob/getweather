import getweatherapp
from unittest.mock import MagicMock, patch
import pytest
from typing import Any

def test_get_temperature_with_mocking_monkeypatch(
        monkeypatch: pytest.MonkeyPatch) -> None:
    def fake_get(url: str, params: dict[str, Any]) -> Any:
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None