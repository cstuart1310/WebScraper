# WebScraper
This script scrapes through a list of websites and returns all uses of a defined search term(s) within the site's raw HTML.

This was extremely useful when performing web development on the Birmingham City University HELS pages, as it allowed me to search for issues across the entire site.

To use:
Input all of the URL's that you want to search through into the links.txt file.
Run the script.
Input the number of search phrases that you would like to use.
Input whether you want a list of sites NOT containing the search phrase(s) to be displayed.
Input whether you would like the line containing the search term to be printed (Useful if you are looking for variations of a similar line)
Confirm the search

The output is in a format which can be copied and pasted into a spreadsheet software such as Excel. (Auto-exporting to a .csv is a potential future feature)

WARNING
This script automatically opens all of the sites inputted sequentially. This may result in your access to a page being throttled or even entirely blocked temporarily based on their DDOS protection.
