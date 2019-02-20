import csv
with open("sample_data.csv", "r", encoding="utf-8") as f:
    fullist = list(csv.reader(f))

for row in fullist:
    fixedphone = ""
    for c in row[5]:
        if c.isdigit():
            fixedphone += c
    fixedphone = "(" + fixedphone[:3] + ")-" + \
        fixedphone[3:6] + "-" + fixedphone[6:]
    row[5] = fixedphone

    fixedname = row[6]
    try:
        fixedname = fixedname.split(" ")[0] + " " + fixedname.split(" ")[-1]
    except:
        fixedname = fixedname.split(" ")[0]
    fixfixedname = ""
    for c in fixedname:
        if c.isalpha() or c == " ":
            fixfixedname += c
    row[6] = fixfixedname

print(fullist)
