start_list = [""] * 100

print start_list

def insert(h, k, v):
    pass

def get(h, k):
    #return v
    pass

def main():
    #get a key and a value
    #hash the key
    #modulo the key
    #make a list based on modulos and insert key at "moduloed" index
    #each entry in the list contains a list of keys
    #each key is a list of key and value
    k = raw_input("What is the secret word?")
    v = raw_input("What is the secret answer?")
    hash_key = hash(k)
    start_list[(hash_key % 100)-1]=[hash_key]
    start_list[(hash_key % 100)-1][hash_key]=[k,v]

    print start_list

main()