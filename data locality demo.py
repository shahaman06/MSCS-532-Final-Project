import time

# -------------------------------
# Linked List (Poor Locality)
# -------------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def create_linked_list(n):
    head = Node(0)
    current = head
    for i in range(1, n):
        current.next = Node(i)
        current = current.next
    return head

def traverse_linked_list(head):
    total = 0
    current = head
    while current:
        total += current.value
        current = current.next
    return total

# -------------------------------
# Array (Good Locality)
# -------------------------------
def array_sum(arr):
    total = 0
    for x in arr:
        total += x
    return total

# -------------------------------
# Performance Comparison
# -------------------------------
n = 1_000_000

print("Running Linked List test...")
head = create_linked_list(n)
start = time.time()
traverse_linked_list(head)
linked_time = time.time() - start

print("Running Array test...")
arr = list(range(n))
start = time.time()
array_sum(arr)
array_time = time.time() - start

print("\n--- Results ---")
print("Linked List Time:", linked_time)
print("Array Time:", array_time)