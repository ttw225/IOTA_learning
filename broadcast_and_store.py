from iota import Iota

server = 'http://140.116.247.123:14267'

# another node : https://nodes.thetangle.org:443

api = Iota(server)

# print(api.get_node_info())

trytes = []
trytes.append(
    'DXRNZCCBZWWLHKSLG9MTZGNEXYFGIMVTHDOHXHZYOQTGRRLOI9T9CCD9STHXBWAICFBANV9GJDFFZ9999')

print(api.broadcast_and_store(trytes))
