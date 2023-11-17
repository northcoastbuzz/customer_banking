# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from savings_account import create_savings_accountf
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_balance     = float(input(f"What is the account balance?\n$"))
    savings_interest    = float(input(f"What is the interest rate?\n(%) "))
    savings_maturity    = int(input(f"How many months has the account matured?\n"))


    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print("f\n")
    print(f"The interest earned for the account is  : ${interest_earned:,.2f}")
    print(f"The account is now valued at            : ${updated_savings_balance:,.2f}")
    print("f\n")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance      = float(input(f"What is the balance for the CD account?\n$"))
    cd_interest     = float(input(f"What is the interest rate?\n(%) "))
    cd_maturity     = int(input(f"How many months has the account matured?\n"))
    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print("f\n")
    print(f"The interest earned for the CD account is  : ${interest_earned:,.2f}")
    print(f"The CD account is now valued at            : ${updated_cd_balance:,.2f}")
    print("f\n")


if __name__ == "__main__":
    # Call the main function.
    main()