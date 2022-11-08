/* ========================================= * 
BEST VIEWED FULLSCREEN
https://codepen.io/ig_design/full/KKVQpVP
* ========================================= */
window.onload = function() {
  document.getElementById('loginName').addEventListener('keyup', enterCheckLogin);
  document.getElementById('loginPassword').addEventListener('keyup', enterCheckLogin);
}
window.onload - function() {
  document.getElementById('signupName').addEventListener('keyup', enterCheckSign);
  document.getElementById('signupPass').addEventListener('keyup', enterCheckSign);
  document.getElementById('signupPass2').addEventListener('keyup', enterCheckSign);
}
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
  
  // ajax해볼자리
//   $.ajax({
//     type: 'POST',
//     url: '{% url "user:join" %}',
//     data: {
//         username: $('#signupName').val(),
//         password1: $('#signupPass').val(),
//         password2: $('#signupPass2').val(),
//         csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
//         action: 'post'
//     },
//     success: function (json) {
//         if (json.status == 1) {
//             // document.getElementById("post-form").reset();
//             document.getElementById("signupForm").reset();
//             window.location.href = 'http://127.0.0.1:8000/';
//             alert('등록되었습니다.');
//         } else if (json.status == 0) {
//             alert('이미 등록된 회원입니다.');
//         }
//     },
//     error: function (xhr, errmsg, err) {
//         alert('에러가 발생했습니다.' + errmsg);
//         console.log(xhr.status + ": " + xhr.responseText);
//     }
// });


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

// function ajaxSignup() {
//   username = document.getElementById("signupName").value;
//   password1 = document.getElementById("signupPass").value;
//   password2 = document.getElementById("signupPass2").value;
//   let data = {username, password1, password2}
//   $.ajax({
//     url: '/box_office/user/join/',
//     type: 'post',
//     data: JSON.stringify(data),
//     headers: {
//       'X-CSRFTOKEN' : '{{ csrf_token }}'
//     },
//     success: function(response) {
//       // 통신에 성공한 경우 실행할 함수. 전달받은 데이터를 매개변수로 통해 받음.
//       console.log('통신 성공');
//       console.log(response);
//     },
//     error: function(e) {
//         // 통신에 실패한 경우 실행할 함수. 오류 객체를 매개변수를 통해 받음.
//         console.log('통신 실패');
//         console.log(e);
//     },
//   });
// }
function SignupAjax() {
  $.ajax({
    type: 'POST',
    // url: '{% url "user:ajax_user" %}',
    url: '/user/ajax_user/',
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
