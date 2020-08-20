# 1st method
# Import all method in module
# import number_module

# 2nd method
# Import some module
# from number_module import factorial, fibonacci
# from number_module import *
# from number_module import factorial as fa
# from number_module import fibonacci as fb

# Call all method
# print(number_module.factorial(5))
# print(number_module.fibonacci(100))

# Call some method
# print(factorial(5))
# print(fibonacci(100))

# print(fa(5))
# print(fb(100))

# Import from package
from numberpackage import *

# Build in Package
import uuid
import socket
import platform

# print(numberpackage.caculate.plus(2, 3))
# print(numberpackage.number_module.factorial(5))

print(platform.system())
print(platform.release())
print(platform.version())
print(platform.machine())
print(socket.hostname())
# print(socket.gethostbyname(socket.gethostname()))
