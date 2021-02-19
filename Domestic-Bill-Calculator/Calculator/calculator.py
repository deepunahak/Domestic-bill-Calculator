from model import Bill
import sys


class Calculator(object):
    datbase = {}
    datbase['total'] = 0
    # Calculator
    def calc_monthly_bill(self, house_sq_ft, water_liter, electricity_kwh, phone_seconds, gas_liter):

        bills = Bill(house_sq_ft, water_liter, electricity_kwh, phone_seconds, gas_liter)

        # House Bill
        one_sq_ft = 10
        if bills.house_sq_ft == None or bills.house_sq_ft == 0:
            print("There is no bill for house, need to mention square feet detail.")
        else:
            house_bill = house_sq_ft * one_sq_ft
            self.datbase["house"] = house_bill
            if house_bill != None:
                self.datbase['total'] += house_bill

        # Water Bill
        one_liter_price = 0.001
        if bills.water_liter == None or bills.water_liter == 0:
            print("There is no bill for water, need to mention water in liters.")
        else:
            water_bill = one_liter_price * water_liter
            self.datbase["water"] = water_bill
            if water_bill != None:
                self.datbase['total'] += water_bill

        # Electricity Bill
        per_unit_electric = 5
        gst_for_elec_bill = 0.18
        if bills.electricity_kwh == None or bills.electricity_kwh == 0:
            print("There is no bill for electricity, need to mention kilowatt hour(kwh) detail.")
        else:
            total_electricity = bills.electricity_kwh * per_unit_electric
            electricity_tax = total_electricity * gst_for_elec_bill
            electricity_bill = total_electricity + electricity_tax

            self.datbase["electricity"] = electricity_bill
            if electricity_bill != None:
                self.datbase['total'] += electricity_bill

        # Phone Bill
        per_second_paisa = 1
        per_minute_paisa = 60 * per_second_paisa
        tax_cess = 0.05
        fixed_charge = 100
        if bills.phone_seconds == None or bills.phone_seconds == 0:
            print("Phone bill fixed charge with tax", (fixed_charge * tax_cess) + fixed_charge,
                  "\n.Need to mention call duration in Seconds")
            self.datbase["phone"] = (fixed_charge * tax_cess) + fixed_charge
            self.datbase['total'] += (fixed_charge * tax_cess) + fixed_charge
        else:
            seconds_to_min = bills.phone_seconds / 60
            total_ph_bill_paisa = per_minute_paisa * seconds_to_min
            total_paisa_to_inr = total_ph_bill_paisa / 100
            phone_tax = (total_paisa_to_inr + fixed_charge) * tax_cess
            phone_bill = total_paisa_to_inr + fixed_charge + phone_tax

            self.datbase["phone"] = phone_bill
            if phone_bill != None:
                self.datbase['total'] += phone_bill

        # Gas Bill
        per_liter_gas = 15
        if bills.gas_liter == None or bills.gas_liter == 0:
            print("There is no bill for gas, need to enter gas in liters")
        else:
            gas_bill = bills.gas_liter * per_liter_gas

            self.datbase["gas"] = gas_bill
            if gas_bill != None:
                self.datbase['total'] += gas_bill

    def print_bill(self):

        print("Total Spending for this month: INR ", self.datbase['total'])
        print("House: INR ", self.datbase["house"])
        print("Water: INR ", self.datbase["water"])
        print("Electricity: INR ", self.datbase["electricity"])
        print("Phone: INR ", self.datbase["phone"])
        print("Gas: INR ", self.datbase["gas"])



    # Application Exit
    def app_exit(self, ch):
        while True:
            if ch == 'Y' or ch == 'y':
                print("Application exit successfully (^_^)")
                sys.exit(0)
            elif ch == 'N' or ch == 'n':
                break
            else:
                print("Invalid input..!!")
