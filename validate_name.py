import re


def validate(FullName):

    result = re.search(r"^([\w .]*), ([\w .]*)$", FullName)
    if not re.match("^([\w .]*), ([\w .]*)$", FullName):
        return "Invalid input. First name and Last name must be composed of letters only. Follow this input format: last name, first name"
    else:
        return "{} {}".format(result[2], result[1])

print(validate(FullName=input("enter your last name and first name separated by comma: ")))
