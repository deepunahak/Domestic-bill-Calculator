# Model for Billing Count

class Bill(object):

    def __init__(self, house_sq_ft, water_liter, electricity_kwh, phone_seconds, gas_liter):
        self.house_sq_ft = house_sq_ft
        self.water_liter = water_liter
        self.electricity_kwh = electricity_kwh
        self.phone_seconds = phone_seconds
        self.gas_liter = gas_liter
        self.total_amount = None
