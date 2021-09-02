import pytest


@pytest.mark.railflow(
    jira_ids=100231,
    case_fields="filedA1",
    result_fields="fieldB1",
    testrail_ids="map id1",
    case_type="test case",
    case_priority="important"
    )  
def test_power():
    """
    Test details are given here.
    """
    a = 3
    b = 2
    c = a ** b
    assert c == 9


@pytest.mark.railflow(case_priority="normal")
@pytest.mark.railflow(case_type="test case")
@pytest.mark.railflow(testrail_ids="map id2")
@pytest.mark.railflow(result_fields="fieldB2")
@pytest.mark.railflow(case_fields="filedA2")
@pytest.mark.railflow(jira_ids=100241)
def test_modulus():
    a = 3
    b = 2
    c = a % b
    assert c == 0
