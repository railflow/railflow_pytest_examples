import pytest


def test_power_in_manipulation():
    """
    Test details are given here.
    """
    a = 3
    b = 2
    c = a ** b
    assert c == 9


@pytest.mark.railflow(
    jira_ids=["100231"],
    case_fields=[{'name':'required text field', 'value': 'test_power_in_manipulation'}],
    result_fields=[{'name':'custom field','value':'test_power_in_manipulation_cr'}],
    case_type="Acceptance",
    case_priority="High"
)
class TestClass:

    def test_add(self):
        a = 3
        b = 2
        c = a + b
        assert c == 5

    def test_subtract(self):
        a = 3
        b = 2
        c = a - b
        assert c == 0

    @pytest.mark.parametrize("a,b,c", [(22, 11, 2), (64, 8, 9), (9, 3, 2)])
    def test_divide(self, a, b, c):
        assert a / b == c

    @pytest.mark.railflow(testrail_ids=[23702, 23703])
    @pytest.mark.parametrize("a,b,c", [(22, 11, 2), (64, 8, 8), (9, 3, 4)])
    def test_divide_for_mapping(self, a, b, c):
        assert a / b == c
