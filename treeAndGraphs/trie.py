# implementation of trie
# reference: https://www.youtube.com/watch?v=o6563NNbdtg
# https://www.youtube.com/watch?v=zIjfhVPRZCg

class Trie:
    def __init__(self):
        self.head = {}

    def insert(self, word):
        curr = self.head
        for char in word:
            if char not in curr:
                curr[char] = {}
            curr = curr[char]
        curr['isCompleteWord'] = True
        return word

    def search(self, word):
        curr = self.head
        for char in word:
            if char not in curr:
                return False
            else:
                curr = curr[char]
        return True

# __main__

t = Trie()
t.insert("hello")
print(t.search("hello"))
