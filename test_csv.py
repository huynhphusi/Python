import csv

with open('example.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)            # Bỏ hàng đầu (header)
    for line in csv_reader:
        print(line)             # Mỗi hàng là một array

"""     with open('new_example.csv', 'w', newline='', encoding='utf-8') as new_csv_file:
        csv_writer = csv.writer(new_csv_file, delimiter=',')

        for line in csv_reader:
            csv_writer.writerow(line) """