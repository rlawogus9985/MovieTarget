window.onload = function () {
  // 페이징에 사용한 모든 a 태그를 가져와서 변수에 저장.
  let a_list = document.getElementsByClassName("page-link");

  // 위 a 태그를 반복하면서 클릭 이벤트를 적용.
  Array.from(a_list).forEach(function (e) {
    e.addEventListener("click", function () {
      // a 태그에 클릭이 발생하면, a 태그에 작성된 data-page 속성 값을
      // 검색창 양식 내 input type=hidden에 저장.
      document.getElementById("page").value = this.dataset.page;
      // 검색 양식을 제출해서 뷰로 전달.
      document.getElementById("searchForm").submit();
    });
  });
};
