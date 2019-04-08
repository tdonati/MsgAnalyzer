import sqlite3


def getContacts():
    file = open('/Users/tylerdonati/Desktop/MsgAnalyzer/contacts.vcf', 'r')

    contacts = {}

    name = ""
    for line in file:
        if line[0:2] == "FN":
            #print(line[3:])
            name = line[3:].rstrip()
        if line[0:3] == "TEL":
            #print(line[line.index('pref:')+5:])
            contacts[(name, line[line.index('pref:')+5:].rstrip())] = []

    print(contacts)
    return contacts


def messages(contacts):
    connection = sqlite3.connect("chat.db")

    crsr = connection.cursor()

    crsr.execute("SELECT text FROM message;")

    ans = crsr.fetchall()


    for i in ans:
        i = str(i)
        currMsg = i[2:-3]
        if ''.join(currMsg.split()) != "":
            print(currMsg)
            #print("\n")

        #print(i)


def main():
    contacts = getContacts()
    messages(contacts)


if __name__ == '__main__':
    main()
