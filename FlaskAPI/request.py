import requests

URL = "http://0.0.0.0:8080/predict"
headers = {"Content-Type": "application/json"}
data = {"input": "./test_input.csv", "mdl": "./models/rf_mae_f1_est30.pkl"}

r = requests.get(URL, headers=headers, json=data)

print("Predicted salary: $%.1fk" % r.json()["response"])
