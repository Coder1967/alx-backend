import 'redis';
import 'util';

client = redis.createClient();

client.on('connect', async function() {
  console.log('Redis client connected to the server');
  await main();
});

client.on('error', function(err) {
  console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, (err, reply) => {
	  redis.print('Reply: ' + reply);
  });
};

function displaySchoolValue(schoolName) {
  client.get(schoolName, (err, data) => {
  console.log(data);
  });
};
util.promisify(displaySchoolValue);

async function main() {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
}
