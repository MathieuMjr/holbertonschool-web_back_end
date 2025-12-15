export default function getStudentIdsSum(studentList) {
  const sum = studentList.reduce((acc, element) => acc + element.id, 0);
  return sum;
}