"""
hands of the clock overlap 11 times every 12 hours or every 1 hour, 5 minutes, and 27.3 seconds
this equates to 65.454545 minutes. How often does this number go into the total minutes passed?
(add 1 because they start overlappi
"""

hh,mm = input().split(':')
minutes = int(hh)*60+int(mm)
print(int(minutes/(12/11*60))+1)