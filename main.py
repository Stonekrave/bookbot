

def main():
  #variable that will hold the location of the text
  book_path = "books/frankenstein.txt"
  #call the read_book function, passes it the path variable,
  #  and sets it equal to a variable
  text = read_book(book_path)


  #calls the count_word function and passes in the text variable
  words = count_words(text)

  #calls the count_letters function and passes in the text variable
  letters = count_letters(text)

  #calls the get_report function and passes in the words and letters variables
  report = get_report(words, letters)

  #prints the final report to console
  print(report)

#creates a function that will read the desired text
#takes the book path as a parameter
def read_book(book_path):
  #opens the text and sets the contents to f
  with open(book_path) as f:
    #reads the contents and sets the contents equal to variable
    file_contents = f.read()
    #return the contents of the text file to the eagerly awaiting variable
    return file_contents

#create a funtion that will count the number of words in the text file
#takes the text variable as a parameter
def count_words(text):
  #splits the text at the default(space) and creates a list containing every word in the text
  words = text.split()
  #returns the length of the  just created list
  return len(words)

#create a function to count the individual letters within the text
#takes the text variable as a parameter
def count_letters(text):
  #uses the lower() method to make sure that all characters are lowercase
  non_duplicate_letters = text.lower()
  #create an empty dictionary to hold the char:count information
  letters_dict = {}
  # for loop will peruse each individual letter in the newly lowered text
  for letter in non_duplicate_letters:
    #if statement will check to see if the current letter already resides in the letters_dict dictionary
    if letter in letters_dict:
      #if the letter is already present, its count will increase by 1
      letters_dict[letter] += 1
    else:
      #if the character is not present, it will receive an initial count
      letters_dict[letter] = 1
  #return the letters dictionary now containing the letters and their respective counts
  return letters_dict

#create a function that will deliver a final report of the findings
#the words and letters variables will be used as paramenters
def get_report(words, letters):
  #create an empty string to hold printable output
  chars_data = ""
  #create an empty list for sorting purposes
  sorted_list = []
  #loop through the letters(which are now contained in the letters_dict dictionary)
  for letter in letters:
    #logic to remove any character that is not a "letter"
    #any time there is a non-char, the logic will continue to the next part
    if not letter.isalpha():
      continue
    #if it is truely a letter, it will be appended to the sorted_list created above
    sorted_list.append(letters[letter])
  #the sorted list will now be actually sorted in reverse
  sorted_list.sort(reverse=True)

  # a for loop will go though the sorted list 
  for char_count in sorted_list:
    #for loop looking at the key:value pairs within the letters dictionary
    for key, value in letters.items():
      #when the value is equal to the character count
      if value == char_count:
        #the key will be set equal to the char variable
        char = key
        #this char_data string will hold the textual information regarding characters and thier wounts
        char_data = f"The {char} character was found {char_count} times\n"
        #the newly created char_data will be added(concatenated) to the previously created empty string
        chars_data += char_data
  
  #the final return will provide the printable format of the report
  return f"---Begin report of books/frankenstein.txt---\n {words} Total words found in the book\n\n{chars_data}---End Report---"
      

main()