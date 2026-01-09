import csv
import os

CSV_FILE_PATH = os.path.join(os.getcwd(), "changed_phone_numbers.csv")

def save_changed_number(old_number, new_number):
    """
    Save old and new phone numbers to a CSV file.
    Appends data if file exists, otherwise creates a new one.
    """
    file_exists = os.path.isfile(CSV_FILE_PATH)

    with open(CSV_FILE_PATH, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Old Number", "New Number"])  # CSV header
        writer.writerow([old_number, new_number])

    print(f" Phone number change saved: Old={old_number}, New={new_number}")
