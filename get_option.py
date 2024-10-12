import polars as pl

class Option:
    def __init__(self, type_op, dte, strike, price=0.0):
        self._data = [type_op, dte, strike, price]

    def get_quote(self, date):
        # Formato "2024-01-03"
        ano, mes, dia = date.split('-')
        file = "HIST_DATA/" + ano + "/" + str(int(mes)) + ".csv"
        interp = pl.read_csv(file).filter(pl.col("[QUOTE_DATE]") == date)
        interp = interp.filter(pl.col("[DTE]") <= self._data[1])
        
        return interp


if __name__ == "__main__":
    minha_opcao = Option('C', 90, 1000)
    print(minha_opcao.get_quote('2014-06-30'))
    #print(search(90, 0.3))
