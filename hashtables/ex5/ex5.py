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
    print(file)
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
