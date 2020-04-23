# Using modules from another file and importing the class

from block import Block

class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions.
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'

def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')
    blockchain.add_block('three')

    print(blockchain)
    print(f"blockchain.py __name__: {__name__}") # Check the name of the module

# If the name of the module is equal to '__main__' then it will run the main function

if __name__ == '__main__':
    main()