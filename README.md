# Visualix_Python



## Prerequisites
- [x] Python 3.6 or later
- [x] pip package manager
- [x] git


## Setup
- Open the terminal
- Clone the repository
	```bash
	git clone https://github.com/Laughing-Kid/Visualix_Python.git
	```
- Change the current working directory

	```bash
	cd Visualix_Python
	```
- Execute the below commands
 	```bash
	pip3 install pipenv
	```
	```bash
	pipenv install
	```
	```bash
	pipenv shell
	```
	
- Install the requirements 
	```bash
	pip install -r requirements.txt
	```
    use conda package management tool for installing the `mkl-fft` library:
    ```
    conda install -c intel mkl_fft 
    ``` 
- Execute the following commands
	```bash
	set FLASK_APP=main_app.py
	```
	```bash
 	set FLASK_ENV=development
	```
	```bash
 	flask run
	```
	
- **If you are using Linux or Mac, use `export` instead of `set` in the above commands**
