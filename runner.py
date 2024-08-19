import ctypes

# Load the shared library
# On Linux/MacOS, use './libhello.so'
# On Windows, use 'hello.dll'
hello_lib = ctypes.CDLL('./libhello.so')

# Call the C function
hello_lib.say_hello()
