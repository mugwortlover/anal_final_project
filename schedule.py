#credit: Ben

def sortTuple(tup):
    lst = len(tup)
    for i in range(0, lst):
        for j in range(0, lst-i-1):
            if (tup[j][1] < tup[j + 1][1]):
                temp = tup[j]
                tup[j] = tup[j + 1]
                tup[j + 1] = temp
    return tup


# Takes in a dictionary where the keys are vertices and the values are the colors
def invertDict(coloring):
  # Checking to see how many colors are used
  largestColor = 0
  for vertex in coloring:
    if coloring[vertex]>largestColor:
      largestColor = coloring[vertex]
  # Creation of the returned dictionary
  meetingTimes = {}
  for i in range(largestColor+1):
    meetingTimes[i]=[]
  # Populating the returned dictionary
  for vertex in coloring:
    meetingTimes[coloring[vertex]]+=[vertex]
  return meetingTimes


# Takes in a dictionary where the keys are the colors and the values are the vertices
def outputMessage(meetingTimes):
  # Creates a list of tuples
  timeSlots = []
  for slot in meetingTimes:
    timeSlots.append((slot,len(meetingTimes[slot])))
  # Sort from greatest to least
  sortedSlots = sortTuple(timeSlots)
  for i in range(len(sortedSlots)):
    print("Meeting Time %s has the groups: %s " % (i+1," | ".join(meetingTimes[sortedSlots[i][0]])))


def coloringSchedule(coloring):
  outputMessage(invertDict(coloring))