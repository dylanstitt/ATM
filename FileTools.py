import os

def validateFile(filename):
  if filename[-4:] != 'txt':
    if os.path.exists(filename):
      return True
    
    print("The file does not exist")
    return
    
  print("The file extention was invalid")
  return


def readFile(filename, readMode):
  if validateFile(filename):
    with open(filename, 'r') as file:
      if readMode.lower() == 'r':
        return file.read()
      
      elif readMode.lower() == 'rl':
        return file.read().splitlines()
      
      else:
        print("That is an invalid read mode")


def writeFile(filename, contents):
  if filename[-4:] != '.txt':
    filename += '.txt'
  
  if isinstance(contents, list):
    with open(filename, 'w') as file:
      for line in contents:
        file.write(str(line))
        
  elif isinstance(contents, str):
    with open(filename, 'w') as file:
      file.write(contents)
      
  else:
    print("The contents given were invalid for writing to the file")
    

def clean(text):
  chars = [chr(i) for i in range(97, 123)]
  chars.append(' ')
  tempText = ''
  
  for char in text:
    if char.lower() in chars:
      tempText += char
      
    elif char == '\n' and tempText[-1] != ' ':
      tempText += chars[-1]
  
  return tempText.lower()


def search(word, file):
  contents = readFile(file, 'r')
  contents = clean(contents).split(' ')
  
  c = 0
  for w in contents:
    if w == word:
      c += 1
  return c