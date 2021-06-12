.DEFAULT_GOAL := run

# Set up Python virtual environment
.PHONY: venv
venv:
	@if [ ! -d ".venv" ]; then python3 -m venv .venv; fi
	@source $$(pwd)/.venv/bin/activate; pip install -U pip; pip install -r requirements.txt;
	@echo "Python virtual environment has been installed/updated."
	@echo "Run 'source .venv/bin/activate' to activate."

.PHONY: venv-dev
venv-dev:
	@source $$(pwd)/.venv/bin/activate; pip install -U pip; pip install -r requirements-dev.txt;
	@echo "Python virtual environment has been installed/updated with development requirements."
	@echo "Run 'source .venv/bin/activate' to activate."

# Build Docker image
.PHONY: build
build: merge.py Dockerfile
	@docker build -t $$USER/merge-intervals:$(shell git rev-parse HEAD) -t $$USER/merge-intervals:latest .

# Run with example data
.PHONY: run
run: merge.py
	@if [ -d ".venv" ]; then source $$(pwd)/.venv/bin/activate; fi
	python merge.py --verbose "[1,3]" "[5,6]" "[3,9]" "[13,20]"

# Run tests
.PHONY: test
test: test_merge.py
	@if [ -d ".venv" ]; then source $$(pwd)/.venv/bin/activate; fi
	python test_merge.py

# Run profiling
.PHONY: profile
profile: merge.py profile.sh
	@if [ -d ".venv" ]; then source $$(pwd)/.venv/bin/activate; fi
	@./profile.sh
