import websocket, json

def on_open(ws):
  print("Opened connection!")

  subscribe_message = {
    "type": "subscribe",
    "channels": [
      {
        "name": "ticker", 
        "product_ids": [f"{product_id}"]
      }
    ]
  }

  ws.send(json.dumps(subscribe_message))


def on_message(ws, message):
  print("Received message!")
  print(json.loads(message))

# accept user input for the product ID
product_id = input("Enter a product ID: ")

# accept user input for the timeframe
timeframe = input("Enter a timeframe: ")


socket = "wss://ws-feed.exchange.coinbase.com"

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
ws.run_forever()