// document.getElementById('nav-select').addEventListener('change', function() {
//     if (this.value) {
//       window.location.href = this.value;
//     }
//   });
//   // document.getElementById('nav-select').addEventListener('focus', function() {
//   //   if (this.options[0].value === "") {
//   //     this.remove(0);
//   //   }
//   // });


function handleSelectChange(event) {
  if (event.target.value) {
    window.location.href = event.target.value;
  }
}

// function handleSelectFocus(event) {
//   if (event.target.options[0].value === "") {
//     event.target.remove(0);
//   }
// }

document.getElementById('nav-select1').addEventListener('change', handleSelectChange);
document.getElementById('nav-select2').addEventListener('change', handleSelectChange);

// document.getElementById('nav-select1').addEventListener('focus', handleSelectFocus);
// document.getElementById('nav-select2').addEventListener('focus', handleSelectFocus);
