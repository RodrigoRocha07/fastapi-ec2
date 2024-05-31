from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message':'Hello World from CrudMaskers'}


@app.get('/test')
async def root():
    return {'message':'this is a test'}