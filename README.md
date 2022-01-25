# Battery Check
### WARNING: might not work on Windows or Linux
<br>
The app notifies you with a beep sound when your battery goes under 25 or over 75.  
  
These are the safest ranges for lithium ion batteries.  
  
<img src="ss.png" width="700">

  
You can configure the ranges with min and max vars in the main.py as:
```python
# CONFIGURE
min = 25
max = 75
```

## Run
### MacOS and Linux
```
pip3 install -r requirements.txt
```
```
python3 main.py
```
### Windows
```
pip install -r requirements.txt
```
```
python main.py
```
