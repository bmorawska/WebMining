import re


# Function to remove the HTML tags
# from the given tags
def RemoveHTMLTags(strr):
    # Print string after removing tags
    return re.compile(r'<[^>]+>').sub('', strr)


# Driver code
if __name__ == '__main__':
    # Given String
    file = 'logi_ftims.txt'
    html = open(file, 'r').read()

    # Function call to print the HTML
    # string after removing tags
    r = RemoveHTMLTags(html)
    f = open("aa.txt", "w")
    f.write(r)
    f.close()

    b = open("aa.txt", "r")
    lines = b.readlines()
    g = open("plain_logs.txt", "w")
    for line in lines:
        if line[0] == '/' and line[1] == '/':
            continue
        if line.replace(' ', '').replace(r'//', '')[0] == '\n':
            continue
        if 'jQuery' in line or 'carousel' in line:
            continue
        if '/**' in line or '});' in line:
            continue

        line = line.strip()
        line = line + '\n'
        print(line)
        g.write(line)

    f.close()
