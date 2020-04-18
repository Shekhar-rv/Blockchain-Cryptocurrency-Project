# This a sample code of how the blockchain works.

# Create a function that a simple hash method using *

def lightning_hash(data):
    return data + '*'

# Create a class Block that takes 3 arguments 

class Block:
    def __init__(self, data, hash, last_hash):
        self.data = data
        self.hash = hash
        self.last_hash = last_hash

# Create a variable with an instance of class Block

foo_block = Block('foo_data', 'foo_hash', 'foo_last_hash')

# Print out the data

print(foo_block.data)
print(foo_block.hash)
print(foo_block.last_hash)

# Create a class Blockchain that creates a genesis block and adds the new blocks to the genesis block

class Blockchain:
    def __init__(self):
        genesis = Block('gen_data', 'gen_hash', 'gen_last_hash')

        self.chain = [genesis]

# Creating a function append the new blocks to the genesis block after hashing

    def add_block(self, data):
        last_hash = self.chain[-1].hash
        hash = lightning_hash(data + last_hash)

        block = Block(data, hash, last_hash)

        self.chain.append(block)

# Creating a instance of class Blockchain

foo_blockchain = Blockchain()
foo_blockchain.add_block('one')
foo_blockchain.add_block('two')
foo_blockchain.add_block('three')

# printing each blocks in the block chain

for block in foo_blockchain.chain:
    print(block.__dict__)
