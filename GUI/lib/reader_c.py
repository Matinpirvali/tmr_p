import ctypes

# Load the DLL
mylib = ctypes.CDLL('mylibrary.dll')

# Define the argument and return types of the function
mylib.add_numbers.argtypes = (ctypes.c_int, ctypes.c_int)
mylib.add_numbers.restype = ctypes.c_int

# Call the C function
result = mylib.add_numbers(3, 4)
print("Result:", result)
