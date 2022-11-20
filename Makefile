e2etest:
	pytest tests/e2e -s --gherkin-terminal-reporter -vv --html=report.html --capture=tee-sys