    with open('new_example.csv', 'w', encoding='utf-8') as new_csv_file:
        csv_writer = csv.writer(new_csv_file)

        for line in csv_reader:
            csv_writer.writerow(line)