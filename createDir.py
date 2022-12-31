import os

def createDirectory(date):
    try:
        if not os.path.exists(date):
            os.makedirs(date)
    except OSError:
        print("Creation of the directory %s failed" % date)