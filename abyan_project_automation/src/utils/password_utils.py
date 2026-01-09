
import random

def _generate_random_password(length=6):
    """Generates a 6-digit numeric password (default length=6)."""
    return ''.join(random.choices('0123456789', k=length))

#  Utility function to save password — placed outside the class
def save_password_to_csv(phone_number, password, file_path='forgot_password_history.csv'):
    import os
    file_exists = os.path.exists(file_path)

    with open(file_path, mode='a', newline='', encoding='utf-8') as file:
        fieldnames = ['Phone Number', 'Password', 'Timestamp']
        import csv
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        from datetime import datetime
        writer.writerow({
            'Phone Number': phone_number,
            'Password': password,
            'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        })

    print("Phone number, password, and timestamp saved to forgot_password_history.csv")

def get_last_saved_password(phone_number, filename='credentials.csv'):
    """
    Returns the last saved password for a given phone number from the credentials CSV.
    Returns None if no password is found.
    """
    import os
    import csv

    if not os.path.exists(filename):
        return None

    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
        for row in reversed(rows):
            if row and row[0] == phone_number:
                return row[1]  # Return the last saved password
    return None





# utilities/password_utils.py

import csv
import random


def generate_numeric_password(length=6):
        return ''.join(random.choices('0123456789', k=length))

def save_credentials_to_csv(phone_number, password, filename='credentials.csv'):
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([phone_number, password])


class PasswordUtils:
    @classmethod
    def save_credentials_to_csv(cls, phone_number, _stored_password, filename):
        pass

    @classmethod
    def generate_numeric_password(cls, length):
        pass


def get_last_saved_password(phone_number):
    return None