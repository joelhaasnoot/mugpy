import requests


class Mugpy:
    base_url = "https://cloud.heymugsy.com/v2/api/"

    user_id = None
    machine_id = None
    auth_key = None

    def __init__(self, user_id, auth_key, machine_id):
        self.user_id = user_id
        self.machine_id = machine_id
        self.auth_key = auth_key

    def coffee_now(self):
        """
            Brew coffee now with the default recipe
            :return Boolean with status result
        """
        params = {"userID": self.user_id, "machineID": self.machine_id, "authKey":self.auth_key}
        response = requests.get(self.base_url+"alexa/coffeeNowCloud.php", params=params)
        if response.ok:
            return True
        else:
            print("Error while making coffee: "+response.content)
            return False

