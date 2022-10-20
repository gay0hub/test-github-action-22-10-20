


import sys

if __name__ == '__main__':
    with open('tmp-out.txt',"w",encoding="utf8") as outf:
        for i in range(len(sys.argv)):
            print(i,sys.argv[i])
            outf.write(f"{i},{sys.argv[i]}\n")
