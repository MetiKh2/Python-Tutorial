def file_length(filename):
    with open(filename) as f:
        for i,l in enumerate(f):
            pass
        return i+1
print('Number if lines in the file :',file_length('test.txt'))

def longest_word(filename):
    with open(filename) as infile:
        words=infile.read().split()
    max_len=len(max(words,key=len))
    return [word for word in words if len(word)==max_len]
print(longest_word('test.txt'))
