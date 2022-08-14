"""FastAPI is a blazing fast, simple, and flexible API Framework for Python."""

from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from enum import Enum


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    vgg = "vgg"


templates = Jinja2Templates(directory='static/templates')


async def homepage(request):
    return templates.TemplateResponse('index.html', {'request': request})

routes = [
    Route('/', endpoint=homepage),
    Mount('/static', StaticFiles(directory='static'), name='static')
]

app = Starlette(debug=True, routes=routes)
