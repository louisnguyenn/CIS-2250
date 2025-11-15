'''
createplot_script2.py
  Author(s): Louis Nguyen, Ahmet Ozer, Arya Oberoi, Zain Murad

  Project: Term Project Milestone 3
  Date of Last Update: March 24, 2025.

  Functional Summary
      createplot_script2.py reads two preprocessed output CSV files created by preprocessing_script2.py
      and combines them into a single dataframe.
      It then creates a line plot with the combined dataframe and displays the visualization
      in any image format.

     Commandline Parameters: 2
        argv[1] = preprocessed priamry dataset (education level)
        argv[2] = preprocessed secondary dataset (experience level)
        argv[3] = graphics file of any image format (PDF, PNG, etc.)
     References
        Datasets from https://data.ontario.ca/dataset/wages-by-education-level/resource/7b325fa1-e9d6-4329-a501-08cdc22a79df and 
        https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1410044301
'''

import sys
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

def main(argv):

    # checking if we are given the correct amount of arguments
    if len(argv) != 4:
        print("Usage: createplot_q2.py <graphics file>")
        sys.exit(1)

    # reading commandline arguments
    dataset1 = argv[1]
    dataset2 = argv[2]
    graphics = argv[3]

    # open the primary csv file using pandas to read the entire CSV file
    try:
        primary_dataset_reader = pd.read_csv(dataset1, encoding="utf-8-sig")
    
    except IOError as err:
        print("Unable to open source file '{}' : {}".format(dataset1, err), file=sys.stderr);
        sys.exit(1);

    # open the secondary csv file using pandas to read the entire CSV file
    try:
        secondary_dataset_reader = pd.read_csv(dataset2, encoding="utf-8-sig")
    
    except IOError as err:
        print("Unable to open source file '{}' : {}".format(dataset2, err), file=sys.stderr);
        sys.exit(1);

    # renaming primary dataset and adding a dataset identifier
    primary_df = primary_dataset_reader.rename(columns={"Education level": "Category"})
    primary_df["Dataset"] = "Education"

    # renaming secondary dataset and adding a dataset identifier
    secondary_df = secondary_dataset_reader.rename(columns={"Experience level": "Category"})
    secondary_df["Dataset"] = "Experience"

    # combine the datasets into a single DataFrame using pandas concat function
    combined_df = pd.concat([primary_df, secondary_df], ignore_index=True)

    print("Creating plot...")
    # creating a figure
    fig = plt.figure()

    # creating a line plot with the combined dataset
    sns.lineplot(x="Year", y="Wages", hue="Category", data=combined_df, errorbar=None)

    # adding title
    plt.title("Wages by Education and Experience Levels Over Time")

    # make the x axis (year) display as an integer instead of a float
    plt.gca().xaxis.set_major_locator(plt.MaxNLocator(integer=True))

    fig.savefig(graphics, bbox_inches="tight")

    print("Plot created.")

main(sys.argv)