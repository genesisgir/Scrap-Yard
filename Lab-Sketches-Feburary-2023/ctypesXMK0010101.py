import ctypes

MessageBoxA = ctypes.windll.user32.MessageBoxA

NULL = 0
MB_OK = 0

MessageBoxA(NULL, ctypes.c_char_p(b"Hello World"), ctypes.c_char_p(b"Alert"), MB_OK)