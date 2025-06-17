import sys #ต้องrunในbashผลถึงจะออกตามโจทย์

if len(sys.argv) > 1:
    print(sys.argv[1])
else:
    print("none")
