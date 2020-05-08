
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
    self.next = LinkedDictNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  def insert_before(self, value):
    current_prev = self.prev
    self.prev = LinkedDictNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

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

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    new_node = LinkedDictNode(value)
    self.length += 1
    if not self.head and not self.tail:
      self.head = new_node
      self.tail = new_node
    else:
      new_node.next = self.head
      self.head.prev = new_node
      self.head = new_node

  def add_to_tail(self, value):
    new_node = LinkedDictNode(value)
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

  ## create a dictionary of the files
  # since we're searching for the file name only, save file name as key
  # in linked list, save each full file directory to the dictionary
  # Going to use rsplit (right split) to get the file name
  for file in files:
    #this produces foo, bar, baz
    file_split = file.rsplit('/', 1)
    ## this is checking if file name already exists in dictionary
    if file_split[1] in file_dict:
      print(file_dict[file_split[1]])
      file_dict[file_split[1]].add_to_tail(file)
    else:
      ## create new linked list, starting with this filepath
      file_dict[file_split[1]] = DoublyLinkedDict(file)
  
  print(file_dict)

  ## For each query, check to see if that file exists.
  # if so, append each filename to the result

  for query in queries:
    if query in file_dict:
      

  return result


########## TODO:Current is having issues with adding new nodes to list


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
