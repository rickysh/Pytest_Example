# Pytest Essentials Guide


## Getting Started with Pytest

* **Installation**  
Use `pip install pytest` in your terminal to install Pytest.

* **Test File Naming Convention:**  
Create Python files with names starting with `test_` or ending with `_test.py` to signify test files to Pytest.

## Writing Your First Pytest

**1. Basic Test Structure:**  
```
def test_add():
    assert 2 + 3 == 5  # Use `assert` for assertions
```
Run tests from the command line using `pytest`. The output will indicate a passing test.

## Essential Pytest Commands and Functions

**2. Running All Tests:**  
`pytest`: Executes all tests in the current directory and subdirectories.

**3. Selecting Specific Tests:**  
- Run a single test file: `pytest test_math.py`.
- Run tests matching a pattern: `pytest test*.py` (tests in all files starting with `test_`). 
- Run tests containing a specific string: `pytest -k "add"` (tests with "add" in their names).

**4. Verbosity Levels:**  
- `-q`: Quiet mode, minimal output.
- `-v`: Verbose mode, detailed output.

**5. Capturing Test Output:**  
The `capsys` fixture captures standard output and error streams (see example in: [test_math.py](tests/test_math.py)).

**6. Skipping Tests:**  
Use `@pytest.mark.skip` to temporarily disable a test.

**7. Marking and Filtering Tests:**  
- Define `<custom_marker>` in `pytest.ini` file. See example [here](tests/pytest.ini).
- Create custom markers in test file: `@pytest.mark.<custom_marker>`.
- Filter running by markers: `pytest -m "<custom_marker>"` to run only `<custom_marker>` tests.

**8. Parametrizing Tests:**  
Use `@pytest.mark.parametrize` to run the same test with different data sets (see example in: [test_math.py](tests/test_math.py)).

## Advanced Pytest Features

**9. Fixtures:**  
- Fixtures provide reusable setup and teardown logic for tests.
- Store common fixtures in a `conftest.py` file. See example [here](tests/conftest.py).

**10. Custom Assertions:**  
Extend Pytest's assertion capabilities with custom functions.See example [here](tests/custom_assertions.py).

**11. Command-Line Options:**  
- `--co`: List all collected test files and functions.
- `--lf`: re-run the failures.
- `--junitfile=report.xml`: Generate JUnit XML report for CI/CD integration.

**12. Plugins:**  
- Extend Pytest functionality with plugins for reporting, linters, coverage, etc.
- Install plugins with `pip install pytest-<plugin-name>`. For example: `pytest-html`: a plugin that generates a HTML report for test results.