import pytest
from lesson_6.task_1 import Company, Engineer, Employee
from lesson_6.constants import (
    COMPANY_NAME1,
    COMPANY_ADDRESS1,
    ENGINEER_NAME1,
    ENGINEER_AGE,
    OTHER_COMPANY_NAME
)


@pytest.fixture(scope='function')
def get_test_name(request):
    """Get name of the test function/method."""
    import sys
    sys.stderr.write('\n' + request.node.name + ' starts!')

    def get_test_name_finish():
        sys.stderr.write('\n' + request.node.name + ' finished!')

    request.addfinalizer(get_test_name_finish)
    return request.fixturename


@pytest.fixture()
def new_company():
    """Add company."""
    company = Company(COMPANY_NAME1, address=COMPANY_ADDRESS1)
    return company


@pytest.fixture()
def other_company():
    """Add other company."""
    company = Company(OTHER_COMPANY_NAME, address=COMPANY_ADDRESS1)
    return company


@pytest.fixture()
def new_engineer():
    """Add engineer."""
    engineer = Engineer(ENGINEER_NAME1, ENGINEER_AGE)
    return engineer


@pytest.fixture()
def new_employee():
    """Add employee."""
    employee = Employee(ENGINEER_NAME1, ENGINEER_AGE)
    return employee


@pytest.fixture()
def engineer_join_company(new_engineer, new_company):
    """Engineer joins a company."""
    return new_engineer.join_company(new_company)


def pytest_sessionstart(session):
    """Create the results attributed to the session instance."""
    session.results = dict()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Add test result to session.results once result is ready."""
    outcome = yield
    result = outcome.get_result()

    if result.when == 'call':
        item.session.results[item] = result


def pytest_sessionfinish(session, exitstatus):
    print('\nExit code:', exitstatus)
    passed = sum(1 for result in session.results.values() if result.passed)
    failed = sum(1 for result in session.results.values() if result.failed)
    print(f'Total: {passed} tests passed and {failed} tests failed.')
