import csv
import os
import random
from datetime import datetime


class RandomDataGenerator:

    @staticmethod
    def generate_valid_saudi_number():
        """
        Generates a valid Saudi mobile number (9 digits) starting with 5.
        Example: 5XXXXXXXX
        """
        number = '5' + ''.join(str(random.randint(0, 9)) for _ in range(8))
        print(f"Generated Saudi mobile number: {number}")
        return number

    @staticmethod
    def generate_Nid_number_Saudi_user():
        return 1234567890

    @staticmethod
    def generate_iqama_number_non_Saudi_user():
        return 2130635150

    @classmethod
    def generate_used_saudi_number(cls):
        pass

