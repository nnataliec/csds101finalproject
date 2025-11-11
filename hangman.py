import random
wordlist = ['man', 'woman', 'child', 'teacher', 'doctor', 'student', 'friend', 'mother', 'father', 'artist', 'manager', 'soldier', 'chef', 'school', 'park', 'city', 'village', 'country', 'home', 'office', 'garden', 'street', 'river', 'ocean', 'airport', 'library', 'book', 'car', 'computer', 'phone', 'table', 'chair', 'door', 'window', 'bottle', 'mirror', 'jacket', 'lamp', 'apple', 'water', 'music', 'air', 'dog', 'cat', 'elephant', 'bird', 'snake', 'love', 'happiness', 'anger', 'fear', 'hope', 'time', 'justice', 'science', 'history', 'education', 'information', 'freedom', 'peace', 'research', 'change', 'team', 'family', 'group', 'jury', 'audience', 'army', 'flock', 'basketball', 'toothpaste', 'school bus', 'haircut', 'information', 'water', 'rice', 'air', 'information', 'music', 'knowledge', 'swimming', 'running', 'dancing', 'cooking', 'apple', 'artist', 'air', 'bank', 'car', 'city', 'dog', 'doctor', 'door', 'education', 'egg', 'family', 'fire', 'flower', 'friend', 'game', 'garden', 'hair', 'history', 'home', 'idea', 'justice', 'key', 'library', 'life', 'love', 'machine', 'map', 'money', 'moon', 'mountain', 'movie', 'music', 'name', 'night', 'ocean', 'paper', 'park', 'people', 'phone', 'planet', 'problem', 'queen', 'rain', 'reason', 'research', 'river', 'road', 'room', 'school', 'science', 'shelf', 'shirt', 'silence', 'sky', 'snow', 'song', 'space', 'star', 'story', 'sun', 'system', 'table', 'teacher', 'time', 'town', 'train', 'travel', 'tree', 'voice', 'wall', 'war', 'water', 'way', 'week', 'wind', 'window', 'wood', 'word', 'work', 'world', 'writer', 'year']
current_word = random.choice(wordlist)
guessed_letters = []
correct_guesses = 0
incorrect_guesses = 0
correct_list = []
incorrect_list = []
#Still need to show where in the word each letter is

print('Welcome to Hangman!')
print('The word has ' + '_ ' * len(current_word) + '(' + str(len(current_word)) + ')' + ' letters.')

while incorrect_guesses <= 6: #Game loop
    print('Guess a letter: ')
    letter = input()
    if len(letter) != 1: #If guess is more than one letter
        print('Please enter a single letter.')
        continue

    if guessed_letters.count(letter) != 0: #If letter was already guessed
        print('You already guessed this letter!')
        continue

    if letter in current_word: #Correct letter
        guessed_letters.append(letter)
        correct_list.append(letter)
        print('Correct! You guessed the letter: ' + letter)
        correct_guesses += current_word.count(letter)
        if current_word.count(letter) == 1:
            print('There is one ' + str(letter) + ' in the word.')
        if current_word.count(letter) > 1:
            print('There are ' + str(current_word.count(letter)) + ' ' + str(letter) + '\'s in the word!')
        if len(guessed_letters) > 1:
            print('You have guessed: ' + str(correct_list) + ' correctly.')
        if len(current_word) == correct_guesses: #Win condition
            print('You have won!')
            print('The word was: ' + current_word)
            break

    if letter not in current_word: #Incorrect letter
        guessed_letters.append(letter)
        incorrect_guesses += 1
        incorrect_list.append(letter)
        print('You have guessed ' + str(incorrect_guesses) + ' letter(s) WRONG! You have ' + str(6 - incorrect_guesses) + ' wrong guess(es) left.')
        print('The hangman grows...')
        if len(guessed_letters) > 1:
            print('You have guessed: ' + str(incorrect_list) + ' incorrectly.')
        if incorrect_guesses >= 6: #Lose condition
            print('RIP hangman! Better luck next time...')
            print('The word was: ' + current_word)
            break