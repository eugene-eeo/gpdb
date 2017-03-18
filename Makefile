run: sim plot

sim:
	python test.py --debug > results.jsonl

plot:
	cat results.jsonl | postproc/plot.py
	cat results.jsonl | postproc/stats.py > stats.jsonl
	cat stats.jsonl   | postproc/table.py

install:
	pip install -r requirements.txt
