# Sales Logging

A Python automation script to create `.xlsx` workbooks based on a pre-defined list.

## Use Case

This script is intended to solve the repetitive task of creating Excel workbooks based on a template original. The application takes in a list of "sales" items (for instance, an invoice) & uses this list to create a seperate Excel file named in accordance to the list based off of an original, `original.xlsx`.

## About the Script

This script uses openpyxl to handle interactions with the Excel workbook(s). Specifically, the `Workbook()` funciton is used:

    from openpyxl import Workbook

The script then takes an external txt file as the read item:

    sample_txt = open('sample.txt', 'r')

This file is read and each line is iterated through and appended to an array:

    for line in sample_txt:
        sales_items.append(line.strip())

The array is then iterated through and the Workbook funciton is used to create new Excel files with unique names gathered from the array:

    for item in sales_items:
        wb = Workbook()
        wb.save(f'workbooks/Sales-Log-{item}.xlsx')

## Using this Script

To use this script, follow the steps outlined below:

1. Clone the repo to your local machine
2. Install the dependencies to your virtual environment

   `pip install -r requirements.txt`

3. Update the `sample_txt` path with the txt file you intend to use
4. Update the naming convention in `wb.save()` if desired
5. Run the application

   python app.py

## Questions

If you have any questions, or difficulties utilizing the script, please do not hesitate to reach out or submit a PR. Thanks!
