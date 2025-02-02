This is a flash card project that tests if User knows a list French words.

Input - a excel list of french word and their english word counterpart.

When  user runs program for first time, the input excel is loaded into a word list using Pandas. A French word is randomly picked from this list. Using Tkinter, the word is displayed on screen for 4 seconds and then 'flipped' to display the English word.

User than clicks 'tick' or 'cross' to indicate whether if they understand the French word:
- If user does not know the word, a new word will be picked-
- If User knows the French word, the word is removed from the word list. The word list containing words that user doesn't know is outputted into a new excel file for studying.

When the user runs the program again, program will load up the studying excel to test user.
