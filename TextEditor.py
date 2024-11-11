from collections import Counter
main_text = 'TS.txt'

#function to read the file and store its contents in a variable
def read_text():
        with open(main_text, 'r') as file:
            text = file.read()
        return text

#function to save the text back to the file after making changes
def save_text(text):
    try:
        with open(main_text, 'w') as file:
            file.write(text)
        print('Changes saved to file.')
    except IOError:
        print('Error: Unable to save the file.')

#define all the functions first, the main loop with the menu input should come last


def allwordcount(text):
    # split text into words, converting all to lowercase to count correctly
    words = text.lower().split()
    # count frequency of each word
    word_counts = Counter(words)
    # 5 most common
    most_common = word_counts.most_common(5)

    print('Top 5 most common words:')
    for word, count in most_common:
        print(f'{word}: {count}')

def singlewordcount(text):
    # ensure its a single word
    single_word = input('Enter a word:').strip().lower()

    if " " in single_word:
         print('Please enter a single word, no spaces allowed.')
         return

    words = text.lower().split()
    word_count = words.count(single_word)

    print(f"The word '{single_word}' appears '{word_count}' times.")

def replaceword(text):
    replaceword1 = input('Enter a word you want to replace:').strip().lower()
    replaceword2 = input('Enter a word you want to put in place of the word you chose:').strip()

    #number of words changed
    count_replacements = text.lower().count(replaceword1)

    #replace the word in the text
    updated_text = text.replace(replaceword1, replaceword2)
    print(f"The word '{replaceword1}' was replaced '{count_replacements}' times with '{replaceword2}'.")

    return updated_text


def addtext(text):
    add_text = input('Enter text you wish to add:').strip()

    #open file in append mode and write additional text
    with open('TS.txt', 'a') as file:
        file.write(add_text + '\n')
    #appends the new content to the text variable in memory, so it stays consistent with what’s in the file
    text += '\n' + add_text

    print(f"{add_text}' was added to the file")
    return text

def deletetext(text):
    delete_text = input('Enter the word you want to delete from the text:').strip()
    #make sure word is in text in a case sensitive way
    if delete_text.lower() in text.lower():
        text = text.replace(delete_text, '',1)
        print(f"The first instance of '{delete_text}' has been deleted.")
    else:
        print('Sorry! That word was not found in the text, choose another word.')
    return text

def highlighttext(text):
    high_text = input('Enter a word you want to see highlighted in the text:').strip()

    if high_text.lower() in text.lower():
        text = text.replace(high_text, f'**{high_text}**')
        print(f'All instances of "{high_text}" have been highlighted.')
    else:
        print('Sorry! That word was not found in the text, enter a new word.')
    return text

#main function to run the menu loop
def main():
    text = read_text() #read the text from the file
    #display menu options
    print('\nText Editor Menu;')
    print('1. Top 5 most common words')
    print('2. Single Word Frequency')
    print('3. Replace a Word')
    print('4. Add Text')
    print('5. Delete Text')
    print('6. Highlight Text')

    #get user choice
    choice = input('Enter your choice: ').strip()

    if choice == '1':
        allwordcount(text) # call the fucntion w/o ressigning it
    elif choice == '2':
        singlewordcount(text) # calls fucntion w/o reassigning it
    elif choice == '3':
        text = replaceword(text) #reasign
    elif choice == '4':
        text = addtext(text) #rassign
    elif choice == '5':
        text = deletetext(text) #reassign
    elif choice == '6':
        text = highlighttext(text) #reassign
    save_text(text) #save the final result back to the file

if __name__ == '__main__':
    main()
