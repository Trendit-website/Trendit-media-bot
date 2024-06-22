'''
This module defines basic helper functions for the Trendit³ Flask application.

These functions perform common tasks that are used throughout the application.

@author: Emmanuel Olowu
@link: https://github.com/zeddyemy
@package: Trendit³ Bot
'''
import random, string, logging, time
from slugify import slugify

from config import Config



def url_parts(url):
    """
    Splits a URL into its constituent parts.

    Args:
        url (str): The URL to split.

    Returns:
        list: A list of strings representing the parts of the URL.
    """
    
    theUrlParts =url.split('/')
    
    return theUrlParts

def int_or_none(s):
    """
    Converts a string to an integer, or returns None if the string cannot be converted.

    Args:
        s (str): The string to convert.

    Returns:
        int or None: The converted integer, or None if conversion is not possible.
    """
    
    try:
        return int(s)
    except:
        return None


def generate_random_string(length=8):
    """
    Generates a random string of specified length, consisting of lowercase letters and digits.

    Args:
        length (int): The desired length of the random string.

    Returns:
        str: A random string of the specified length.
    """
    characters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


def console_log(label: str ='Label', data: any =None) -> None:
    """
    Print a formatted message to the console for visual clarity.

    Args:
        label (str, optional): A label for the message, centered and surrounded by dashes. Defaults to 'Label'.
        data: The data to be printed. Can be of any type. Defaults to None.
    """

    print(f'\n\n{label:-^50}\n', data, f'\n{"//":-^50}\n\n')


def log_exception(label: str ='EXCEPTION', data='Nothing') -> None:
    """
    Log an exception with details to a logging handler for debugging.

    Args:
        label (str, optional): A label for the exception, centered and surrounded by dashes. Defaults to 'EXCEPTION'.
        data: Additional data to be logged along with the exception. Defaults to 'Nothing'.
    """

    logging.exception(f'\n\n{label:-^50}\n {str(data)} \n {"//":-^50}\n\n')  # Log the error details for debugging


