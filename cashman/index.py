from flask import Flask, jsonify, request

from cashman.model.expense import Expense, ExpenseSchema
from cashman.model.income import Income, IncomeSchema
from cashman.model.transaction_type import TransactionType

app = Flask(__name__)

transactions = [
	Income('Salary', 5000),
	Income('Dividends', 200),
	Expense('pizza', 50),
	Expense('Rock Concert', 100)
]


@app.route('/incomes')
def get_incomes():
	schema = IncomeSchema(many=True)
	incomes = schema.dump(
		filter(lambda t: t.type == TransactionType.INCOME, transactions)
	)
	return jsonify(incomes.data)

@app.route("/incomes", methods=['POST'])
def hello_world():
	incomes.append(request.get_json())
	return '', 204

