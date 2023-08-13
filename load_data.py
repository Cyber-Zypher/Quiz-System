import csv
import pymysql

# Database connection settings
db_config = {
    "host": "localhost",
    "user": "UNAME",
    "password": "PASSWORD",
    "database": "DB_NAME"
}

# Connect to the database
connection = pymysql.connect(**db_config)

def load_questions_from_csv(file_path):
    with open(file_path, "r") as csvfile:
        csvreader = csv.DictReader(csvfile)
        questions = []
        for row in csvreader:
            questions.append(row)
        return questions

def insert_questions_into_db(questions):
    with connection.cursor() as cursor:
        for question in questions:
            query = "INSERT INTO questions (question_text, option1, option2, option3, option4, correct_option) " \
                    "VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (
                question['question_text'],
                question['option1'],
                question['option2'],
                question['option3'],
                question['option4'],
                int(question['correct_option'])
            ))
        connection.commit()

def main():
    file_path = "data.csv"
    questions = load_questions_from_csv(file_path)
    insert_questions_into_db(questions)
    print("Questions and answers loaded into the database.")

    connection.close()

if __name__ == "__main__":
    main()
