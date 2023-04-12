import { v4 as uuidv4 } from 'uuid';

interface WebSocketMessage {
    connection_id: string,
    function_name: string,
    args: any[]
}

export class WebSocketClient {
    private socket: WebSocket;
    private connectionId: string;
    private messageQueue: WebSocketMessage[];

    constructor(url: string) {
        this.socket = new WebSocket(url);
        this.connectionId = uuidv4();
        this.messageQueue = [];
        this.init();
    }

    private async init() {
        await this.connect();
        //Process any queued messages
        while (this.messageQueue.length > 0) {
            const message = this.messageQueue.shift();
            await this.send(message!.connection_id, message!.function_name, ...message!.args);
        }
    }

    private async connect() {
        const connected = new Promise((resolve) => {
            this.socket.onopen = () => {
                resolve(this.socket.OPEN);
            };
        });
        await connected;
        this.socket.onmessage = (event) => {
            const data = JSON.parse(event.data);
            const connectionId = data.connection_id;
            const result = data.result;
            //Handle result for function call by connection ID
        };
    }

    public async send(connectionID: string, functionName: string, ...args: any[]): Promise<any> {
        const message: WebSocketMessage = {
            connection_id: connectionID,
            function_name: functionName,
            args: args
        };

        if (this.socket.readyState === WebSocket.OPEN) {
            const response = new Promise((resolve) => {
                this.socket.onmessage = (event) => {
                    const data = JSON.parse(event.data);
                    if (data.connection_id === connectionID && data.function_name === functionName) {
                        resolve(data.result);
                    }
                };
            });

            this.socket.send(JSON.stringify(message));
            return response;
        } else {
            this.messageQueue.push({
                connection_id: connectionID,
                function_name: functionName,
                args: args
            });
        }
    }

    public getConnectionId(): string {
        return this.connectionId;
    }
}