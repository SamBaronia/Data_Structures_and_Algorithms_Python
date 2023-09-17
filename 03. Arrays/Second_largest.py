#URL = https://practice.geeksforgeeks.org/problems/second-largest3735/1


def print2largest(self,arr, n):
	# code here
	f_lar, s_lar= -1,-1
	for i in arr:
	    if i > f_lar and i > s_lar :
	        s_lar = f_lar
	        f_lar = i
	    if i > s_lar and i < f_lar :
	        s_lar = i
	return s_lar
		        