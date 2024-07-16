import Currency from "./3-currency";

export default class Pricing {
    constructor(amount, currency) {
        this._amount = amount;
        this._currency = currency;

        if (typeof this._amount !== 'number') {
            throw new TypeError('Amount must be a number');
        }
        if (!(this._currency instanceof Currency)) {
            throw new TypeError('Currency must be a Currency');
        }
    }

    get amount() {
        return this._amount;
    }

    get currency() {
        return this._currency;
    }

    set amount(newAmount) {
        this._amount = newAmount;
    }

    set currency(newCurrency) {
        this._currency = newCurrency;
    }

    displayFullPrice() {
        return `${this._amount} ${this._currency.displayFullCurrency()}`;
    }

    static convertPrice(amount, conversionRate) {
        return amount * conversionRate;
    }
}