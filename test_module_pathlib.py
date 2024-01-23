from pathlib import Path

file_path = Path('bt1.tex')
with file_path.open(mode='w', encoding='utf-8') as file:
    for i in range(5):                                      # for i=0 to 4
        file.write("Nội dung thứ " + str(i+1) + "\n")       # write content to file