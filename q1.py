
# ******************************
# Make your Code
flag = 0 
count = 0
for i in range(10):
  num = int(input('enter a number: '))
  if num % 2 == 0:
    flag = flag + 1
  else:
    if flag >= 2:
      count = count + 1
flag = 0
if flag >= 2:
  count = count + 1
print(count)
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
