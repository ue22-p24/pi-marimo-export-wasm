import marimo

__generated_with = "0.14.9"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    return mo, pd


@app.cell
def _(mo):
    # to find the data, both from dev. runtime and from wasm export
    from pathlib import Path
    base_path = mo.notebook_location() or Path(".")
    return (base_path,)


@app.cell
def _(base_path, pd):
    csv_path = base_path / "public" / "titanic.csv"
    df = pd.read_csv(csv_path)
    return (df,)


@app.cell
def _(mo):
    mo.md(r"""# sélectionnez un genre""")
    return


@app.cell
def _(mo):
    dr = mo.ui.dropdown(['male', 'female'])
    dr
    return (dr,)


@app.cell
def _(mo):
    mo.md(r"""qui nous donne cette sélection""")
    return


@app.cell
def _(df, dr):
    extract = df[df.Sex == dr.value]
    df if len(extract) != 0 else "No match"
    return (extract,)


@app.cell
def _(mo):
    mo.md(r"""et ce graphique""")
    return


@app.cell
def _(extract, mo):
    mo.mpl.interactive(
        extract[['Age']].plot())
    return


@app.cell
def _(mo):
    mo.md(r"""## une parabole""")
    return


@app.cell
def _(mo):
    sl = mo.ui.slider(start=2, stop=10, step=1)
    sl
    return (sl,)


@app.cell
def _():
    import numpy as np
    import matplotlib.pyplot as plt
    return np, plt


@app.cell
def _(np, sl):
    X = np.linspace(-10, 10)
    Y = X**2 * sl.value
    return X, Y


@app.cell
def _(X, Y, mo, plt):
    fig, ax = plt.subplots()
    ax.set_ylim(0, 100)
    ax.plot(X, Y)

    mo.mpl.interactive(ax)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
