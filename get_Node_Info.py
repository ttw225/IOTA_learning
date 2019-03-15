from iota import Iota

server = 'http://140.116.247.123:14267'

# Generate a random seed.
api = Iota(server)

# Specify seed.
api = Iota(server, 'SEED9GOES9HERE')

print(api.get_node_info())
