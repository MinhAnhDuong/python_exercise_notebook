import csv
import os
import io

def main():

    
    main_menu = '''
    1. List of exercises
    2. Training records
    3. Find
    0. Exit the program
    '''

    exercises_menu = '''
    1. Add a new exercise
    2. Back to the main menu
    0. Exit the program
    '''

    training_records_menu = '''
    1. List of training records
    2. Add a new training record 
    3. Back to the main menu
    0. Exit the program
    '''

    find_menu = '''
    1. Find an exercise
    2. Find a training record
    3. Back to the main menu
    0. Exit the program
    '''

    while True:

        print(main_menu)
        
        user_choice = input("Choose an option: ")
        
        if user_choice == "1":

            while True:

                print(exercises_menu)

                user_choice = input("Choose an option: ")

                if user_choice == "1":
                    add_new_exercise()
                elif user_choice == "2":
                    break
                elif user_choice == "0":
                    exit()

        elif user_choice == "2":

            while True:

                print(training_records_menu)

                user_choice = input("Choose an option: ")

                if user_choice == "1":
                    list_training_records()
                elif user_choice == "2":
                    add_new_training_record()
                elif user_choice == "3":
                    break
                elif user_choice == "0":
                    exit()

        elif user_choice == "3":

            while True:
                print(find_menu)
                user_choice = input("Choose an option: ")

                if user_choice == "1":
                    find_exercise()
                elif user_choice == "2":
                    find_training_record()
                elif user_choice == "3":
                    break
                elif user_choice == "0":
                    exit()

        elif user_choice == "0":

            exit()

    
def list_of_exercises():

    if not os.path.exists("all_exercises.csv"):
        with open("all_exercises.csv", mode="w") as csv_file:
            print("\nCreating new file for exercises")
            print("There are no exercises yet, please enter exercises in the exercise list ")
            fieldnames = ["Cviky", "Poznamky"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
        return
    else:
        with open("all_exercises.csv", mode='r') as file:
            csv_file = csv.DictReader(file)
            print("\nSeznam cviku")
            for row in csv_file:
                print(dict(row))
        return
    
        

def add_new_exercise():

    print("Add new exercise ")

    cvik = input("Enter new exercise: ")
    poznamka = input("Enter new note: ")

    with io.open("all_exercises.csv", mode="r", newline='', encoding='utf-8') as csv_file:
        for exer, note in csv.reader(csv_file):
                if cvik == exer.lower():
                    print(f"\nExercise cannot be added.\nExercise has already been added: \n\t\t>{exer}, {note}")
                    return
        else:
            with open("all_exercises.csv", mode="a") as csv_file:
                fieldnames = ["Cviky", "Poznamky"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writerow({'Cviky': cvik,'Poznamky': poznamka})
                print("\nYour new exercise was added.")
            return


def list_training_records():

    if not os.path.exists("all_training_records.csv"):
        with open("all_training_records.csv", mode="w") as csv_file:
            print("\nCreating new file for training record")
            print("There are no training record yet, please enter training records in the training record list ")
            fieldnames = ["Cviky","Datum", "Pocet serii", "Pocet opakovani", "Poznamky"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
        return

    else:
        with open("all_training_records.csv", mode='r') as file:
            csv_file = csv.DictReader(file)
            print("\nList of training records: ")
            for row in csv_file:
                print(dict(row))
        return


def add_new_training_record():
    try:
        with open("all_exercises.csv", mode='r') as file:
            csv_file = csv.DictReader(file)

            find_request = input("\nWhat exercise did you do?: ")
            found = False

            for exercise_record in csv_file:
                    for value in exercise_record.values():
                        if find_request in value:
                            found = True
                            record_value = value
                            date = input("Enter the date: ")
                            series = int(input("Enter the number of series: "))
                            repeats = int(input("Enter the number of repeats: "))
                            note = input("Enter a note: ")

                            if not os.path.exists("all_training_records.csv"):
                                with open("all_training_records.csv", mode="w") as csv_file:
                                    print("\nCreating new file for training record")
                                    print("There are no training record yet, please enter training records in the training record list ")
                                    fieldnames = ["Cviky","Datum", "Pocet serii", "Pocet opakovani", "Poznamky"]
                                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                                    writer.writeheader()
                                return
                                    

                            else:
                                with open("all_training_records.csv", mode="a") as csv_file:
                                    fieldnames = ["Cviky","Datum", "Pocet serii", "Pocet opakovani", "Poznamky"]
                                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                                    writer.writerow({'Cviky': record_value,'Datum': date,'Pocet serii':series, 'Pocet opakovani': repeats, 'Poznamky': note})
                                return

    except FileNotFoundError:
        print("No exercises are available yet, to enter a training record, enter an exercise first. ")


    if not found:
        with open("all_exercises.csv", mode='r') as file:
            csv_file = csv.DictReader(file)
            print("\nSeznam cviku")
            for row in csv_file:
                print(dict(row))
        print("\nThe exercise you are looking for was not found.\nTo enter a new workout record, it is only possible to use from an existing exercise")
        return



def find_exercise():

    find_request = input("\nWhat exercise do you find?: ").strip().lower()

    with io.open("all_exercises.csv", mode='r',newline='', encoding='utf-8') as file:
        for exer, notes in csv.reader(file):
            if find_request == exer.lower():
                print(f"\nCvik: {exer} \nPoznamky ke cviku: {notes}")
                return
        else:
            print("Exercise has not been found")
            return


def find_training_record():

    find_request_training_record = input("\nWhat training record are you looking for?: ").strip().lower()

    with io.open("all_training_records.csv", mode='r',newline='', encoding='utf-8') as file:
        for exer, date, series, repeats, note in csv.reader(file):

            if find_request_training_record == exer.lower():
                print(f"\nCvik: {exer} \nDatum: {date} \nPocet serii: {series} \nPocet opakovani: {repeats} \nPoznamka ke cviku: {note}")
                return

        else:
            print("The training record you entered was not found")
            return


main()

