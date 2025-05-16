import sys
from stats import get_number_of_words, char_frequency_map, sorted_list, display_sorted_list

def get_book_text(file_path):
  with open(file_path, 'r') as file:
    text = file.read()
  return text


def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_path = sys.argv[1]

  book_text = get_book_text(book_path)
  print(f"============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}...")
  word_count = get_number_of_words(book_text)
  print(f"----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print(f"--------- Character Count -------")
  frequency_map = char_frequency_map(book_text)
  display_sorted_list(sorted_list(frequency_map))
if __name__ == "__main__":
  main()  