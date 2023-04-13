# Reversi

In this branch I added wsServer.py to replace server.py, backendservicews.ts to replace backendservice.ts, 
and websocketclient.ts to support the new backendservice.

I also updated the VITE_API_BASE in \web\.env to use ws:// instead of http://.

The websocketclient.ts class is instantiated by backendservicews.ts with the server url (`${API_BASE}/ws`) 
and acts as a persistent connection for each instance of the web client using a uuidv4 to ensure a unique id. 
The class uses a message interface that includes the client id, function to call, and args as a json and 
handles the sending and response handling of the message. There is also a queue for calls in case a new event 
is triggered before a prior response is received.

The backendservicews.ts redefines the same functions we previously had but uses the WebSocketClient.send 
function to send them over the websocket.

The wsServer.py tracks a dict of active connections using a single endpoint (@app.websocket("/ws/") that 
redirects new websocket connections to an async websocket handler function, which adds it as an active 
connection and listens for a json message from that connection in the background. When a message does come, 
it parses the function name and args and passes them to the handle_function_call function which maps the data 
to the appropriate python functions, which accomplish the same this as before.

The result of the functions are then packaged into a json with only a result field and sent back over the
same websocket where the WebSocketClient is awaiting the response and parsing the result field for the 
GameData that will be returned by the backendservicews.ts functions.
