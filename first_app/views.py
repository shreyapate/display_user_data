import requests
from rest_framework.views import APIView
from django.http import HttpResponse

class GetUserDetails(APIView):
    def get(self, request):
        try:
            url = "https://jsonplaceholder.typicode.com/users"
            response = requests.get(url, headers={"Content-Type": "application/json"})

            if response.status_code == 200:
                users = response.json()
                modified_response = []

                for user in users:
                    res = {
                        "id": user.get("id"),
                        "name": user.get("name", ""),
                        "lat": user["address"]["geo"]["lat"],
                        "lng": user["address"]["geo"]["lng"],
                        "company_name": user["company"]["name"]
                    }
                    modified_response.append(res)

                return HttpResponse([modified_response])

            return HttpResponse("There was an error in getting response!")

        except Exception as e:
            return HttpResponse(f"error: {e}")
