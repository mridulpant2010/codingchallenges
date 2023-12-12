
import typer

class WordCount:

    def __init__(self) :
        self.app = typer.Typer()
    
    def byte_count(self,filename): #m
        with open(filename, 'rb') as file:
            data = file.read()
            count = len(data)
        typer.echo(f"Number of bytes in the file {filename}: {count}")
    
    def character_count(self,filename): #c
        count=0
        with open(filename, 'rb') as file:
            data = file.read()
            for each_char in data:
                if each_char != "\n":
                    count+=1
        typer.echo(f"Number of characters in the file {filename}: {count}")
    
    def line_count(self,filename): #l
        with open(filename, 'r') as file:
            data = len(file.readlines())
        typer.echo(f"Number of lines in file {filename}: {data}")
    
    
    def word_count(self,filename): #w
        with open(filename,"r") as file:
            data = file.read()
            word_count = len(data.split())
        typer.echo(f"Number of words in file {filename}: {word_count}")

    
    def main(self,filename,c:bool=False,l:bool=False,w:bool=False,m:bool=False): 
        if c:
            self.character_count(filename)
        if l:
            self.line_count(filename)
        if w:
            self.word_count(filename)
        if m:
            self.byte_count(filename)
            
        if not(c or l or w or m):
            self.character_count(filename)
            self.line_count(filename)
            self.word_count(filename)
            self.byte_count(filename)
             


# wc = WordCount()
# @wc.app.command()
# def hello_world(name:str):
#     print('hello ' + name)
# wc.app()

#how to provide the filename?

wc = WordCount()
filename="/Users/user/Documents/GitHub/codingchallenges/wc/test.txt"
# wc.byte_count()
# wc.character_count(filename="/Users/user/Documents/GitHub/codingchallenges/wc/test.txt")
# wc.line_count(filename="/Users/user/Documents/GitHub/codingchallenges/wc/test.txt")
# wc.word_count(filename="/Users/user/Documents/GitHub/codingchallenges/wc/test.txt")

#what if i have multiple flags and one argument, how to tackle this problem?
typer.run(wc.main)

## how to provide the argument for each of the filename
## i have to learn how can i make this as a command line utility instead of everytime writing the python3 filename.py
## how to default provide the string using grep