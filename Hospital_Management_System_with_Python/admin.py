from doctor import Doctor
from patient import Patient

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Please, enter the username: ')
        password = input('Please, enter the password: ')

        # check if the username and password match the registered ones
        #ToDo1
      
        return self.__username == username and self.__password == password
            
            # raise Exception("incorrect username or password!")
    
    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...... the speciality of the doctor in that order.
        """
        #ToDo2
        doctor_first_name = input("Please, enter the name of the doctor: ")
        doctor_surname = input("Please, enter the surname of  doctor: ")
        speciality = input("Please, enter the speciality of doctor: ")
        return doctor_first_name, doctor_surname, speciality
      
    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """
        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        #ToDo3
    
        try: 
            a_op = int(input("Please, enter the operation you want to choose: "))
        
                # register
            if a_op == '1':
                print("-----Register-----")

                    # get the doctor details
                print('Enter the doctor\'s details:')

                    #ToDo4
                doctor_first_name, doctor_surname, speciality = self.get_doctor_details()

                # check if the name is already registered
                name_exists = False
                for doctor in doctors:
                    if doctor_first_name == doctor.get_first_name() and doctor_surname == doctor.get_surname():
                        print('Name already exists.')
                            #ToDo5
                        break
                            # save time and end the loop
                    
                        #ToDo6
                if name_exists == False:       
                    doctors .append(Doctor(doctor_first_name,doctor_surname, speciality))
                    print('Doctor registered.')
                    self.view(doctors)

                # View
            elif a_op == '2':
                print("-----List of Doctors-----")
                print("ID|     FUll name     | Speciality")
                self.view(doctors)
                    #ToDo7
                    
                # Update
            elif a_op == '3':
                while True:
                    print("-----Update Doctor's Details-----")
                    print('ID |          Full name           |  Speciality')
                    print("Doctor is updated finally !!!")
                    self.view(doctors)

                    try:
                        index = int(input('Please,enter the ID of the doctor: ')) - 1
                        doctor_index = self.find_index(index, doctors)
                        if doctor_index != False:
                            break
                        
                        else:
                            print("Doctor is not found!")
                    
                    except ValueError:
                        print("Invalid id entered !!!")
                
                # menu
                print('Choose the field to be updated:')
                print(' 1 First name')
                print(' 2 Surname')
                print(' 3 Speciality')   
                
                a_op = int(input("Choose a number: "))
                
                #ToDo8
                if a_op == 1:
                    new_first_name = input("Please, enter the new first name:")
                    doctors[index].set_first_name(new_first_name)
                    print("New firstname is updated !!!")
                    self.view([doctors[index]])
                                        
                elif a_op == 2:
                    new_surname = input("Please, enter the new surname:")
                    doctors[index].set_surname(new_surname)
                    print("New surname is updated !!!")
                    self.view([doctors[index]])
                                    
                elif a_op == 3:
                    new_speciality = input("Please, enter the new speciality:")
                    doctors[index].set_speciality(new_speciality)
                    print("New speciality is updated")
                    self.view([doctors[index]])
                                
                # Delete
            elif a_op == '4':
                print("-----Delete Doctor-----")
                print('ID |          Full Name           |  Speciality')
                print("Doctor is deleted !!!")
                self.view(doctors)
                    # do exception handling here
                
                try:
                    index = int (input("Enter the ID of the doctor to be deleted: ")) -1
                    doctor_index = self.find_index(index, doctors)
                    
                    if (doctor_index != False):
                        doctors.pop (index)
                        print ("Doctor is deleted !!!")
                        self.view(doctors)
                    
                    else: 
                        print("Invalid operation choosed !!! Please re-correct it !!!")
                
                except:
                    print("Invalid Input Entered!!!")

        except ValueError:
            print("Please choose the valid operator.")
 
    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        #ToDo10
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")
        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        
        self.view(patients)
        try:
            patient_index = input('Please enter the patient ID: ')

            try:
                # patient_index is the patient ID mines one (-1)
                patient_index = int(patient_index) -1

                # check if the id is not in the list of patients
                if patient_index not in range(len(patients)):
                    print('The id you have entered was not found.')
                    return # stop the procedures

            except ValueError: # the entered id could not be changed into an int
                print('The id you have entered is incorrect')
                return # stop the procedures
        
        except ValueError:
            print("Invalid input entered !!!")

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors) != False:
                    
                # link the patients to the doctor and vice versa
                #ToDo11
                patients[patient_index].link(doctors[doctor_index].full_name())
                # self.view(patients)
                doctors[doctor_index].add_patient(patients[patient_index].full_name())
                
                print('The patient is now assigned to the doctor !!!')

            # if the id is not in the list of doctors
            else:
                print('The id you have entered was not found !!!')

        except ValueError: # the entered id could not be changed into an in
            print('The id you have entered is incorrect !!!')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        
        self.view_patient(patients)

        print("-----Discharge Patient-----")
        try:      
            Patient_index = int(input('Please enter the patient ID: '))-1
                
            if Patient_index in range(len(patients)):
                discharge_patients.append(patients.pop(Patient_index))
                self.view_discharge(discharge_patients)
                with open("patientdata.txt","r") as fd:
                    read_lines = fd.readlines()
                del read_lines[Patient_index]
                # self.view_patient(patients)

                with open("patientdata.txt", "w") as fd:
                    for i in read_lines:
                        fd.write(i)
                        
            else:
                print("Patient you have entered is not available !!!")
            
        except ValueError: # the entered id could not be changed into an in
            print('The id you have entered is incorrect')
        #ToDo12
       
    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        
        self.view(discharged_patients)
        #ToDo13

    def admin_details(self):
        print(f"username : {self.__username}")
        print(f"password : {self.__password}")
        print(f"address : {self.__address}")

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        try:
            a_op = int(input('Choose a number: '))

            if a_op == 1:
                self.admin_details()
                new_username = input("Please, enter the new username:")
                
                confirm_new_username = input("Please, enter the same username:")

                if (new_username == confirm_new_username):
                    print("Matched !!!")
                    self.__username = new_username
                    
                    print("Username is Updated !!!")
                    self.admin_details()
                else:
                    print("Username Matched !!!")

                #ToDo14
            
            elif a_op == 2:
                self.admin_details()
                new_password = input('Please, enter the new password: ')
                confirm_new_password = input('Please, enter the confirm new password: ')
                # validate the password
                
                if new_password == confirm_new_password:
                    self.__password = new_password
                    print("__Password updated__")
                    self.admin_details()
                
                else:
                    print("Password do not match. Please try again !!!")
                    self.update_details()
                 
            elif a_op == 3:
                self.admin_details()
                new_address = input("Please, enter the new address: ")
                confirm_address = input("Please, confirm the new address: ")
                if new_address == confirm_address:
                    self.__address = new_address
                    print("Your new address is updated !!!")
                    self.admin_details()
                    
                #ToDo15
            else:
                print("Invalid Choice Entered !!!")
                #ToDo16

        except ValueError:
            print("Invalid Input Entered !!!")

    #Relocating the product
    def rellocatedoctor(self,patients,doctors):
        print("-----Select Doctors-----")
        print("Relocate doctor: ")
        print("__")
        print('ID |              Full Name              |  Speciality   ')
        self.view(doctors)
        try:
            doctors_index = input('Please, enter the doctor ID that you want to relocate: ')
            # doctor_index is the patient ID mines one (-1)
            doctors_index = int(doctors_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctors_index, doctors) != False:
                print('The id is found finally !!!')
            # if the id is not in the list of doctors
            else:
                print('The id you have entered is not found !!!')
        except ValueError: # the entered id could not be changed into an in
            print('The id you have entered is incorrect. Please, enter a correct id !!!')

        print("------------Relocate----------")


        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')

        self.view(patients)
        try:
            patients_index = input('Please, enter the patient ID you want to relocate the doctor you have selected: ')

            # patient_index is the patient ID mines one (-1)
            patients_index = int(patients_index) -1

            # check if the id is not in the list of patients
            if patients_index in range(len(patients)):
                patients[patients_index].link(doctors[doctors_index].full_name()) 
                doctors[doctors_index].add_patient(patients[patients_index].full_name())
                print("Finally, rellocated!!!")
                self.view(patients)
            else:
                print('The id you have entered was not found !!! Please, enter the valid ID')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id you have entered is incorrect. Please, enter the correct ID !!!')

