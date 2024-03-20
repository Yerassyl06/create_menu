import fastapi
from database.db import main_menu

api = fastapi.FastAPI()

@api.get('/', include_in_schema=False)
async def redirect_to_api_docs():
    return fastapi.responses.RedirectResponse(url=api.docs_url)

@api.get('/get_menu_id/{id:int}')
async def get_menu_id(id):
    return main_menu['menu'][id-1]

@api.put('/menu_item')
async def put_data():
    num = int(input())
    for i in range(num):
        menu_item = input()
    print('how much item do you want to order?:', num)
    print(menu_item)


