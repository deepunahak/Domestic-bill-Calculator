from calculator import Calculator


# Description:This file will run Calculator application


def main():
    calc = Calculator()
    while True:
        print("\n")
        print("1. Calculate Bill.")
        print("2. Exit the Application..!!!")
        print("\n")
        ops = input("Enter your choice: ")
        # switch(operation)
        if ops == '1':
            print("-*-"*20)
            house_sq_ft = int(input("Enter area detail in square feet to count bill for house: "))
            water_liter = int(input("Enter water detail in liter to count water bill: "))
            electricity_kwh = int(input("Enter Electricity detail in kilowatt hour(kwh) to count Electricity bill: "))
            phone_seconds = int(input("Enter Phone duration in seconds to count phone bill: "))
            gas_liter = int(input("Enter gas detail in liter to count gas bill: "))
            print("-*-"*20)
            calc.calc_monthly_bill(house_sq_ft, water_liter, electricity_kwh, phone_seconds, gas_liter)
            calc.print_bill()
        elif ops == '2':
            ch = input("Enter Y or N (YES or NO) OR y or n (yes or no): ")
            calc.app_exit(ch)
        
        else:
            print("Invalid Input")


main()
