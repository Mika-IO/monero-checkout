<div align='center'>
    <tbody><tr><td><pre>   
    <img src="https://user-images.githubusercontent.com/55309160/157948512-45484369-6d86-46ca-9345-9038637a7960.png"/>
    </pre><!-- white text and background :) /!-->
    <font color="#FFFFFF">Package monero-checkout 💸</font></td></tr></tbody>
    <br>
    <img src='https://img.shields.io/badge/Python-3.10-green'></img>
</div>

A python tool to handler monero payments.

# :pushpin: **TODO** 


> Project Planning :heavy_check_mark:

> Connect to rpc server :warning:

> Create wallet :warning:

> Connect wallet :warning:

> Generate a payment :warning:

> Check payment status :warning:


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