# def file_read(fname):
#     txt=open(fname)
#     print(txt.read())

#file_read('test.txt')

def file_read(fname):
    with open(fname) as f:
        content_list=f.readlines()
        print(content_list)
file_read('test.txt')
