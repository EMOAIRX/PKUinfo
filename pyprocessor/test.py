import re

# 示例字符串
input_string = "Some text with a date and time: 2023-09-18 15:30:45"
pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'
match = re.search(pattern, input_string)

if match:
    extracted_datetime = match.group(1)
    print("Extracted datetime:", extracted_datetime)
else:
    print("No datetime found in the input string.")
