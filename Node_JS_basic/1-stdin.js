const readline = require('readline');

// Créer une interface de lecture pour la saisie utilisateur
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Afficher le message de bienvenue
console.log('Welcome to Holberton School, what is your name?');

// Lire la réponse de l'utilisateur
rl.question('', (name) => {
  // Afficher le nom de l'utilisateur
  console.log(`Your name is: ${name}`);

  // Fermer l'interface de lecture
  rl.close();
});

// Afficher un message de fermeture lorsque le programme se termine
rl.on('close', () => {
  console.log('This important software is now closing');
});
