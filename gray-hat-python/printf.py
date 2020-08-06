from ctypes import *

msvcrt = cdll.msvcrt
message_string = "Hello World from Python!\n"
msvcrt.printf("Testing: %s", message_string);


