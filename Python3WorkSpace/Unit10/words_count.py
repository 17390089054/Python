
def count_words(filename):
    try:
        with open(filename) as file:
            contents=file.read()
    except FileNotFoundError:
        #pass 代表什么都不要做
        print("Sorry, the file "+filename+" done not exist!")
    else:
        #计算文件大致包含多少个单词
        words=contents.split()
        num_words=len(words)
        print("The file "+filename+" has about "+str(num_words)+" words.")

filename="alice.txt"       
count_words(filename)
