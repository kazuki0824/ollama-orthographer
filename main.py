import json
from pickle import FALSE

import ollama


item_dict0 = {
    1: "BluetoothがOn",
    2: "ホーム画面のアイコン数が100以下",
    3: "WiFiが有効",
    4: "BTが有効",
    5: "BTペアリングしたデバイスが存在しない",
    6: "ホーム画面のアイコンが101以上",
    7: "Wifi, Bluetoothともにオン",
    8: "ホーム画面のアイコンが10以上",
    9: "ホーム画面のアイコンが100以下",
    10: "ホーム画面のアイコンが100未満"
}
answer0 = {
    1: "A",
    2: "B",
    3: "C",
    4: "A",
    5: "D",
    6: "~B",
    7: "A&C",
    8: "E"
}

item_dict1 = {
    1: "GAS有効",
    2: "ホーム画面のアイコン数がいっぱいではない",
    3: "CAN信号受信かつ現在通知が1つもない",
    4: "通知の数が0件"
}
answer1 = { 1: "A", 2: "B", 3: "C&D", 4: "D" }


predefined_prompt1 = fr'''Read each of the following unique ID and condition detail pairs and express the relationship as a boolean expression with simple alphabet(s) such as A, ~A, A&B.
The result is in JSON key-value pair of “unique Id”: “relationship expression”. 
Rules:
- give the same number to the items that mean the same thing (i.e., variants)
- put ~ in front of the number for the opposite, and negative meaning

Example:
{json.dumps(item_dict1, ensure_ascii=False)}
becomes
{json.dumps(answer1, ensure_ascii=False)}
.
'''

predefined_prompt2 = (f'Please process the following items in the same manner.'
                      f'The result is ONLY in JSON key-value pair of “unique Id”: “relationship expression”. '
                      f'Don\'t say anything but JSON. \n')


payload = predefined_prompt1 + predefined_prompt2 + json.dumps(item_dict0, ensure_ascii=False)
print(payload)

response1 = ollama.chat(model='llama3.1', messages=[
    {
        'role': 'user',
        'content': payload,
    },
])

result = json.loads(response1['message']['content'])
print(result)
print(result == answer0)