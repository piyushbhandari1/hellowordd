def replace_word ():
    str = input("Enter text here: ")

    word_to_replace = input("Please enter the word you want to replace : ")
    word_replacement = input("Please enter the word you want to replace it with : ")
    print(str.replace(word_to_replace,word_replacement))

replace_word()