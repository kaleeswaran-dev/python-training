import urllib.request
import json

BASE_URL = "https://jsonplaceholder.typicode.com/"

def get_data(endpoint):
    url = f"{BASE_URL}/{endpoint}"

    with urllib.request.urlopen(url) as response:
        return json.load(response)


def create_data(endpoint):
    data = {
    "title": "Hello",
    "body": "This is my post",
    "userId": 1
}
    # python to converts json
    json_data = json.dumps(data).encode("utf-8")
    url = f"{BASE_URL}/{endpoint}"
    request = urllib.request.Request(
    url,
    data=json_data,
    headers={"Content-Type": "application/json"},
    method="POST"
)
    with urllib.request.urlopen(request) as response:
        result = json.load(response)

    print(result)


def getPost(endpoint):
    url = f"{BASE_URL}/{endpoint}"
    with urllib.request.urlopen(url) as response:
        return json.load(response)
    

   


def deletePost(endpoint):
    url=f"{BASE_URL}/{endpoint}"
    request = urllib.request.Request(
        url,
        method="DELETE"
    )
    with urllib.request.urlopen(request) as res:
        return res.status
def get_users():
    posts = get_data("users")
    responses = []
    for post in posts[:5]:
       responses.append( {
        "id": post["id"],
        "userName":post["username"],
        "email":post["email"]
    })
    return responses
    #
    # print(response ," response")

users = get_users()
print(users)

# get = create_data("posts")
# print("result " , get)

# getvalue = getPost("posts/1")
# print("result " , getvalue)

# delete = deletePost("posts/1")
# print("result " , delete)




def statuscode_meaning(statuscode):
    if statuscode == 200:
        print("succsuss")
    elif statuscode==201:
        print("user created")
    elif statuscode==404:
        print("user not found")
    elif statuscode==401:
        print("user not authendicated")
    elif statuscode==500:
        print("Internal server error")


code = statuscode_meaning(200)
print(code)






# sqlalgami


