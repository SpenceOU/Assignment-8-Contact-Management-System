class Contact:
    '''
    Contact class to represent a contact with a name and number.
    Attributes:
        name (str): The name of the contact.
        number (str): The phone number of the contact.
    '''

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"

class Node:
    '''
    Node class to represent a single entry in the hash table.
    Attributes:
        key (str): The key (name) of the contact.
        value (Contact): The value (Contact object) associated with the key.
        next (Node): Pointer to the next node in case of a collision.
    '''

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    HashTable class to represent a hash table for storing contacts.
    Attributes:
        size (int): The size of the hash table.
        data (list): The underlying array to store linked lists for collision handling.
    Methods:
        hash_function(key): Converts a string key into an array index.
        insert(key, value): Inserts a new contact into the hash table.
        search(key): Searches for a contact by name.
        print_table(): Prints the structure of the hash table.
    '''

    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        # Add up the character codes, then wrap into the array with modulo
        total = 0
        for char in key:
            total += ord(char)
        return total % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.data[index]
        new_node = Node(key, Contact(key, value))

        # Empty slot: the new node becomes the head of the chain
        if current is None:
            self.data[index] = new_node
            return

        # Walk the chain: if the name already exists, update the number
        while True:
            if current.key == key:
                current.value.number = value
                return
            if current.next is None:
                break
            current = current.next

        # Name not found: add the new node at the end of the chain
        current.next = new_node

    def search(self, key):
        index = self.hash_function(key)
        current = self.data[index]
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self):
        for index in range(self.size):
            current = self.data[index]
            if current is None:
                print(f"Index {index}: Empty")
            else:
                line = f"Index {index}: "
                while current is not None:
                    line += f"- {current.value} "
                    current = current.next
                print(line)

# Test your hash table implementation here.
table = HashTable(10)
table.print_table()

table.insert("John", "909-876-1234")
table.insert("Rebecca", "111-555-0002")
table.print_table()

contact = table.search("John")
print("\nSearch result:", contact)

# Edge case 1: hash collisions (Amy and May both hash to index 5)
table.insert("Amy", "111-222-3333")
table.insert("May", "222-333-1111")
table.print_table()

# Edge case 2: duplicate key updates the number
table.insert("Rebecca", "999-444-9999")
table.print_table()

# Edge case 3: searching for a name that is not in the table
print(table.search("Chris"))