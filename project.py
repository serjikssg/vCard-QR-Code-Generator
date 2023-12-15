from tabulate import tabulate
from validators import email
import qrcode, sys, os


info = {
    "name": "",
    "email": "",
    "phone": "",
    "address": "",
    "city": "",
    "state": "",
    "zip": "",
    "contry": "",
    "company": "",
    "title": "",
    "website": "",
    "note": "",
    "birthday": "",
}


def main():
    global info
    while True:
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")

        print("\n   VCard qr-code generator, by Serjik G.\n")

        headers = ["Line", "Feild", "     Information     "]
        table = []
        for i, j in enumerate(info):
            table.append([i + 1, j.capitalize(), info[j]])

        print(tabulate(table, headers, tablefmt="grid"))

        print("\n  [ q:Quit | s:Show qr-code | f:Save as ]\n")
        x = input("    Enter line number to edit: ").strip().lower()

        if x in ["q", "quit", "exit"]:
            sys.exit("Good bye!")
        elif x == "s":
            qr_gen(vcart())
            continue
        elif x == "f":
            print("-----------------------------------------------")
            x = input("  Please provide the file name: ").strip()

            qr_file(vcart(), x)
            continue
        else:
            try:
                x = int(x)
            except:
                continue

        if x - 1 not in range(len(list(info.keys()))):
            print("-----------------------------------------------")
            input(" 🙁  Not in the List!")
            continue

        print("-----------------------------------------------")
        edit = input(f"  {list(info.keys())[x - 1]}: ").strip()
        if list(info.keys())[x - 1] == "email" and not email(edit):
            print("-----------------------------------------------")
            input(" 🙁 Invalid Email! - Press Enter to continue.")
        else:
            info[list(info.keys())[x - 1]] = edit


def vcart():
    data = f"""BEGIN:VCARD
VERSION:4.0
FN:{info["name"]}
EMAIL;TYPE=EMAIL:{info["email"]}
TEL;TYPE=MOBILE:{info["phone"]}
ADR;TYPE=HOME:;;{info["address"]};{info["city"]};{info["state"]};{info["zip"]};{info["contry"]}
ORG:{info["company"]}
TITLE:{info["title"]}
URL:{info["website"]}
NOTE:{info["note"]}
BDAY:{info["birthday"]}
END:VCARD"""

    return data


def qr_gen(data):
    try:
        v = qrcode.make(data)
        v.show()

    except:
        print(" 🙁  GUI not available!")
        input("(Press Enter to continue.)")


def qr_file(data, filename):
    try:
        v = qrcode.make(data)
        v.save(f"{filename}.png")

        print("-----------------------------------------------")
        print(f" 🙂  {filename}.png has been saved successfully!")

        input("\n     (Press Enter to continue.)").strip()

    except:
        print("-----------------------------------------------")
        print(" 🙁  Invalid file name!")
        input("(Press Enter to continue.)")


if __name__ == "__main__":
    main()
