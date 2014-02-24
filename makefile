# MAKEFILE for Electron Beam AIMS Paper

# Ultimate target is the pdf
# all: ElectronBeamAIMS.pdf

# Create .pdf from .tex list
# (run pdflatex-bibtex sequence to accomodate references)
ElectronBeamAIMS.pdf: ElectronBeamAIMS.tex
	pdflatex -shell-escape ElectronBeamAIMS
	bibtex ElectronBeamAIMS
	pdflatex -shell-escape ElectronBeamAIMS
	pdflatex -shell-escape ElectronBeamAIMS

$
# Clean up unneccessary dependencies by running "make clean"
.PHONY: clean

clean:
	-rm *.dvi *.log *.toc *.aux *.out *.bbl *.blg *.spl *~
	-rm ElectronBeamAIMS.pdf
