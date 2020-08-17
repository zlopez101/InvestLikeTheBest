# import PyPDF2

# with open("Kat-Cole-Episode-184-vF.pdf", "rb") as pdf:
#     pdfReader = PyPDF2.PdfFileReader(pdf)
#     for num in range(pdfReader.numPages)[3:4]:
#         page = pdfReader.getPage(num)
#         text = page.extractText()

#         print([tex for tex in text.split("\n") if tex.strip()])
import re

with open("Kat_cole.txt", "r", encoding="utf-8") as file:

    content = file.read()
    pattern = re.compile(r"(Patrick O'Shaughnessy)")
    new_text = pattern.sub("</p><p> <b>Patrick O'Shaughnessy</b>", content)
    pattern = re.compile(r"(Kat Cole)")
    newest_text = pattern.sub("</p><p> <b>Kat Cole</b>", new_text)
    with open("edited_kate_cole.txt", "w") as file:
        file.write(newest_text)


# my_string = """
# In her mind, because she had the obligation to be grateful, that for a period disabled her right to want or
# deserve things that were better for her family. Now, eventually she came to a different and better conclusion,
# which is just because things could be worse, just because yes, I should be grateful for something, it does
# not remove my desire and maybe even my obligation to make things better. And I think that's where it ties
# to your word ambition or drive. That there can be a healthy relationship between those two things and there
# can be a deep imbalance, going both ways.

# pattern = re.compile(r"(Patrick O'Shaughnessy|Kat Cole)")

# print(dir(pattern))
# result = pattern.sub(pat, my_string)
# print(result)
