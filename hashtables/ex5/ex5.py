
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
      file_dict[file_split[1]].append(file)
    else:
      ## create new list
      file_dict[file_split[1]] = [file]
  
  # print(file_dict)

  ## For each query, check to see if that file exists.
  # if so, append each filename to the result

  for query in queries:
    if query in file_dict:
      ## Need some sort of loop or map to go over each value in file_dict[query] then append it to results
      for paths in file_dict[query]:
        result.append(paths)

  return result


########## TODO:Current is having issues with adding new nodes to list


# if __name__ == "__main__":
#   files = [
#     '/bin/foo',
#     '/bin/bar',
#     '/usr/bin/baz',
#     '/usr/foo'
#   ]
#   queries = [
#     "foo",
#     "qux",
#     "baz"
#   ]
#   print(finder(files, queries))
