def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    number_found = False

    for letter in s:

        if not letter.isalnum():
            return False

        if letter.isdigit():

            if not number_found and letter == "0":
                return False

            number_found = True

        elif number_found:
            return False

    return True


main()
