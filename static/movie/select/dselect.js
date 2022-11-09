window.onload = function () {
  // // 페이징에 사용한 모든 a 태그를 가져와서 변수에 저장.
  // let a_list = document.getElementsByClassName("page-link");
  // // 위 a 태그를 반복하면서 클릭 이벤트를 적용.
  // Array.from(a_list).forEach(function (e) {
  //   e.addEventListener("click", function () {
  //     // a 태그에 클릭이 발생하면, a 태그에 작성된 data-page 속성 값을
  //     // 검색창 양식 내 input type=hidden에 저장.
  //     document.getElementById("page").value = this.dataset.page;
  //     // 검색 양식을 제출해서 뷰로 전달.
  //     document.getElementById("searchForm").submit();
  //   });
  // });
};

////////////////////무기입방지
// 감독선택후 무기입 방지
function selectDataDirector() {
  let selected_director = document.getElementById("selected_director").value;

  if (selected_director == 0 || selected_director == "") {
    alert("감독을 선택하시고 완료버튼을 눌러주세요.");
    return false;
  }

  document.getElementById("selected_director_hidden_input").value = selected_director;
  // alert("선택이 완료되었습니다.");
  sessionStorage.setItem("selected_director", selected_director);
  document.getElementById("selectedDirectorForm").submit();
}

// 장르 선택 후 무기입 방지
function selectDataGenre() {
  let selected_genre = document.getElementById("selected_genre").value;

  if (selected_genre == 0 || selected_genre == "") {
    alert("장르를 선택하시고 완료버튼을 눌러주세요");
    return false;
  }

  document.getElementById("selected_genre_hidden_input").value = selected_genre;
  sessionStorage.setItem("selected_genre", selected_genre);
  // alert("선택이 완료되었습니다.");
  document.getElementById("selectedGenreForm").submit();
}

// actor1, actor2, actor3 무기입 방지
function selectDataActors() {
  let selected_actor1 = document.getElementById("selected_actor1").value;
  let selected_actor2 = document.getElementById("selected_actor2").value;
  let selected_actor3 = document.getElementById("selected_actor3").value;

  if (selected_actor1 == 0 || selected_actor1 == "" || selected_actor2 == 0 || selected_actor2 == "" || selected_actor3 == 0 || selected_actor3 == "") {
    alert("세 명의 배우 모두를 선택해주세요.");
    return false;
  }

  document.getElementById("selected_actor1_hidden_input").value = selected_actor1;
  document.getElementById("selected_actor2_hidden_input").value = selected_actor2;
  document.getElementById("selected_actor3_hidden_input").value = selected_actor3;
  // alert("선택이 완료되었습니다.");
  document.getElementById("selectedActorsForm").submit();
}

function selectDataNationsAuditOpendt() {
  let selected_nations = document.getElementById("movieNations").value;
  let selected_opendt = document.getElementById("movieOpenDt").value;
  let selected_audit = document.getElementById("movieAudit").value;
  // if (selected_nations == 0 || selected_nations =="" || selected_opendt == 0 || selected_opendt =="" || selected_audit == 0 || selected_audit =="") {
  //   alert("모든 선택사항을 골라주세요.")
  //   return false;
  // }

  document.getElementById("selected_nations_hidden_input").value = selected_nations;
  document.getElementById("selected_opendt_hidden_input").value = selected_opendt;
  document.getElementById("selected_audit_hidden_input").value = selected_audit;
  alert("모든 선택이 완료되었습니다.\n결과를 확인해 보실까요?");
  document.getElementById("selectedNationsOpendtAuditForm").submit();
}
////////////////////무기입방지

// 감독 선택을 위한 js
function TableDirector(e) {
  // e.innerHTML로 DOM 안의 텍스트를 가져와서 .trim()으로 앞뒤 불필요한 공백을 지워준다.
  let selected_director = e.innerHTML.trim();
  // 필요한 텍스트 파일인 selected_director를 사용하여 id가 selected_director인 곳에 value로 집어넣어준다.
  document.getElementById("selected_director").value = selected_director;
  //감독을 선택하면 선택했다는 텍스트를 넣어준다.
  $(".showDirectors>span").text("감독을 선택하셨습니다.");
}
// 장르 선택을 위한 js
function TableGenre(e) {
  let selected_genre = e.innerHTML.trim();
  document.getElementById("selected_genre").value = selected_genre;
  document.getElementById("genre").value = selected_genre;
  // document.getElementById("pageForm").submit();
  //장르를 선택하면 선택했다는 텍스트를 넣어준다.
  $(".showGenres>span").text("장르를 선택하셨습니다.");
}
// 배우 선택을 위한 js
function TableActor(e) {
  selected_actor = e.innerHTML.trim();
  let fill_actor1 = document.getElementById("selected_actor1").value;
  let fill_actor2 = document.getElementById("selected_actor2").value;
  let fill_actor3 = document.getElementById("selected_actor3").value;
  
  if (fill_actor1 == 0 || fill_actor1 == "") {
    document.getElementById("selected_actor1").value = selected_actor;
    document.getElementById("actor1").value = selected_actor;
  } else if (fill_actor2 == 0 || fill_actor2 == "") {
    document.getElementById("selected_actor2").value = selected_actor;
    document.getElementById("actor2").value = selected_actor;
  } else {
    fill_actor3 = document.getElementById("selected_actor3").value;
    document.getElementById("selected_actor3").value = selected_actor;
    document.getElementById("actor3").value = selected_actor;
  }
  document.getElementById("pageForm").submit();
  // 배우를 선택하면 선택했다는 텍스트를 넣어준다.
  // $(".showActors>div>sbmit").text("배우를 선택하셨습니다.");
  // $('.showSelect').css({
  //   "border-bottom": "2px solid white"
  // });
}
// 배우 선택을 취소하기 위한 js
function DeleteSelectActor1() {
  let input = document.getElementById("selected_actor1");
  let input2 = document.getElementById("actor1");
  input.value = null;
  input2.value = null;
  document.getElementById("pageForm").submit();
}
function DeleteSelectActor2() {
  let input = document.getElementById("selected_actor2");
  let input2 = document.getElementById("actor2");
  input.value = null;
  input2.value = null;
  document.getElementById("pageForm").submit();
}
function DeleteSelectActor3() {
  let input = document.getElementById("selected_actor3");
  let input2 = document.getElementById("actor3");
  input.value = null;
  input2.value = null;
  document.getElementById("pageForm").submit();
}
// 배우 선택을 취소하기 위한 js 끝

// 페이징을 클릭하면 검색했던 내용을 pageForm에 제출하기 위한 js
function searchFormCheck(searchWord, pageNumber) {
  document.getElementById("searchWord").value = searchWord;
  document.getElementById("page").value = pageNumber;
  document.getElementById("pageForm").submit();
}

