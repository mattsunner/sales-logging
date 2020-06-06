from openpyxl import Workbook


# Import sample list
sample_txt = open('sample.txt', 'r')

# Iterate through list and add each item to an array
sales_items = []

for line in sample_txt:
    sales_items.append(line.strip())

# Iterate through the array and create a new, standardized workbook for each item


# Tear down & close