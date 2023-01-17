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
