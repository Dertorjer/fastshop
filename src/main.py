from fastapi import FastAPI
from sqladmin import Admin
from fastapi.staticfiles import StaticFiles

from src.admin import BasketAdmin
from src.base_settings import base_settings
from src.general.databases.postgres import postgres
from src.general.views import router as status_router
from src.routes import BaseRoutesPrefixes

app = FastAPI(
    debug=base_settings.debug,
    docs_url=BaseRoutesPrefixes.swagger if base_settings.debug else None,
    redoc_url=BaseRoutesPrefixes.redoc if base_settings.debug else None,
    openapi_url=BaseRoutesPrefixes.openapi if base_settings.debug else None,
)

app.mount("/static", StaticFiles(directory="static"), name="static")


def include_routes(application: FastAPI) -> None:
    application.include_router(
        router=status_router,
    )


@app.on_event('startup')
async def startup():
    postgres.connect(base_settings.postgres.url)
    engine = postgres.get_engine()
    admin = Admin(app=app, engine=engine)

    admin.add_view(BasketAdmin)



@app.on_event('shutdown')
async def shutdown():
    await postgres.disconnect()


include_routes(app)
