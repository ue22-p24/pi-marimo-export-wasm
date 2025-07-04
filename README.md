# a sample marimo project that runs as a wasm static website

## export

```bash
marimo export html-wasm titanic.py -o export --mode run
```

## run dev server

```bash
python -m http.server --directory export
```

## open the web page
```
http://localhost:8000
```

## Important limitations: no xlsx support

in real life we ended up with a code that could not avoid loading data from a xlsx file;  
turns out we've never been able to get that one to run as a wasm static website,
because `pd.read_excel()` function relies on features (namely the `pyopenxl`
library) that are not available as wasm.
