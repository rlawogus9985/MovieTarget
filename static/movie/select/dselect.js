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
  if (selected_nations == 0 || selected_nations =="" || selected_opendt == 0 || selected_opendt =="" || selected_audit == 0 || selected_audit =="") {
    alert("모든 선택사항을 골라주세요.")
    return false;
  }
  else {
    document.getElementById("selected_nations_hidden_input").value = selected_nations;
    document.getElementById("selected_opendt_hidden_input").value = selected_opendt;
    document.getElementById("selected_audit_hidden_input").value = selected_audit;
    alert("모든 선택이 완료되었습니다.\n결과를 확인해 보실까요?");
    document.getElementById("selectedNationsOpendtAuditForm").submit();}
}
////////////////////무기입방지

// 감독 선택을 위한 js
function TableDirector(e) {
  // e.innerHTML로 DOM 안의 텍스트를 가져와서 .trim()으로 앞뒤 불필요한 공백을 지워준다.
  let selected_director = e.innerText.trim();
  // 필요한 텍스트 파일인 selected_director를 사용하여 id가 selected_director인 곳에 value로 집어넣어준다.
  document.getElementById("selected_director").value = selected_director;

  // 수정해보려고함 2023 01 09 아래
  // 이메일 등록 관련 모달창 관련 자바스크립트 코드 - 시작점에서 null값이 출력이되서 click event객체가 없었음
  // 질문 결과 위에서 제이쿼리 객체로 사용했으면 아래에서 바닐라자바스크립트에서 dom get element 사용시 값을 가져올 수 없다고함.
  // 그래서 제이쿼리 대신에 자바스크립트 바닐라코드로 변경
  // const spanShowDirectors = document.querySelector("span#showDirectorsSpan")
  // spanShowDirectors.textContent = "감독을 선택하셨습니다.";

  //감독을 선택했을 때 css
  // let showcss = document.getElementsByClassName("showSelect")
  // showcss.css({"background-image": "linear-gradient(45deg, #ff6d2f 0%, #ff2f20 100%)",
  // "border-radius": "25px"});

  $(".showSelect").css({"background-image": "linear-gradient(45deg, #ff6d2f 0%, #ff2f20 100%)",
  "border-radius": "25px"});
}

// 장르 선택을 위한 js
function TableGenre(e) {
  let selected_genre = e.innerText.trim();
  document.getElementById("selected_genre").value = selected_genre;
  document.getElementById("genre").value = selected_genre;
  // document.getElementById("pageForm").submit();

  //장르를 선택했을 때 css
  
  $(".showSelect").css({"background-image": "linear-gradient(45deg, #ff6d2f 0%, #ff2f20 100%)",
  "border-radius": "25px"});

}

// 배우 선택을 위한 js
let name = []
function TableActor(e) {
  // selected_actor = e.innerText.trim();
  // let fill_actor1 = $(this);

  // 신입사원이 아닌 배우의 중복된 체크
  if(e != '신입 배우' ) {
    for(let i=0; i<name.length; ++i) 
      if(name[i] === e ) {return;}
    }
  name.push(e);

  if(name.length > 3) {
    return;
  }

  $.each(name, function(i, item) {
    let temp = $("#selected_actor"+(i+1)).val(item)
  //   let fill_actor = $(".show_actor"+(i+1));

  //   fill_actor.css({"background-image": "linear-gradient(45deg, #ff6d2f 0%, #ff2f20 100%)",
  // "border-radius": "25px"})
    let fill = document.getElementById("selected_actor"+(i+1))
    fill.className = "actos"
  })

  // 배우선택 취소 
  const clz = document.querySelectorAll('input#selected_actor1, input#selected_actor2,input#selected_actor3');
 
  for(let i=0; i<clz.length; i++){
    clz[i].addEventListener('click', ()=>{
      //alert($(this))
      //clz[i].style.display="none";
      $("#selected_actor"+(i+1)).val("")
      let remove = document.getElementById("selected_actor"+(i+1))
      remove.classList.remove('actos')
      // clz[i].remove();
      delete name[i];
       
    }, 10);

  }

  // actor 중복검사
  // if (selected_actor != "신입 배우") {
  //   if (selected_actor == fill_actor1 || selected_actor == fill_actor2 || selected_actor == fill_actor3) {
  //     alert("중복선택하셨습니다. 배우를 다시 선택해주세요.");
  //     return;
  //   }
  // }

  // if (fill_actor1 == 0 || fill_actor1 == "") {
  //   document.getElementById("selected_actor1").value = selected_actor;
  //   document.getElementById("actor1").value = selected_actor;
  // } else if (fill_actor2 == 0 || fill_actor2 == "") {
  //   document.getElementById("selected_actor2").value = selected_actor;
  //   document.getElementById("actor2").value = selected_actor;
  // } else {
  //   fill_actor3 = document.getElementById("selected_actor3").value;
  //   document.getElementById("selected_actor3").value = selected_actor;
  //   document.getElementById("actor3").value = selected_actor;
  // }

  // document.getElementById("pageForm").submit();
}


