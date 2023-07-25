# Task_1_Spelling_Checker_WideBot

Task 1 - Spelling Checker
Using this dictionary, implement a spell checker class that takes this dictionary as input, this
class has three main operations:

• Store this dictionary in a suitable data structure.

• Take an input word and return the nearest 4 words if this word is not in the dictionary

• Take an input word and add this word to the dictionary

For each operation specify the time and space complexity
Note: You could assume that the nearest 4 words from a word are the 2 words before and
after this word in lexicographic order if they exist.

**The time and space complexity For each operation:**

**Time complexity:**
1. `insert`: The time complexity of inserting a word into the trie is O(k), where k is the length of the word. In the worst case, we have to traverse the entire word to insert it into the trie.

2. `build_from_file`: This method reads words from the file and inserts them into the trie using the `insert` method. The time complexity of reading the file and inserting all words is O(n * k), where n is the number of words in the file, and k is the average length of the words.

3. `_print_trie`: This method performs a depth-first traversal of the trie to print all words. The time complexity of this operation is O(m), where m is the total number of characters in all words present in the trie.

4. `find_nearest_words`: The time complexity of this operation depends on the length of the input word and the number of words with the same prefix as the input word. In the worst case, where there are many words with the same prefix, the time complexity can be O(k * n), where k is the length of the input word, and n is the number of words with the same prefix.

5. `add_word`: The time complexity of adding a word to the trie is O(k), where k is the length of the word. Similar to the `insert` method, we need to traverse the entire word to add it to the trie.

**Space complexity:**
1. The space complexity of the trie is O(N * M), where N is the number of nodes in the trie and M is the average number of children per node. In this implementation, M is effectively limited to the number of unique characters in the input words (usually the alphabet size).

2. Additional space will be used to store the words read from the file, but it will be O(N * k), where N is the number of words and k is the average length of the words.

3. The space used during the `find_nearest_words` operation is primarily due to the `result` list, which will contain at most 4 words. So, the space complexity is O(1) for this operation.

Overall, the space complexity is dominated by the space used to represent the trie data structure. The trie's space complexity is relatively efficient for storing and searching large dictionaries of words with common prefixes. However, it grows linearly with the number of unique characters in the input words.
