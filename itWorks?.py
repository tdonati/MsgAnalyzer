import sqlite3
import vcfpy
import re


connection = sqlite3.connect("chat.db")

crsr = connection.cursor()

crsr.execute("SELECT text FROM message;")

ans = crsr.fetchall()

# for i in ans:
#     i = str(i)
#     currMsg = i[2:-3]
#     if ''.join(currMsg.split()) != "":
#         print(currMsg)
#         print("\n")
#     #print(i)


# reader = vcfpy.Reader.from_path('/Users/tylerdonati/Desktop/fun project/Martin Leung and 26 others.vcf')
# print(reader.header.names)
#
# for record in reader:
#     if not record.is_snv():
#         continue
#     line = [record.FN, record.VOICE]
#     print('\t'.join(map(str, line)))

file = open('/Users/tylerdonati/Desktop/fun project/Martin Leung and 26 others.vcf', 'r')

for line in file:
    if line[0:2] == "FN":
        print(line)
    if line[0:3] == "TEL":
        print(line[line.index('pref:')+5:])
