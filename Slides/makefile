tex = $(wildcard *.tex)
pdfs = $(tex:%.tex=%.pdf)

all: $(pdfs)

%.pdf: %.tex
	pdflatex $<
	../Scripts/generate_website.py
	rm *aux
	rm *log
	rm *nav
	rm *out
	rm *snm
	rm *toc
	rm *vrb
