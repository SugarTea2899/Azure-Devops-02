from locust import HttpUser, task

class Test(HttpUser):
    
    @task
    def check_azure_prediction(self):
        self.client.post("/predict", json = {
            "CHAS":{
                "0":0
            },
            "RM":{
                "0":6.575
            },
            "TAX":{
                "0":291.0
            },
            "PTRATIO":{
                "0":12.3
            },
            "B":{
                "0":393.9
            },
            "LSTAT":{
                "0":2.98
            }
        })
