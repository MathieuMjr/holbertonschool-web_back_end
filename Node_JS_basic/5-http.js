const { createServer } = require('node:http');
const fs = require('fs');

const hostname = '127.0.0.1';
const port = '1245';

// Function that parse csv
function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', ((err, data) => {
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
          results[content[3]] = { students_nb: 1, students_list: [content[0]] };
        } else {
          results[content[3]].students_nb += 1;
          results[content[3]].students_list.push(content[0]);
        }
      }
      resolve(results);
    }));
  });
}

const app = createServer((req, res) => {
  if (req.url === '/') {
    res.statusCode = 200;
    res.setHeader('Content-type', 'text/plain');
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.statusCode = 200;
    res.setHeader('Content-type', 'text/plain');
    countStudents('database.csv')
      .then((results) => {
        const totalStudents = Object.values(results)
          .reduce((sum, field) => sum + field.students_nb, 0);
        res.write('This is the list of our students\n');
        res.write(`Number of students: ${totalStudents}\n`);
        for (const [key, value] of Object.entries(results)) {
          res.write(`Number of students in ${key}: ${value.students_nb}. List: ${value.students_list.join(', ')}\n`);
        }
        res.end();
      })
      .catch((error) => {
        res.statusCode = 500;
        res.end(error.message);
      });
  }
});

module.exports = app;

app.listen(port, hostname, () => {
  console.log('Coucou les roudoudoux !');
});
