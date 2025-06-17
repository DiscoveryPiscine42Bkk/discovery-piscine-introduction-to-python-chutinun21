#!/usr/bin/python3
import sys #ต้องrunในbashผลถึงจะออกตามโจทย์

if len(sys.argv) == 2:
    parameter = sys.argv[1]
    user_input = input("What was the parameter? ")

    if user_input == parameter:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")
