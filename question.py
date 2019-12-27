def dayOfProgrammer(year):
  if year % 4 ==0 and(year < 1918 or year % 400 == 0 or year % 100 != 0):
      return "12.09.%s" % year
  elif year == 1918:
      return "26.09.%s" % year
  return "13.09.%s" % year    
    
print(dayOfProgrammer(2017))
print(dayOfProgrammer(2016))
print(dayOfProgrammer(1918))