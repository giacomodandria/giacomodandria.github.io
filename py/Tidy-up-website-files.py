import os
import shutil
import subprocess
from bs4 import BeautifulSoup, Comment

print('succesfully imported libraries.')

# rename index files to represent actual content
html_file_names = [('index-5.html', 'about-us.html'),
                   ('index-6.html', 'our-projects.html'),
                   ('index-7.html', 'book-us.html'),
                   ('', ''),
                   ('', ''),
                   ('', '')]

# deletes files and folders
files = ['index1c4a.html',
         'index-2.html',
         'index-3.html',
         'index-4.html',
         'index40a0.html',
         'index970c.html']

folders = ['xml',
           'other',
           'php',
           'woff',
           'json']

for file in range(len(files)):
    try:
        os.remove(files[file])
    except:
        print(f'Missing file: {files[file]}')
    
for folder in range(len(folders)):
    try:
        shutil.rmtree(folders[folder])
    except:
        print(f'Missing folder: {folders[folder]}')

print('succesfully deleted files/folders')

# adding filenames files on current, CSS and JS folders
command = 'dir /b > filenames.txt'
subprocess.call(command, shell=True)

command = 'cd css && dir /b > filenames.txt'
subprocess.call(command, shell=True)

command = 'cd js && dir /b > filenames.txt'
subprocess.call(command, shell=True)

print('successfully added filenames.txt files')

# adds all html files names in the files list
files_html = []

with open('filenames.txt', 'r') as filenames:
    for line in filenames:
        if line[len(line)-6:len(line)-1] == '.html':
            files_html.append(line[:len(line)-1])
        else:
            pass

# delete httrack added lines and all comments
for file in range(len(files_html)):
    print(f'    Working on: {files_html[file]}')
    with open(files_html[file], 'r') as input_file:
        soup = BeautifulSoup(input_file, 'lxml')

        for element in soup(text=lambda text: isinstance(text, Comment)):
            element.extract()
            
    with open(f'1{files_html[file]}', 'wb') as output_file:
              output_file.write(soup.encode('UTF-8'))#.prettify().encode('UTF-8'))       
        
for file in range(len(files_html)):
    os.remove(files_html[file])
    os.rename(f'1{files_html[file]}', files_html[file])

print('Succesfully deleted comments')

# opens files in vscode to beautify them with the correct plugin
for file in range(len(files_html)):
    command = f'code {files_html[file]}'
    subprocess.call(command, shell=True)

print('Files have been succesfully opened in vscode: make sure to beautify them.')


while True:
    beautified = input('\nInsert y if files have been beautified: ')
    if beautified == 'y':
        break
    else:
        print('Make sure files have been beautifid')
        continue

print()

# deletes lines that contain srcset in HTML files
words_to_replace = ['srcset', 'data-srcset', 'data-src']

for file in range(len(files_html)):
    print(f'    Working on: {files_html[file]}')
    with open(files_html[file], 'r') as oldfile, open(f'1{files_html[file]}', 'w') as newfile:
        for line in oldfile:
            if not any(bad_word in line for bad_word in words_to_replace):
                newfile.write(line)
                
print('Renaming files... ', end = '')

for file in range(len(files_html)):
    os.remove(files_html[file])
    os.rename(f'1{files_html[file]}', files_html[file])
    
print('Succesfully deleted srcset lines.')

# replce words in HTML files
old_domain = 'localhost'
new_domain = 'giacomodandria.github.io'
http = 'http'
https = 'https'
httpss = 'httpss'

for i in range(len(files_html)):
    print(f'    Working on: {files_html[i]}')
    # Read in the file
    with open(files_html[i], 'r') as file :
      filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(old_domain, new_domain)
    filedata = filedata.replace(http, https)
    filedata = filedata.replace(httpss, https)
    for j in range(len(html_file_names)):
        if html_file_names[j][0] == '':
            break
        else:
            filedata = filedata.replace(html_file_names[j][0], html_file_names[j][1])

    # Write the file out again
    with open(files_html[i], 'w') as file:
      file.write(filedata)

print('Succesfully replaced words in HTML files.')

# replace words in CSS files
files_css = []

with open('css/filenames.txt', 'r') as filenames:
    for line in filenames:
        files_css.append(line[:len(line)-1])

old_domain = 'localhost'
new_domain = 'giacomodandria.github.io'
http = 'http'
https = 'https'
httpss = 'httpss'

for i in range(len(files_css)):
    try:
        print(f'    Working on: {files_css[i]}')
        # Read in the file
        with open(f'css/{files_css[i]}', 'r') as file :
          filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(old_domain, new_domain)
        filedata = filedata.replace(http, https)
        filedata = filedata.replace(httpss, https)

        # Write the file out again
        with open(f'css/{files_css[i]}', 'w') as file:
          file.write(filedata)
    except UnicodeDecodeError:
        print(f'Unable to read unicode char in {files_css[i]} file. Skipping to the next one.')

print('Succesfully replaced words in CSS files.')

# replace words in JS files
files_js = []

with open('js/filenames.txt', 'r') as filenames:
    for line in filenames:
        files_js.append(line[:len(line)-1])

old_domain = 'localhost'
new_domain = 'giacomodandria.github.io'
http = 'http'
https = 'https'
httpss = 'httpss'

for i in range(len(files_js)):
    try:
        print(f'Working on: {files_js[i]}')
        # Read in the file
        with open(f'js/{files_js[i]}', 'r') as file :
          filedata = file.read()

        # Replace the target string
        filedata = filedata.replace(old_domain, new_domain)
        filedata = filedata.replace(http, https)
        filedata = filedata.replace(httpss, https)

        # Write the file out again
        with open(f'js/{files_js[i]}', 'w') as file:
          file.write(filedata)
    except UnicodeDecodeError:
        print(f'Unable to read unicode char in {files_js[i]} file. Skipping to the next one.')

print('Succesfully replaced words in JS files.')

# delete filenames files from folders
os.remove('filenames.txt')
os.remove('css/filenames.txt')
os.remove('js/filenames.txt')

print('Succesfully deleted filenames.txt files.')

# rename html files
for i in range(len(html_file_names)):
    if html_file_names[i][0] == '':
            break
    else:
        os.rename(html_file_names[i][0], html_file_names[i][1])

print('Succesfully renamed files.')
print('Script finished!')