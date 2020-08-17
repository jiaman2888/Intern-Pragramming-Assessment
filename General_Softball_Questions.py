# Write a function that takes a paragraph of text and tells you what the most popular word is.

def CountMostWord(self, text: str) -> int:
    wordFreq = {}
    for c in text.split():
        if c in wordFreq.keys():
            wordFreq[c] += 1
        else:
            wordFreq[c] = 1
    maxNum = -1
    mostPop = ''
    for k, v in wordFreq.items():
        if maxNum <= v:
            maxNum = v
            mostPop = k

    return mostPop

    # time complexity: O(n), space complexity: O(n)

# Write a function that takes a string and returns it in reverse order.

def reverseString(self, s: List[str]) -> None:
    l = 0
    r = len(s) - 1
     while l < r:
        m = s[r]
        s[r] = s[l]
        s[l] = m
        l = l + 1
        r = r - 1

        # time complexity: o(n), space complexity: o(1)


# (optional) Write a function that takes a paragraph (string data type) and returns the largest word in the string. If there are two or more words that are the same length, return the first word from the string with that length. Ignore punctuation and assume the string will not be empty. For example using the paragraph below.

def FindLargestWord(text):
    len_word = []
    ListWord = text.split()
    ListWord.sort(key=lambda s: len(s))

    maxLength = len(ListWord[-1])
    for i in range(len(ListWord) - 1, -1, -1):
        if i == 0 or len(ListWord[i - 1]) != maxLength:
            return ListWord[i]
    return ""






