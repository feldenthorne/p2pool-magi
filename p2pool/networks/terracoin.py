from p2pool.bitcoin import networks

PARENT = networks.nets['terracoin']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 12*60*60//30 # shares
REAL_CHAIN_LENGTH = 12*60*60//30 # shares
TARGET_LOOKBEHIND = 20 # shares
SPREAD = 10 # blocks
IDENTIFIER = 'efba2ef800a1b75e'.decode('hex')
PREFIX = 'a7e0b4f5e29eb866'.decode('hex')
P2P_PORT = 9323
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = False
WORKER_PORT = 9322
BOOTSTRAP_ADDRS = 'rav3n.dtdns.net'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-alt'
VERSION_CHECK = lambda v: 80002 <= v
VERSION_WARNING = lambda v: 'Upgrade Terracoin to >= 0.8.0.4!' if v < 80004 else None
