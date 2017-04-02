# find the longest palindromic substring contained in a  
# http://www.geeksforgeeks.org/longest-palindromic-substring-set-2/
def question2(a):
    res = ""
    for i in xrange(len(a)):
        # for palindromic with odd length, such as 'ada'
        temp = palindromic(a,i,i)
        if len(temp) > len(res):
            res = temp
        
        # for palindromic with even length, such as 'adda'
        temp = palindromic(a,i,i+1)
        if len(temp) > len(res):
            res = temp  
    return res

def palindromic(string, start, end):
    # the first and the last character much be the same to be a palindromic
    while start >= 0 and end < len(string) and string[start] == string[end]:
        start -= 1
        end += 1
    return string[start+1:end]

print question2("") # ""
print question2("a") # a
print question2("abcbdd")  # bcb
print question2("abcccba")  # abcccba

# The goal of this question is to find the longest palindrome substring contained in a string a. My idea is to loop through every characters in a and find the longest possible palindrome with that character in the middle. I set an empty string as the output string 'res', and updated 'res' only when length of a possible palindrome is longer than 'res'. There are two cases that a string can be a palindrome, one is its length is an odd number, and the middle of the string is different with its adjacent letters, such as "ada". The other case is that the length is an even number, and there are two letters in the middle, such as "daad".  
# I used a helper function to find the longest palindrome. The first and the last character must be the same, and the characters that have the same difference from the first and the last characters much be same to be a palindrome. Thus, I used a condition to check whether the symmetric characters are the same: "while start >= 0 and end < len(string) and string[start] == string[end]:". There are three loops in this approach, therefore the time complexity is O ( n^2 ).  Space complexity is O ( 1 ) as we used a variable to store and update the output string.'''