import pytest


@pytest.mark.railflow(
    jira_ids=["100231"],
    case_fields=[{'name': 'required text field', 'value': 'test_power'}],
    result_fields=[{'name': 'custom field', 'value': 'test_power_cr'}],
    case_type="Acceptance",
    case_priority="High"
)
def test_power():
    """
    Test details are given here.
    """
    a = 3
    b = 2
    c = a ** b
    assert c == 9


@pytest.mark.railflow(case_priority="Low")
@pytest.mark.railflow(case_type="Security")
@pytest.mark.railflow(case_fields=[{'name': 'required text field', 'value': 'Hello from PyTest'}])
@pytest.mark.railflow(result_fields=[{'name': 'custom field', 'value': 'Result from PyTest'}])
@pytest.mark.railflow(jira_ids=["id1", "id2"])
def test_modulus():
    a = 3
    b = 2
    c = a % b
    assert c == 0


# @pytest.mark.railflow(testrail_ids=[23700, 23701])
def test_mapping_to_other_cases():
    a = 3
    b = 2
    c = a + b
    assert c == 4
