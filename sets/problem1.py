# find average using set 


def average(array):
   lenth = len(set(array))
   avg = sum(set(array))/lenth
   
   return avg