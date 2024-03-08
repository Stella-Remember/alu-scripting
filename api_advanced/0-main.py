<<<<<<< HEAD
n
=======
#!/usr/bin/python3
"""
0-main
>>>>>>> c588c9e4dfd21b02eef21ba28277f43e19df1293
"""
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
