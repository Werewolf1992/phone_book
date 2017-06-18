**Contact's Base**

To set up project locally proceed with the following steps:
- go to directory you wanna place project in
- in terminal type `git clone https://github.com/Werewolf1992/phone_book.git` or clone using your favourite tool
- using virtualenv (https://virtualenv.pypa.io/en/stable/) create environment for project or launch project globally.
- go to the app directory `cd phone_book/`
- in 'phone_book' directory using pip (https://pypi.python.org/pypi/pip) type: `pip install -r requirements.txt`
- in the same directory type `python3 manage.py migrate`
- then type `python3 manage.py runserver`
- in your browser go to http://127.0.0.1:8000/
- enjoy the app