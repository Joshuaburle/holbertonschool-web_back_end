const fs = require('fs');

const readDatabase = (path) => new Promise((resolve, reject) => {
  fs.readFile(path, 'utf8', (err, data) => {
    if (err) {
      reject(new Error('Cannot load the database'));
      return;
    }

    const students = data.split('\n');
    const fieldGroups = {};

    students.forEach((element) => {
      const result = element.split(',');
      if (element !== '' && result[0] !== 'firstname') {
        const domain = result[3];
        if (!fieldGroups[domain]) {
          fieldGroups[domain] = [];
        }
        fieldGroups[domain].push(result[0]);
      }
    });

    resolve(fieldGroups);
  });
});

export default readDatabase;
