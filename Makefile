OPENAPI_SPEC ?= openapi/openapi.yaml
USER_ID := $(shell id -u)
GROUP_ID := $(shell id -g)

all: indexes bundle lint

indexes:
	docker run --rm --user $(USER_ID):$(GROUP_ID) \
		-e HOME=/tmp \
		-w / \
		-v ./specs:/specs \
		-v ./tool:/tool \
		python:3.11-slim \
		bash -c "pip install --no-cache-dir --user -r /tool/requirements.txt && PATH=/tmp/.local/bin:\$$PATH python /tool/generate_indexes.py"

bundle:
	docker run --rm --user $(USER_ID):$(GROUP_ID) \
		-v ./specs:/spec \
		-v ./$(OPENAPI_SPEC):/gen/openapi.yaml \
		-v ./redocly.yaml:/redocly.yaml:ro \
		redocly/cli:2.40.0 \
		bundle openapi.yaml --config /redocly.yaml --force --ext yaml -o /gen/openapi.yaml 2> /dev/null

lint:
	docker run --rm --user $(USER_ID):$(GROUP_ID) \
		-v ./$(OPENAPI_SPEC):/spec/openapi.yaml \
		-v ./redocly.yaml:/redocly.yaml:ro \
		redocly/cli:2.40.0 \
		lint --config /redocly.yaml --lint-config error openapi.yaml
