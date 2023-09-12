
# Reversing characters in a string, specify a minimum size for reversal. Any strings smaller
# than the minimum size will not be reversed.
#
# There might be shorter ways to write this, but i don't know anything about python, yet!
def reverse_chars(str, minLength):
    if len(str) >= minLength: 
        return str[::-1]
    else:
        return str

# print(reverse_chars("hell0", 5))

def traverse_sentence_and_optionally_reverse(sentence):
    for word in sentence.split():
        print(reverse_chars(word, 5), end=' ')

traverse_sentence_and_optionally_reverse("It's a good world")
