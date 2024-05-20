CONTAINER_NAME=ngrok-local
HELP_CMDS = config token logs build run stop clean
config_DESC = Write default variables to .env and invoke update-token
token_DESC = Prompt for a token and update NGROK_AUTHTOKEN in the .env file
logs_DESC = Show logs of the running container 
build_DESC = Build the Docker image named $(CONTAINER_NAME)
run_DESC = Run the Docker container in detached mode with environment variables 
stop_DESC = Stop the running container
clean_DESC = Remove the Docker image
writemd_DESC = Write the help content to README.md in Markdown format
.PHONY: help config token logs build run stop clean writemd

help:
	@echo "Makefile commands:"
	@$(foreach cmd,$(HELP_CMDS), \
		echo "  make $(cmd) - $($(cmd)_DESC)"; \
	)

helpS:
	@echo "Makefile commands:"
	@echo "  make config - create a basic .env file"
	@echo "  make token  - update to your Ngrok.com token"
	@echo "  make logs   - Show logs of the running container named $(CONTAINER_NAME)"
	@echo "  make build  - Build the Docker image named $(CONTAINER_NAME)"
	@echo "  make run    - Run the Docker container named $(CONTAINER_NAME) in detached mode with environment variables from .env file"
	@echo "  make stop   - Stop the running container named $(CONTAINER_NAME)"
	@echo "  make clean  - Remove the Docker image named $(CONTAINER_NAME)"

build:
	docker build -t $(CONTAINER_NAME) .

run:
	docker run -d --rm --env-file .env --name $(CONTAINER_NAME) -t $(CONTAINER_NAME)

logs:
	docker logs $$(docker ps -q -f name=$(CONTAINER_NAME))

stop:
	docker stop $(CONTAINER_NAME)

clean:
	docker image rm $(CONTAINER_NAME)

token:
	@if [ ! -e .env ]; then\
		echo Please run first: make bootstrap; exit 1; \
	else  \
		echo "Paste your token or CTRL+C to cancel:";\
		read TOKEN; \
		if [ ! -z "$$TOKEN" ]; then \
			if grep 'NGROK_AUTHTOKEN=' .env 2>&1 >/dev/null  ; then \
	       		sed -i "s/NGROK_AUTHTOKEN=.*/NGROK_AUTHTOKEN=$$TOKEN/" .env ;\
			else echo "NGROK_AUTHTOKEN=$$TOKEN" >> .env;\
			fi;\
		else \
			echo "A token needs to be provided" && exit 1; \
		fi;\
	fi;

config:
	@echo "PORT=11434" > .env
	@echo "CONTAINER_NAME=ngrok-local" >> .env
	@echo "IMAGE_NAME=ngrok-local" >> .env
	@make update-token

writemd:
	@echo "# Makefile Commands" > README.md
	@echo "" >> README.md
	@$(foreach cmd,$(HELP_CMDS), \
		echo "## $(cmd)" >> README.md; \
		echo "$($(cmd)_DESC)" >> README.md; \
		echo "" >> README.md; \
	)

