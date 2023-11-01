import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="hello")
def hello_get(req: func.HttpRequest) -> func.HttpResponse:
    user = req.params.get("user")
    if not user:
        user = "Fahima"
    if user:
        return func.HttpResponse(f'Hello {user}!');