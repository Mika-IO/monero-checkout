# Example Package

A python tool to handler monero payments.

##  How run tests

Upgrade pip

    python3 -m pip install --upgrade pip

Install virtualenv

    python3 -m pip install virtualenv

Create virtualenv

    python3 -m venv ./venv

Active virtual enviroment

    # windows
    
    cd venv/scripts
    activate 

    # linux
    source ./venv/bin/activate

Install dependencies

    pip install -r requirements.txt

Run tests

    coverage run --source=src -m unittest discover -s tests -b && coverage html --omit='venv/*'