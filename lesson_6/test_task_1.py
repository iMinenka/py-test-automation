import pytest
import logging

from lesson_6.task_1 import Company, Engineer
from lesson_6.constants import (
    COMPANY_NAME1,
    COMPANY_ADDRESS1,
    ENGINEER_NAME1,
    ENGINEER_AGE
)

logger = logging.getLogger(__name__)


def test_company_creation(new_company):
    """Test company creation and its attributes."""
    logger.info(f'Testing {new_company} exists')
    assert new_company, 'Company does not exist'
    logger.info(f'Testing {new_company} is of Company class')
    assert isinstance(new_company, Company), f'{new_company} is not company class.'
    logger.info(f"Testing company's attributes of {COMPANY_NAME1}")
    assert new_company.name == COMPANY_NAME1, "Incorrect company's name"
    assert new_company.address == COMPANY_ADDRESS1, "Incorrect company's address"
    assert new_company.employees == [], "Incorrect company's employees"
    assert new_company.is_bankrupt is False, "Incorrect company's is_bankrupt"
    assert new_company._Company__money == 1000, "Incorrect company's _Company__money"


@pytest.mark.xfail(raises=AssertionError, reason='Comparing with wrong content.')
def test_engineer_creation(new_engineer):
    """Test engineer creation and its attributes."""
    logger.info(f'Testing {ENGINEER_NAME1} is of Engineer class')
    assert isinstance(new_engineer, Engineer), f'{new_engineer} is not employee class.'
    logger.info(f"Testing engineer's attributes of {ENGINEER_NAME1}")
    assert new_engineer.name == 'wrong name', "Incorrect engineer's name"
    assert new_engineer.age == ENGINEER_AGE, "Incorrect engineer's age"
    assert new_engineer.sex == '<not specified>', "Incorrect engineer's sex"
    assert new_engineer.address is None, "Incorrect engineer's address"
    assert new_engineer.company is None, "Incorrect engineer's company"
    assert new_engineer._Employee__money == 0, "Incorrect engineer's _Employee__money"
    assert new_engineer.is_employed is False, "Incorrect engineer's is_employed status."


def test_engineer_join_company_success(engineer_join_company, new_engineer, new_company):
    """Test employee joins company."""
    # test employee is not employed
    logger.info(f"Testing {new_engineer} joined {new_company}")
    assert new_engineer.company == new_company, f'Employee {new_engineer} did not join company {new_company}'
    assert new_company.employees == [new_engineer], f'Company {new_company} did not hire company {new_engineer}'


def test_engineer_join_company_fail(engineer_join_company, new_engineer, new_company, new_employee, other_company):
    """Test employee joins company."""
    # case 1 - employed engineer cannot join new company
    logger.info(f"Testing employed engineer cannot join other company")
    with pytest.raises(ValueError):
        new_engineer.join_company(other_company)
    assert new_engineer.company == new_company, f'{new_engineer} should not join other company.'
    # case 2 - company cannot hire an engineer twice
    logger.info(f"Testing company cannot hire an engineer twice.")
    with pytest.raises(ValueError):
        new_company.add_employee(new_engineer)
    assert new_company.employees == [new_engineer], f'{new_engineer} is employed already'
    # case 3 - make sure employee is an instance of Engineer or Manager
    logger.info(f"Testing only Engineer or Manager can join company.")
    with pytest.raises(ValueError):
        new_company.add_employee(new_employee)
    assert new_employee not in new_company.employees, f'{new_employee} is not Engineer or Manager'



