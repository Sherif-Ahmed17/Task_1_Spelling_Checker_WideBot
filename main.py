from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def build_from_file(self, file_path):
        with open(file_path, 'r', encoding='latin-1') as file:
            for line in file:
                word = line.strip()
                self.insert(word)

    def _print_trie(self, node, prefix):
        if node.is_end_of_word:
            print(prefix)

        for char, child_node in node.children.items():
            self._print_trie(child_node, prefix + char)

    def print_trie(self):
        self._print_trie(self.root, "")

    # Operation: Take an input word and return the nearest 4 words if not in the dictionary
    def find_nearest_words(self, word):
        result = []

        def traverse(node, prefix):
            if len(result) >= 4 or not node:
                return

            if node.is_end_of_word:
                result.append(prefix)

            for char in sorted(node.children):
                traverse(node.children[char], prefix + char)

        node = self.root
        for char in word:
            if char not in node.children:
                # If the character is not found, return the result so far
                traverse(node, word[:-1])
                return result
            node = node.children[char]

        # If the input word exists in the dictionary, return an empty list
        if node.is_end_of_word:
            print(f"The word '{word}' already exists in the dictionary.")
            return []

        # Traverse the trie to find the nearest 4 words
        traverse(node, word)

        return result

    # Operation: Take an input word and add this word to the dictionary
    def add_word(self, word):
            node = self.root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            if node.is_end_of_word:
                print(f"The word '{word}' already exists in the dictionary.")
            else:
                node.is_end_of_word = True
                print(f"Added '{word}' to the dictionary.")


# Example usage:
if __name__ == "__main__":
    dictionary_file_path = "E:\WideBot – AI assignment\Task 1 - Spelling Checker\dictionary.txt"  # Replace with the actual file path

    trie = Trie()
    trie.build_from_file(dictionary_file_path)

    # # Print the trie
    # trie.print_trie()

    # Example usage of find_nearest_words
    # input_word = "apricot"
    input_word = "ap"
    nearest_words = trie.find_nearest_words(input_word)
    print(f"Nearest 4 words for '{input_word}': {nearest_words}")

    # Example usage of add_word
    new_word = "poque"
    trie.add_word(new_word)

    # Example usage of add_word with an existing word
    existing_word = "apple"
    trie.add_word(existing_word)
