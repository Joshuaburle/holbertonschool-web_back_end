import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(req, res) {
    const database = process.argv[2];

    readDatabase(database)
      .then((fieldGroups) => {
        let output = 'This is the list of our students\n';
        const fields = Object.keys(fieldGroups).sort(
          (a, b) => a.toLowerCase().localeCompare(b.toLowerCase()),
        );

        fields.forEach((field) => {
          const list = fieldGroups[field].join(', ');
          output += `Number of students in ${field}: ${fieldGroups[field].length}. List: ${list}\n`;
        });

        res.status(200).send(output.trim());
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    const database = process.argv[2];

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    readDatabase(database)
      .then((fieldGroups) => {
        const list = fieldGroups[major] ? fieldGroups[major].join(', ') : '';
        res.status(200).send(`List: ${list}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
