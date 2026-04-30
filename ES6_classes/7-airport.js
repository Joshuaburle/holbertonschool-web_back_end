export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  // Customize primitive conversion (used by console.log and toString)
  [Symbol.toStringTag]() {
    return this._code;
  }

  toString() {
    return `[object ${this._code}]`;
  }
}
