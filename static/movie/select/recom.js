// 자동완성 봉인.
// $(document).ready(function () {
//   //   $(".search_input").keydown(function () {
//   //     $(".search_input").css("background-color", "yellow");
//   //   });
//   const searchInput = document.querySelector(".search_input");

//   searchInput.addEventListener("keyup", (e) => {
//     let findWord = searchInput.value;
//     console.log(findWord);
//     searchFindTitleAjax();
//   });
// });

// function searchFindTitleAjax() {
//   $.ajax({
//     type: "GET",
//     url: "/movie/recommendation/autofind/",
//     data: {
//       searchTitle: $(".search_input").val(),
//     },
//     datatype: "json",
//     success: function (data) {
//       console.log(data);

//       //   $('.auto_title').val() = data
//     },
//   });
// }

// $("searchInput").autocomplete({
//   source: function (request, response) {
//     $.ajax({
//       url: "/movie/recommendation/autofind/",
//       type: "GET",
//       data: {
//         searchTitle: $(".search_input").val(),
//       },
//       success: function (data) {
//         response(
//           $.map(data, function (item) {
//             return {
//               label: item.movienm,
//               value: item.movienm,
//               idx: item.movienm,
//             };
//           })
//         ); // response
//       },
//       error: function () {
//         alert("통신에 실패했습니다.");
//       },
//     });
//   },
//   minLength: 2,
//   autoFocus: false,
//   select: function (evt, ui) {
//     console.log("전체 data:" + JSON.stringify(ui));
//     console.log("db Index : " + ui.item.idx);
//     console.log("검색 데이터:" + ui.item.value);
//   },
//   focus: function (evt, ui) {
//     return false;
//   },
//   close: function (evt) {},
// });

$(document).ready(function () {
  $("#similarityDesc").click(function () {
    $("#currentOption").text("유사도 내림차순");
  });
  $("#similarityAsc").click(function () {
    $("#currentOption").text("유사도 오름차순");
  });
  $("#voteAverageDesc").click(function () {
    $("#currentOption").text("평점 내림차순");
  });
  $("#voteAverageAsc").click(function () {
    $("#currentOption").text("평점 오름차순");
  });
  $("#releaseDateDesc").click(function () {
    $("#currentOption").text("상영일 내림차순");
  });
  $("#releaseDateAsc").click(function () {
    $("#currentOption").text("상영일 오름차순");
  });
  $("#sortSearch").click(function () {
    let criteria = $("#currentOption").text();
    // console.log($("#searchInput").val());
    $("#criteriaInput").val(criteria);
    $("#sortSearchWord").val($("#searchInput").val());
    // console.log($("#criteriaInput").val());
    $("#sortCriteriaForm").submit();
  });
});
