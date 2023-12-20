

## how to provide the argument for each of the filename
    - how to tackle the situation when a file is in a different folder and passed as an argument 
    - how can python read the file from a specific relative filepath 
    - how can i make path global over here? how instead of writing the python command everytime i make it a global? the main thing is to run this utility from any location of the commandline.
      - i have to learn how can i make this as a command line utility instead of everytime writing the python3 filename.py
      - how to default provide the string using grep
      - `export ccwc = "python3 ~/Documents/Github/codingchallenges/wc/src/main.py"`
        - entry point in the setup.py file helps a lot.
        Soln: https://betterprogramming.pub/build-your-python-script-into-a-command-line-tool-f0817e7cebda

    - should we be using the classes for these type of tasks is it beneficial?
      - we can have a class and at last a main method which can be called in setup.py and main method will have all the object instantiation and method calling.


## building the project
    - command: python3 wc/setup.py sdist bdist_wheel  
    - sudo pip3 install dist/wordcount-0.1.1-py3-none-any.whl 

## pending
  - unit test cases are not completed.
  - ccwc utility isnot working expectedly.
  - https://betterprogramming.pub/build-your-python-script-into-a-command-line-tool-f0817e7cebda
