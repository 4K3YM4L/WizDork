# WizDork
WizDork is a Python script that automates Google dorking by allowing you to quickly filter and search for specific pages using various search operators.

With WizDork, you can easily search for pages that contain specific keywords, are part of a specific website or domain, have a specific file type, link to a specific URL, and much more. The script also allows you to display Google's cached version of a specific URL, view information about a specific search term, and even get the definition of a word or phrase.

To use WizDork, simply run the script in your terminal, select the filter you want to use, and enter the search term. The script will then open a new tab in your default browser and display the search results.

Feel free to modify and improve upon the script to fit your needs. If you have any questions, issues, or suggestions, please don't hesitate to open an issue or submit a pull request.

## Installation
```
git clone https://github.com/4K3YM4L/WizDork.git
cd WizDork
pip install -r requirements.txt
python wizdork.py
```
## Usage

**Enter filter(s) name to use - choose multiple filters by separating them with commas:**

```You can enter one or more filter names, separated by commas. For example, you could enter `intext` to use only the intext filter, or `intext,filetype` to use both the Intext and Filetype filters.```

You can use the following text to describe the usage of the Math and Logical operators in this tool:

**Math Operators:**
```
"not equal to": "!="
"greater than or equal to": ">="
"less than or equal to": "<="
```
**Logical Operators:**
```
"not": "NOT"
"xor": "XOR"
"nand": "NAND"
"nor": "NOR"
```
These operators can be used in combination with filters to create complex search queries. For example, you can use the ">=" operator to search for results greater than or equal to a certain value, or you can use the "NOT" operator to exclude certain results from your search. The "XOR", "NAND", and "NOR" operators can be used for more advanced logical operations.
