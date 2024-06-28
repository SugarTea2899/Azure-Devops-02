from locust import HttpUser, task

class Test(HttpUser):
    
    @task
    def check_azure_prediction(self):
        data = {
            "features": {
                "CHAS": 0,
                "RM": 6.575,
                "TAX": 296.0,
                "PTRATIO": 15.3,
                "B": 396.9,
                "LSTAT": 4.98
            }
        }
        self.client.post("/predict", json=data)
