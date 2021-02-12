# activate project venv
source venv/bin/activate

# deactivate and remove
deactivate
rm -rf venv

# install a new env with virtualenvwrapper and enable it
mkvirtualenv shortyenv -p python3
workon shortyenv

# install the requirements
pip install -r requirements.txt
