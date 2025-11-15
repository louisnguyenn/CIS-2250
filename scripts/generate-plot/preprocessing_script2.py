'''
preprocessing_script2.py
  Author(s): Louis Nguyen, Ahmet Ozer, Arya Oberoi, Zain Murad

  Project: Term Project Milestone 3
  Date of Last Update: March 24, 2025.

  Functional Summary
      preprocessing_script2.py reads two files and processes them
      into a new CSV where we can analyze the data using a visualization.
      It reads the following parameters: Year, Education level, and Experience level.
      These required parameters will help us answer our question of wage differences between
      education and experience level overtime, to show if education and experience level impacts
      wages.

      There are expected to be four fields:
        1. Year
        2. Education level (from primary dataset)
        3. Experience level (from secondary dataset)
        4. Hourly Wages

     Commandline Parameters: 7
        argv[1] = primary dataset (education level)
        argv[2] = secondary dataset (experience level)
        argv[3] = year start
        argv[4] = year end
        argv[5] = education level
        argv[6] = experience level
     References
        Datasets from https://data.ontario.ca/dataset/wages-by-education-level/resource/7b325fa1-e9d6-4329-a501-08cdc22a79df and 
        https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410044301
'''

import sys
import csv

def main(argv):

    # checking if we have been given the correct amount of parameters
    if len(argv) != 7:
        print("Usage: preprocessing_q2.py <v0913_05.csv> <14100328.csv> <year start> <year end> <education level> <experience level>")
        sys.exit(1)
    
    # reading commandline arguments
    primary_dataset_file = argv[1]
    secondary_dataset_file = argv[2]
    year_start = int(argv[3])
    year_end = int(argv[4])
    education_level = argv[5]
    experience_level = argv[6]

    # opening the primary dataset
    try:
        primary_dataset_file_fh = open(primary_dataset_file, encoding="utf-8-sig")

    except IOError as err:
        print("Unable to open file '{}' : {}".format(primary_dataset_file, err), file=sys.stderr)
        sys.exit(1)

    # opening output files
    try:
        primary_output_fh = open('primary_dataset_1.csv', 'w', newline='', encoding='utf-8-sig')

    except IOError as err:
        print("Unable to open file 'primary_dataset_output.csv' : {}".format(err), file=sys.stderr)
        sys.exit(1)

    # opening the secondary dataset
    try:
        secondary_dataset_file_fh = open(secondary_dataset_file, encoding="utf-8-sig")

    except IOError as err:
        print("Unable to open file '{}' : {}".format(secondary_dataset_file, err), file=sys.stderr)
        sys.exit(1)

    # opening output files in write mode
    try:
        secondary_output_fh = open('secondary_dataset_1.csv', 'w', newline='', encoding='utf-8-sig')

    except IOError as err:
        print("Unable to open file 'secondary_dataset_output.csv' : {}".format(err), file=sys.stderr)
        sys.exit(1)

    primary_dataset_reader = csv.reader(primary_dataset_file_fh, skipinitialspace=True)
    secondary_dataset_reader = csv.reader(secondary_dataset_file_fh, skipinitialspace=True)

    # skip the header row for both datasets using the next() function
    # the next function skips the first iteration, so when we are reading from the file using csv.reader()
    # it will skip the first line (the header) of the CSV file
    next(primary_dataset_reader, None)
    next(secondary_dataset_reader, None) 

    # creating csv writers to write the datasets onto a output CSV file
    primary_writer = csv.writer(primary_output_fh)
    secondary_writer = csv.writer(secondary_output_fh)

    # writing headers to the output files
    primary_writer.writerow(['Education level', 'Year', 'Wages'])
    secondary_writer.writerow(['Experience level', 'Year', 'Wages'])

    # government of ontario dataset (education level)
    print("Reading first file...")
    for row_data_fields in primary_dataset_reader:
        year = row_data_fields[0].strip()

        if int(year) >= year_start and int(year) <= year_end:
            geography_field = row_data_fields[1].strip()
            education_level_field = row_data_fields[4].strip()
            wages_field = row_data_fields[6].strip()

            if geography_field == "Canada" and education_level_field == education_level:
                    if row_data_fields[3].strip() == "Average hourly wage rate":
                        if wages_field.strip() != "":   # removing any blanks or empty strings that could be in the CSV file
                            primary_writer.writerow([education_level_field, year, wages_field]) # writing the row to the output CSV file

    print("First file preprocessing done.\n")

    # Statistics Canada dataset (experience level)
    print("Reading second file...")
    for row_data_fields_2 in secondary_dataset_reader:
        year = row_data_fields_2[0].strip()
        year_split = int(year.split('-')[0]) # splitting the date and taking the year (e.g. 2019-01 -> 2019)
                                             # this formatted date only shows up on the Statistics Canada dataset, so we rmeove
                                             # it for only this file and correctly process the year
    
        if year_split >= year_start and year_split <= year_end:
            experience_level_field = row_data_fields_2[4].strip()
            geography_field_2 = row_data_fields_2[1].strip()
            average_offered_hourly_wage = row_data_fields_2[12].strip()

            if experience_level_field == experience_level and geography_field_2 == "Canada":
                if row_data_fields_2[5].strip() == "Average offered hourly wage" and row_data_fields_2[6].strip() == "Dollars":
                    if average_offered_hourly_wage.strip() != "":   # removing any blanks or empty strings that could be in the CSV file
                        secondary_writer.writerow([experience_level_field, year_split, average_offered_hourly_wage]) # writing the row to the output CSV file

    print("Second file preprocessing done.")

main(sys.argv)