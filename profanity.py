import urllib

__author__ = 'adam.mulroy'


def read_textfile(filepath):
    output = open(filepath)
    content = output.read()
    output.close()
    check_profanity(content)


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    connection.close()
    if 'true' in output:
        print("Profanity found.")
    elif "false" in output:
        print("No profanity found.")
    else:
        print("Output variable empty.")

path = r'C:\Users\adam\PycharmProjects\Udacity\Resources\movie_quotes.txt'
read_textfile(path)
