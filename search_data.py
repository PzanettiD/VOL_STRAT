import polars as pl

def search(dte, dist):
    consolidado = pl.read_csv("HIST_DATA/consolidado.csv")
    consolidado = consolidado.filter(((pl.col("[STRIKE]")) / (pl.col("[UNDERLYING_LAST]")) <= (dist + 0.005)))
    consolidado = consolidado.filter(((pl.col("[STRIKE]")) / (pl.col("[UNDERLYING_LAST]")) >= (dist - 0.005)))
    consolidado = consolidado.filter((pl.col("[DTE]") >= dte-2) & (pl.col("[DTE]") < dte+2))
    return consolidado

print(search(90, 0.9).select(["[QUOTE_READTIME]", "[STRIKE]", "[UNDERLYING_LAST]", "[STRIKE_DISTANCE_PCT]", "[DTE]"]))
