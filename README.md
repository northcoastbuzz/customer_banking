# Project Name

A simple banking system project with Python.

## Project Structure

- `Account.py`: Contains the base class representing a generic bank account.
- `savings_account.py`: Implements a Savings Account with interest calculations.
- `cd_account.py`: Implements a Certificate of Deposit (CD) account with interest calculations.
- `customer_banking.py`: This script provides a simple interactive interface for users to simulate the creation and management of savings and CD accounts.

## Project Description

This project aims to create a basic banking system with different account types. Each Python file represents a specific aspect of the system.

### Account.py

The `Account.py` file contains the `Account` class, which serves as the base class for different types of bank accounts in the project. The class contains functions for setting the account balance and setting the interest rate.  This completed file was provided by Ohio State in the initial file set for this assignment and no changes were made by the author to this file.

### savings_account.py

The `savings_account.py` file implements the `create_savings_account` function, providing functionality for creating a savings account, calculating interest earned, and updating the account balance. This functionality is built upon the `Account` class from the `Account.py` file.

#### Function `create_savings_account(balance, interest_rate, months)`
This function takes three parameters:

- `balance` (float): The initial savings account balance.
- `interest_rate` (float): The Annual Percentage Rate (APR) interest rate for the savings account.
- `months` (int): The length of months over which the interest is calculated.

**Returns:**

- `new_balance` (float): The updated savings account balance after adding the interest earned.
- `earned_interest` (float): The amount of interest earned during the specified period.

This function facilitates the management of a savings account, allowing users to create an account, calculate interest, and retrieve updated account details after a specified period.

### cd_account.py

The `cd_account.py` file provides the `create_cd_account` function, which enables the creation of a Certificate of Deposit (CD) account. This function utilizes the `Account` class from the `Account.py` file to manage the CD account's functionalities, including interest calculation and balance updating.

#### Function `create_cd_account(balance, interest_rate, months)`
This function takes three parameters:

- `balance` (float): The initial CD account balance.
- `interest_rate` (float): The Annual Percentage Rate (APR) interest rate for the CD account.
- `months` (int): The length of months for the CD account.

**Returns:**

- `new_balance` (float): The updated CD account balance after adding the interest earned.
- `earned_interest` (float): The amount of interest earned during the specified CD period.

This function facilitates the management of a CD account, allowing users to create an account, calculate interest, and retrieve updated account details after a specified CD period.

### customer_banking.py

The `customer_banking.py` file contains the `main` function, which serves as the entry point for the banking system simulation. This function prompts the user to input information for both a savings account and a CD account, calculates the interest earned, and displays the updated balances.
