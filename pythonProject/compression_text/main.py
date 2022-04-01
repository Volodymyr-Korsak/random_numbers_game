def choice():
    question = int(input("To compress text, enter: 1\n"
                     "To decompress text, enter 2\n"))
    if question == 1:
        compression_text()
    elif question == 2:
        de_compression_text()
    else:
        print("You entered the wrong value\nhave a cup of coffee and try again")

def compression_text():
    text = input("enter text to compress: ")
    tmp,res,counter= text[0],'',1
    for i in text[1:]+"#":
        if i == tmp:
            counter += 1
        else:
            if counter == 1:
                res += tmp
            else:
                res += str(counter) + tmp
            counter = 1
        tmp = i
    print(res)

def de_compression_text():
    cod = input("enter text to compress: ")
    res,tmp = '',''
    for i in cod:
        if i.isdigit():
            tmp += i
        else:
            if tmp:
                res += int(tmp) * i
                tmp = ''
            else:
                res += i
    print(res)

if __name__ == '__main__':
    choice()

