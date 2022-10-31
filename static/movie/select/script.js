const input = document.querySelector(".finder__input");
const finder = document.querySelector(".finder");
const form = document.querySelector("form");

input.addEventListener("focus", () => {
  finder.classList.add("active");
});

input.addEventListener("blur", () => {
  if (input.value.length === 0) {
    finder.classList.remove("active");
  }
});

form.addEventListener("submit", (ev) => {
  ev.preventDefault();
  finder.classList.add("processing");
  finder.classList.remove("active");
  input.disabled = true;
  setTimeout(() => {
    finder.classList.remove("processing");
    input.disabled = false;
    if (input.value.length > 0) {
      finder.classList.add("active");
    }
  }, 1000);
});

function movieSelect() {
  let nations = document.getElementById('movieNations').value;
  let opendt = document.getElementById('movieOpenDt').value;
  let autidt = document.getElementById('movieAudit').value;
  document.getElementById('nations').value = nations;
  // document.getElementById('openDt').value = opendt;
  document.getElementById('audit').value = autidt;
  document.getElementById('movieSelect').submit();
  // alert('선택이 완료되었습니다.')
}