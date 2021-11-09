import pytest


@pytest.mark.railflow(
    case_fields="field",
    result_fields="output",
    case_type="Normal tests",
    case_priority="Important",
    smart_assignment=["user1@gmail.com, user2@gmail.com"],
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

    @pytest.mark.railflow(
        jira_ids=100334,
        case_fields="function fields",
        result_fields="function result fields",
        testrail_ids=[1234, 213],
        case_type="function type",
        case_priority="function priority"
    )
    @pytest.mark.parametrize("a,b,c", [(22, 11, 2), (64, 8, 8), (9, 3, 3)])
    def test_divide(self, a, b, c):
        assert a / b == c
