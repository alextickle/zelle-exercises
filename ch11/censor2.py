#censor.py
import string

def main():
        filename = raw_input("Enter the filename of the doc to censor: ")
        filenamecurses = raw_input("Enter the filename where the curses are stored: ")
        outfilename = raw_input("Enter the outfile name: ")
        infile = open(filename, 'r')
        infilec = open(filenamecurses, 'r')
        lines = []
        linesc = []
        words = []
        censored = []
        curses = []
        for line in infilec:
                linesc.append(line)
        infilec.close()
        for line in infile:
                lines.append(line)
        infile.close()
        for w in linesc:
                curses = curses + string.split(w)
        for w in lines:
                words = words + string.split(w)
        censored = words
        count = 0
        for word in censored:
                if (word in curses):
                        cword = ""
                        for i in range(len(word)):
                                cword = cword + "*"
                        censored[count] = cword
                count = count + 1
        outfile = open(outfilename, 'w')
        wpl = 0
        for i in censored:
                outfile.write(" %s " % (i))
                wpl = wpl + 1
                if wpl % 8 == 0:
                        outfile.write("\n")
			
			

main()
