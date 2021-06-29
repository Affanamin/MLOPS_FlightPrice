###### First of all create environment through given Command
'''
**conda create -n wineq python=3.7 -y**
'''
###### Then activate environment through given command
'''
**activate wineq**
'''
###### Then create "template.py" file; Where we present structure of application 

###### Apply Commands
**git init**

**pip install dvc**

**dvc init**

###### Add Data in the given location
**dvc add data_given/winequality.csv**

###### Then Commit your Code
**git add . && git commit -m "first commit"**

###### Add code to your github repository
**git push origin main**

##### Other Important Commands

// dvc repro

// dvc metrics show

// dvc metrics diff

**Tox Command**

tox

**For Rebuilding**

tox -r

**Pytest Command**

pytest -v

**Setup Command**

pip install -e . 

**build your own package commands-**

python setup.py sdist bdist_wheel

create an artifcats folder

-------------------------------------------------------

mlflow server command -

-------------------------------------------------------


mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts --host localhost -p 1234

-------------------------------------------------------
