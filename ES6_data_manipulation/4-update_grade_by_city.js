export default function updateStudentGradeByCity(studentList, location, newGrades) {
 const filtered = studentList.filter(element => element.location === location)
 const result = filtered.map(element => {
  const match = newGrades.find(item => item.studentId === element.id);
  const newElement = {...element};
  if (match) {
    newElement.grade = match.grade;
  } else {
    newElement.grade = 'N/A';
  }
  return newElement;
  });
 return result;
}