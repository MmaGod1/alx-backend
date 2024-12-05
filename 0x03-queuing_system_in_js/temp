import { createClient, print } from 'redis';

const client = createClient();

(async () => {
  client.on('connect', function() {
    console.log('Redis client connected to the server');
});

  client.on('error', function(error) {
    console.log(`Redis client not connected to the server: ${error}`);
  });
  await client.connect();
})();

client.hset(
  'HolbertonSchools',
  'Portland', '50',
  'Seattle', '80',
  'New York', '20',
  'Bogota', '20',
  'Cali', '40',
  'Paris', '2',
  print
);

client.hgetall('HolbertonSchools', function (error, result) {
  if (error) {
    console.log(error);
    throw error;
  }
  console.log(result);
});
