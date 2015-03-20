from p2pool.bitcoin import networks
PARENT = networks.nets['magi']
SHARE_PERIOD = 10 # seconds
CHAIN_LENGTH = 12*60*60//10 # shares
REAL_CHAIN_LENGTH = 12*60*60//10 # shares
TARGET_LOOKBEHIND = 100 # shares
SPREAD = 20 # blocks
IDENTIFIER = '05c1a0cfe46bf6ab'.decode('hex')
PREFIX = 'ecfe4cafcc0af6a9'.decode('hex')
P2P_PORT = 9233
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 9232
VERSION_CHECK = lambda v: v >= 71041
