import time
import csv
from django.db import IntegrityError, transaction
from app.models import EmployeeRecord, DepartmentRecord

from datetime import datetime

def run():
    # Define the path to the directory containing the weather data files
    data_file = '../wx_data/employees_data.csv'
    # Keep track of the number of records ingested
    num_records = 0

    # Keep track of the start time
    start_time = time.time()
    # Extract the station ID from the file name
    with open(data_file, 'r', encoding='utf-8-sig') as csvfile:
        # Create a CSV reader object
        csvreader = csv.reader(csvfile)
        next(csvreader)
        d_dict = dict()

        # Loop through each row in the CSV file'
        for row in csvreader:
            emp = row[0]
            full_name = row[1]
            job_title = row[2]
            gender = row[5]
            age = int(row[7])
            hire_date = datetime.strptime(row[8], "%m/%d/%Y").strftime("%Y-%m-%d")
            salary = int(row[9].replace(",", "").replace("$", ""))
            bonus = row[10]
            country = row[11]
            city = row[12]
            exit_date = None if row[13] == "" else datetime.strptime(row[13], "%m/%d/%Y").strftime("%Y-%m-%d")

            department = row[3]
            if department not in d_dict:
                r = DepartmentRecord(name=department)
                r.save()
                d_dict[department] = r
            record = EmployeeRecord(emp, full_name, job_title, d_dict[department].id, gender, age, hire_date, salary,
                                    bonus, country, city, exit_date)
            # Attempt to save the record to the database
            try:
                with transaction.atomic():
                    record.save()
                    num_records += 1
            except IntegrityError:
                print("unable to add ")
                pass

    # Calculate the elapsed time
    elapsed_time = time.time() - start_time

    # Print a summary of the results
    print(f"Ingested {num_records} records in {elapsed_time:.2f} seconds")
