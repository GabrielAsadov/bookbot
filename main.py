import sys
from stats import count_letters
from stats import sort_letters
from stats import count_words
# ... imports and get_book_text function (though get_book_text is not needed in main if count_letters uses it internally)


def main():
	if len(sys.argv) != 2:
		print ("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
# 1. Get the total word count and print it
	book_length = count_words(sys.argv[1])
	print (book_length , "words found in the document")

        	# 2. Call count_letters and CAPTURE its return value (the dictionary of counts)
        	#    Let's put it into a variable called 'char_counts_dict'
	char_counts_dict = count_letters(sys.argv[1])

        	# 3. Now, call sort_letters and pass it the 'char_counts_dict' variable.
        	#    CAPTURING its return value (the sorted list of dictionaries)
        	#    Let's put it into a variable called 'sorted_char_list'
	sorted_char_list = sort_letters(char_counts_dict)

        	# 4. Finally, print the 'sorted_char_list'
	print ( "============ BOOKBOT ============")
	print(f"Analyzing book found at {sys.argv[1]}...")
	print("----------- Word Count ----------")
	print(f"Found {book_length} total words")
	print("--------- Character Count -------")
	for item in sorted_char_list:
		if item["char"].isalpha():
			print(f"{item['char']}: {item['num']}")
	print("============= END ===============" ) # You'll format this printing later for the report
main()
