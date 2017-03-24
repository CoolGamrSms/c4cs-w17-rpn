#!/usr/bin/env python3

from flask import Flask, render_template
import sys, operator

app = Flask(__name__)

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '_': operator.truediv,
    '^': operator.pow,
    '%': operator.mod,
}

def easter_egg(arg):
    return arg[::-1]

def calculate(arg):
    if '1337' in arg:
        return easter_egg(arg)

    stack = list()
    for operand in arg.split():
        try:
            operand = float(operand)
            stack.append(operand)
        except:
            arg2 = stack.pop()
            arg1 = stack.pop()
            operator_fn = OPERATORS[operand]
            result = operator_fn(arg1, arg2)

            stack.append(result)
    return stack.pop()

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/calc/<query>")
def calc_route(query):
	print("CALCULATING: "+query)
	result = ''
	try:
		result = str(calculate(query));
	except:
		result = 'ERROR'
	return result

if __name__ == '__main__':
    app.run(host='192.168.0.35', port=3000)
