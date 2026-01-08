const fs = require('fs');

function readDatabase() {
  return new Promise((resolve, reject) => {
    fs.readFile(process.argv[2], 'utf8', ((err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const results = {};

      const lines = data.split('\n'); // le fichier devient un tableau de ligne en se basant sur \n pour répartir les lignes
      const filteredLines = lines.filter((line) => line.trim() !== ''); // retirer les lignes vides
      const studentLines = filteredLines.slice(1);
      // on lit le tableau de ligne à partir de l'index 1 (sans les entêtes)

      for (const line of studentLines) { // pour chaque ligne...
        const content = line.split(','); // va faire un tableau en séparant les valeurs via la ','
        if (!(content[3] in results)) {
          results[content[3]] = [content[0]];
        } else {
          results[content[3]].push(content[0]);
        }
      }
      resolve(results);
    }));
  });
}

module.exports = readDatabase;
