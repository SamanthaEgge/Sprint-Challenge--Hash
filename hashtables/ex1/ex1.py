def get_indices_of_item_weights(weights, length, limit):
  ##init some values
  result = []
  weight_dict = {}

  index = 0
  ## generating the dictionary
  for wt in weights:
    weight_dict[wt] = index
    index = index +1
    print(index)

  ## mathing according to hints
  if length == 1:
    result = None
    return result
  for wt in weight_dict:
    print('limit', limit)
    print('wt', wt)
    if weight_dict[limit-wt]:
      print(weight_dict[limit-wt])
      if weight_dict[wt] > weight_dict[limit-wt]:
        result.append(weight_dict[wt])
        result.append(weight_dict[limit-wt])
      else:
        result.append(weight_dict[limit-wt])
        result.append(weight_dict[wt])

  if len(result) == 0:
    result = None

  return result
