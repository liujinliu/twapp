# twapp 

------

tornado web app  

------

## Requirments

The fowlling modules should be installed:
> * tornado >= 4.2

## How to start server 
### 1. package build
```
make build
```
The package can be found under dist path, a whl package

### 2. install package
```
# virtualenv --no-site-packages dist/tmp
# source dist/tmp/bin/activate
# pip install dist/twapp*.whl
# twapp-start --help
Usage: twapp-start [OPTIONS]

Options:

  --help                           show this help information
  --base-dir                       put the config files here
  --debug                          debug option (default False)
  --port                           app listen port (default 8888)
```

### 3. start server
```
twapp-start
```
