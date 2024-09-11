#match statements

#match the output and execute. It run python version > 3.10


# match variable:
#     case pattern1
#         code block
#     case pattern2
#         code block


#write a program to ask the user which browser he want to run automation

browser_name = input("enter the name of the browser\n")
browser_name = browser_name.lower()
match browser_name:
    case "firefox":
        print("Excute the firefox code")
    case "chrome":
        print("Excute the chrome code")
    case "edge":
        print("Excute the edge code")
    case "safari":
        print("Excute the safari code")
    case _:
        print("broswer not found code")
