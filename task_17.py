import num2words


def len_of_written_words(n):

    list_of_words = []

    for i in range(1,n+1):
        list_of_words.append(num2words.num2words(i))

    l = "".join(list_of_words)

    l = l.replace(" ", "")
    l = l.replace("-", "")

    return(len(l))

print(len_of_written_words(1000))