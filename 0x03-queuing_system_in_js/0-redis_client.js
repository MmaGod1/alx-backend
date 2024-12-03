import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

// Listen for error event
client.on('error', (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});
