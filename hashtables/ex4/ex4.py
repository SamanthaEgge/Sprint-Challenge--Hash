def has_negatives(a):
  #initializing some shizzz
  result = []
  numb_dict = {}

  ### numbers will be in random order, so -1 number might come before a positive one
  ## Do a check of each number??
  ## create a dict with the inverse value
  ## if numb_dict[key] exists as a key, add to result?

  ## Generate dict
  for number in a:
    numb_dict[number] = -number

  ## Now to check 
  for key in numb_dict:
    if key < 0:
      if numb_dict[-key]:
        result.append(key)
 
  return result


if __name__ == "__main__":
  print(has_negatives([-1,-2,1,2,3,4,-4]))
