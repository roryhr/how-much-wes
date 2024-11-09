.PHONY: dev test

dev:
	source activate py312 && flask --app main --debug run   

test:
	source activate 312 && pytest