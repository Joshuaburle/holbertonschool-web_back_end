export default class HolbertonCourse {
    constructor(name, length, students) {
        this.name = name;
        this.length = length;
        this.students = students;
    }

    get name() {
        return this._name;
    }

    get length() {
        return this._length;
    }

    get students() {
        return this._students;
    }

    set name(value) {
        if (typeof value !== 'string') {
            throw new TypeError('name must be a string');
        }
        this._name = value;
    }

    set length(value) {
        if (typeof value !== 'number') {
            throw new TypeError('length must be a number');
        }
        this._length = value;
    }

    set students(value) {
        if (!Array.isArray(value)) {
            throw new TypeError('students must be an array');
        }
        this._students = value;
    }
}
