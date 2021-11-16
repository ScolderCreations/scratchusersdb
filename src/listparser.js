function lpCreateList1() {
  fetch('https://scoldercreations.github.io/scratchusersdb/users.txt')
  .then(response => response.text())
  .then(data => var userstxt = data);

  userstxt = userstxt.split("\n");
  return userstxt
}

var scratchusersarray = lpCreateList1();