// 배우 선택을 취소하기 위한 js
function DeleteSelectActor1() {
 


  //1번 아이템 삭제
  var i = 0;
  while (i < name.length) {
    if (name[i] === name[0]) {
      name.splice(0, 1);
    } else {
      ++i;
    }
  }
  return name;
  
  // console.log(name);




  // let input = document.getElementById("selected_actor1");
  // input.value = null;
  // let input2 = document.getElementById("actor1");
  // input2.value = null;
  // document.getElementById("pageForm").submit();
}
function DeleteSelectActor2() {
  name.splice(1, 1);
 
 

  // let input = document.getElementById("selected_actor2");
  // let input2 = document.getElementById("actor2");
  // input.value = null;
  // input2.value = null;
  // document.getElementById("pageForm").submit();
}
function DeleteSelectActor3() {

  name.splice(2, 1);

  // let input = document.getElementById("selected_actor3");
  // let input2 = document.getElementById("actor3");
  // input.value = null;
  // input2.value = null;
  // document.getElementById("pageForm").submit();
}

// 배우 선택을 취소하기 위한 js 끝

// jQuery(document).ready(function () {
//   $("#modal").show();
// });
// function closeModal() {
//  $('.searchModal').hide();
// };

// 페이징을 클릭하면 검색했던 내용을 pageForm에 제출하기 위한 js
function searchFormCheck(searchWord, pageNumber) {
  document.getElementById("searchWord").value = searchWord;
  document.getElementById("page").value = pageNumber;
  document.getElementById("pageForm").submit();
}

// 이메일 등록 관련 모달창 관련 자바스크립트 코드 - 시작점 #######################
// 모달창 자바스크립트
window.onload = function() {
  function openEmailModal() {
    document.getElementById("emailModal").style.display="flex";
    document.getElementById("modalOpenBtn").style.display="none";
    document.getElementById("modalCloseBtn").style.display="flex";
  }
  
  function closeEmailModal() {
    document.getElementById("emailModal").style.display="none";
    document.getElementById("modalOpenBtn").style.display="flex";
    document.getElementById("modalCloseBtn").style.display="none";
  }
  
  const modalOpenBtn = document.querySelector("button#modalOpenBtn");
  modalOpenBtn.addEventListener('click', openEmailModal);
  
  const modalCloseBtn = document.querySelector("button#modalCloseBtn");
  
  modalCloseBtn.addEventListener('click', closeEmailModal);   
  
}



// ################ 모달창의 등록하기 버튼 클릭시 실행되는 onclick속성의 자바스크립트 ajax로 접속해있는 user의 email의 존재여부를 판단
function emailCheckAjax() {
  $.ajax({
    type: 'POST',
    url: '/user/ajax_confirm_email/',
    data: JSON.stringify({
        emailName: $('#userEmailId').val(),
        emailDomain: $('#userEmailDomain').val(),
    }),
    headers: {
      'X-CSRFTOKEN': $('#csrf_token').val()
    },
    success: function (json) {
        if (json.result == 'True') {

          filmEmailConstitutionSubmit(); //이메일 유효성 검사 자바스크립트


        } else {
          alert('영화사이메일 등록이 이미 되어있습니다.');
        }
    },
    error: function (xhr, errmsg, err) {
        alert('에러가 발생했습니다.' + errmsg);
        console.log(xhr.status + ": " + xhr.responseText);
    }
  }); 
}

