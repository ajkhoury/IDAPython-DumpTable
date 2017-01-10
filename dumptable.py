import sys

from idautils import *
from idc import *

def printf(format, *args):
    sys.stdout.write(format % args)

def main():
    imagebase = idaapi.get_imagebase()
    address = idaapi.askaddr(imagebase + 0x19000, "Enter address of table: ")
    if (address != None):
        idx = 0
        while (address != BADADDR):
            name = GetTrueName(Qword(address))
            if not name:
                break
            printf("[%04d] %-10s\n", idx, name)
            address += 8
            idx += 1
        

if __name__ == "__main__":
    main()