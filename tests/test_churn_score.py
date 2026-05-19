import pytest

from src.churn_score import score_churn


def test_score_between_zero_and_one():
    value = score_churn(months_active=3, complaints=4)
    assert 0 <= value <= 1.5


def test_low_risk_customer():
    assert score_churn(months_active=24, complaints=0) == pytest.approx(0.2)


def test_recent_customer_with_complaints():
    assert score_churn(months_active=2, complaints=5) == pytest.approx(0.9)