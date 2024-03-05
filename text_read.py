import numpy as np
convert_time = lambda x: x.decode()

data = np.loadtxt("ASTR19_F23_group_project_data.txt", dtype={'names': ('day', 'time', 'height'), 'formats': ('i4', 'U5', 'f4')}, converters={1: convert_time}, skiprows=1)


def time_str_to_float(time_str):
    hours, minutes = map(int, time_str.split(':'))
    return hours + minutes / 60.0

time_string = data['time']

vectorized_conversion = np.vectorize(time_str_to_float)

time_float = vectorized_conversion(time_string)

print(time_float)
