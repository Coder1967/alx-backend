import 'redis';
client = redis.createClient();

client.on('connect', function() {
  console.log('Redis client connected to the server');
});

function publishMessage(message, time) {
  setTimeout(function() {
    console.log("About to send" + message);
    client.publish('holberton school channel', message);
  }, time);
}
client.on('error', function(err) {
  console.log(`Redis client not connected to the server: ${err}`);
});

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
