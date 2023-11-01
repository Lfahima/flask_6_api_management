# flask_6_api_management
This is assignment #6 for HHA 504
setting up flask enpoint :

i copied your flsk app_basic.py fom there i updated it so that it defauls to fahima instea of world and also return a json object intsea dof a string. 

testing:
i then installed all the requirnemnt and ran python3 app_flask.py. i then added /hello to the end of the url and received the json obkject 

doc of th endpoint is below 
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


Steps and observations on Azure API Management integration.
i followed the tuoroial provided in the instruction oif assibment 
the forst steap was to install core tool packahges used brew 
i used the following command :
```
brew tap azure/functions
brew install azure-functions-core-tools@4
# if upgrading on a machine that has 2.x or 3.x installed:
brew link --overwrite azure-functions-core-tools@4
```
then i intinated a azure funtion usieung the following command
```
func init LocalFunctionProj --python -m V2
```

i then went to the project folder using this command 
```
cd LocalFunctionProj
```

I copiied this code into the functions_app.y file 
```
import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="HttpExample")
@app.route(route="hello")
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse("HttpExample function processed a request!")
```

I then did 
```
func start
```
and ran into issues. I followed the instructions in this page : [https://learn.microsoft.com/en-us/azure/azure-functions/functions-run-local?tabs=macos%2Cisolated-process%2Cnode-v4%2Cpython-v2%2Chttp-trigger%2Ccontainer-apps&pivots=programming-language-csharp#x86-emulation-on-arm64](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt).

I had to run my terminal in Rosetta and then restarted my laptop. From there I had reinstall brew, python, and all the azure tools.

then for deoployment i used this commands from week 2 
i first went into this URL: [https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt)
and got this code :
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
which gave me a code and i TYPED THAT CODE INTO THE WEBSITE.
I then pasted this code: az to make sure it was installed. 
I used this code to login: az login --use-device-code
I used this code to get the subscription id: az account list --output table
which gave me the student subscriptn iD 
I then used this code az account set --subscription (my subscription id)
I then went into the LocalFunctionProj folder by using the following command : cd LocalFunctionProj.
From here I created the azure function app using the following command:
```
az functionapp create --resource-group Fahima504  --runtime python --runtime-version 3.9 --functions-version 4 --name fahima-azure-function --os-type linux --storage-account fahimastorageaccount --consumption-plan-location america
```
I then published the app using the following command: `func azure functionapp publish fahima-azure-function`.
This is when I faced an issue where the URL was not working and the function was not being deployed. I realized this is because of two things:
- One unused import of flask that I removed 
- I needed to change the http_auth_level to be ANONYMOUS so I didn't need an api key to access the function.
These two changes fixed the issue and once I ran `func azure functionapp publish fahima-azure-function` the application was available at [https://fahima-azure-function.azurewebsites.net/api/hello](https://fahima-azure-function.azurewebsites.net/api/hello).

