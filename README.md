# Visualix_Python



## Install Requirements
```bash
pip install -r requirements.txt
```

## Setup
- open the terminal
- clone the repository
	```bash
	git clone https://github.com/Laughing-Kid/Visualix_Python.git
	```
- change the directory

	```bash
	cd Visualix_Python
	```
- execute the below commands
 	```bash
	pip3 install pipenv
	```
	```bash
	pipenv install
	```
	```bash
	pipenv shell
	```
	
- install the requirements 
	```bash
	pip install -r requirements.txt
	```
    use conda package management tool for installing the `mkl-fft` library:
    ```
    conda install -c intel mkl_fft 
    ``` 
- execute the following commands
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
