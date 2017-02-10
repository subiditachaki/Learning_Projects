# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
		# import ipdb
		# ipdb.set_trace()
		self.data = data  # Assign data
		self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
	def __init__(self):
		# import ipdb
		# ipdb.set_trace()
		self.head = None

	# This function prints contents of linked list
	# starting from head
	def printList(self):
	# import ipdb
	# ipdb.set_trace()
		temp = self.head
		while (temp):
			print temp.data
			temp = temp.next

	def push(self,new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	def insert_after(self, prev_node, new_data):
		new_node = Node(new_data)
		new_node.next = prev_node.next
		prev_node.next = new_node

	def append(self, new_data):
		last = self.head
		while(last.next):
			last = last.next

		new_node = Node(new_data)
		last.next = new_node

	def delete_node(self, node_to_delete):
		temp = self.head 

		if temp.data == node_to_delete:
			self.head = temp.next
		else:
			while(temp.data != node_to_delete):
				prev = temp
				temp = temp.next

			prev.next = temp.next
		temp = None
 
	def count_length(self):
		temp = self.head
		count = 1
		while(temp.next):
			count+=1
			temp = temp.next

		print("length of Linked list = " + str(count))

# Code execution starts here
if __name__=='__main__':
	# import ipdb
	# ipdb.set_trace()

	# Start with the empty list
	llist = LinkedList()

	llist.head  = Node(1)
	second = Node(2)
	third  = Node(3)

	llist.head.next = second; # Link first node with second
	second.next = third; # Link second node with the third node

	llist.append(4)
	llist.push(0)
	llist.insert_after(llist.head, 6)
	llist.delete_node(0)
	llist.count_length()


	llist.printList()