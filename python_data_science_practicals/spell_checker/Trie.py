class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        current_trie = self.root
        for char in word:
            if char not in current_trie.children:
                current_trie.children[char] = TrieNode()

            current_trie = current_trie.children[char]

        current_trie.is_word = True


    def exists(self, word):
        """
        Check if word exists in trie
        """
        current_trie = self.root
        for char in word:
            if char not in current_trie.children:
                return False
            current_trie = current_trie.children[char]

        return current_trie.is_word


if __name__ is '__main__':
    def test_Trie():

        valid_words = ['the', 'a', 'there', 'answer', 'any', 'by', 'bye', 'their']
        word_trie = Trie()
        for valid_word in valid_words:
            word_trie.add(valid_word)

        # Tests
        assert word_trie.exists('the')
        assert word_trie.exists('any')
        assert not word_trie.exists('these')
        assert not word_trie.exists('zzz')
        print('All tests passed!')

    test_Trie()
