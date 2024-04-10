local:
	sanic src.stupid_api.server:app -p 7777 --dev --debug --workers=1 --access-log

build:
#	@rm requirements*
	@poetry export -f requirements.txt --output requirements.txt --without-hashes --without-urls
	@docker-compose build

up:
	@docker-compose up -d --remove-orphans --build

down:
	@docker compose down

logs:
	@docker compose logs -f

push:
	@docker push alancota/stupid-api:rc1

make hub: build push