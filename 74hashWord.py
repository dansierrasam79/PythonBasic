# Write a Python program to hash a word.
if __name__ == "__main__":
    import hashlib
    hash_object = hashlib.md5(b'Hello World')
    print(hash_object.hexdigest())
