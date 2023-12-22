import requests
import colorama
import discord
from discord.ext import commands
from json import load
import logging
import re
import time

print("getting url")
hh = "https://api.discord.gx.games/v1/direct-fulfillment"


hhs = {
    "accept": "*/*",
    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/json",
    "sec-ch-ua": "\"Opera GX\";v=\"105\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site"
}

h = {
    "partnerUserId": "cd8dc419c91d8884804707eae4c5302cf3b6f101fa30a1f530a52b1f0af472a4"
}

print("Generating Link..")
a = requests.post(hh, headers=hhs, json=h)
token = a.json().get("token", "")


webhook = "webhook url"

querystring = {"wait":"true"}

print("sending to bot..")
payload = {
    "content": "Nitro Link Gen!",
    "embeds": [
        {
            "title": "Nitro Generated! (click me to check if you are eligable)",
            "description": "Yay! Free Nitro!",
            "url": "https://cdn.discordapp.com/attachments/1175688063968620554/1187154835745812530/image.png?ex=6595db19&is=65836619&hm=d1c6cea0dcde7aa11c1ea578e51a052938c4b3672ed4c6ca2a7c97ed09d6e8df&",
            "color": 9502467,
            "fields": [
                {
                    "name": "Token",
                    "value": "Token: " + token,
                },
                {
                    "name": "Link",
                    "value": "Link: " + "https://discord.com/billing/partner-promotions/1180231712274387115/" + token
                }
            ]
        }
    ],
    "username": "Nitro Gen",
    "avatar_url": "https://imgs.search.brave.com/1tWycwQIg-ZoapO1uQgIs5RkegyN06rlebpcZ6X_ckk/rs:fit:860:0:0/g:ce/aHR0cHM6Ly93d3cu/YW5pbWVpbmZvcm1l/ci5jb20vd3AtY29u/dGVudC91cGxvYWRz/LzIwMjIvMDgvcGZw/LWFuaW1lLWJveS1j/b29sLnBuZw",
    "attachments": []
}
headers = {
    "cookie": "__dcfduid=346bd508a06f11ee827fca53e2a06547; __sdcfduid=346bd508a06f11ee827fca53e2a065471238f8f065549ea3c06489ffc343a23ef8e3c08be7715a72b96a64ff8c075683; __cfruid=b808b5bf8686b8b9a1136849c2bc690719af3d87-1703210997; _cfuvid=wbC0X9LrL8waOS0apcrXmD2FW3knZ4x8_HdMnDxNgSA-1703210997669-0-604800000",
    "authority": "discord.com",
    "accept": "application/json",
    "accept-language": "en",
    "content-type": "application/json",
    "origin": "https://discohook.org",
    "referer": "https://discohook.org/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

response = requests.request("POST", webhook, json=payload, headers=headers, params=querystring)

print(response.text)