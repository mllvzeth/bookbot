
def get_number_of_words(text):
  words = text.split()
  return len(words)

def char_frequency_map(text):
  frequency_map = {}
  for char in text:
    if char.isalpha():
      char = char.lower()
      if char in frequency_map:
        frequency_map[char] += 1
      else:
        frequency_map[char] = 1
    else:
      if char in frequency_map:
        frequency_map[char] += 1
      else:
        frequency_map[char] = 1
  return frequency_map

def sorted_list(frequency_map):
  sorted_list = []
  sorted_list = sorted(frequency_map.items(), key=lambda item: item[1], reverse=True)
  return sorted_list

def display_sorted_list(sorted_list):
  for char, count in sorted_list:
    print(f"{char}: {count}")
