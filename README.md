city = ["hyderabad", "chennai","KDP", "bangalore"]
# vowels = "aeiou"
# d1 = {}
# def check_Vow(city, vowels):
# 	count = {}.fromkeys(vowels,0)
# 	for charectors in city:
# 		if charectors in count:
# 			count[charectors]+=1
# 	return count
# print(check_Vow(city,vowels))
# vowels = "aeiou"


d1 = {}
def check_Vow(city, vowels):
	# k = city.casefold()
	count = {}.fromkeys(vowels, 0)
	for i in city:

		if i in count:
			count[i] += 1
	return count
			
vowels = "aeiou"

k = "hyderabad"
d1 = dict.fromkeys(city,check_Vow(k,vowels))
print(d1)

