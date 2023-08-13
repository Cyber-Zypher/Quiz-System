
# Quiz game using Python and MySQL
A Simple commandline Quiz game made with Python and MySQL Database.
The Code uses PyMySQL Python Library to function. This code has a very simple syntax which makes it easy to understand and beginner friendly.



## Install the required Libraries.

Clone the project

```
pip install pymysql
```
or
```
python -m pip install pymysql
```

## Initialize the Database

```
CREATE DATABASE quiz_system;

USE quiz_system;

CREATE TABLE questions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question_text TEXT,
    option1 TEXT,
    option2 TEXT,
    option3 TEXT,
    option4 TEXT,
    correct_option INT
);

CREATE TABLE quiz_results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_name VARCHAR(50),
    score INT
);
```

## Instructions

- After installing the needed libraries. Edit the `data.csv` file to load the questions and its answers.

- Then, run the `load_data.py` script to load the questions and answers to the SQL database.

- Don't run the `load_data.py` more than once, It will cause duplicate questions and cause clutter on your database.

- Then Finally, run the `app.py` to play the quiz.


## Authors

- [@sindhu_vaibhav_KL](https://www.instagram.com/sindhuvaibhav2007/)
- [And our friends @Medusa Infosystems International](https://www.instagram.com/themedusaclan_official/)

