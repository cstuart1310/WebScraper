import urllib.request #Used to grab the html
import io #Used to mess with files with weird encoding
import time #Delays


foundCount=0
foundLinks=[]
errorLinks=[]
searchPhrases=[]
phraseMode="or"

def find(siteURL):
   with io.open('site.txt', "r", encoding="utf-8") as file:#Reads the file
        for line in file:#Checks every line
            for searchPhrase in searchPhrases:
                searchPhraseIndex=searchPhrases.index(searchPhrase)
                #print("phrase index",searchPhraseIndex)
                if searchPhrase in line:
                    print("------------------------------\nFound",searchPhrase, "at",siteURL)
                    print(line,"\n------------------------------")
                    foundLinks.append([searchPhrase,siteURL,line])


def scrape(siteURL):
    #Gets html
    try:
        with urllib.request.urlopen(siteURL) as url: #"Opens" URL (Gets data)
            site = url.read() #Reads the html code
    #      file = open('site.txt','w')#Opens the output file
            site=site.decode("utf-8")#Decodes the site
            with io.open('site.txt', "w", encoding="utf-8") as file:#Writes the site to a file
                file.write(site)
    except (urllib.error.HTTPError, ValueError):#Error handling for invalid links
        print("Page does not exist!",siteURL)
        errorLinks.append(siteURL)#Adds to array to tell user broken links at end of program


def printLinks(foundLinks):#Prints the found data nicely
    for searchPhrase in searchPhrases:
        print("----------------")
        print("Links containing",searchPhrase)
        alreadyPrinted=[]#Used to prevent printing the same link multiple times if multiple phrase uses have been found
        for foundArray in foundLinks:
            if foundArray[0]==searchPhrase and foundArray[1] not in alreadyPrinted:#Checks if array piece has the right phrase and if the link has already been printed
                if printURL==True:
                    print(foundArray[1])
                if printLine==True:
                    print(foundArray[2],"\n")
        if printNotFound==True:
            print("\nLinks not containing",searchPhrase)
            for link in links:
                if link not in foundArray:
                    print(link)
#Main


#intro
print("\n"*100)
print("Site finder")
print("This program will look through the HTML of a given page(s) for a certain thing")

#Input search phrases
searchPhraseNo=int(input("Number of search phrases:"))
for searchPhraseCounter in range(0,searchPhraseNo):
    toFind=input("Input phrase to look for:")
    searchPhrases.append(toFind)
    foundLinks.append(toFind)

linkFile=open("links.txt","r")#Opens link file
links = [link.rstrip() for link in linkFile]#Gets links from file without trailing \n
linkFile.close()#Closes the link file for memory conservation
linksLength=len(links)#Stored as a variable for convenience

print("Print a list of URLs where the search phrase was NOT found? y/n")
printNotFound=input(">")
if printNotFound=="y":
    printNotFound=True
else:
    printNotFound=False

print("Print the line of HTML containing the search phrase? y/n/only (Only the line and not the URL)")
printLine=input(">")
if printLine=="y":
    printLine=True
    printURL=True
elif printLine=="only":
    printLine=True
    printURL=False
else:
    printLine=False
    printURL=True

print("Found",linksLength,"links to look through")
print("This might take a while, begin? y/n (CTRL + C to quit)")
continueInp=input(">")

if continueInp=="y":
    print("---------------")
    siteIndex=0
    for siteURL in links:#Iterates through each URL in the file
        siteIndex+=1#Counter of no of sites checked
        scrape(siteURL)#Gets HTML as plain text
        print("Read HTML for site",siteURL,siteIndex,"/",linksLength)
        find(siteURL)#Looks for phrase in HTML
    
    print("-----Done scraping!-----")
    #Post search
    print("URLS containing set phrase:")
    printLinks(foundLinks)#Prints found data in human readable format

    
    if len(errorLinks)>0:#If there is at least one link that didn't load
        print("-----Links that errored for some reason-----")
        for link in errorLinks:
            print(link)


#Quit
elif continueInp=="n":
    print("Quitting")

else:
    print("Invalid input")