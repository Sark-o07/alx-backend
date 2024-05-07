import {createClient} from 'redis';

const client = createClient();

client.on('error', err => {
	console.log(`Redis client not connected to the server: ${err}`);
}).on('connect', () => {
	console.log('Redis client connected to the server');
});

// Subscribe to holberton school channel
client.subscribe('holberton school channel');

// Listen for messages on channels and print the message when received
client.on('message', (channel, message) => {
	console.log(`${message}`);
	if (message === 'KILL_SERVER') {
		// Unsubscribe from channel and end server connection.
		client.unsubscribe('holberton school channel');
		client.end(true);
	}
});
