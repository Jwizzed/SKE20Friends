import requests
print("ใส่ชื่อเล่น แล้ว space แล้ว ชื่อเล่น กี่คนก็เอาเล้ย ถ้าไม่ขึ้น คือใส่ชื่อผิดไม่ก็ไม่ได้ลงชื่อเล่นไว้")
response = requests.get("https://api.sheety.co/8efde9fae6e32c3008a5325368a6de23/friends/name")
ask_name = input("Enter a nickname: ").lower()
for i in response.json()['name']:
    try:
        for j in ask_name.split():
            if i[f'nickname'].lower() == j.lower():
                print(f"No: {i['no']}")
                print(f"Nisit_Id: {i['รหัสนิสิต']}")
                print(f"Name: {i['ชื่อ-นามสกุล']}")
                print(f"Email: {i['emailGoogle']}")
                print(f"Office_Email: {i['emailOffice365']}")
                print(f"Nickname: {i['nickname']}")
                print("-----------")
    except KeyError:
        pass