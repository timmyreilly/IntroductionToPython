## Welcome to the wonderful world of Python!

These are the supporting files to my blog post found here: 
http://timmyreilly.com/python-introduction/ 


#Setting Up your Dev Environment

### Before we get started learning and buildling with Python we need to setup our development environment. 

1. Install Python
2. Install virtualenv
3. Install virtualenvwrapper or virtualenvwrapper-win
4. Create a virtual environment 
 

## 1. Install Python

[Windows](http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/)

[Mac](http://docs.python-guide.org/en/latest/starting/install/osx/)


## 2. Install virtualenv

```
$ pip install virtualenv
```

## 3. Install virtualenvwrapper or virtualenvwrapper-win

virtualenv wrappers make it easy to manage multiple environments and can make iterating on project easy. 

[Windows](http://timmyreilly.azurewebsites.net/python-flask-windows-development-environment-setup/)

[Mac](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

[Linux](http://newcoder.io/begin/setup-your-machine/) 

_Still Having Issues?_ __[Here's another helpful guide](http://newcoder.io/begin/setup-your-machine/)__

## 4. Create a virtual environment

```
$ mkvirtualenv helloworld
```

cd into root of project

```
$ setprojectdir .

$ deactivate

$ workon helloworld
```

## 5. Install a package

We're going to install [requests](http://docs.python-requests.org/en/master/) 

```
$ pip install requests
```

