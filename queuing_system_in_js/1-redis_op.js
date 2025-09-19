// 1-redis_op.js
const redis = require('redis');

// Création du client
const client = redis.createClient();

client.on('error', (err) =>
  console.log('Redis client not connected to the server:', err)
);

client.on('connect', () => {
  console.log('Redis client connected to the server');

  // Fonction pour définir une valeur (callback style)
  function setNewSchool(schoolName, value, cb) {
    client.set(schoolName, value, (err, reply) => {
      if (err) {
        console.error(err);
        if (cb) cb(err);
        return;
      }
      console.log('Reply: OK'); // équivalent à redis.print
      if (cb) cb();
    });
  }

  // Fonction pour récupérer une valeur (callback style)
  function displaySchoolValue(schoolName, cb) {
    client.get(schoolName, (err, reply) => {
      if (err) {
        console.error(err);
        if (cb) cb(err);
        return;
      }
      console.log(reply);
      if (cb) cb();
    });
  }

  // 1. Créer la clé Holberton
  client.set('Holberton', 'School', redis.print);

  // 2. Afficher Holberton, puis créer HolbertonSanFrancisco et l'afficher
  displaySchoolValue('Holberton', () => {
    setNewSchool('HolbertonSanFrancisco', '100', () => {
      displaySchoolValue('HolbertonSanFrancisco');
    });
  });
});
