from admin import Admin
from doctor import Doctor
from patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the actors
    admin = Admin('Admin','123','B1 1AB') # username is 'Admin', password is '123'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    patients = [Patient('Sara','Smith', 20, '07012345678','B1 234', 'Fever'), Patient('Mike','Jones', 37,'07555551234','L2 2AB', 'Headache'), Patient('Daivd','Smith', 15, '07123456789','C1 ABC', 'Bone')]
    discharged_patients = []
    admin.write_patientsfile(patients)

    # keep trying to login tell the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password entered.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin details')
        print(' 6- Reallocating the patient to the doctor ')
        print(' 7- Patient Report')
        print(' 8- Quit')

        # get the option
        a_op = input(' Choose an option: ')

        if a_op == '1':
            admin.doctor_management(doctors)
        
            # 1- Register/view/update/delete doctor
         #ToDo1
        
        elif a_op == '2':
            print("__patients__")
            print("----------------")
            print("ID  |   FULL NAME    |   Doctor's FULL NAME   |   AGE   |   MOBILE   |   POSTCODE   ")
            admin.view_patient(patients)
            # 2- View or discharge patients
            #ToDo2
            

            while True:
                a_op = input('Do you want to discharge a patient(Y/N):').lower()

                if a_op == 'yes' or a_op == 'y':
                    #ToDo3
                    admin.discharge(patients,discharged_patients)

                elif a_op == 'no' or a_op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif a_op == '3':
            admin.view_discharge(discharged_patients)
            # 3 - view discharged patients
            #ToDo4

        elif a_op == '4':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)

        elif a_op == '5':
            # 5- Update admin detais
            admin.update_details()

        elif a_op == '6':
            # 6- Reallocating the patient id
            admin.rellocatedoctor(patients , doctors)

        elif a_op == '7':
            admin.get_patient_report(doctors, patients)

        elif a_op == '8':
            break

            # 6 - Quit
            #ToDo5  

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option entered. Please, try again !!!')

if __name__ == '__main__':
    main()