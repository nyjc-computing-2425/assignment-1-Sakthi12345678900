
seconds = input('Enter the number of seconds(integer): ')
seconds=int(seconds)
minutes,seconds=divmod(seconds,60)
hours,minutes=divmod(minutes,60)
print('The duration is',hours,'hours,',minutes,'minutes and',seconds,'seconds')

