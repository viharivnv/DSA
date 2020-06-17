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
    current = root
    if word[0] in current.children.keys():
        pass
    else:
        current.children[word[0]]=Node()
    current=current.children[word[0]]

    if word[1:].startswith(str(current.children.keys())):
        pass
    else:
        current.children[word[1:]]=Node()
    current = current.children[word[1:]]
    current.endOfWord = True


def allWords(prefix, node, results):
    '''
    Recursively call the loop
    Prefix will be prefix + current character
    Node will be position of char's child
    results are passed by reference to keep storing result

    Eventually, when we reach EOW, the prefix will have all the chars from starting and will be the word that we need. We add this word to the result
    '''
    if node.endOfWord:
        results.append(prefix)
    for char in node.children.keys():
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
    if word[0] in current.children.keys():
        print("test1")
        current=current.children[word[0]]
    else:
        return False

    current = current.children[word[0]]
    if word[1:] in current.children.keys():
        print('test')
        pass
    else:
        return False

    return search_result


def getWordsWithPrefix(prefix, node, prefix_result):
    '''
    We loop through charcters in the prefix along with trie
    If mismatch, return
    If no mismatch during iteration, we have reached the end of prefix. Now we need to get words from current to end with the previx that we passed. So call allWords with prefix
    '''
    current = node
    if prefix[0] in current.children.keys():
        if prefix[1:].startswith(current.children.keys()):
            pass

    allWords(prefix, current, prefix_result)



def main():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]

    # Trie object
    root = Node()

    level=0
    # Construct trie
    for key in keys:
        insertWord(root, key)

    results = []
    prefix = ''
    allWords(prefix, root, results)
    # prefix will be added to every word found in the result, so we start with ''
    # results is empty, passed as reference so all results are stored in this list
    print('All words in trie: {}\n\n'.format(results))

    while(True):
        check=int(input("Enter 1 to continue to search a key or 0 to exit:"))
        if check:
            str = input("Enter the Prefix you want")
            if searchWord(root, str):
                prefix_result = []
                getWordsWithPrefix(str, root, prefix_result)
                print('\nWords starting with', str)
                for word in prefix_result:
                    print(word)
            else:
                print('No such Key or pre-fix!!!')
                ins = int(input('Enter 1 to insert:'))
                if (ins):
                    str1 = input('Enter the whole word you want to add')
                    insertWord(root, str1)

        else:
            break




if __name__ == '__main__':
    main()

