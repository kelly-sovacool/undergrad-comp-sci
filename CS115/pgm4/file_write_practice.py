def main():
    # don't use tilde in filepath
    file = open('/Users/Kelly/Desktop/basic_file_write.txt', 'w')
    file.write('0\n1\n2\n3\n4\n5')
    file.close()
main()