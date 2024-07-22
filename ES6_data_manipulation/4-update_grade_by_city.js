export default function updateStudentGradeByCity(students, city, newGrade) {
  if (!Array.isArray(students)) {
    return [];
  }
  return students
    .filter((student) => student.location === city)
    .map(student => {
        const gradeObject = newGrades.find(grade => grade.studentId === student.id);
        return {
          ...student,
          grade: gradeObject ? gradeObject.grade : 'N/A'
        };
      });
  }