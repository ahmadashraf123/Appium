import random
import csv
import os

class PhoneNumberGenerator:
    CSV_FILE = 'phone_numbers.csv'

    def __init__(self):
        # Ensure CSV file exists with header
        if not os.path.exists(self.CSV_FILE):
            with open(self.CSV_FILE, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['phone_number'])

    def load_existing_numbers(self):
        with open(self.CSV_FILE, mode='r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            return {row[0] for row in reader if row}

    def generate_unique_number(self):
        existing = self.load_existing_numbers()
        while True:
            number = '5' + ''.join(random.choices('0123456789', k=8))
            if number not in existing:
                return number

    def save_number(self, number):
        with open(self.CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([number])
