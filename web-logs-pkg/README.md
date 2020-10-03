# WebLogs
A python package to stream live logs of any application(s) on browser using flask

# Installation
The package can be installed using pip by typing the pollowing-
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
            "logName" : "Log 1",
            "logPath" : "Log1.log"
        },
        {
            "logName" : "Log 2",
            "logPath" : "log2.log" 
        },
        {
            "logName" : "Log 3",
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

### Todos

 - Write Tests
 - Add Night Mode
 - Make new working with Cookie cutter


License
----

MIT