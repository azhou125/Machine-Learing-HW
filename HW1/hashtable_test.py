# Here are a set of very simple tests. Please make sure your code passes the provided tests -- this serves as a check that our grading script will work.
# You are encouraged to add additional tests of your own, but you do not need to submit this file.

from hashtable_chaining import HashTable as HashTableChaining
from hashtable_linear_probing import HashTable as HashTableProbing

def print_array(table):
    print("#Start#")
    for i in range(table.array.size):
        if table.array.get(i) is None:
            print("None")
            continue
        (k, v) = table.array.get(i)
        print("key: %s, value: %s" %(k, v))
    print("#End#\n")

for (name, HashTable) in [("linear probing", HashTableProbing)]: #("chaining", HashTableChaining)
    table = HashTable()
    
    table.insert(1, "1")
    table.insert(11, "11")

    table.remove(1)
    table.insert(11, "11new")
    table.insert(2, "2")
    table.insert(4, "4")
    table.insert(5, "5")

    table.remove(2)

    table.insert(22, "22")

    table.insert(7, "7")
    table.insert(8, "8")

    table.insert(6, "6")
    table.remove(6)

    table.insert(21, "21")
    
    table.remove(21)

    table.insert(0, "0")
    
    table.remove(0)
    table.remove(11)
    table.remove(22)
    table.remove(4)
    table.remove(5)
    table.remove(7)
    table.remove(8)

    table.insert(9, "9")
    table.remove(9)

    table.insert(0, "0")
    table.insert(4, "4")
    table.insert(15, "15")
    table.insert(14, "14")
    table.remove(15)
    table.insert(14, "new14")

    print_array(table)
    print table.size()