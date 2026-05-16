const http = require('http');
const fs = require('fs');

const database = process.argv[2];

function countStudents(path) {
  return fs.promises.readFile(path, 'utf8')
    .then((data) => {
      const lines = data
        .split('\n')
        .filter((line) => line.trim() !== '');

      const students = lines.slice(1);
      const fields = {};

      students.forEach((student) => {
        const studentData = student.split(',');
        const firstName = studentData[0];
        const field = studentData[3];

        if (!fields[field]) {
          fields[field] = [];
        }

        fields[field].push(firstName);
      });

      const output = [`Number of students: ${students.length}`];

      Object.keys(fields).forEach((field) => {
        const list = fields[field];

        output.push(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
      });

      return output.join('\n');
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  }

  if (req.url === '/students') {
    countStudents(database)
      .then((students) => {
        res.end(`This is the list of our students\n${students}`);
      })
      .catch((error) => {
        res.end(`This is the list of our students\n${error.message}`);
      });
  }
});

app.listen(1245);

module.exports = app;
