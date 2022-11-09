// 현재 다음페이지로 넘어가는 버튼의 onclick에 Storage에 저장하는 jvs 함수들을 다 빼놓은 상태
// 이유 -> 나중에 필요하면 함수다시 작성하고 각페이지마다 비활성화 주석되어있는 script에 static 활성화해주면될듯함.
// 위치는 </body>의 아래있는 commment 주석임. 모든 페이지 위치 동일

function sessionDirectorDataImport() {
  let selected_director = document.getElementById("selected_director").value;
  sessionStorage.setItem("selected_director", selected_director);
}

function sessionGenreDataImport() {
  let selected_genre = document.getElementById("selected_genre").value;
  sessionStorage.setItem("selected_genre", selected_genre);
}

function sessionActorsDataImport() {
  let selected_actor1 = document.getElementById("selected_actor1").value;
  let selected_actor2 = document.getElementById("selected_actor2").value;
  let selected_actor3 = document.getElementById("selected_actor3").value;
  sessionStorage.setItem("selected_actor1", selected_actor1);
  sessionStorage.setItem("selected_actor2", selected_actor2);
  sessionStorage.setItem("selected_actor3", selected_actor3);
}

function sessionNationsOpendtAuditDataImport() {
  let selected_actor1 = document.getElementById("selected_nations").value;
  let selected_actor3 = document.getElementById("selected_opendt").value;
  let selected_actor2 = document.getElementById("selected_audit").value;
  sessionStorage.setItem("selected_nations", selected_actor1);
  sessionStorage.setItem("selected_opendt", selected_actor2);
  sessionStorage.setItem("selected_audit", selected_actor3);
}

// 어디에써야할지 모르겠는 Storage에서 key로 value 꺼내올 때 사용하는 jvs
// sessionStorage.getItem("selected_director")
// sessionStorage.getItem("selected_genre")
// sessionStorage.getItem("selected_actor1")
// sessionStorage.getItem("selected_actor2")
// sessionStorage.getItem("selected_actor3")
// sessionStorage.getItem("selected_nations")
// sessionStorage.getItem("selected_opendt")
// sessionStorage.getItem("selected_audit")

// 결과페이지에서 버튼을 클릭했을때 toggle을 해서 스타일을 변경하는 방식으로
// hidden을 없애는 방식
$(function () {
  $("#btn_salesAcc").click(function () {
    $(".SalesToggle").toggle();
  });
  $("#btn_audiAcc").click(function () {
    $(".AudiToggle").toggle();
  });
});
