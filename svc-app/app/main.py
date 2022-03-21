from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import motor.motor_asyncio

origins = [
    "*",
    "http://localhost",
    "http://localhost:*",
]


app = FastAPI(
    title="Jira Cloud Backup Tool API",
    description="descr", # DESCRIPTION
    version="1.0.0", #
    openapi_url="/api/v1/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS", "*"],
    allow_headers=["*"],
)



@app.on_event("startup")
async def startup():
    conn_str = "mongodb://jira_user:jira_password@svc-mongo:27017/jira_backup"
    client = motor.motor_asyncio.AsyncIOMotorClient(conn_str, serverSelectionTimeoutMS=5000)
    try:
        print(await client.server_info())
    except Exception:
        print("Unable to connect to the server.")
    return


@app.on_event("shutdown")
async def shutdown():
    return


@app.get("/", summary="RestAPI index")
async def index():
    return {"methods": [
        {"GET /": "index method"},
    ]}



if __name__ == "__main__":
    print("RUN ME LIKE from folder upper than `/app` LIKE: uvicorn app.main:app --reload --port 8002")
    quit()
    # OR you can try two bottom lines for debug reasons 
    # import uvicorn
    # uvicorn.run("main:app", host="0.0.0.0", port=8002, reload=True, debug=True, use_colors=True)
