document.getElementById('nav-select').addEventListener('change', function() {
    if (this.value) {
      window.location.href = this.value;
    }
  });
  // document.getElementById('nav-select').addEventListener('focus', function() {
  //   if (this.options[0].value === "") {
  //     this.remove(0);
  //   }
  // });