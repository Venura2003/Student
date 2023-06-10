from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

students = []

@app.route('/')
def index():
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        grade = request.form['grade']
        student = {'name': name, 'age': age, 'grade': grade}
        students.append(student)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    del students[student_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
