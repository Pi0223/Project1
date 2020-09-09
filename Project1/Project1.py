# Taiki Nakamura/ neko senpai
# C02705348

# Represent the data as a string
hospital_capacity_by_state_string = '''
Hospital Capacity by State:
=================================================================================================
State(A)   Beds(B)    Occupancy_Rate(D)  Availability(F)   Adult_Population(J) Population_65+(K) 
=================================================================================================
5AZ     12,868  0.62    4,938   5,187,520   1,106,362
6CA     68,554  0.67    22,831  29,868,127  5,148,448  
11FL    51,190  0.66    17,651  16,166,865  3,926,889
21MA    13,759  0.74    3,603   5,405,787   1,049,751
36NY    51,713  0.78    11,549  15,594,924  3,008,351
50WA    11,808  0.65    4,123   5,554,591   1,029,040

=================================================================================================
Source:https://globalepidemics.org/hospital-capacity/
'''
str = hospital_capacity_by_state_string
print(str)

#print(str.upper())
#print(str.swapcase())
print(str.casefold())
#print(hospital_capacity_by_state_string) _amt
#print(type(hospital_capacity_by_state_string)) _amt

# Represent the data as a list of Tuple
list_of_tuple = [('AZ', 12868, 0.62, 4938, 5187520, 1106362),
                 ('CA', 68554, 0.67, 22831, 29868127, 5148448),
                 ('FL', 51190, 0.66, 17651, 16166865, 3926889),
                 ('MA', 13759, 0.74, 3603, 5405787, 1049751),
                 ('NY', 51713, 0.78, 11549, 15594924, 3008351),
                 ('WA', 11808, 0.65, 4123, 5554591, 1029040)
                 ]

print(list_of_tuple)
#print(list_of_tuple) _amt
#for i in list_of_tuple: _amt
#   print(i)

'''
for each_tuple in list_of_tuple:
    for each_item in each_tuple:
        each_item[0] = HospitalCapacity(each_item[0], each_item[1], each_item[2])
    print("I hope we made an object above")
'''

# Represent the data as a custom class

class HospitalCapacity:
    def __init__(self, state_name: str, num_beds: int, occupancy_rate: int, available_beds: int, adult_pop: int, adult_senior: int):
        self.state = state_name
        self.numberBeds = num_beds
        self.occupancyRate = occupancy_rate
        self.availableBed = available_beds
        self.populationPpl = adult_pop
        self.populationSenior = adult_senior       
#hospitalCap = HospitalCapacity('CA', 68554) _amt
#print("The hospital capacity in each of the states: " + numberBeds.name) _amt
#print("The number of bed", numberBeds.name, "is in", "state.name",  _amt
#   str() _amt

if __name__ == "__main__":
    print("test")

