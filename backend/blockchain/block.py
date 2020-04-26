import time
from backend.util.crypto_hash import crypto_hash

# Creating a global variable (with CAPS)
GENESIS_DATA = {
    'timestamp':1,
    'last_hash': 'genesis_last_hash',
    'hash': 'genesis_hash',
    'data': []
}

class Block:
    """
    Block: a unit of storage.
    Storage transactions in a blockchain that supports a crytocurrency.
    """
    def __init__(self, timestamp, last_hash, hash, data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data

    def __repr__(self):
        return ( 
            f'timestamp: {self.timestamp}, '
            f'last_hash: {self.last_hash}, '
            f'hash: {self.hash}, '
            f'Block-data: {self.data}'
        )

    @staticmethod # Setting the function under a class, the function does not have a self keyword so we use a decorator static method
    def mine_block(last_block, data):
        """
        Mine a block based on the given last_block and data.
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        hash = crypto_hash(timestamp, last_hash, data)

        return Block(timestamp, last_hash, hash, data)

    @staticmethod
    def genesis():
        """
        Generate the genesis block.
        """
        #return Block(
        #    GENESIS_DATA['timestamp'],
        #    GENESIS_DATA['last_hash'],
        #    GENESIS_DATA['hash'],
        #    GENESIS_DATA['data']
        #)
        return Block(**GENESIS_DATA)

def main():
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'foo')
    print(block)

# If the name of the module is equal to '__main__' then it will run the main function

if __name__ == '__main__':
    main()