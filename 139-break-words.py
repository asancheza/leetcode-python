#!/usr/bin/python

# Time:  O(n)
# Space: O(n)
#
# Given a string s and a dictionary of words dict, 
# determine if s can be segmented into a space-separated sequence of one or more dictionary words.
# 
# For example, given
# s = "leetcode",
# dict = ["leet", "code"].
# 
# Return true because "leetcode" can be segmented as "leet code".
#

def break_words(s, d):
	if not s:
		return False

	count = {}
	word = ''

	for i in s:
		word += i

		if word in d:
			count[word] = 1
			word = ''

	sum = 0

	for k,v in count.items():
		if v == 1:
			sum += len(k)

	if sum == len(s):
		return True

	return False

print break_words('leetcodes', ['leet', 'code', 'paper'])