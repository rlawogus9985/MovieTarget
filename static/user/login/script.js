/* ========================================= * 
		        BEST VIEWED FULLSCREEN
   https://codepen.io/ig_design/full/KKVQpVP
 * ========================================= */

   function loginFormCheck() {
    
    // 로그인 아이디 비밀번호 확인
    let loginname = document.getElementById("loginname").value;
    let loginpassword = document.getElementById("loginpassword").value;

    document.getElementById("username").value = loginname;
    document.getElementById("password").value = loginpassword;
    document.getElementById("loginForm").submit();
  }
   function SignupFormCheck() {

    // 아이디 검사
    let idTxt = document.getElementById("signupname").value;
    if (idTxt.length < 4 || idTxt.length > 12) {
      alert("아이디 글자 수를 확인해 주세요.");
      return false;

    }
    // 비밀번호 글자수 검사
    let pwTxt = document.getElementById("signuppass").value;
    if (pwTxt.length < 8 || pwTxt.length > 20) {
      alert("비밀번호 글자 수를 확인해 주세요.")
      return false;
    }
    // 비밀번호 일치 검사
    let PwChkTxt = document.getElementById("signuppass2").value;
    if (PwChkTxt != pwTxt) {
      alert("입력하신 비밀번호를 확인해주세요.")
      return false;
    }
    
    document.getElementById("joinusername").value = idTxt;
    document.getElementById("joinpassword1").value = pwTxt;
    document.getElementById("joinpassword2").value = PwChkTxt;
    document.getElementById("signupForm").submit();
  }