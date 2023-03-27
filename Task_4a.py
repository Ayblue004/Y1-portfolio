# Import all required dependecies 
import datetime
import pandas as pd
import matplotlib.pyplot as plt

# Get the content of the file
df = pd.read_csv('Task_4a.csv')

# Displays all available options to the user and returns user response
def mainmenu():
    print("\t\t****Welcome to the Dashboard****")
    print('1) Return all current data')
    print('2) Return data for a specific region')
    print('3) Return Property trends')

    # Prompts the user on what input they should provide
    option = input("Please enter an option '1' or '2'...")
    # Checks if the user entered the correct input
    while True:
        if option != "1" and option != "2" and option != "3":
            print("Not a valid option")
            option = input("Please enter only 1 or 2: ")
        else:
            return int(option)
        

# Prints all the data from the Task_4a.csv file 
def alldata():
    print(df)


def region_check(region, startdate, enddate):  # region, startdate, enddate

    df1 = df.loc[:, startdate:enddate]
    df2 = df.loc[:, 'Region Code':'Rooms']

    result = pd.concat([df2, df1], axis=1, join='inner').where(df2["Region"] == region)
    result = pd.DataFrame(result)
    result.dropna(inplace=True)
    print(result)
    ave = df1.mean()
    ave.plot()
    plt.show()
    return result

def property_trend(property, startdate, enddate):
    df1 = df.loc[:, startdate:enddate]
    df2 = df.loc[:, 'Region Code':'Rooms']

    result = pd.concat([df2, df1], axis=1, join='inner').where(df2["Region"] == property)
    result = pd.DataFrame(result)
    result.dropna(inplace=True)
    print(result)
    ave = df1.mean()
    ave.plot()
    plt.show()
    return result

# Properties 
# Bungalow
# Semi-Detached
# Detached


x = mainmenu()
while x == 1 or x == 2 or x == 3:
    if x == 3:
        while True:
            print()

            property = input("Please enter the property type")
            property = property.capitalize()
            if property in df['Property Type'].values:
                while True:
                    startdate = input("PLEASE ENTER A START DATE AS MONTH-YEAR e.g. JAN-20")
                    startdate = startdate.capitalize()
                    if startdate not in df.columns:
                        print("Error start date not found")
                    else:
                        while True:
                            enddate = input("PLEASE ENTER AN END DATE AS MONTH-YEAR e.g. JAN-20")
                            enddate = enddate.capitalize()
                            if enddate not in df.columns:
                                print("Error end date not found")
                            else:
                                property_trend(property, startdate, enddate)
                                break
                        break
                break
            else:
                print("Property not found")
    elif x == 1:
        alldata()

    elif x == 2:
        while True:
            print()

            region = input("Please enter the name of the region you would like to check:")
            region = region.capitalize()
            if region in df.Region.values:
                while True:
                    startdate = input("PLEASE ENTER A START DATE AS MONTH-YEAR e.g. JAN-20")
                    startdate = startdate.capitalize()
                    if startdate not in df.columns:
                        print("Error start date not found")
                    else:
                        while True:
                            enddate = input("PLEASE ENTER AN END DATE AS MONTH-YEAR e.g. JAN-20")
                            enddate = enddate.capitalize()
                            if enddate not in df.columns:
                                print("Error end date not found")
                            else:
                                region_check(region, startdate, enddate)
                                break
                        break
                break
            else:
                print("Region not found")

    x = mainmenu()
