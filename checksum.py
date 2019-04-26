import iota

# some IOTA address
Adr = iota.Address(
    b"VOBLCCGXZOHUWUWTYJBZUFQBTDEOC9UZTUCORAKPAXPZLXRVWDZDKOIQHWIYXSCMKFMWYYCZBUHRWQSHX")

print("Original input excl. checksum address:")
print(Adr)
print("Length: %s" % len(Adr))

AdrInclCheckSum = Adr.with_valid_checksum()
print("\nInput address including checksum:")
print(AdrInclCheckSum)  # the last 9 trytes is the checksum
print("Length incl checksum: %s" % len(AdrInclCheckSum))
