/* ========================================= * 
BEST VIEWED FULLSCREEN
https://codepen.io/ig_design/full/KKVQpVP
* ========================================= */
window.onload = function() {
  document.getElementById('loginName').addEventListener('keyup', enterCheckLogin);
  document.getElementById('loginPassword').addEventListener('keyup', enterCheckLogin);
  document.getElementById('signupName').addEventListener('keyup', enterCheckLogin);
  document.getElementById('signupPass').addEventListener('keyup', enterCheckLogin);
  document.getElementById('signupPass2').addEventListener('keyup', enterCheckLogin);
}

function enterCheckLogin(e) {
  if (e.key == "Enter") loginFormCheck();
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
    
    // function enterCheckSign(e) {
    //   if (e.key == "Enter") SignupFormCheck();
    // }
    function enterCheckSign() {
      if (window.event.keycode == 13) {
        SignupFormCheck();
      }
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
  
  document.getElementById("joinUserName").value = idTxt;
  document.getElementById("joinPassword1").value = pwTxt;
  document.getElementById("joinPassword2").value = PwChkTxt;
  document.getElementById("signupForm").submit();
  alert("회원가입이 완료되었습니다.")
  }
  
  