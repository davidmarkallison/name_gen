# name_gen

A random name generator! This tool generates a random name (or list of random names) for you to use when creating fictional characters! It uses two text files to generate names!

## Getting Started

If you have used the command line or python before then you'll find this a walk in the park!

### Prerequisites?

1. Python 3.x.x installed. 
2. Command line knowledge, I guess.

Run:
```
python -V
```
in your command line to see if you have Python version 3 installed (Python version 2.x.x will give you errors! Sorry!).

### How do I use it?

**Windows**

1. Open CMD (Command Prompt)

2. Navigate to the folder conatining main.py using the 'cd' command (change directory):
```
C:\> cd path\to\file\containing\main\files\ 
```

3. To run the script and generate just ONE random name:
```
python name_gen.py
```

4. Alternatively, replace "25" in the following code to declare the amount of names you want to generate:
```
python name_gen.py -n 25
```

5.  Don't like the command line output? Want to write to a file instead? Try this:
```
python name_gen.py -n 25 -o RandomNames
```
**NOTE: The .txt extension is added automatically to your output file!**