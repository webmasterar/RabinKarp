# License MIT 2016 Ahmad Retha

##
# The hash() function takes a string s of length m and creates a numerical
# representation. Say s = 'ATA', and ord('A') = 65 and ord('T') = 84, and m = 3;
# using a prime base of 101, we sum up the total to get the hash (d):
#
# d = (101^2 * 65) + (101^1 * 84) + (101^0 * 65)
#
def hash(s, m):
	d = 0
	i = 1
	while i <= m:
		d += 101**(m-i) * ord(s[i-1])
		i += 1
	return d

##
# rollhash() is used to update the hash for the next position in T. We do this
# by subtracting the value of the character we want to remove, remChar, from the
# old hash. Then we multiply the result by the base (101). Finally, we add the
# value of the next char, insChar. A rolling/updating hash is faster than doing
# a full hash over and over again with the hash() function.
#
# Example: T = 'ATATG', i = 0, m = 3. Imagine we already have an old hash for ATA
# from position 0 of T. To get the next hash we remove the first 'A' and we add
# the next character 'T' of T, meaning the next hash would be for TAT.
#
# d = oldHash - (101^2 * 65)
# d = d * 101
# d = d + 101^0 * 84
#
def rollhash(oldHash, remChar, insChar, m):
	d = oldHash - (101**(m-1) * ord(remChar))
	d *= 101
	d += 101**0 * ord(insChar)
	return d

##
# Main function
#
def main():
	T = 'CATATCGGCATA'
	n = len(T)
	P = 'ATA'
	m = len(P)

	print 'Looking for pattern ' + P + ' in text ' + T + ':\n'

	PHashed = hash(P, m)
	THashed = hash(T[0:m], m)

	i = 0
	found = False

	##
	# This is the body of the Rabin-Karp search
	#
	while i < n - m + 1:
		if PHashed == THashed and P == T[i:i+m]:
			found = True
			print 'Match found at position', i
		if i < n - m:
			THashed = rollhash(THashed, T[i], T[i+m], m)
		i += 1

	if not found:
		print 'No matches found!'


if __name__ == '__main__':
	main()
