import websocket, json

def on_open(ws):
  print("Opened connection!")

  subscribe_message = {
    "type": "subscribe",
    "channels": [
      {
        "name": "ticker", 
        "product_ids": ["BTC-USD"]
      }
    ]
  }

  ws.send(json.dumps(subscribe_message))


def on_message(ws, message):
  print("Received message!")
  print(json.loads(message))

socket = "wss://ws-feed.exchange.coinbase.com"

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
ws.run_forever()