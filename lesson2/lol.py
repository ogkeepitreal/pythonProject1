import csv
with open('lesson_csv.csv', 'r') as file:
    csv_reader = csv.DictReader(file)

#    for line in csv_reader:
#        print(line)

    with open('lol_copy.csv', 'w') as wfile:

        names = ['Name','Date of birth','Town']
        csv_writer = csv.DictWriter(wfile, lineterminator='\n', fieldnames=names)

        csv_writer.writeheader()

        for line in csv_reader:
            csv_writer.writerow(line)
            print(line)

#with open('lesson_csv.csv', 'r') as file:
#    csv_reader = csv.reader(file)

#   headers = next(csv_reader)
#
#   for name, dob, city in csv_reader:
#        print(name, dob, city)
#
#    print(headers)
#
#    with open('lol_copy.csv', 'w') as wfile:
 #       csv_writer = csv.writer(wfile, lineterminator='\n',
   #                             delimiter=',',
  #                              quoting=csv.QUOTE_ALL
 #                               )

    #    for line in csv_reader:
     #       csv_writer.writerow(line)

#with open('lol_copy.csv', 'r') as new_file:
 #   csv_reader = csv.reader(new_file, delimiter=',')

  #  for line in csv_reader:
   #     print(line)