from iota import Iota
from iota.crypto.addresses import AddressGenerator

seed = b'TOKGLENCLJ9CVOFFOROSBODVWFEQE9UOOOGJODTLOQ9SBSXGOXDXHBTRELFDNACYSLEYXGUEZPKSYGYSK'

# generator = AddressGenerator(seed)

generator =\
    AddressGenerator(
        seed=seed,
        security_level=3,
    )

# Generate a list of addresses:
# addresses = generator.get_addresses(index=0, count=5)
# NOOO! Document was wrong!!!!!!! use `start` instead `index`
addresses = generator.get_addresses(start=0, count=5)
print(addresses)
print('='*20)
# Generate a list of addresses in reverse order:
# addresses = generator.get_addresses(start=42, count=10, step=-1)
addresses = generator.get_addresses(start=0, count=5)
print(addresses)
