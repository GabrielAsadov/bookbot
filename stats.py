def get_book_text(x):
        with open(x) as f:
                book_contents = f.read()
                return book_contents

def count_words(x):
        y = get_book_text(x)
        words = y.split()
        amount = len(words)
        return amount
def count_letters(x):
	y = get_book_text(x)
	z = y.lower()
	d = {}
	for i in z:
		d[i] = d.get(i,0)+1
	return d
def sort_by_count(list):
	return list["num"]
def sort_letters(x):
	dict_list = []
	for char, num in x.items():
		dict_list.append({"char" : char , "num" : num})
	dict_list.sort(reverse=True , key = sort_by_count)
	return dict_list 
