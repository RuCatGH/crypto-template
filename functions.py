from modules import *
from utils.networks import *


def get_client(account_number, private_key, proxy, email_address=None, email_password=None) -> Client:
    return Client(account_number, private_key, proxy, email_address, email_password)
