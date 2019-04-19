import sqlite3
from google.cloud import language_v1
from google.cloud.language_v1 import enums
from google.cloud import storage
import six
import sys


def getContacts():
    file = open('/Users/tylerdonati/Desktop/MsgAnalyzer/contacts.vcf', 'r')

    contacts = {}
    names = {}

    name = ""
    for line in file:
        if line[0:2] == "FN":
            #print(line[3:])
            name = line[3:].rstrip()
        if line[0:3] == "TEL":
            #print(line[line.index('pref:')+5:])
            contacts[(name, line[line.index('pref:')+5:].rstrip())] = []
            names[line[line.index('pref:')+5:].rstrip()] = name

    print(contacts)
    print(names)
    return contacts


def messages(contacts):
    connection = sqlite3.connect("chat.db")

    crsr = connection.cursor()

    crsr.execute("SELECT text FROM message;")

    ans = crsr.fetchall()

    client = language_v1.LanguageServiceClient()


    for i in ans:
        i = str(i)
        currMsg = i[2:-3]
        if isinstance(currMsg, six.binary_type):
            content = currMsg.decode('utf-8')
        if ''.join(currMsg.split()) != "":
            type_ = enums.Document.Type.PLAIN_TEXT
            document = {'type': type_, 'content': content}
            response = client.analyze_sentiment(document)
            sentiment = response.document_sentiment
            print('Score: {}'.format(sentiment.score))
            print('Magnitude: {}'.format(sentiment.magnitude))

            #print(currMsg)
        if i == 10:
            break

        #print(i)


def explicit():
    from google.cloud import storage

    # Explicitly use service account credentials by specifying the private key
    # file.
    storage_client = storage.Client.from_service_account_json(
        '/Users/tylerdonati/Desktop/MsgAnalyzer/apikey.json')

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    print(buckets)


def main():
    explicit()
    #contacts = getContacts()
    #messages(contacts)



if __name__ == '__main__':
    main()
