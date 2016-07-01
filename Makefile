run:
	python test.py --debug > results.jsonl
	cat results.jsonl | postproc/stats.py > stats.jsonl
	cat stats.jsonl   | postproc/table.py

install:
	pip install -r requirements.txt
