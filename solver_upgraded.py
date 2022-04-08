words = []
with open("wordlist.txt") as object:
    for line in object:
        words.append(line.strip())
def play_wordle(words):#:
    while len(words) > 1:
        letters_in_word = []
        word_from_user = input("word :-")
        color_pattern = input("pattern:-")
        for position in range(5):
            letter = word_from_user[position].lower()
            color = color_pattern[position].lower() #green, yellow, or black
            words_to_remove = []
            for word in words:
                if color == 'g':
                    if word[position] != letter:
                        words_to_remove.append(word)
                        if letter not in letters_in_word:
                            letters_in_word.append(letter)
                elif color == 'y':
                    if letter not in word:
                        words_to_remove.append(word)
                    elif word[position] == letter:
                        words_to_remove.append(word)
                    if letter not in letters_in_word:
                        letters_in_word.append(letter)
                elif color == 'b':
                    if letter in word:
                        if letter not in letters_in_word:
                            words_to_remove.append(word)
                        elif words[position] == letter:
                            words_to_remove.append(word)
            for word in words_to_remove:
                words.remove(word)
        print(words)
        print("Best suggestions:-" , words[0:5])
        guess = input("Did you guess correctly (Y/N)?: ").lower()
        if guess == 'y':
            print("You win")
            return
play_wordle(words)