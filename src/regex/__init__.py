import re

# ================================================================
# Example 1: Using `re.findall()`
# ================================================================
# `re.findall()` returns all matches of a pattern in the string as a list.
text = "The cost is 100 dollars, and the discount is 20 dollars."
pattern = r"\d+"  # Matches one or more digits

matches = re.findall(pattern, text)
print("FindAll Example:", matches)  # Output: ['100', '20']

# ================================================================
# Example 2: Using `re.search()`
# ================================================================
# `re.search()` searches for the first match of the pattern anywhere in the string.
text = "The cost is 100 dollars."
pattern = r"\d+"  # Matches one or more digits

search_result = re.search(pattern, text)
if search_result:
    print("Search Example: Match found:", search_result.group())  # Output: 100
else:
    print("Search Example: No Match")

# ================================================================
# Example 3: Using `re.match()`
# ================================================================
# `re.match()` checks for a match only at the start of the string.
text = "100 dollars is the cost."
pattern = r"\d+"  # Matches one or more digits

match_result = re.match(pattern, text)
if match_result:
    print("Match Example: Match found:", match_result.group())  # Output: 100
else:
    print("Match Example: No Match")

# ================================================================
# Example 4: Using `re.split()`
# ================================================================
# `re.split()` splits the string wherever the pattern matches.
text = "apple,banana;cherry orange"
pattern = r"[,; ]"  # Matches commas, semicolons, or spaces

split_result = re.split(pattern, text)
print("Split Example:", split_result)  # Output: ['apple', 'banana', 'cherry', 'orange']

# ================================================================
# Example 5: Using `re.sub()`
# ================================================================
# `re.sub()` replaces matches of the pattern with a specified string.
text = "Contact us at 123-456-7890 or 987-654-3210."
pattern = r"\d{3}-\d{3}-\d{4}"  # Matches phone numbers in the format xxx-xxx-xxxx
replacement = "XXX-XXX-XXXX"

sub_result = re.sub(pattern, replacement, text)
print("Sub Example:", sub_result)  # Output: "Contact us at XXX-XXX-XXXX or XXX-XXX-XXXX."

# ================================================================
# Additional Notes:
# 1. Regular expressions are powerful but require careful pattern design.
# 2. Use tools like https://regex101.com/ for testing and debugging regex patterns.
# 3. Refer to the Python `re` module documentation for advanced usage.
