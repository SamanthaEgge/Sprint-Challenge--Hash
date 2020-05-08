def get_indices_of_item_weights(weights, length, limit):
  ##init some values
  result = []
  weight_dict = {}

  index = 0
  ## generating the dictionary
  for wt in weights:
    if wt in weight_dict:
      save = weight_dict[wt]
      weight_dict[wt] = [save, index]
    else:
      weight_dict[wt] = index
    index = index +1

  print(weight_dict)

  ## mathing according to hints
  if length == 1:
    result = None
    return result
  for wt in weight_dict:
    # print('limit', limit)
    # print('wt', wt)
    key_check = limit-wt
    print('limit,wt,keycheck', limit, wt, key_check)
    if key_check in weight_dict:
      print('we in here?')
      if isinstance(weight_dict[wt],list):
        print('check this garbage',weight_dict[wt][0])
        result.append(weight_dict[wt][1])
        result.append(weight_dict[wt][0])
      if weight_dict[wt] > weight_dict[key_check]:
        print('we in true?')
        result.append(weight_dict[wt])
        result.append(weight_dict[key_check])
        return result
      else:
        print('we in true2?')
        result.append(weight_dict[key_check])
        result.append(weight_dict[wt])
        return result

  if len(result) == 0:
    result = None


  print('can access weight_dict', weight_dict[6])

  return result
