import csv

def createCsv(data):
    with open('treatments.csv', 'w', newline='') as csvfile:
        fieldnames = ['Name', 'Address', 'Treatment', 'Place', 'Sessions', 'Cost', 'Mileage', 'Expense']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in data:
            writer.writerow({'Name': row.name, 'Address': row.address, 'Treatment': row.treatment, 
            'Place': row.place, 'Sessions': row.sessions, 'Cost': row.cost, 'Mileage': row.mileage, 'Expense': row.expense})

        
