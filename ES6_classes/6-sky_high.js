import Building from './5-building';

export default class SkyHighBuilding extends Building {
    constructor(sqft, floors) {
        super(sqft);
        this._floors = floors;

        if (typeof this.__sqft !== 'number') {
            throw new TypeError('Sqft must be a number');
        }

        if (typeof this._floors !== 'number') {
            throw new TypeError('Floors must be a number');
        }
    }
    get sqft() {
        return this._sqft;
    }

    get floors() {
        return this._floors;
    }

    evacuationWarningMessage() {
        return `Evacuate slowly the ${this._floors} floors!`;
    }
}