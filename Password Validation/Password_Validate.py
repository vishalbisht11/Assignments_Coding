# Python program to check the validity of a password chosen by a user
# The program consists of two functions: validate() and main().
# The validate() functions implements the validation procedure as follows:
# a) contains at least 1 letter between [A-Z],
# b) contains at least 1 letter between [a-z],
# c) contains at least 1 number between [0-9],
# d) contains at least 1 special character from [$#@],
# e) have a minimum length of 6 characters, and
# f) have a maximum length of 12 characters.
# The parameter or the input to the function validate() is a string password.
# If password fits above criteria, valid is printed else not valid is printed.

import re   # Regular expressions module
import logging  # Logging module


def main():
    password = input("Hey Hi User! Please type the Password:")
    validate(password=password)  # Calling validate function by passing password as parameter.

# Configuring the logging. DEBUG is the minimum security level set. The log file name is PasswordValidationLog.log
# which will be opened in append mode. The format to write the message in the log file is Time when that log
# record is created followed by name of the logging module, name of the level and the message sent.
# The time format set is Date-Month-Year  Hour: Minute: Second.
logging.basicConfig(level=logging.DEBUG, filename="PasswordValidationLog.log", filemode="a", datefmt='%d-%b-%y  %H:%M:%S',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


# Validate function, which accepts the user's password and check whether its valid or not valid.
def validate(password):
    temp = 1
    while True:
        if len(password) < 6:   # Checking whether length of password is more than 6 characters or not.
            temp = 0
            break
        elif len(password) > 12:  # Checking whether length of password is less than 12 characters or not.
            temp = 0
            break
        elif not re.search("[a-z]", password):  # Checking whether password contains lowercase character/s sor not.
            temp = 0
            break
        elif not re.search("[A-Z]", password):  # Checking whether password contains uppercase character/s sor not.
            temp = 0
            break
        elif not re.search("[0-9]", password):  # Checking whether password contains number/s sor not.
            temp = 0
            break
        elif not re.search("[$@#]", password):  # Checking whether password contains special character/s [$#@] sor not.
            temp = 0
            break
        elif re.search("\s", password):  # Checking whether password contains space or not.
            temp = 0
            break
        else:
            temp = 1
            print("Valid.")
            logging.debug("Password: %s valid.", password)
            break

    if temp == 0:
        print("Not valid.\nPassword length should be more than 6 characters and not more than 12 characters."
              "It should also contain at least 1 uppercase character, 1 lowercase character, 1 number and minimum"
              "any of the special characters: #$@. ")
        logging.debug("Password: %s not valid.", password)


if __name__ == "__main__":
    main()
