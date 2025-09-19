const redis = require('redis');

// Création du client
const client = redis.createClient();

client.on('error', (err) => console.log('Redis client not connected to the server:', err));
client.on('connect', () => {
  console.log('Redis client connected to the server');

  // Supprimer la clé si elle existe pour avoir le même output
  client.del('HolbertonSchools', redis.print);

  // Création du hash
  client.hset('HolbertonSchools', 'Portland', 50, redis.print);
  client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
  client.hset('HolbertonSchools', 'New York', 20, redis.print);
  client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
  client.hset('HolbertonSchools', 'Cali', 40, redis.print);
  client.hset('HolbertonSchools', 'Paris', 2, redis.print);

  // Afficher le hash
  client.hgetall('HolbertonSchools', (err, obj) => {
    if (err) console.error(err);
    else console.log(obj);
  });
});
