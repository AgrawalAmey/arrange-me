from bs4 import BeautifulSoup

def cleanme(html):
    soup = BeautifulSoup(html,"lxml") # create a new bs4 object from the html data loaded
    for script in soup(["script", "style"]): # remove all javascript and stylesheet code
        script.extract()
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text

testhtml = "<!DOCTYPE HTML>\n<head>\n<title>THIS IS AN EXAMPLE </title><style>.call {font-family:Arial;}</style><script>getit</script><body>I need this text captured<h1>And this</h1></body>"
testhtml2 = "<!DOCTYPE HTML>\n<head>\n<title>THIS IS AN EXAMPLE </title><style>.call {font-family:Arial;}</style><script>getit</script><body>I need this text captured WOAH<h1>And this</h1></body>"
array=[testhtml,testhtml2]
print(array)
cleaned=[]
length=len(array)
for i in range(0,length):
    cleaned.append(cleanme(array[i]))
print (cleaned)
