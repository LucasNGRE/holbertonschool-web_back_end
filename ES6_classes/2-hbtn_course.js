export default class HolbertonCourse {
    constructor(name, length, students) {
        this._name = name;
        this._length = length;
        this._students = students;

        if (typeof this._name !== 'string') {
            throw new TypeError('Name must be a string');
          }
          if (typeof this._length !== 'number') {
            throw new TypeError('Length must be a number');
          }
          if (!Array.isArray(this._students) || !this._students.every(student => typeof student === 'string')) {
            throw new TypeError('Students must be an array of strings');
          }
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
  
    set name(newName) {
        this._name = newName;
    }
  
    set length(newLength) {
        this._length = newLength;
    }
  
    set students(newStudents) {
        this._students = newStudents;
    }
}