def minMeetingRooms(intervals):
  allHoursNeeded = []
  allHours = []
  roomsNeeded = 0
  highestHour = 0
  lowestHour = 99999999999
  for interval in intervals:
    if interval[0] < lowestHour:
      lowestHour = interval[0]
    if interval[1] < lowestHour:
      lowestHour = interval[1]
    if interval[0] > highestHour:
      highestHour = interval[0]
    if interval[1] > highestHour:
      highestHour = interval[1]
    for hour in range(interval[0],interval[1] + 1):
      allHours.append(hour)
  for hour in range(lowestHour, highestHour + 1):
    allHoursNeeded.append([hour,0])
  for hour in allHours:
    for pair in allHoursNeeded:
      if hour == pair[0]:
        pair[1] += 1
  for pair in allHoursNeeded:
    if pair[1] > roomsNeeded:
      roomsNeeded = pair[1]

  return roomsNeeded

#print(minMeetingRooms([[1,16],[15,30],[31,35]]))
#print(minMeetingRooms([[1,50]]))
print(minMeetingRooms([(928,5032),(3072,3741),(3960,4588),(482,2269),(2030,4360),(150,772)]))