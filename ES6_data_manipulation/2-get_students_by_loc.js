export default function getStudentsByLocation(studentList, city) {
  const result = studentList.filter(element => element.location === city);
  return result;
}