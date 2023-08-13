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

def get_questions():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM questions")
        questions = cursor.fetchall()
    return questions

def save_quiz_result(user_name, score):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO quiz_results (user_name, score) VALUES (%s, %s)", (user_name, score))
        connection.commit()

def main():
    user_name = input("Enter your name: ")
    questions = get_questions()
    score = 0

    for question in questions:
        print(question[1])  # Print the question text
        for i in range(2, 6):
            print(f"{i-1}. {question[i]}")  # Print the options

        user_answer = int(input("Enter your answer (1-4): "))
        if user_answer == question[6]:  # Check if the answer is correct
            score += 1

    print(f"Your score: {score}/{len(questions)}")
    save_quiz_result(user_name, score)

    connection.close()

if __name__ == "__main__":
    main()
