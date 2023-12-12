
The coding challenge from the John Cricket: Challenge is to build a wc


Step One
In this step your goal is to write a simple version of wc, let’s call it ccwc (cc for Coding Challenges) that takes the command line option -c and outputs the number of bytes in a file.

If you’ve done it right your output should match this:

>ccwc -c test.txt
  342190 test.txt
If it doesn’t, check your code, fix any bugs and try again. If it does, congratulations! On to…

Step Two
In this step your goal is to support the command line option -l that outputs the number of lines in a file.

If you’ve done it right your output should match this:

>ccwc -l test.txt
    7145 test.txt
If it doesn’t, check your code, fix any bugs and try again. If it does, congratulations! On to…

Step Three
In this step your goal is to support the command line option -w that outputs the number of words in a file. If you’ve done it right your output should match this:

>ccwc -w test.txt
   58164 test.txt
If it doesn’t, check your code, fix any bugs and try again. If it does, congratulations! On to…

Step Four
In this step your goal is to support the command line option -m that outputs the number of characters in a file. If the current locale does not support multibyte characters this will match the -c option.

You can learn more about programming for locales here: https://learn.microsoft.com/en-us/globalization/locale/locale-and-culture

For this one your answer will depend on your locale, so if can, use wc itself and compare the output to your solution:

>wc -m test.txt
  339292 test.txt

>ccwc -m test.txt
  339292 test.txt
If it doesn’t, check your code, fix any bugs and try again. If it does, congratulations! On to…

Step Five
In this step your goal is to support the default option - i.e. no options are provided, which is the equivalent to the -c, -l and -w options. If you’ve done it right your output should match this:

>ccwc test.txt          
    7145   58164  339292 test.txt
If it doesn’t, check your code, fix any bugs and try again. If it does, congratulations! On to…

The Final Step
In this step your goal is to support being able to read from standard input if no filename is specified. If you’ve done it right your output should match this:

>cat test.txt | ccwc -l 
    7145
If it doesn’t, check your code, fix any bugs and try again. If it does, congratulations! You’ve done it, pat yourself on the back, job well done!