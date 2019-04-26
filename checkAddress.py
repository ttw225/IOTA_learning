import iota

InputAddr = b"VOBLCCGXZOHUWUWTYJBZUFQBTDEOC9UZTUCORAKPAXPZLXRVWDZDKOIQHWIYXSCMKFMWYYCZBUHRWQSHXUPABOQSAW"
if len(InputAddr) != 90:
    if len(InputAddr) != 81:
        print("Incorrect lenght of the given address. Please enter an address with length 81 or an address including checksum.")
        exit(2)
    else:  # Add checksum
        Adr = iota.Address(InputAddr)
        InputAddr = Adr.with_valid_checksum()
        print("Input Address Didn't include checksum.\nAutomatic generating.")


try:
    # address including checksum
    Adr2 = iota.Address(InputAddr)
except:
    print("Not valid input address given")
    exit(1)

print("\nInput address excl checksum:")
print(Adr2[:81])  # return only first 81 characters
print("Input address incl checksum:")
print(Adr2)
print("Is it valid addr based on checksum? %s" %
      (Adr2.is_checksum_valid()))
