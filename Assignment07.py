# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log:
#  WMarcus, 3/11/25, Created Script
# ------------------------------------------------------------------------------------------ #

import json

MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

students: list = []
menu_choice: str

class Person:
    """
    This class holds Person data.

    Properties:
    first_name (str): The student's first name
    last_name (str) : The student's last name

    ChangeLog:
    WMarcus 3/11/25: Created the class
    """
    def __init__(self, first_name : str = "", last_name : str = ""):
        self.first_name = first_name
        self.last_name = last_name
    @property 
    def first_name(self):
        return self.__first_name 
    @first_name.setter 
    def first_name(self, value = str):
        if value.isalpha() or value == "":
            self.__first_name = value
        else:
            raise ValueError("The first name may only contain letters.")
    @property 
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, value = str):
        if value.isalpha() or value == "":
            self.__last_name = value
        else:
            raise ValueError("The last name may only contain letters")
    def __str__(self):
        return f'{self.first_name},{self.last_name}'

class Student(Person):
    """
    This class holds student data.

    Properties:
        first_name (str): The student's first name
        last_name (str): The student's last name
        course_name (str): The student's course name

    ChaneLog:
    WMarcus 3/11/25: Created class and properties
    """
    def __init__(self, first_name : str = "", last_name : str = "", course_name : str = ""):
        super().__init__(first_name = first_name, last_name = last_name)
        self.course_name = course_name

    @property 
    def course_name(self):
        return self.__course_name

    @course_name.setter 
    def course_name(self, value = str):
        self.__course_name = value

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.course_name}'

class FileProcessor:
    """
    This class contains methods that interact with "Enrollments.JSON"

    Methods:
        read_data_from_file: Reads data from .JSON, then adds to a list of dictionaries
        write_data_to_file: Writes a list of dictionaries to a .JSON file

    ChangeLog:
    WMarcus 3/11/25: Created class and methods
    """

    @staticmethod
    def read_data_from_file(file_name : str, student_data : list):
        """
        This method reads JSON data and adds it to a list of dictionaries.

        Parameters:
            file_name (str): The name of the .JSON file
            student_data (str): A list of student data, represented as dictionaries

        ChangeLog:
            WMarcus 3/11/25: Created method
        """
        try:
            file = open(file_name, "r")
            dict_list = json.load(file) #returns list of dict rows
            for each in dict_list:
                student_obj : Student = Student(first_name=each["FirstName"],
                                                last_name = each["LastName"],
                                                course_name = each["CourseName"])
                student_data.append(student_obj)
            file.close()
        except FileNotFoundError as e:
            IO.output_error_messages("Data file does not exist!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()
        return student_data

    @staticmethod
    def write_data_to_file(file_name : str, student_data : list):
        """
        This method writes a list of dictionaries to a JSON file.

        Parameters:
            file_name (str): The name of the JSON file
            student_data (list): A list of student data, represented as dictionaries

        ChangeLog:
            WMarcus 3/11/25: Created method
        """
        try:
            dict_list : list = []
            for each in student_data:
                student_json : dict = {"FirstName": each.first_name,
                     "LastName": each.last_name,
                     "CourseName": each.course_name}
                dict_list.append(student_json)
            file = open(file_name, "w")
            json.dump(dict_list, file)
            file.close()
            print("The following data was saved:\n")
            IO.output_student_courses(student_data = students)
        except TypeError as e:
            IO.output_error_messages("Data not saved: Please check that the data is a valid JSON format", e)
        except Exception as e:
            IO.output_error_messages("Data not saved: There was a non-specific error!", e)
        finally:
            if not file.closed:
                file.close()

class IO:
    """
    This class contains the methods that collect and store data from the user.

    Methods:
        output_error_messages: Displays technical error information
        output_menu: Displays the menu of options
        input_menu_choice: Collects and stores menu interaction input
        input_student_data: Collects and stores student registration information
        output_student_courses: Prints all student information entered thus far

    ChangeLog:
        WMarcus 3/11/25: Created class and methods
    """
    @staticmethod
    def output_error_messages(message : str, error: Exception = None):
        """
        This method displays technical error information.

        Parameters:
            message (str): Customized message associated with exception
            error (Exception): The exception raised during execution of code

        ChangeLog:
            WMarcus 3/11/25: Created method
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message --")
            print(error, error.__doc__, type(error), sep = "\n")

    @staticmethod
    def output_menu(menu: str):
        """
        This method displays the menu of options.

        Parameters:
            menu (str): String containing user input choices

        ChangeLog:
            WMarcus 3/11/25: Created method
        """
        print()
        print(menu)
        print()

    @staticmethod
    def input_menu_choice():
        """
        This method collects and stores menu interaction input.

        return: String with user input

        ChangeLog:
            WMarcus 3/11/25: Created method

        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1", "2", "3", "4"):  
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__()) 

        return choice

    @staticmethod
    def input_student_data(student_data: list):
        """
        This method collects and stores student registration information

        Parameters:
            student_data (str): A list of student data, represented as dictionaries

        return: A list of student data, represented as dictionaries

        ChangeLog:
            WMarcus 3/11/25: Created method
        """
        try:
            student = Student() 
            student.first_name = input("What is the student's first name? ")
            student.last_name = input("What is the student's last name? ")
            student.course_name = input("What is the student's course name? ")
            student_data.append(student)
        except ValueError as e:
            IO.output_error_messages("That value is not the correct type of data!", e)
        except Exception as e:
            IO.output_error_messages("There was a non-specific error!", e)
        return student_data

    @staticmethod
    def output_student_courses(student_data: list):
        """
        This method prints all student information entered thus far.

        Parameters:
        student_data (str): A list of student data, represented as dictionaries

        """
        for student in student_data:
            message = f"{student.first_name} {student.last_name} is enrolled in {student.course_name}"
            print(message)

students = FileProcessor.read_data_from_file(file_name=FILE_NAME, student_data=students)
while True:
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    if menu_choice == "1":
        students = IO.input_student_data(student_data=students)
        continue

    elif menu_choice == "2": 
        IO.output_student_courses(student_data = students)
        continue

    elif menu_choice == "3":  
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    elif menu_choice == "4":  
        break 