//이메일 유효성 검사 자바스크립트 
function filmEmailConstitutionSubmit() {
  let userEmailId=document.getElementById("userEmailId").value;
  let userEmailDomain=document.getElementById("userEmailDomain").value;
  if (userEmailId == 0 || userEmailId == "" || userEmailDomain == 0 || userEmailDomain == "") {
    alert("이메일을 제대로 입력하였는지 확인해주세요.");
    return false;
  }
  else {
    
    authBackendsAjax(); // 토큰검사를위해서 위한 자바스크립트 Ajax  주석 비주석 포인트
    // alert("입력하신 이메일에서 링크를 눌러주세요")
    // document.getElementById("emailname_input").value = userEmailId;
    // document.getElementById("emaildomain_input").value = userEmailDomain;
    // alert("영화사 이메일등록이 완료되었습니다.");
    // document.getElementById("film_email_constitution_form_id").submit();
  }
}

// 토큰검사를위해서 위한 자바스크립트 Ajax
function authBackendsAjax(){

  $.ajax({
    async: false, // 비동기인 ajax의 스케줄링을 위한 설정(default : true)
    type: 'POST',
    url: '/user/ajax_token_email/',
    data: JSON.stringify({
      userEmailId: $('#userEmailId').val(),
      userEmailDomain: $('#userEmailDomain').val(),
    }),
    headers: {
      'X-CSRFTOKEN': $('#csrf_token').val()
    },
    success: function (json) {
        if (json.result == 'True') {

          alert("입력하신 이메일에서 링크를 눌러주세요\n만약 이메일이 오지 않았다면 입력한 이메일을 다시 한 번 확인하고 등록하기 버튼을 눌러주세요.")
                    
        } else {

          alert('이미 등록된 Email이거나 유효하지 않은 Email일 수있습니다.\nEmail을 제대로 입력했는지 다시 한 번 확인해주세요.');
          return false;
    
        }
    },
    error: function (xhr, errmsg, err) {
        alert('유효하지 않은 이메일입니다. 다시 한번 확인해주세요.');
        // alert('에러가 발생했습니다.' + errmsg);
        console.log(xhr.status + ": " + xhr.responseText);
    }
  });
};

// function emailDivtagClick () {
//   let userEmailId=document.getElementById("userEmailId").value;
//   let userEmailDomain=document.getElementById("userEmailDomain").value;
//   document.getElementById("emailname_input").value = userEmailId;
//   document.getElementById("emaildomain_input").value = userEmailDomain;
//   alert("영화사 이메일등록이 완료되었습니다.");
//   document.getElementById("film_email_constitution_form_id").submit();
// }




//################# 다음으로가기버튼클릭시 email 존재여부 확인 ajax
function nextBtnEmailCheckAjax() {
  $.ajax({
    type: 'POST',
    url: '/user/ajax_confirm_email/', 
    data: JSON.stringify({
        emailName: $('#emailname_input').val(),
        emailDomain: $('#emaildomain_input').val(),
    }),
    headers: {
      'X-CSRFTOKEN': $('#csrf_token').val()
    },
    success: function (json) {
        if (json.result == 'True') {
          alert('앗! 영화사를 설립하는 것을 깜박했습니다.\n다음에 배우3명을 캐스팅하기 전에\n이메일을 등록해주시겠어요?');
          return false;
        } 
        else {
          selectDataDirector();
        }
    },
    error: function (xhr, errmsg, err) {
        alert('에러가 발생했습니다.' + errmsg);
        console.log(xhr.status + ": " + xhr.responseText);
    }
  })}
function ToResultBtnEmailCheckAjax() {
  $.ajax({
    type: 'POST',
    url: '/user/ajax_confirm_email/', 
    data: JSON.stringify({
        emailName: $('#emailname_input').val(),
        emailDomain: $('#emaildomain_input').val(),
    }),
    headers: {
      'X-CSRFTOKEN': $('#csrf_token').val()
    },
    success: function (json) {
        if (json.result == 'True') {
          alert('이메일을 등록해주세요.');
          return false;
        } 
        else {
          selectDataNationsAuditOpendt();
        }
    },
    error: function (xhr, errmsg, err) {
        alert('에러가 발생했습니다.' + errmsg);
        console.log(xhr.status + ": " + xhr.responseText);
    }
  })}
  

// 이메일 등록 관련 모달창 관련 자바스크립트 코드 - 끝점 #######################

