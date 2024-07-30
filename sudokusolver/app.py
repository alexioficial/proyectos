from flask import Flask, render_template, request
from solver import solve_sudoku

app = Flask(__name__)

@app.route('/')
def index():
    htmltable = ''
    for i in range(1, 10):
        htmltable += '<tr>'
        for j in range(1, 10):
            htmltable += f'<td id="c_{i}_{j}"><input type="text" id="i_{i}_{j}"></td>'
        htmltable += '</tr>'
    return render_template('Solver.html', htmltable = htmltable)

@app.post('/Solve')
def Solve():
    try:
        data = request.get_json()['d']
        solve_sudoku(data)
        return {'estatus': 0, 'res': data}
    except Exception as e:
        return {'estatus': 1, 'msj': str(e)}