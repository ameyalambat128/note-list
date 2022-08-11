# Note-List

![Notetaking-App](https://user-images.githubusercontent.com/63185829/143322196-ef1b39a0-4205-4875-99e2-b08128cb7956.png)

### Cloning the repository

- Clone the repository using the command below :
```bash
git clone https://github.com/ameyalambat128/Notetaking-App.git

```

> Install python if you haven't!


- Move into the directory where we have the project files : 
```bash
cd Notetaking-App

```


- Install the virtual environment package
```bash
python -m pip install --user virtualenv  
```

- Create a virtual environment :
```bash
# If you are on Windows
virtualenv env
# If you are on Linux or Mac
python -m venv env
```

- Activate the virtual environment :
```bash
# If you are on Windows
.\env\Scripts\activate
# If you are on Linux or Mac
source env/bin/activate
```

- Install Django from the command line : 
```bash
python -m pip install django
```
> Install these frameworks too
```bash
pip install djangorestframework
pip install django-cors-headers   
```

#

### Running the App

- To run the Notes App, we use :
```bash
python manage.py runserver
```

> Then, the development server will be started at http://127.0.0.1:8000/

#
