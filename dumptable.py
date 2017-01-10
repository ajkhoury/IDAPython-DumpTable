import sys
import idaapi

def printf(format, *args):
    sys.stdout.write(format % args)

def main():
    address = idaapi.askaddr(idaapi.get_imagebase() + 0x19000, "Enter address of table: ")
    if (address != None):
        idx = 0
        while (address != BADADDR):
            name = idaapi.get_true_name(BADADDR, Qword(address))
            if not name:
                break 
            printf("[%04d] %s = %X\n", idx, name, Qword(address))     
            address += 8 if idaapi.get_inf_structure().is_64bit() else 4   
            idx += 1
        
if __name__ == "__main__":
    main()