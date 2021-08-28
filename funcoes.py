import pandas as pd
import xlwings

def exibirdf(df):
	print(df)
	print("\n funcao so com pandas \n")
	filtro = ['nome', 'cargo']
	df = df[filtro]
	print(df)

def layout(df, layout):
	filtro = ['nome', 'cargo']
	filtro_df = df[filtro]
	layout["B1"].options(pd.DataFrame, header=1, index=False, expand='table').value = filtro_df


if __name__ == "__main__":
	exibir(df)
	layout(df, layout)