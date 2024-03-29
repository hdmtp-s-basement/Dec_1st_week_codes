#!/usr/bin/env python3
from reddit_dose import *
import fontstyle


def choose():
    choice = int(input(fontstyle.apply("\n\n\n 0 -> sub_comment_stream \n\n 1 -> sub_submissions_hot \n\n 2 -> sub_submission_stream \n\n 3 -> redditor_stream_comnts \n\n 4 -> redditor_stream_submissions \n\n 5 -> sub_submissions_top \n\n 6 -> search subreddit \n\n 7 -> search comments \n\n 8 -> search an user's comment \n\n 9 -> store_username \n\n 10 -> exit(): ", "bold/Italic/purple")))
    
    if(choice == 0):
        try:
            sub_comment_stream()
        except KeyboardInterrupt:
            print(fontstyle.apply("\n\tAdios!\n\t", "bold/Italic/red"))
    elif(choice == 1):
        try:
            sub_submissions_hot()
        except KeyboardInterrupt:
            print(fontstyle.apply("\n\tAdios!\n\t", "bold/Italic/red"))
    elif(choice == 2):
        try:
            sub_submission_stream()
        except KeyboardInterrupt:
            print(fontstyle.apply("\n\tAdios!\n\t", "bold/Italic/red"))
    elif(choice == 3):
        try:
            redditor_stream_comnts()
        except KeyboardInterrupt:
            print(fontstyle.apply("\n\tAdios!\n\t", "bold/Italic/red"))
    elif(choice == 4):
        try:
            redditor_stream_submissions()
        except KeyboardInterrupt:
            print(fontstyle.apply("\n\tAdios!\n\t", "bold/Italic/red"))
    elif(choice == 5):
        try:
            sub_submissions_top()
        except KeyboardInterrupt:
            print(fontstyle.apply("\n\tAdios!\n\t", "bold/Italic/red"))
    elif(choice == 6):
        try:
            search_sub()
        except KeyboardInterrupt:
            print(fontstyle.apply("\n\tAdios!\n\t", "bold/Italic/red"))
    elif(choice == 7):
        try:
            search_comment()
        except KeyboardInterrupt:
            print(fontstyle.apply("\n\tAdios!\n\t", "bold/Italic/red"))
    elif(choice == 8):
        try:
            search_user_comment()
        except KeyboardInterrupt:
            print(fontstyle.apply("\n\tAdios!\n\t", "bold/Italic/red"))
    elif(choice == 9):
        try:
            store_username()
        except KeyboardInterrupt:
            print(fontstyle.apply("\n\tAdios!\n\t", "bold/Italic/red"))

choose()
