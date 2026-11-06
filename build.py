# Convierte kreova.html (formato artifact) en index.html completo para GitHub Pages.
import pathlib, sys
here = pathlib.Path(__file__).resolve().parent
src = (here / "kreova.html").read_text(encoding="utf-8")
head, body = src.split("</style>", 1)
out = f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex, nofollow">
<style>[hidden]{{display:none!important}} body{{margin:0}} img{{max-width:100%}}</style>
{head}</style>
</head>
<body>
{body.strip()}
</body>
</html>
"""
(here / "index.html").write_text(out, encoding="utf-8")
print("index.html listo", len(out), "bytes")
