import handleProfileSignup from './6-final-user';

console.log(handleProfileSignup("Bob", "Dylan", "bob_dylan.jpg"));
handleProfileSignup("John", "Doe", "Gerald.jpg")
  .then(result => {
    console.log(result);
  });