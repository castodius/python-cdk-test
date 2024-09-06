.PHONY: install test deploy destroy clean lint

VENV := .venv
VENV_ACTIVATE := ${VENV}/bin/activate

all: install

install:
	@(\
		python3 -m venv ${VENV}; \
		. ${VENV_ACTIVATE}; \
		pip install -r requirements.txt -r requirements-dev.txt; \
		npm ci; \
	)

test:
	@(\
		. ${VENV_ACTIVATE}; \
		pytest; \
	)

deploy:
	@(\
		. ${VENV_ACTIVATE}; \
		npx cdk deploy --path-metadata false --require-approval never; \
	)

destroy:
	@(\
		. ${VENV_ACTIVATE}; \
		npx cdk destroy --force; \
	)

clean:
	@(\
		rm -rf .venv; \
		rm -rf node_modules; \
		rm -rf cdk.out; \
	)

lint:
	@(\
		. ${VENV_ACTIVATE}; \
		ruff check; \
		ruff format; \
	)
