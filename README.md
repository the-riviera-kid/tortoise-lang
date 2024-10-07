# tortoise-lang
The Tortoise Language (inspired by an exercise in The Pragmatic Programmer)

## Running code analysis tools:
We have three code analysis tools in tools.bash file, pytest, black, and pylint.  
Every time we change something in the code these analysis tools should be run.

To run the scripts:

1. create a virtual environment (one time only)  
        virtualenv -p python3 venv
2. start the virtual environment  
source venv/bin/activate
3. install the tools we need (one time only)  
        pip install pytest pylint black
4. run the script  
        bash ./tools.bash