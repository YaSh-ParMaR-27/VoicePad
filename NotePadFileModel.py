import os
import string
from tkinter import filedialog


class File_Model:
    def __init__(self):
        self.url = ""
        self.key=string.ascii_letters+''.join([str(x) for x in range(0,10)])
        # Or It can also be
        # self.key = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.offset = 5

    def encrypt(self, plaintext):
        result = ''
        for ch in plaintext:
            try:
                # self.key.index(ch) will throw exception for special characters
                # As there are no special characters in self.key
                i = (self.key.index(ch) + self.offset) % 62
                result += self.key[i]
            except ValueError:
                result += ch  # If exception comes we will append the character itself
        return result

    def decrypt(self, ciphertext):
        result = ''
        for ch in ciphertext:
            try:
                i = (self.key.index(ch) - self.offset) % 62
                result += self.key[i]
            except ValueError:
                result += ch
        return result

    # We might think that the bracket part in line 27 can produce negative values and we are taking mod of that value
    # So question arises how can you take modulus(%) of negative values
    # ANS :- In python internally mod is solved using the below formula :

    # 1) a - b * math.floor(a/b)
    # 2) Sign of the mod will be of the denominator (unlike c or java where it is of numerator)

    def open_file(self):
        self.url = filedialog.askopenfilename(title='Select File', filetypes=[("Text Documents", "*.*")])

    def new_file(self):
        self.url = ""

    def save_as(self, msg):
        encrypted_text = self.encrypt(msg)
        self.url = filedialog.asksaveasfile(mode='w', defaultextension='.ntxt',
                                            filetypes=([("All Files", "*.*"), ("Text Documents", "*.txt")]))
        self.url.write(encrypted_text)
        filepath = self.url.name
        self.url.close()
        self.url = filepath

    def save_file(self, msg):
        if self.url == "":
            self.url = filedialog.asksaveasfilename(title='Select File', defaultextension='.ntxt',
                                                    filetypes=[("Text Documents", "*.*")])
        filename, file_extension = os.path.splitext(self.url)
        content = msg
        if file_extension == '.ntxt':
            content = self.encrypt(content)
        with open(self.url, 'w', encoding='utf-8') as fw:
            fw.write(content)

    def read_file(self, url=''):
        if url != '':
            self.url = url
        else:
            self.open_file()
        base = os.path.basename(self.url)
        file_name, file_extension = os.path.splitext(self.url)
        fr = open(self.url, "r")
        contents = fr.read()
        if file_extension == '.ntxt':
            contents = self.decrypt(contents)
        fr.close()
        return contents, base


