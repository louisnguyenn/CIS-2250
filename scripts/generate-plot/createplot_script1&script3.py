'''
createplot_script1&script3.py
  Author(s): Louis Nguyen, Ahmet Ozer, Arya Oberoi, Zain Murad

  Project: Term Project Milestone 3
  Date of Last Update: March 24, 2025.

  Functional Summary
    createplot_script1&script3.py reads a preprocessed output file and displays the data on a line plot.

     Commandline Parameters: 2
        argv[1] = preprocessed dataset in CSV format
        argv[2] = question number (1 or 3)
     References
        Datasets from https://data.ontario.ca/dataset/wages-by-education-level/resource/7b325fa1-e9d6-4329-a501-08cdc22a79df
'''

import csv
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main(argv):

    try:
        openFile = open(sys.argv[1], encoding="utf-8-sig")
    except IOError as err:
        print("Error", file=sys.stderr)
        sys.exit(1)
    
    readCSV = csv.reader(openFile, skipinitialspace=True)
    
    question = sys.argv[2]

    dataFields = []

    for row_data_fields in readCSV:
        data = []
        for i in range(len(row_data_fields)):
            data.append(row_data_fields[i])
        dataFields.append(data)
        
        
    if(question == "1"):
        
        levels = []
        wages = []
        
            
        for i in range(len(dataFields)):
            levels.append(dataFields[i][4]) 
            wages.append(float(dataFields[i][5]))

        sns.lineplot(x=levels, y=wages, label='Both Sexes', color='green')

        plt.xlabel("Education Level")
        plt.ylabel('Average Hourly Wage Rate')
        plt.title('Average Hourly Wage Rate by Education Level in Canada')
        plt.xticks(rotation=30, ha='right')
        plt.legend()
        plt.tight_layout()
        plt.show()
    
    if(question == "3"):
         
        levels = []
        maleWage = []
        femaleWage = []
         
        for i in range(len(dataFields)):
            levels.append(dataFields[i][4]) 
            maleWage.append(float(dataFields[i][5]))
            femaleWage.append(float(dataFields[i][6]))
            
        sns.lineplot(x=levels, y=maleWage, label='Male', color='blue')
        sns.lineplot(x=levels, y=femaleWage, label='Female', color='red')
        
        plt.xlabel("Education Level")
        plt.ylabel('Average Hourly Wage Rate')
        plt.title('Average Hourly Wage Rate by Education Level for Males and Females in Canada')
        plt.xticks(rotation=30, ha='right')
        plt.legend()
        plt.tight_layout()
        plt.show()
    
main(sys.argv)