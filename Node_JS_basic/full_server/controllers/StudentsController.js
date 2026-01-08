const readDatabase = require('../utils');

class StudentsController {
  static async getAllStudents(req, res) {
    res.status(200);
    res.write('This is the list of our students\n');
    try {
      const results = await readDatabase();
      const sortedResults = Object.fromEntries(
        Object.entries(results).sort(([fieldA], [fieldB]) => fieldA.toLowerCase()
          .localeCompare(fieldB.toLowerCase())),
      );
      let output = '';
      for (const key of Object.keys(sortedResults)) {
        output += `Number of students in ${key}: ${sortedResults[key].length}. List: ${sortedResults[key].join(', ')}\n`;
      }
      res.write(output);
      res.end();
    } catch (error) {
      res.write(error.message);
      res.end();
    }
  }

  static async getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    // récupère ce qui arrive depuis l'URL, par ex : /students:CS
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter mus be CS or SWE\n');
      return;
    }
    try {
      const results = await readDatabase();
      res.status(200).send(`List: ${results[major].join(', ')}`);
    } catch (error) {
      res.write(error.message);
      res.end();
    }
  }
}

module.exports = StudentsController;
