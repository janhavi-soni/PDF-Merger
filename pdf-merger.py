import os
from pypdf import PdfMerger


lst=[]
for f in os.listdir():
    if f.endswith("pdf"):
        lst.append(f)

sorted_list = sorted(lst)

merger = PdfMerger()
for pdf in sorted_list:
    merger.append(pdf)

merger.write("results.pdf")
merger.close()
    