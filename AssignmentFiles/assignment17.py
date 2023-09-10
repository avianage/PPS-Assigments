
# To count total characters in file, total words in file, total lines in file and 
# frequency of given word in file.

file = input("\nEnter File Name: ")

search = input("Enter Word to be Searched for Frequency: ")

def file_stats(file, search):
    try:
        with open(file, 'r') as file_read:
            content = file_read.read()

        total_char = len(content)
        words = content.split()
        total_word = len(words)
        total_line = content.count('.')
        word_freq = words.count(search) 

        return total_char, total_word,  total_line, word_freq

    except FileNotFoundError:
        print("\nInput File Not Found.")
        return -1, -1, -1, -1

    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        return -1, -1, -1, -1
    
chars, words, lines, freq = file_stats(file, search)

print(f"\nTotal characters in the file: {chars}.")
print(f"Total words in the file: {words}.")
print(f"Total lines in the file: {lines}.")
print(f"Frequency of the word '{search}': {freq}.\n")
