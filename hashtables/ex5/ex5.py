
### This is some serious o(n^2) at least
# def finder(files, queries):
#   result = []
#   file_dict = {}

#   ## create a dictionary
#   # what should be my key: value pairs?
#   # save whole path as key?
#   ## use rsplit('/', 1) to check query against value

#   for file in files:
#     ## this is taking off the last bit of the file name to save as value
#     file_split = file.rsplit('/', 1)
#     file_dict[file] = file_split[1]

#   ### Need to check for each key in file_dict if the value = queries
#   ### Brute force is going to be A BIG BITCH
#   for file in file_dict:
#     # print(file)
#     for check in queries:
#       if file_dict[file] == check:
#         result.append(file)

#   return result

class LinkedDictNode:
  def __init__(self, file, prev=None, next=None):
    self.file = file
    self.prev = prev
    self.next = next

  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next
​
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev
​
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

class DoublyLinkedDict:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0
​
  def __len__(self):
    return self.length
​
  def add_to_head(self, value):
    new_node = ListNode(value)
    self.length += 1
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node
​
  def add_to_tail(self, value):
    new_node = ListNode(value)
    self.length += 1
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.prev = self.tail
      self.tail.next = new_node
      self.tail = new_node

def finder(files, queries):
  result = []
  file_dict = {}

  ## create a dictionary
  # what should be my key: value pairs?
  # save whole path as key?
  ## use rsplit('/', 1) to check query against value

  for file in files:
    ## this is taking off the last bit of the file name to save as value
    file_split = file.rsplit('/', 1)
    file_dict[file] = file_split[1]

  ### Need to check for each key in file_dict if the value = queries
  ### Brute force is going to be A BIG BITCH
  for file in file_dict:
    # print(file)
    for check in queries:
      if file_dict[file] == check:
        result.append(file)

  return result

# if __name__ == "__main__":
#   files = [
#     '/bin/foo',
#     '/bin/bar',
#     '/usr/bin/baz'
#   ]
#   queries = [
#     "foo",
#     "qux",
#     "baz"
#   ]
#   print(finder(files, queries))
