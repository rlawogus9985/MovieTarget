/* ========================================= * 
BEST VIEWED FULLSCREEN
https://codepen.io/ig_design/full/KKVQpVP
* ========================================= */
window.onload = function() {
  document.getElementById('loginName').addEventListener('keyup', enterCheckLogin);
  document.getElementById('loginPassword').addEventListener('keyup', enterCheckLogin);
  document.getElementById('signupName').addEventListener('keyup', enterCheckSign);
  document.getElementById('signupPass').addEventListener('keyup', enterCheckSign);
  document.getElementById('signupPass2').addEventListener('keyup', enterCheckSign);
}
// window.onload - function() {
//   document.getElementById('signupName').addEventListener('keyup', enterCheckSign);
//   document.getElementById('signupPass').addEventListener('keyup', enterCheckSign);
//   document.getElementById('signupPass2').addEventListener('keyup', enterCheckSign);
// }
function enterCheckLogin(e) {
  if (e.key == "Enter") loginFormCheck();
}
function enterCheckSign(e) {
  if (e.key == "Enter") SignupFormCheck();
}





function loginFormCheck() {
  // Form에 제출하기전 user가 입력한 input태그의 id를 통하여 value를 변수명 객체에 초기화  
  let username = document.getElementById("loginName").value;
  let password = document.getElementById("loginPassword").value;
  // 로그인 아이디 및 패스워드 무입력 검사
  if (username==0 || username=="") {
    alert("ID를 입력해주세요.")
    return false;
  } 
      else if(password==0 || password=="") {
        alert("PW를 입력해주세요.")
        return false;
      }
      document.getElementById("userName").value = username;
      document.getElementById("passWord").value = password;
      document.getElementById("loginForm").submit();
    }
    
function SignupFormCheck() {

  // 무입력 아이디 검사
  let idTxt = document.getElementById("signupName").value;
  if (idTxt==0 || idTxt=="") {
    alert("회원가입에 사용하실 ID를 입력해주세요.")
    return false;
  }
  
  // 4이상 12이하의 아이디 검사
  if (idTxt.length < 4 || idTxt.length > 12) {
    alert("ID 글자 수를 확인해 주세요.");
    return false;
  }
  
  // 무입력 비밀번호 검사
  let pwTxt = document.getElementById("signupPass").value;
  if (pwTxt==0 || pwTxt=="") {
    alert("회원가입에 사용하실 PW를 입력해주세요.")
    return false;
  }

  // 비밀번호 글자수 검사
  let PwChkTxt = document.getElementById("signupPass2").value;
  if (pwTxt.length < 8 || pwTxt.length > 20) {
    alert("PW 글자 수를 확인해 주세요.")
    return false;
  }

  // 비밀번호 일치 검사
  if (PwChkTxt != pwTxt) {
    alert("입력하신 비밀번호를 확인해주세요.")
    return false;
  }
  
  // 옛날방식 어려움
  // if (!isIdChecked)
  // ~~~
  // return false;

  document.getElementById("joinUserName").value = idTxt;
  document.getElementById("joinPassword1").value = pwTxt;
  document.getElementById("joinPassword2").value = PwChkTxt;
  document.getElementById("signupForm").submit();
  alert("회원가입이 완료되었습니다.")
  }
  
// 옛날방식 어려움
// let isIdChecked = False;  // 아이디 중복 검사 실시했는지(통과했는지) 여부.

// function idCheck() {
//   ...
// }


////////// Ajax /////////////
function signupAjax() {
  $.ajax({
    type: 'POST',
    url: '/user/ajax_user_signup/',
    data: JSON.stringify({
        username: $('#signupName').val()
    }),
    headers: {
      'X-CSRFTOKEN': $('#csrf_token').val()
    },
    success: function (json) {
        if (json == 'True') {
            alert('회원가입을 할 수 있는 ID입니다.');
            SignupFormCheck();
        } else {
            alert('회원가입을 할 수 없는 ID입니다.');
        }
    },
    error: function (xhr, errmsg, err) {
        alert('에러가 발생했습니다.' + errmsg);
        console.log(xhr.status + ": " + xhr.responseText);
    }
  }); 
}

// 원본 Ajax login jvs
function loginAjax() {
  $.ajax({
    type: 'POST',
    url: '/user/ajax_user_login/',
    data: JSON.stringify({
        username: $('#loginName').val(),
        password: $('#loginPassword').val()
    }),
    headers: {
      'X-CSRFTOKEN': $('#csrf_token').val()
    },
    success: function (json) {
        if (json == 'False') {
            alert('ID와 PW를 확인해주세요.');
            
        } else {
            loginFormCheck();
        }
    },
    error: function (xhr, errmsg, err) {
        alert('에러가 발생했습니다.' + errmsg);
        console.log(xhr.status + ": " + xhr.responseText);
    }
  }); 
}


//////테스트 중
// function loginAjax() {
//   $.ajax({
//     type: 'POST',
//     url: '/user/ajax_user_login/',
//     data: JSON.stringify({
//         username: $('#loginName').val(),
//         password: $('#loginPassword').val()
//     }),
//     headers: {
//       'X-CSRFTOKEN': $('#csrf_token').val()
//     },
//     success: function (json) {
//         if (json == 'UserNameNone') {
//             alert('ID를 입력해주세요.');  
//         } else if (json == 'UserPassNone') {
//             alert('PW를 입력해주세요.')
//         } else if (json == 'InvalidPw') {
//             alert('해당 ID의 PW와 일치하지 않습니다.')
//         }
//         else if (json == 'True') {
//             loginFormCheck();
//         }
//     },
//     error: function (xhr, errmsg, err) {
//         alert('에러가 발생했습니다.' + errmsg);
//         console.log(xhr.status + ": " + xhr.responseText);
//     }
//   }); 
// }

////////// Ajax /////////////