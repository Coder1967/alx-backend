import 'redis';
client = redis.createClient();

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

client.subscribe("holberton school channel");

client.on('message', (err, msg) => {
  console.log(msg);
  if (msg === 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});

client.on('error', function(err) {
  console.log(`Redis client not connected to the server: ${err}`);
});
