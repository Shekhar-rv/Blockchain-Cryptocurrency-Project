# Import library for sha256

import hashlib
import json

def crypto_hash(*args):
    """
    Return a sha-256 hash of the given number of arguments.
    To get the sha-256 hash you need to encode the data as utf-8 to convert it to a byte chain and the call the hexdigest funcion.
    To see the unqiue string output we need to use hexdigest() otherwise you get the memory address representation.
    """
    stringified_args = sorted(map(lambda data: json.dumps(data), args)) # Dumps the arguments regardless of its type into a str representation

    joined_data = ''.join(stringified_args)

    return hashlib.sha256(joined_data.encode('utf-8')).hexdigest() 

def main():
    print(f"crypto_hash('one', 2, [3]): {crypto_hash('one', 2, [3])}")
    print('\n')
    print(f"crypto_hash(2, [3], 'one'): {crypto_hash(2, [3], 'one')}")
if __name__ == '__main__':
    main()