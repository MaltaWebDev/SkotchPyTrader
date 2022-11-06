import websocket, json
import dateutil.parser

# create empty objects to count ticks into minutes
minutes_processed = {}
minute_candlesticks = []
current_tick = None
previous_tick = None
current_open = []
current_high = []
current_low = []
current_close = []

def on_open(ws):
  print("Opened connection!")

  subscribe_message = {
    "type": "subscribe",
    "channels": [
      {
        "name": "ticker", 
        # "product_ids": [f"{product_id}"]
        "product_ids": ["BTC-USD"]
      }
    ]
  }

  ws.send(json.dumps(subscribe_message))

def on_message(ws, message):
  # pull vars into scope
  global current_tick, previous_tick
  global minutes_processed, minute_candlesticks

  previous_tick = current_tick
  current_tick = json.loads(message)

  # parse the time and convert to a datetime object
  tick_datetime_object = dateutil.parser.parse(current_tick["time"])
  tick_dt = tick_datetime_object.strftime("%Y-%m-%dT%H:%M:%S")
  # print("{} @ {}".format(current_tick["price"], tick_dt))



socket = "wss://ws-feed.exchange.coinbase.com"

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
ws.run_forever()