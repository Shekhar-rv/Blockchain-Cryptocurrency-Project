class Block:
    """
    Block: a unit of storage.
    Storage transactions in a blockchain that supports a crytocurrency.
    """
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'Block-data: {self.data}'

def main():
    block = Block('foo')
    print(block)
    print(f"block.py __name__: {__name__}") # Check the name of the module

# If the name of the module is equal to '__main__' then it will run the main function

if __name__ == '__main__':
    main()