import webbrowser
from googlesearch import search
from urllib.parse import quote_plus
from colorama import init, Fore, Style
import pyfiglet
import texttable

# Copyright © 2023 4K3YM4L
# https://github.com/4K3YM4L
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this script and associated documentation files (the "Script"), to deal
#in the Script without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Script, and to permit persons to whom the Script is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Script.

#THE SCRIPT IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SCRIPT OR THE USE OR OTHER DEALINGS IN
#THE SCRIPT.

text = pyfiglet.figlet_format("WizDork", font="Banner3")
init()
print(text)
# Define the table object
table = texttable.Texttable()
init()
print(Fore.MAGENTA + '')
# Set the table properties
table.set_cols_width([15,90])
table.set_deco(texttable.Texttable.HEADER)
table.header(["Google Dork", "Description"])
# Define the filters to use in the query
# Print the table
print(table.draw())

# Initialize colorama
init()

# Print the text with colored and bold text
print(Fore.RED + Style.BRIGHT + "allintext       : " + Style.RESET_ALL + "Searches for pages that contain all the keywords specified in the text of the page")

print(Fore.RED + Style.BRIGHT + "intext          : " + Style.RESET_ALL + "Searches for pages that contain any of the keywords specified in the text of the page")

print(Fore.RED + Style.BRIGHT + "inurl           : " + Style.RESET_ALL + "Searches for pages that have the search term in their URL")

print(Fore.RED + Style.BRIGHT + "allinurl        : " + Style.RESET_ALL + "Searches for pages that contain all the keywords specified in their URL")

print(Fore.RED + Style.BRIGHT + "intitle         : " + Style.RESET_ALL + "Searches for pages that have the search term in their title")

print(Fore.RED + Style.BRIGHT + "allintitle      : " + Style.RESET_ALL + "Searches for pages that contain all the keywords specified in their title")

print(Fore.RED + Style.BRIGHT + "site            : " + Style.RESET_ALL + "Searches for pages that are part of a specific website or domain")

print(Fore.RED + Style.BRIGHT + "filetype        : " + Style.RESET_ALL + "Searches for pages that have a specific file type")

print(Fore.RED + Style.BRIGHT + "link            : " + Style.RESET_ALL + "Searches for pages that link to a specific URL")

print(Fore.RED + Style.BRIGHT + "numrange        : " + Style.RESET_ALL + "Searches for pages that have a number in a specific range")

print(Fore.RED + Style.BRIGHT + "before          : " + Style.RESET_ALL + "Searches for pages that were indexed by Google before a specific date")

print(Fore.RED + Style.BRIGHT + "after           : " + Style.RESET_ALL + "Searches for pages that were indexed by Google after a specific date")

print(Fore.RED + Style.BRIGHT + "allinanchor     : " + Style.RESET_ALL + "Searches for pages that contain all the keywords specified in anchor text of links to the page")

print(Fore.RED + Style.BRIGHT + "inanchor        : " + Style.RESET_ALL + "Searches for pages that contain any of the keywords specified in anchor text of links to the page")

print(Fore.RED + Style.BRIGHT + "allinpostauthor : " + Style.RESET_ALL + "Searches for pages that are authored by a specific person and contain all the keywords specified")

print(Fore.RED + Style.BRIGHT + "inpostauthor    : " + Style.RESET_ALL + "Searches for pages that are authored by a specific person and contain any of the keywords specified")

print(Fore.RED + Style.BRIGHT + "related         : " + Style.RESET_ALL + "Searches for pages that are similar to a specific URL")

print(Fore.RED + Style.BRIGHT + "cache           : " + Style.RESET_ALL + "Displays Google's cached version of a specific URL")

print(Fore.RED + Style.BRIGHT + "info            : " + Style.RESET_ALL + "Displays information about a specific search term")

print(Fore.RED + Style.BRIGHT + "define          : " + Style.RESET_ALL + "Displays the definition of a word or phrase")

print(Fore.RED + Style.BRIGHT + "stocks          : " + Style.RESET_ALL + "Displays information about stocks and financial markets")

print(Fore.RED + Style.BRIGHT + "map             : " + Style.RESET_ALL + "Displays a map of a specific location")

print(Fore.RED + Style.BRIGHT + "movie           : " + Style.RESET_ALL + "Displays information about movies")

print(Fore.RED + Style.BRIGHT + "weather         : " + Style.RESET_ALL + "Displays current and forecasted weather conditions")

print(Fore.RED + Style.BRIGHT + "book            : " + Style.RESET_ALL + "Searches for books on Google Books")

print(Fore.RED + Style.BRIGHT + "time            : " + Style.RESET_ALL + "Displays the current time in a specific location")

print(Fore.RED + Style.BRIGHT + "phonebook       : " + Style.RESET_ALL + "Searches for phone numbers and addresses on Google")

print(Fore.RED + Style.BRIGHT + "phone           : " + Style.RESET_ALL + "Searches for information about a specific phone number")


filters = {
    "allintext": "allintext:",
    "intext": "intext:" ,
    "inurl": "inurl:",
    "allinurl": "allinurl:",
    "intitle": "intitle:",
    "allintitle": "allintitle:",
    "site": "site:",
    "filetype": "filetype:",
    "link": "link:",
    "numrange": "numrange:",
    "before": "before:",
    "after": "after:",
    "allinanchor": "allinanchor:",
    "inanchor": "inanchor:",
    "allinpostauthor": "allinpostauthor:",
    "inpostauthor": "inpostauthor:",
    "related": "related:",
    "cache": "cache:",
    "info": "info:",
    "define": "define:",
    "stocks": "stocks:",
    "map": "map:",
    "movie": "movie:",
    "weather": "weather:",
    "book": "book:",
    "time": "time:",
    "phonebook": "phonebook:",
    "phone": "phone:"
}
# Define the math and operator to use in the query
math_dict = {
    "greater than": ">",
    "less than": "<",
    "equal to": "=",
    "not equal to": "!=",
    "greater than or equal to": ">=",
    "less than or equal to": "<=",
}
operator_dict = {
    "and": "AND",
    "or": "OR",
    "not": "NOT",
    "xor": "XOR",
    "nand": "NAND",
    "nor": "NOR",
}

# Prompt the user for the filters to use
filter_input = input("Enter filter(s) name to use  - choose multiple filters by separating them with commas: ")

# Build the query string
query = ""
for f in filter_input.split(","):
    if f.strip() in filters:
        dork = input(f"Enter the search term for {f.strip()}: ")
        query += filters[f.strip()] + quote_plus(dork) + " "
        math = input(f"Do you want to use math operators for {f.strip()}? (y/n): ")
        if math.lower() == "y":
            math_op = input("Enter the math operator (greater than, less than, equal to, not equal to, greater than or equal to, or less than or equal to): ")
            num = input("Enter the number to compare the search term with: ")
            query += math_dict[math_op.lower()] + num + " "
        op = input(f"Do you want to use a logical operator for {f.strip()}? (y/n): ")
        if op.lower() == "y":
            log_op = input("Enter the logical operator (and, or, not, xor, nand, or nor): ")
            query += operator_dict[log_op.lower()] + " "
            manual_text = input("Enter anything you want: ")
            query += manual_text.strip() + " "
    else:
        query += f.strip() + " "
query = quote_plus(query)

# Perform the search and open the browser window
search_url = f"https://www.google.com/search?q={query}"
webbrowser.open_new_tab(search_url)
