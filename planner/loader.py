import csv


def time_to_minutes(time_string):
    """
    This function is a helper function that will take a string like "9:40 AM" and convert it to minutes
    so the expected return is 580, this way it is easier to compare conflicting class times as one number 
    """
    # save and split on the space between 9:40 " " AM
    parts = time_string.split(" ")
    # AM / PM
    day_period = parts[1]
    # split on : for "9 40" to have hours and minutes separated
    time_parts = parts[0].split(":")
    # rename variables and turn into ints
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    # if PM add 12 hours as long as 12 is not in the hour slot
    if day_period == "PM" and hours != 12:
        hours += 12
    # edge case for 12 AM expected result is 0
    if day_period == "AM" and hours == 12:
        hours = 0
    # total = hours * 60 + minutes
    total = hours * 60 + minutes
    return total

def load_sections(path):
    """
    This function is going to open the CSV file with csv.DictReader, it will clean each row
    split each into their own dictionary then appended all returned into a cleaned list of rows
    """
    # open the exported excel file
    with open(path, encoding="utf-8-sig") as f:
        # empty list to hold the cleaned rows
        cleaned_rows = []
        # variable to read through the excel sheet 
        reader = csv.DictReader(f)
        # for each row build a new dictionary for each with the nine keys crn,course_num etc. add it to a list and return 
        for row in reader:
            # new dictionary - changed course_num and is_lab into ints, days into a list split on the comma and space, used
            # the helper function for times and then keep the rest as text
            section = {"crn": row["crn"],
                       "subject":row["subject"],
                       "course_num":int(row["course_num"]),
                       "is_lab":int(row["is_lab"]),
                       "course_name":row["course_name"],
                       "days":row["days"].split(", "),
                       "start_time":time_to_minutes(row["start_time"])
                       ,"end_time":time_to_minutes(row["end_time"]),
                       "building":row["building"]}
            # append to my list 
            cleaned_rows.append(section)
        return cleaned_rows
        


if __name__ == "__main__":


    clock = "8:00 AM"
    clock2 = "2:20 PM"
    print(time_to_minutes(clock))
    print(time_to_minutes(clock2))
    path = "data/MTSU Classes Dataset.csv"
    result = load_sections(path)
    print(len(result))
    print(result[-1])
    # Sample of output:
    # 480
    #860
    #52
    #{'crn': '12077',
    #  'subject': 'CSCI',
    #  'course_num': 7400,
    #  'is_lab': 0,
    #  'course_name': 'Cloud Computing for Data Analysis',
    #  'days': ['Tuesday', 'Thursday'],
    #  'start_time': 880,
    #  'end_time': 965,
    #  'building': 'KOM'}


    
