
import time

count=0
count1=0
class Node:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


def insertWord(root, word):
    '''
    Loop through characters in a word and keep adding them at a new node, linking them together
    If char already in node, pass
    Increment the current to the child with the character
    After the characters in word are over, mark current as EOW
    '''
    global count1
    current = root
    for char in word:

        if char in current.children.keys():
            pass
        else:
            count1 += 1
            current.children[char] = Node()
        current = current.children[char]
    current.endOfWord = True


def allWords(prefix, node, results):
    '''
    Recursively call the loop
    Prefix will be prefix + current character
    Node will be position of char's child
    results are passed by reference to keep storing result

    Eventually, when we reach EOW, the prefix will have all the chars from starting and will be the word that we need. We add this word to the result
    '''
    global count
    if node.endOfWord:
        # count+=1
        results.append(prefix)
    for char in node.children.keys():
        count+=1
        # print char, node, node.children
        allWords(prefix + char, node.children[char], results)


def searchWord(root, word):
    '''
    Loop through chars of the word in the trie
      If char in word is not in trie.children(), return
      If char found, keep iterating
    After iteration for word is done, we should be at the end of word. If not, then word doesn't exist and we return false.
    '''
    current = root
    search_result = True
    for char in word:
        if char in current.children.keys():
            pass
        else:
            search_result = False
            break
        current = current.children[char]

    return search_result


def getWordsWithPrefix(prefix, node, prefix_result):
    '''
    We loop through charcters in the prefix along with trie
    If mismatch, return
    If no mismatch during iteration, we have reached the end of prefix. Now we need to get words from current to end with the previx that we passed. So call allWords with prefix
    '''

    global count
    current = node

    for char in prefix:
        if char in current.children.keys():
            count += 1
            pass
        else:
            return

        current = current.children[char]
    allWords(prefix, current, prefix_result)


def getcount(prefix, node, prefix_result):
    '''
    We loop through charcters in the prefix along with trie
    If mismatch, return
    If no mismatch during iteration, we have reached the end of prefix. Now we need to get words from current to end with the previx that we passed. So call allWords with prefix
    '''

    global count
    current = node

    for char in prefix:
        if char in current.children.keys():
            count += 1
            pass
        else:
            return

        current = current.children[char]
    allWords(prefix, current, prefix_result)

def main():
    # Input keys (use only 'a' through 'z' and lower case)
    start_ = time.time_ns()
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]

    # Trie object
    root = Node()

    level=0
    # Construct trie

    for key in keys:
        insertWord(root, key)

    stop = time.time_ns()
    print(stop-start_)
    print(count1)


    prefix_result = []
    start = time.time_ns()
    str = input("Enter the Prefix you want")
    getWordsWithPrefix(str, root, prefix_result)
    print('\nWords starting with', str)
    for word in prefix_result:
        print(word)
    stop = time.time_ns()
    print(count)
    print(stop-start)




if __name__ == '__main__':
    main()

"""root = Node()
#words = ['bed', 'ben']
words = ['bed', 'bedlam', 'bond','bomb', 'bomber', 'bombay']
for word in words:
    insertWord(root, word)

results = []
prefix = ''
allWords(prefix, root, results)
# prefix will be added to every word found in the result, so we start with ''
# results is empty, passed as reference so all results are stored in this list
print('All words in trie: {}\n\n'.format(results))


search_word = 'bomb'
search_result = searchWord(root, search_word)
print('Search {} in {}: {}'.format(search_word, words, search_result))

search_word = 'bomber'
search_result = searchWord(root, search_word)
print('Search {} in {}: {}'.format(search_word, words, search_result))

prefix_result = []
prefix = 'b'
getWordsWithPrefix(prefix, root, prefix_result)
print('\n\nWords starting with {}: {}'.format(prefix, prefix_result))"""