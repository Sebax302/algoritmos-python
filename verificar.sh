#!/usr/bin/env bash
raiz="$(cd "$(dirname "$0")" && pwd)"; ok=0; mal=0
for f in "$raiz"/bloque_*/*.py; do if python3 -c "import ast,sys; ast.parse(open(sys.argv[1],encoding='utf-8').read())" "$f"; then ok=$((ok+1)); else echo "ERROR: $f"; mal=$((mal+1)); fi; done
echo "Válidos: $ok | fallos: $mal"; exit $((mal>0))
