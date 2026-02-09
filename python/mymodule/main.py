import sys
import argparse
import ctypes
import ctypes.util
import os

def init_mylib():
    LIB_NAME = "mylib"
    LIB_DIR = "mylib"
    if sys.platform.startswith("linux"):
        libname = LIB_NAME + ".so"
    elif sys.platform == "win32":
        libname = LIB_NAME + ".dll"
    else:
        raise RuntimeError("Unsupported platform")
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    lib_path = os.path.join(script_dir, LIB_DIR, libname)
    mylib = ctypes.CDLL(lib_path)
    
    mylib.sum_of_array.argtypes = [ctypes.POINTER(ctypes.c_int32), ctypes.c_size_t]
    mylib.sum_of_array.restype = ctypes.c_int32    
    
    return mylib
    
mylib = init_mylib()

def my_sum(arr):
    c_arr = (ctypes.c_int32 * len(arr))(*arr)
    res = mylib.sum_of_array(c_arr, len(arr))
    return res

def my_sum_py(arr):
    return sum(arr)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("numbers", nargs="*", type=int)
    args = parser.parse_args()    
    
    res = my_sum(args.numbers)
    print(f"Sum: {res}")

if __name__ == "__main__":
    main()