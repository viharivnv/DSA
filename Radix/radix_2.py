
import time

count=0
count1=0
class RadixNode:
    def __init__(self, k=None):
        """
        Initialize a Radix Tree Node
        :param k: key value of the node (default None)
        """
        self.key = k
        self.children = {}
        self.isLeaf = False

    def leafOrNot(self):
        """
        Check if the node is a leaf or not
        :return: Boolean
        """
        return self.isLeaf

    def __str__(self):
        """
        Specify the string to be returned when the Node is printed
        :return: String
        """
        return self.key


class RadixTree:
    def __init__(self):
        """
        Initialize a Radix Tree
        """
        self.root = RadixNode()

    def insert(self, x, k):
        """
        Insert a string at the given node
        :param x: node at which specified string is to be inserted
        :param k: string which is to be inserted at the node
        :return: None
        """
        global count1

        if k == '':

            x.isLeaf = True
            return
        combos = getAllStrings(k)
        for a in combos:
            for b in x.children.keys():

                if a[0] == b[:len(a[0])]:

                    if a[0] != b:

                        x.children[a[0]] = RadixNode(a[0])
                        x.children[a[0]].children[b[len(a[0]):]] = x.children[b]
                        x.children[a[0]].children[b[len(a[0]):]].key = b[len(a[0]):]
                        if a[1][len(a[0]):] != '':

                            x.children[a[0]].children[a[1][len(a[0]):]] = RadixNode(a[1][len(a[0]):])
                            x.children[a[0]].children[a[1][len(a[0]):]].isLeaf = True
                        else:
                            x.children[a[0]].isLeaf = True
                        del x.children[b]
                    else:

                        self.insert(x.children[b], k[len(a[0]):])
                    return
        x.children[k] = RadixNode(k)
        x.children[k].isLeaf = True

    def search(self, x, k):
        """
        Search for a string at the given node
        :param x: node at which specified string is to be searched for
        :param k: string which is to be searched for at the node
        :return: None
        """
        if k == '':
            return x.leafOrNot()
        for a in getAllStrings(k):
            if a[0] in x.children.keys():
                return self.search(x.children[a[0]], k[len(a[0]):])
        return False

    def count(self, x, string):
        """
        Print the complete sorted tree
        :param x: node at which leaves are searched for
        :param string: contains the string that is formed by parent nodes of x
        :return: None
        """

        global count1
        for a in sorted(x.children.keys()):
            if x.children[a].isLeaf:
                count1+=1
            self.count(x.children[a], string + a)

    def print_tree(self, x, string, prefix):
        """
        Print the complete sorted tree
        :param x: node at which leaves are searched for
        :param string: contains the string that is formed by parent nodes of x
        :return: None
        """
        global count
        for a in sorted(x.children.keys()):

            if x.children[a].isLeaf:
                if (string + a).startswith(prefix):
                    count+=1
                    print(string+a)
            self.print_tree(x.children[a], string + a,prefix)

    def spell_checker(self, string):
        """
        Checks is a string exists in the tree
        :param string: string whose validity is to be checked
        :return: Boolean
        """
        return self.search(self.root, string)


def getAllStrings(string):
    """
    Yield all string instances from index 0, decreasing string length by 1 at each iteration
    :param string: the string whose instances are to be found
    :return: Tuple
    """
    for a in range(len(string), 0, -1):
        yield (string[:a], string)


def main():

    print("Tree 2:")
    R2 = RadixTree()
    words = ["the", "a", "there", "these", "an"]
    start_=time.time_ns()
    for word in words:
        R2.insert(R2.root, word)
    print(time.time_ns()-start_)
    R2.count(R2.root, "")
    print(count1)
    str = input("enter")
    start=time.time_ns()
    R2.print_tree(R2.root, "",str)
    stop=time.time_ns()

    print(count1)


if __name__ == '__main__':
    main()