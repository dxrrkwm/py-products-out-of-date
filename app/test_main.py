import datetime
from app.main import outdated_products
from unittest.mock import patch
import pytest


@pytest.mark.parametrize("mock_today, products, result", [
    (
        datetime.date(2025, 1, 27),
        [
            {"name": "salmon",
             "expiration_date": datetime.date(2025, 1, 25),
             "price": 600},
            {"name": "duck",
             "expiration_date": datetime.date(2025, 2, 1),
             "price": 160}
        ],
        ["salmon"]
    ),
])
@patch("app.main.datetime.date")
def test_outdated_products(mock_date: datetime.date,
                           products: list[dict],
                           result: list[str],
                           mock_today: datetime.date) -> None:
    mock_date.today.return_value = mock_today
    assert (outdated_products(products)
            == result), "Result is not as expected"