# file Handling
    def read_patientsfile(self, readpatientfile):
        PatientsList = []
        try:
            with open (readpatientfile, "r") as fd:
                for i in fd:
                    print(i.split(" , "))
                    PatientsList.append(i)
        
        except FileNotFoundError:
            print ("The file you are trying to search is not found !!!")

        finally:
            return PatientsList
        
    def write_patientsfile(self, writepatientsfile):
        try:
            with open("patientdata.txt" , "w") as fd:
                fd.write("ID |       Full Name        |      Doctor`s Full Name      | Age |    Mobile     | Postcode  \n")
                
                for index, i in enumerate(writepatientsfile):
                    fd.write(f"{index+1:3}{i.full_name():^30}|{i._Patient__doctor:^30}|{i._Patient__age:^5}|{i._Patient__mobile:^15}|{i._Patient__postcode:^10}\n")

            fd.close()

        except FileNotFoundError:
            print("The file you are trying to search is not found !!!")

        else:
            return True
        
    def get_patient_report(self, doctors, patients):
        print("-----------Reports-----------")
        print("Please, choose the operation: ")
        print("1. The total number of doctors available in this system: ")
        print("2. The total number of patients per doctor: ")
        print("3. The total number of appointments per month per doctor: ")
        print("4. The total number of patients based on the type of illness: ")
        a = input(" Please, choose the required options: ")

        try:
            if a == "1":
                all=len(doctors)
                print(f"Numbers of doctor: {all}")
                
            elif a == "2":
                for doctor in doctors:
                    
                    Appointment = doctor.Appointment()
                    TotalPatients = doctor.total_patients()
                    
                    print(f"{0} consists {1} patients". format(doctor.full_name(),TotalPatients))
                    
            elif a == "3":
                for doctor in doctors:
                    Appointment = doctor.Appointment()
                    print(f"{0} consists {1} this months".format(doctor.full_name(),Appointment))
                    
            elif a == "4":
                for patient in patients:
                    symptoms = patient.get_symptoms()
                    j = 0
                    for i in patients:
                        if i.get_symptoms() == symptoms:
                            j += 1
                    print(f"{j} for {symptoms}")
                    
            else:
                print("Invalid Option Entered !!!")

        except Exception as b:
            print(b)

admin = Admin('Admin','123','B1 1AB') # username is 'Admin', password is '123'
doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
patients = [Patient('Sara','Smith', 20, '07012345678','B1 234','Fever'), Patient('Mike','Jones', 37,'07555551234','L2 2AB','Headache'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC','Bone')]
discharged_patients = []
