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

client.hSet('HolbertonSchools', 'Portland', '50', print);
client.hSet('HolbertonSchools', 'Seattle', '80', print);
client.hSet('HolbertonSchools', 'New York', '20', print);
client.hSet('HolbertonSchools', 'Bogota', '20', print);
client.hSet('HolbertonSchools', 'Cali', '40', print);
client.hSet('HolbertonSchools', 'Paris', '2', print);

client.hGetAll('HolbertonSchools', function (error, result) {
  if (error) {
    console.log(error);
    throw error;
  }
  console.log(result);
});
