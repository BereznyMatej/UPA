SHELL = /usr/bin/env bash
NAME = CSV_structures
LOGIN = xberez03_xvaloo00_xsvenk00

========================
all:
    latex $(NAME).tex
    dvips -t a4 $(NAME).dvi
    ps2pdf $(NAME).ps
========================

zip:
    zip $(LOGIN)-fit.zip *.tex Makefile

clean:
    rm -f $(NAME).{aux,dvi,log,pdf,ps} $(LOGIN)-fit.zip