from mysql.connector import errorcode
import mysql.connector

# GLOBAL VARIABLES

# Connection Details
config = {
    'host': 'localhost',
    'user': 'root',
    'password': '****',
    'database': 'school'
}

database_name = 'school'
databse_school = 'CREATE DATABASE {}'.format(database_name)
table_student = 'CREATE TABLE students (student_id INT PRIMARY KEY AUTO_INCREMENT, first_name VARCHAR(32) NOT NULL, last_name VARCHAR(32) NOT NULL, age INT NOT NULL, grade FLOAT NOT NULL)'
add_student = 'INSERT INTO students (first_name, last_name, age, grade) VALUES(%s, %s, %s, %s)'
upgrade_student = "UPDATE students SET grade = {} WHERE first_name = '{}'"
delete_student = "DELETE FROM students WHERE last_name = '{}'"

# function establish connection to database and return that connection
def make_connection():
    try:
        return mysql.connector.connect(**config)
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Something is wrong with your username or password')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print('Database does not exist')
        else:
            print(err)
    
    exit(1)


def insert_row():
    cnx = make_connection()

    with cnx.cursor() as cursor:
        first_name = input('Enter first name: ')
        last_name = input('Enter last name: ')

        age = int(input('Enter age: '))
        while age < 5 and age > 18:
            print('Student age must be between 5 and 18', end = '\n\n')
            age = int(input('Enter age: '))

        grade = float(input('Enter grade: '))
        while grade < 1 and grade > 100:
            print('Please enter valid grade', end='\n\n')
            grade = float(input('Enter grade: '))

        data_student = (first_name, last_name, age, grade)
        cursor.execute(add_student, data_student)
        
    cnx.commit()
    cnx.close()


def upgrade_grade():
    print('As assignment mention only grade can upgrade based on first_name')

    cnx = make_connection()
    with cnx.cursor() as cursor:
        first_name = input('Enter first name: ')

        new_grade = float(input('Enter new grade: '))
        while new_grade < 1 and new_grade > 100:
            print('Please enter valid grade', end='\n\n')
            new_grade = float(input('Enter new grade: '))

        cursor.execute(upgrade_student.format(new_grade, first_name))
        
    cnx.commit()
    cnx.close()


def delete_record():
    print('As assignment mention row can deleted based on last_name')
    cnx = make_connection()

    with cnx.cursor() as cursor:
        last_name = input('Enter last name: ')
        cursor.execute(delete_student.format(last_name))
        
    cnx.commit()
    cnx.close()


def fetch_records():
    cnx = make_connection()

    with cnx.cursor() as cursor:
        cursor.execute('SELECT * FROM students')
        rows = cursor.fetchall()
        
        for row in rows:
            print(row)

    cnx.close()


def table_exist():
    connection = make_connection()

    with connection.cursor() as cursor:
        cursor.execute('SHOW TABLES')
        rows = cursor.fetchall()

        if ('students', ) not in rows:
            print('Table does not exist')
            print('Creating table students')

            cursor.execute(table_student)

    connection.close()

def menu():
    print('========================================MENU========================================')
    print('i -> INSERT RECORD')
    print('u -> UPDATE RECORD')
    print('d -> DELETE RECORD')
    print('s -> DISPLAY ALL RECORD')
    print('q -> quit')

    choice = input('Enter command: ').lower()
    while choice not in ('i', 'u', 'd', 's', 'q'):
        print('Please enter valid choice')
        choice = input('Enter command: ').lower()

    return choice

if __name__ == '__main__':
    # check whether students table exist or not
    table_exist()

    running = True
    while running:
        choice = menu()

        if   choice == 'q':
            running = False
        elif choice == 'i':
            insert_row()
        elif choice == 'u':
            upgrade_grade()
        elif choice == 'd':
            delete_record()
        elif choice == 's':
            fetch_records()

        print(end="\n\n")