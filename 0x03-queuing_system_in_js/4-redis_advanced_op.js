const redis = require('redis');
client = redis.createClient();

client.on('connect', function() {
  console.log('Redis client connected to the server');
  main();
});

client.on('error', function(err) {
  console.log(`Redis client not connected to the server: ${err}`);
});

function setHash(hashName, fieldName, fieldValue) {
  client.hset(hashName, fieldName, fieldValue, (err, reply) => {
	  redis.print("Reply: " + reply);
  });
};

function printHash(hashName) {
  client.HGETALL(hashName, (err, reply) => console.log(reply));
};

function main() {
	
  const hash = {
	  Portland: 50,
	  Seattle: 80,
	  'New York': 20,
	  Bogota: 20,
	  Cali: 40,
	  Paris: 2,
  };
  for (const [field, value] of Object.entries(hash)) {
    setHash('HolbertonSchools', field, value);
  }
  printHash('HolbertonSchools');
};
