import iota
from datetime import datetime
from pprint import pprint

MySeed = b"LUEMBUSKXRNZQO9ZFLHNVCRMJD9QISVRALLJZPMKXQCMJLSYTAGZR9ILUL9NODGKHLGWHZSKJQTMP9AOF"
TargetAddresses = []
TargetAddresses.append(
    b"CXDUYK9XGHC9DTSPDMKGGGXAIARSRVAFGHJOCDDHWADLVBBOEHLICHTMGKVDOGRU9TBESJNHAXYPVJ9R9")
TargetAddresses.append(
    b"CYJV9DRIE9NCQJYLOYOJOGKQGOOELTWXVWUYGQSWCNODHJAHACADUAAHQ9ODUICCESOIVZABA9LTMM9RW")

NowIs = datetime.now()  # get a actual date & time - just to have some meaningfull info

# preparing transactions
pt = []
for targetaddress in TargetAddresses:
    pt.append(iota.ProposedTransaction(address=iota.Address(targetaddress),  # 81 trytes long address
                                       message=iota.TryteString.from_unicode(
        'Hello world message.\n Now is %s' % (NowIs)),
        # Up to 27 trytes
        tag=iota.Tag(b'RBTC9D9DCDEAKDCDFD9DSC'),
        value=0))

api = iota.Iota("https://nodes.thetangle.org:443")
# api = iota.Iota("http://140.116.247.123:14267")

print("Preparing/Broadcasting... Wait please...")
# the whole process initiated in a single call
FinalBundle = api.send_transfer(depth=3,
                                transfers=pt,
                                min_weight_magnitude=14)['bundle']  # it returns a dictionary with a bundle object

# bundle is broadcasted, let's print it
print("\nGenerated bundle hash: %s" % (FinalBundle.hash))
print("\nTail Transaction in the Bundle is a transaction #%s." %
      (FinalBundle.tail_transaction.current_index))

print("\nList of all transactions in the bundle:\n")
for txn in FinalBundle:
    pprint(vars(txn))
    print("")
