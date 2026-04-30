export default class HolbertonClass {
    constructor(size, location) {
        this.size = size;
        this.location = location;
    }

    get size() {
        return this._size;
    }

    get location() {
        return this._location;
    }

    set size(value) {
        if (typeof value !== 'number') {
            throw new TypeError('size must be a number');
        }
        this._size = value;
    }

    set location(value) {
        if (typeof value !== 'string') {
            throw new TypeError('location must be a string');
        }
        this._location = value;
    }

    [Symbol.toPrimitive](hint) {
        if (hint === 'number') {
            return this._size;
        }
        return this._location;
    }
}
