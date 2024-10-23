.PHONY: dev test

dev:
	source activate py38 && flask --app main --debug run   

test:
	source activate py38 && pytest