# flask_6_api_management
This is assignment #6 for HHA 504

### Setting up the flask enpoint:
I copied the entire code from the flask folder -- app_basic.py (located in Professor Hants' git)
From there I updated the code so that it defaults to 'fahima' instead of 'world' and also return a json object intsead of a string. 

### Testing the flask endpoint:
I then installed all the requirements and ran python3 app_flask.py 
I then added /hello to the end of the url and received the json object. 

### Documentation of my API:

Document of the endpoint is below: 
 ```
    This is an example hello world function that takes in a name and if it is not provided it uses Fahima
    ---
    parameters:
      - name: name
        in: query
        type: string
        required: false
        default: Fahima
    responses:
      200:
        description: Returns a JSON object with a message that says ```Hello `name`!```
```


### Steps and observations on Azure API Management integration:
I followed the tutorial provided in the instructions of this assignment. 
The first step was to install "core tool packages using brew" 
I used the following command:
```
brew tap azure/functions
brew install azure-functions-core-tools@4
# if upgrading on a machine that has 2.x or 3.x installed:
brew link --overwrite azure-functions-core-tools@4
```
Then I initiated a azure function using the following command:
```
func init LocalFunctionProj --python -m V2
```
I then went to the project folder using this command: 
```
cd LocalFunctionProj
```
I copied this code into the functions_app.y file 
```
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="HttpExample")
@app.route(route="hello")
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("HttpExample function processed a request!")
```

I then followed by this command: 
```
func start
```
This is where I ran into issues. 
After doing some research, I followed the instructions in this page: [https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=macos%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-csharp#x86-emulation-on-arm64](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt).

I had to run my terminal in Rosetta and then restarted my laptop. From there, I had to reinstall brew, python, and all the azure tools.

Then for deployment, I used the commands from week 2.  
1. I first went into this URL: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt
2. I copied and pasted this code into my terminal to install azure: curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
3. To ensure azure was installed I used this command: az
4. I then used this code to login: az login --use-device-code
5. I was provided with a url and a code in my terminal.
I copied the code and went into the url and inserted the code in the space provided. 
I used this code to get the subscription id: az account list --output table
which gave me the student subscription ID
I then used this code with the provided student subscription ID: az account set --subscription (my subscription ID)
I then went into the LocalFunctionProj folder by using the following command: cd LocalFunctionProj.
From here I created the azure function app using the following command:
```
az functionapp create --resource-group Fahima504  --runtime python --runtime-version 3.9 --functions-version 4 --name fahima-azure-function --os-type linux --storage-account fahimastorageaccount --consumption-plan-location america
```
I then published the app using the following command: `func azure functionapp publish fahima-azure-function`
This is when I faced an issue where the URL was not working and the function was not being deployed. 
I later realized this is because of two things:
- One unused import of flask that I removed 
- I needed to change the http_auth_level to be ANONYMOUS so I didn't need an api key to access the function
These two changes fixed the issue, and once I ran `func azure functionapp publish fahima-azure-function` the application was available at [https://fahima-azure-function.azurewebsites.net/api/hello](https://fahima-azure-function.azurewebsites.net/api/hello).