##Purpose of The Project


##Starting Project in New Environment
This project should use python version `3.9.0-win32` to be able to run.
When you copied this project to new Windows folder do the following steps to prepare the project:
1. Create venv name 'venv' inside this project based on python 3.9.0-win32: `python -m venv venv`
2. Activate the venv using command: `venv\Scripts\activate`
3. Install all requirements of this project from 'requirements.txt' file: 
`pip install -r requirements.txt`

##Run E-AFU Data Import
###Data Preparation
1. Make sure your manual afu data is available. Set your manual afu path to `app_config.json` -> `manual_afu_path`
2. Set your id in `app_config.json` -> `caseworker_id`
3. Open your manual afu excel file and fill the column `Date Entered` for rows you want to enter manually
###Photo Preparation
1. All photo you wanted to import should be place inside a folder (in school name format) inside `D:\BY_SCHOOL_AFU_PHOTOS`
###Execution
1. Type command: `python main.py` in terminal of PyCharm or directly open `e-afu_helper.bat` file in desktop
2. Enter your E-AFU path
3. Enter the database encryption code
4. 

##Structure of the Project
Folder 'main_actions' contains main action we can perform to E-AFU

Path 'main_actions/general_actions' contains actions that can be performed per E-AFU, specifically to update afu_house form/section that only need to be updated once per E-FU application.
It also contains general purpose task such as rotating photos of a chosen folder.

Path 'main_actions/by_school_actions' contains actions that performed at different time per school

##Test modules
All test module is placed under folder tests. To run test for test modules under this folder, use script `python -m unittest -v tests.[module_name]`


