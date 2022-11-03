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

// 감독 선택을 위한 js
function TableDirector(e) {
  // e.innerHTML로 DOM 안의 텍스트를 가져와서 .trim()으로 앞뒤 불필요한 공백을 지워준다.
  selected_director = e.innerHTML.trim();
  // 필요한 텍스트 파일인 selected_director를 사용하여 id가 selected_director인 곳에 value로 집어넣어준다.
  document.getElementById("selected_director").value = selected_director;
}
// 장르 선택을 위한 js
function TableGenre(e) {
  selected_genre = e.innerHTML.trim();
  document.getElementById("selected_genre").value = selected_genre;
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
}
// 배우 선택을 취소하기 위한 js
function DeleteSelectActor1() {
  let input = document.getElementById("selected_actor1");
  input.value = null;
}
function DeleteSelectActor2() {
  let input = document.getElementById("selected_actor2");
  input.value = null;
}
function DeleteSelectActor3() {
  let input = document.getElementById("selected_actor3");
  input.value = null;
}

function searchFormCheck(searchWord, pageNumber) {
  document.getElementById("searchWord").value = searchWord;
  document.getElementById("page").value = pageNumber;
  document.getElementById("pageForm").submit();
}
