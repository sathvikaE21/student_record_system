from flask import Flask, render_template, request, redirect
import mysql.connector
from db_config import get_db_connection

app = Flask(__name__)

@app.route('/')
def index():
    sort_by = request.args.get('sort_by', 'roll_no')
    conn = get_db_connection()
    cursor = conn.cursor()
    query = f"SELECT * FROM student ORDER BY {sort_by} ASC"
    cursor.execute(query)
    students = cursor.fetchall()
    conn.close()
    return render_template('index.html', students=students)


@app.route('/add', methods=['POST'])
def add_student():
    roll_no = int(request.form['roll_no'])
    name = request.form['name']
    grade = request.form['grade']
    marks = int(request.form['marks'])
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO student VALUES (%s, %s, %s, %s)", (roll_no, name, grade, marks))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/update', methods=['POST'])
def update_student():
    roll_no = int(request.form['roll_no'])
    marks = int(request.form['marks'])
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE student SET marks = %s WHERE roll_no = %s", (marks, roll_no))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete', methods=['POST'])
def delete_student():
    roll_no = int(request.form['roll_no'])
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM student WHERE roll_no = %s", (roll_no,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
