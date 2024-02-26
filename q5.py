def print_words(file_name):
    """"
    :param file_name: the file name
    :return: the number of words that satisfy these conditions
    """
    punctuation = ",.!?'\n\t"
    number_of_words = 0
    with open(file_name, "r") as file:
        for line in file:
            for p in punctuation:
                line = line.replace(p,"")
            words = line.split(" ")
            for word in words:
                if (word.startswith('un') or word.startswith("Un")) and (word.endswith("an") or word.endswith("An")):
                    number_of_words +=1
        print(number_of_words)

print(print_words("/Users/valentinasierragarzon/PycharmProjects/session11/midterm/un"))