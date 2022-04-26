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
    jira_ids=["301219"],
    case_fields=[
        {
            "name": "Required text field",
            "value": "Class"
        }
    ],
    result_fields=[
        {
            "name": "Custom field",
            "value": "Result from class"
        }
    ],
    case_type="Railflow",
    case_priority="Critical"
)
class TestClass:

    def test_add(self):
        a = 3
        b = 2
        c = a + b
        assert c == 3

    def test_subtract(self):
        a = 3
        b = 2
        c = a - b
        assert c == 0

    def test_subtract_two(self):
        a = 3
        b = 2
        c = a - b
        assert c == 0

    @pytest.mark.railflow(
        jira_ids=["11111"],
        case_fields=[
            {
                "name": "Required text field",
                "value": "method"
            }
        ],
        result_fields=[
            {
                "name": "Custom field",
                "value": "Result from method"
            }
        ],
        case_type="Automated",
        case_priority="High"
    )    
    @pytest.mark.parametrize("a,b,c", [(22, 11, 2), (64, 8, 9), (9, 3, 2)])
    def test_divide(self, a, b, c):
        assert a / b == c

    # @pytest.mark.railflow(testrail_ids=[23702, 23703])
    @pytest.mark.parametrize("a,b,c", [(22, 11, 2), (64, 8, 8), (9, 3, 4)])
    def test_divide_for_mapping(self, a, b, c):
        assert a / b == c
