# Import library for sha256

import hashlib
import json

def crypto_hash(data):
    """
    Return a sha-256 hash of the given data.
    To get the sha-256 hash you need to encode the data as utf-8 to convert it to a byte chain and the call the hexdigest funcion.
    To see the unqiue string output we need to use hexdigest() otherwise you get the memory address representation.
    """
    stringified_data = json.dumps(data) # Dumps the data regardless of its type into a str representation

    return hashlib.sha256(stringified_data.encode('utf-8')).hexdigest() 

def main():
    print(f"crypto_hash([2]): {crypto_hash([2])}")

if __name__ == '__main__':
    main()