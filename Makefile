ph20_3.pdf: ph20_3.tex w3fig2.png w3fig3.png
	pdflatex --interaction-mode=nonstop ph20_3.tex

w3fig2.png: week3.py
	python week3.py

w3fig3.png: week3.py
	python week3.py
