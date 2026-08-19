'''
Basic Regular Expression (Regex) Tutorial

    Main Steps:
    1. re.compile() - Compile a regex pattern into a regex object

    2a. re.search() - Search for a pattern in a string
    2b. re.match() - Match a pattern at the beginning of a string
    2c. re.findall() - Find all occurrences of a pattern in a string
    2d. re.finditer() - Find all occurrences of a pattern in a string and return an iterator
    2e. re.sub() - Replace occurrences of a pattern in a string with a specified replacement

    3. mo.group() - Get the matched string from a match object
'''
import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())

'''
\d - Matches any digit (0-9)
\D - Matches any non-digit character
\w - Matches any word character (alphanumeric or underscore)
\W - Matches any non-word character
\s - Matches any whitespace character
\S - Matches any non-whitespace character
\. \^ \$ \* \+ \? \{ \} \[ \] \( \) - literal characters that need to be escaped
* - Matches 0 or more occurrences of the preceding character or group
+ - Matches 1 or more occurrences of the preceding character or group
? - Matches 0 or 1 occurrence of the preceding character or group
| - Acts as a logical OR between two patterns
{} - Matches a specific number of occurrences of the preceding character or group
'''