import logging

class InvalidStateException(Exception):
    pass

class InvalidIMEIException(Exception):
    pass

# Set all the error logging in this class
class ErrorLogging :
     

        # Set the filepath for the error log
        error_log_filepath = "error.log"

        # Configure the logging
        logging.basicConfig(filename=error_log_filepath, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

        # Array of randomly generated error messages
        # Commented error messages are passive aggressive statements. 
        # Only activate commented error messages if you have a strong heart and mind.

        # IMEI is blank
        error_messages = [
            # "I can't even with you right now.",
            # "Do you not know how to copy and paste properly?",
            # "Arthas did nothing wrong",
            # "You're wasting your time. Populate the IMEI properly.",
            # "What is your IQ?",
            # "Just have somebody else swap for you.."
            "It's Blank.",
            "Please, Populate the field",
            "You forgot to type in the IMEI",
            "Boss Ahead",
            "NANI???"
        ]
        
        # IMEI is short
        short_error_messages = [
            # "I'm being as lazy as you are with these error messages",
            # "Did you not learn how to use a computer as a child?",
            # "Are you blind?",
            # "Can you do anything right?",
            # "What came first, the messed up IMEI command or the failed SIM Swap?"
            "The Etruscan shrew is the smallest mammal on earth, much like the IMEI input",
            "The IMEI is too short.",
            "Try again, it's too short",
            "Generally the playoff run of the Toronto Maple Leafs."
        ]

        # IMEI is long
        long_error_messages = [
            # "Your power level is clearly under 9000.",
            # "Fact: That input was trash."
            "The IMEI is too long.",
            "Try again, it's too long.",
            "It's an IMEI number not a python. Shorten it to 15 integers",
            "I always got yelled at for keeping the fridge open too long."
        ]

        # IMEI has a letter
        letter_error_messages = [
            # "Failure ahead...",
            # "It's alright. It's been a long day.",
            # "If you input the IMEI properly next time, you'll successfully complete the sim swap.",
            # "Did you input it correctly?",
            # "Try again!"
            "Check for letters.",
            "The IMEI can only be integers",
            "Please delete any letters"
           
        ]