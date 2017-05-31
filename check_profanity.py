import urllib
#from urllib.request import urlopen
def read_text():
    quotes = open("E:\learning\python\open.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    conn = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = conn.read()
    #print(output)
    conn.close()
    if "true" in output:
        print("Profanity Alert")
    elif "false" in output:
        print("this document has no curse words!")
    else:
        print("Could not scan the document properly")
    

read_text()
    
