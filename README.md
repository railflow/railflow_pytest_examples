# Railflow Pytest Examples

Examples of using railflow package for selenium, appium, rest api tests
for integration with testrail.

The plugin is ready now and can be accessed from the directory itself.
The plugin now works for both python 2.7 and python 3.4 or greater.

Installation
============

You can install the plugin via pip using the following command.

    pip install pytest-railflow-testrail-reporter

Writing Tests
=============

The plugin supports following metadata attributes. All other undefined
metadata attributes will be rejected with a warning.

  Function level Attributes | Class level Attributes
  --------------------------|-----------------------
  jira\_ids | case\_fields
  case\_fields | result\_fields
  result\_fields | case\_type
  testrail\_ids | case\_priority
  case\_type | smart\_assignment
  case\_priority | 

The attributes should be defined in the markers with marker name
`railflow`.

So a sample test case looks like:

    import pytest

    @pytest.mark.railflow(testrail_ids=121131)
    def test_sample():
        """
        This is a sample test
        """
        assert 1 == 1

Run the Test
============

Write the above test to a file with `test_` as prefix (eg:
`test_file.py`). Now run the test using the command:

    pytest --jsonfile test_output.json test_file.py

Here `test_output.json` is the name of output json file.

JSON output
===========

The output of above `test_file.py` is stored in `test_output.json` file which is given below:



    [
        {
            "railflow_test_attributes": {
                "testrail_ids": 121131
            },
            "class_name": null,
            "test_name": "test_sample",
            "details": "This is a sample test",
            "markers": "",
            "result": "PASSED",
            "duration": 0.0004558590007945895,
            "timestamp": "2021-08-27T04:08:28",
            "message": null,
            "file_name": "test_file"
        }
    ]


Other Examples
==============

Function level
--------------

1.  All attributes can be defined inside a single railflow marker as
    shown below.

<!-- -->

    import pytest

    @pytest.mark.railflow(
    jira_ids=100231,
    case_fields="filedA1",
    result_fields="fieldB1",
    testrail_ids="map id1",
    case_type="test case",
    case_priority="important"
    )  
    def test_add():
    """
    Add two numbers
    """
    a = 2 + 7
    assert a == 9


The JSON output of above file will look like this:

    {
       "railflow_test_attributes": {
            "jira_ids": 100231,
            "case_fields": "filedA1",
            "result_fields": "fieldB1",
            "testrail_ids": "map id1",
            "case_type": "test case",
            "case_priority": "important"
        },
        "class_name": null,
        "test_name": "test_add",
        "details": "Test details are given here.",
        "markers": "",
        "result": "PASSED",
        "duration": 0.00040752196218818426,
        "timestamp": "2021-08-27T07:35:00",
        "message": null,
        "file_name": "test_calculation"
    }
    
2.  It is also possible to define the attributes in separate markers for
    a single test. But the metadata should be added in reverse order as
    shown below:

<!-- -->

    import pytest

    @pytest.mark.railflow(case_priority="normal")
    @pytest.mark.railflow(case_type="test case")
    @pytest.mark.railflow(testrail_ids="map id2")
    @pytest.mark.railflow(result_fields="fieldB2")
    @pytest.mark.railflow(case_fields="filedA2")
    @pytest.mark.railflow(jira_ids=100241)
        """
        Add two numbers
        """
        a = 2 + 7
        assert a == 9

Class Level
-----------

Class level marker attributes are different from function level markers. If the `railflow` marker is defined in function level within a class, it will override the class level marker. Class level definition of `railflow` marker is given below:

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
   
Usage with pytest-splinter
==========================

pytest-railflow-testrail-reporter supports the [pytest-splinter](https://github.com/pytest-dev/pytest-splinter) plugin and thus includes the screenshot path in the JSON file if the test fails.

We can write a test case, for example, visit a url, reload it and check if the url is same as given below:

    @pytest.mark.railflow(
    jira_ids=100414,
    case_fields="field_splint reload",
    result_fields="field_B3",
    testrail_ids="map id4",
    case_type="test browser splinter",
    case_priority="important"
    )
    def test_reload(browser):
        "test reload page"
        url = "https://www.duckduckgo.com"
        browser.visit(url)
        browser.reload()
        assert browser.url == 'https://www.google.com'
        
The browser reloads `www.duckduckgo.com` and validates if it is `www.google.com`. We are intentionally failing the test to generate screenshot at the failure. As the test fails, the failure screenshot will be generated and stored in a folder with name of test file. The screenshot file name includes the name of test case and browser.

So the JSON output will be as follows:

    {
        "railflow_test_attributes": {
            "jira_ids": 100414,
            "case_fields": "field_splint reload",
            "result_fields": "field_B3",
            "testrail_ids": "map id4",
            "case_type": "test browser splinter",
            "case_priority": "important"
        },
                "class_name": null,
        "test_name": "test_reload",
        "details": "test reload page",
        "markers": "",
        "result": "FAILED",
        "duration": 2.566374588001054,
        "timestamp": "2021-09-02T09:32:35",
        "message": "browser = <splinter.driver.webdriver.firefox.WebDriver object at 0x7fe56805e880>\n\n    @pytest.mark.railflow(\n        jira_ids=100414,\n        case_fields=\"field_splint reload\",\n        result_fields=\"field_B3\",\n        testrail_ids=\"map id4\",\n        case_type=\"test browser splinter\",\n        case_priority=\"important\"\n        )\n    def test_reload(browser):\n        \"test reload page\"\n        url = \"https://www.duckduckgo.com\"\n        browser.visit(url)\n        browser.reload()\n>       assert browser.url == 'https://www.google.com'\nE       AssertionError: assert 'https://duckduckgo.com/' == 'https://www.google.com'\nE         - https://www.google.com\nE         + https://duckduckgo.com/\n\ntest_splinter.py:48: AssertionError",
        "file_name": "test_splinter",
        "splinter_screenshot_dir": " /home/user/railflow/railflow_pytest_examples/test_splinter/test_reload-browser.png"
    }

More test cases can be found in the repository itself. A JSON file output of all tests and splinter screenshot files of failed tests can also be found here.

Create Virtual Environment with Python and run the tests
========================================================

1. Open terminal/command prompt in desired folder. Run the command:
    
       python3 -m venv <environment name>
    
2. A folder with environment name appears there. Now activate the environment using the following command:

       source <environment name>/bin/activate
    
3. Now you can see the environment name in the terminal. To run the tests, we have to install necessary packages in the virtual environment. To install pytest-railflow-testrail-reporter, run:

       pip install pytest-railflow-testrail-reporter
    
4. For pytest-splinter, run:

       pip install pytest-splinter
    
Now create the test file in the folder and run the tests.
    
