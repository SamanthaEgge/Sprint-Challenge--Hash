def intersection(arrays):
  result = []
  ## get numbah of arrays
  numbArrays = len(arrays)
  #init array dictionary
  arrayDict = {}

  ## create dictionary based upon array input
  ## if key is found, increment value by 1
  ## if key = len(arrays), add to result
  ## profit?

  for smolArray in arrays:
    for number in smolArray:
      if number not in arrayDict:
        arrayDict[number] = 1
      arrayDict[number] += 1
      if arrayDict[number] == numbArrays:
        ### how do i get the KEEEEY
        print('this passed')


  return result


if __name__ == "__main__":
  arrays = []

  arrays.append(list(range(1000000,2000000)) + [1,2,3])
  arrays.append(list(range(2000000,3000000)) + [1,2,3])
  arrays.append(list(range(3000000,4000000)) + [1,2,3])

  print(intersection(arrays))
