#  Hint:  You may not need all of these.  Remove the unused functions.
## Need to connect flights from source to destination
## Decoder ring

class Ticket:
  def __init__(self, source, destination):
    self.source = source
    self.destination = destination


def reconstruct_trip(tickets, length):
  route_dict = {}
  route = []

  ### find the initial location, append to route array
  ### Search ticket dict keys for prev value, add value to route array
  ### loop until destination is none
  
  ### Build route Dict
  for path in tickets:
    route_dict[path.source] = path.destination
  
  print(route_dict)

  ## W
  while len(route) < length-1:

    ## Grabbing start location
    if len(route) == 0:
      route.append(route_dict["NONE"])

    #Based upon previous location, add next location
    route.append(route_dict[route[len(route)-1]])    

  print(route)

  return route


### Order: LAX, SFO, BHM, FLG, XNA, SAP, SLC, PIT, ORD
# ticket_1 = Ticket("PIT", "ORD")
# ticket_2 = Ticket("XNA", "SAP")
# ticket_3 = Ticket("SFO", "BHM")
# ticket_4 = Ticket("FLG", "XNA")
# ticket_5 = Ticket("NONE", "LAX")
# ticket_6 = Ticket("LAX", "SFO")
# ticket_7 = Ticket("SAP", "SLC")
# ticket_8 = Ticket("ORD", "NONE")
# ticket_9 = Ticket("SLC", "PIT")
# ticket_10 = Ticket("BHM", "FLG")

# tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

# reconstruct_trip(tickets,10)