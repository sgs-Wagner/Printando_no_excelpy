import funcoes
import pandas as pd
import xlwings as xw

def main():
	dados = {
	'nome': ['wagner', 'souza', 'gomes', 'silva'],	
	'idade': [21, 22, 23, 30],
	'cargo': ['pf', 'pm', 'pc', 'as'],
	}

	df = pd.DataFrame(dados)
	wb = xw.Book(r'C:\Users\Souza\Desktop\silva\tela.xlsx')
	layout = wb.sheets["Plan1"]
	
	funcoes.exibirdf(df)
	funcoes.layout(df, layout)

if __name__ == "__main__":
	main()