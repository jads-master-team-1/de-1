.PHONY: init run/dev run/prod build/dev build/prod
.DEFAULT_GOAL := help

NAMESPACE := jads-master-team-1
NAME := de-1

help: ## Show this help
	@echo "${NAMESPACE}/${NAME}"
	@echo
	@fgrep -h "##" $(MAKEFILE_LIST) | \
	fgrep -v fgrep | sed -e 's/## */##/' | column -t -s##

##

init: ## Initialize the environment
	for f in services/*/*.txt; do \
		pip install -r "$$f"; \
	done

##

run/dev: ## Run development app
	docker-compose -p $(subst -,_,$(NAME))_dev -f docker-compose.dev.yml up

run/prod: ## Run production app
	docker-compose -p $(subst -,_,$(NAME))_prod -f docker-compose.prod.yml up

##

build/dev: ## Build development app
	docker-compose -p $(subst -,_,$(NAME))_dev -f docker-compose.dev.yml build

build/prod: ## Build production app
	docker-compose -p $(subst -,_,$(NAME))_prod -f docker-compose.prod.yml build
