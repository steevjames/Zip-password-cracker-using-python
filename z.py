import zipfile

zip_file = zipfile.ZipFile("file.zip")

words=["pass1","secret","anathorpassword", "secretpass","finalpass"]

print("Total passwords to test:", len(words))

passWordFound=False

for word in words:
    try:
        zip_file.extractall(pwd=bytes(word, "utf-8") )
        print("[+] Password found:", word)
        passWordFound = True
    except:
        continue

if not passWordFound:
    print("[!] Password not found, try other wordlist.")
