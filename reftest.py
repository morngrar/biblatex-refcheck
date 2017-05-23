#!/usr/bin/python3

"""Script for testing BibLaTeX bibliography file for comma-errors.

Takes bibliography-file as input, reports on stdout if the file looks OK or not, and also provides function check_file() which returns True or False respectively, for use in automation of LaTeX compilation.
"""

def check_file(filename):
    i = 0
    fault = False
    with open(filename) as f:
        for line in f:
            i += 1
            if len(line) > 2:
                if line[-2] is not ",":
                    print("COMMA-ERROR on LINE {0}!".format(str(i)))
                    fault = True

        if not fault:
            print("Everything checks out: OK")
            return True
        else:
            print("Errors need to be fixed before continuing with LaTeX compilation!")
            return False

if __name__=="__main__":
    import sys
    check_file(sys.argv[1])
