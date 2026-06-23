import pytest
from app.operations import OperationFactory


@pytest.mark.parametrize(
    "operation,a,b,expected",
    [
        ("add", 2, 3, 5),
        ("subtract", 5, 2, 3),
        ("multiply", 4, 3, 12),
        ("divide", 10, 2, 5),
        ("power", 2, 3, 8),
        ("root", 27, 3, 3),
    ],
)
def test_operations(operation, a, b, expected):
    result = OperationFactory.create_operation(operation).execute(a, b)
    assert result == pytest.approx(expected)


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        OperationFactory.create_operation("divide").execute(5, 0)


def test_root_zero():
    with pytest.raises(ValueError):
        OperationFactory.create_operation("root").execute(9, 0)


def test_invalid_operation():
    with pytest.raises(ValueError):
        OperationFactory.create_operation("bad")