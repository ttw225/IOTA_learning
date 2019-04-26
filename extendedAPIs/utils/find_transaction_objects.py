from iota.commands.extended.utils import find_transaction_objects
address=[]
address.append('LEYNSIMADMXAUYRGXKKEXPHDMZLRISZBSRZXUMCIKP9JQDOXSCIUGKYFFNPPVPGCHEJAWWSDHCKGOORPC')

transactions = find_transaction_objects(addresses=address)

for transaction in transactions:
  # Ignore input transactions; these have cryptographic signatures,
  # not human-readable messages.
  if transaction.value < 0:
    continue

  print(f'Message from {transaction.hash}:')

  message = transaction.signature_message_fragment
  if message is None:
    print('(None)')
  else:
    print(message.decode())
