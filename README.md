# WebLogs
Weblogs is a python package that gives you capability of streaming logs to the browser. It's a tail -F with UI. Multiple logs from different paths can be added by providing the details in a json file. 

# Installation
The package can be installed using pip by typing the following-
```sh
pip3 install weblogs
```


## Usage
The package uses a json file to get the path and names of multiple Log files. The Json file need not be in the Project directory but it is still recommended to keep it there to prevent accidental deletion. To initilize the package you will be required to provide the full path of the json file. An example json file is given below -
example.json
```
{
    "logs" : [
        {
            "logName" : "Logs 1",
            "logPath" : "Log1.log"
        },
        {
            "logName" : "Logs 2",
            "logPath" : "log2.log" 
        },
        {
            "logName" : "Logs 3",
            "logPath" : "log3.log" 
        }
    ]
}
```
The Log file needs to be in text editable format.


After installing the package, go the the main directory where you would like to have your project created and then type the following-

```sh
weblogsadmin create path/to/json
```

## Screenshot
![Main Page](https://user-images.githubusercontent.com/19774313/93512859-90c1d000-f942-11ea-82b0-69042f5ce68e.png)

