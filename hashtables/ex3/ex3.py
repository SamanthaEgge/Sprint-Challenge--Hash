def intersection(arrays):
  result = []
  ## get numbah of arrays
  print(len(arrays))
  numbArrays = len(arrays)
  #init array dictionary
  arrayDict = {}

  ## create dictionary based upon array input
  ## if key is found, increment value by 1
  ## if key = len(arrays), add to result
  ## profit?

  
  # print('we in intersection')
  # print(arrays)
  for smolArray in arrays:
    for number in smolArray:
      if number not in arrayDict:
        arrayDict[number] = 0
      arrayDict[number] += 1
      # print('arrayDict')
      # print(arrayDict)
      if arrayDict[number] == numbArrays:
        ### how do i get the KEEEEY --- I am not a smart lass
        result.append(number)
        # print(number)
  # print(result)
  return result


# if __name__ == "__main__":
#   arrays = []

#   arrays.append(list(range(1000000,2000000)) + [1,2,3])
#   arrays.append(list(range(2000000,3000000)) + [1,2,3])
#   arrays.append(list(range(3000000,4000000)) + [1,2,3])

#   print(intersection(arrays))
