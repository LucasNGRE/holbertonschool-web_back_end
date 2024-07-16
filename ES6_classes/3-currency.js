export default class Currency {
    constructor(code, name) {
        this._code = code;
        this._name = name;

        if (typeof this._code !== 'string') {
            throw new TypeError('Code must be a string');
        }
        if (typeof this._name !== 'string') {
            throw new TypeError('Name must be a string');
        }
    }

    displayFullCurrency() {
        return `${this._name} (${this._code})`;
    }

    get code() {
        return this._code;
    }

    get name() {
        return this._name;
    }

    set code(newCode) {
        this._code = newCode;
    }

    set name(newName) {
        this._name = newName;
    }
}
