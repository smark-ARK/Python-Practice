from cgitb import html
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

client_side = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Client</title>
</head>
<body>
    <h1>
        Simple Websockets Chat App
    </h1>
    <form action="" onsubmit="sendMessage(event)">
        <input type="text" id="message_text" autocomplete="off"/>
        <button>send</button>
        </form>
    <ul id="messages">


    </ul>
    <script>
        var ws=new WebSocket("ws://localhost:8000/ws");
        ws.onmessage=function(event){
            var messages=document.getElementById("messages")
            var message=document.createElement('li')
            var content=document.createTextNode(event.data)
            message.appendChild(content)
            messages.appendChild(message)
        };
        function sendMessage(event){
            var input=document.getElementById("message_text")
            ws.send(input.value)
            input.value=''
            event.preventDefault()
        }
    </script>
    
</body>
</html>"""


@app.get("/")
async def get():
    return HTMLResponse(client_side)


@app.websocket("/ws")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()
    while True:
        data = await ws.receive_text()
        await ws.send_text(data=f"message was: {data}")
