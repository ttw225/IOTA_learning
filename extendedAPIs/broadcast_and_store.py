# from iota.commands.extended.broadcast_and_store import BroadcastAndStoreCommand
from iota.api import Iota

newTrytes = []
newTrytes.append('WCTC9D9DCDEAKDCDFD9DSC')

# transactions = broadcast_and_store(newTrytes)
# transactions = BroadcastAndStoreCommand(newTrytes)
# transactions = Iota.broadcast_and_store(trytes=newTrytes)
transactions = []
test = Iota.broadcast_and_store()

# transactions = BroadcastAndStoreCommand._execute(newTrytes)

# B = BroadcastAndStoreCommand()

for transaction in transactions:
    if transaction.value < 0:
        continue

    print(f'Message from {transaction.hash}:')

    message = transaction.signature_message_fragment
    if message is None:
        print('(None)')
    else:
        print(message.decode())
