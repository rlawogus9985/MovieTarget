/* ========================================= * 
BEST VIEWED FULLSCREEN
https://codepen.io/ig_design/full/KKVQpVP
* ========================================= */
window.onload = function() {
  // 깜박이는 것이 키업**
  document.getElementById('loginName').addEventListener('keyup', enterCheckLogin); 
  document.getElementById('loginPassword').addEventListener('keyup', enterCheckLogin);
  document.getElementById('signupName').addEventListener('keyup', enterCheckSign);
  document.getElementById('signupPass').addEventListener('keyup', enterCheckSign);
  document.getElementById('signupPass2').addEventListener('keyup', enterCheckSign);


  // 찾기 모달창
  function openModalFindEmail() {
    document.getElementById("findModalCloseBtn").style.display="flex";
    document.getElementById("findModal").style.display="flex";    
  }
  function closeModalFindEmail() {
    document.getElementById("findModal").style.display="none";
    document.getElementById("findModalCloseBtn").style.display="none"; 
  }
  const modalOpenBtn = document.querySelector("span#h6SpanFind");
  modalOpenBtn.addEventListener('click', openModalFindEmail);
  const modalCloseBtn = document.querySelector("button#findModalCloseBtn");
  modalCloseBtn.addEventListener('click', closeModalFindEmail);
  // 찾기 모달창


}

function enterCheckLogin(e) {
  // if (e.key == "Enter") loginFormCheck();
  if (e.key == "Enter") loginAjax(); // 엔터를 눌르면 동작해라**
}


function enterCheckSign(e) {
  // if (e.key == "Enter") SignupFormCheck();
  if (e.key == "Enter") signupAjax();
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
  
  document.getElementById("joinUserName").value = idTxt;
  document.getElementById("joinPassword1").value = pwTxt;
  document.getElementById("joinPassword2").value = PwChkTxt;
  document.getElementById("signupForm").submit();
  alert("회원가입이 완료되었습니다.")

}


////////// Ajax /////////////
// 원본 Ajax login jvs
function loginAjax() {
  $.ajax({
    type: 'POST',
    url: '/user/ajax_user_login/',
    data: JSON.stringify({
        loginname: $('#loginName').val(),
        loginpassword: $('#loginPassword').val(),
    }),
    headers: {
      'X-CSRFTOKEN': $('#csrf_token').val()
    },
    success: function (json) {
        if (json.result == 'True') {
          loginFormCheck();
        } else {
          alert('ID를 확인해주세요.');
        }
    },
    error: function (xhr, errmsg, err) {
        alert('에러가 발생했습니다.' + errmsg);
        console.log(xhr.status + ": " + xhr.responseText);
    }
  }); 
}

// 원본 Ajax signup jvs
function signupAjax() {
  $.ajax({
    type: 'POST',
    url: '/user/ajax_user_signup/',
    data: JSON.stringify({
        signupname: $('#signupName').val(),
        // signuppassword: $('#signupPass').val(),
    }),
    headers: {
      'X-CSRFTOKEN': $('#csrf_token').val()
    },
    success: function (json) {
        if (json.result == 'True') {
          SignupFormCheck();
        } else  {
          alert('회원가입 할 수 없는 ID입니다.');
        } 
    },
    error: function (xhr, errmsg, err) {
        alert('에러가 발생했습니다.' + errmsg)
        console.log(xhr.status + ": " + xhr.responseText);
    },
  }); 
}

// ###################################################
// // 아이디찾기 관련 자바스크립트 ###########

// 아이디 찾기 버튼과 연동되는 자바스크립트함수
function wantFindId(){
  toFindIdplzInputEmail();
}

// 아이디 찾기 무기입 방지
function toFindIdplzInputEmail(){ 
  let userEmailId=document.getElementById("findUserEmailId").value;
  let userEmailDomain=document.getElementById("findUserEmailDomain").value;
  if (userEmailId == 0 || userEmailId == "" || userEmailDomain == 0 || userEmailDomain == "") {
    alert("아이디를 찾기 위한 이메일을 제대로 입력하였는지 확인해주세요.");
    return false
  }
  else {
    fidnModalBtnEmailCheckAjax();
  }
};

// 아이디 찾기 ajax 함수
function fidnModalBtnEmailCheckAjax() {
  $.ajax({
    async: false,
    type: 'POST',
    url: '/user/ajax_to_find_confirm_email/',
    data: JSON.stringify({
        emailName: $('#findUserEmailId').val(),
        emailDomain: $('#findUserEmailDomain').val(),
    }),
    headers: {
      'X-CSRFTOKEN': $('#csrf_token').val()
    },
    success: function (json) {
        if (json.result == 'True') {
          alert('아이디를 찾기위한 이메일이 성공적으로 발송되었습니다.\n입력하신 이메일의 메일을 확인해주세요.')
        } 
        // else {
        //     alert('입력하신 이메일은 등록된 이메일이 아닙니다.\n다시 확인해주세요.')
        //     return false;
        //   }
        },
        error: function (xhr, errmsg, err) {
          alert('입력하신 이메일은 등록된 이메일이 아닙니다.\n다시 확인해주세요.');
          // console.log(xhr.status + ": " + xhr.responseText);
        }
      })}
      
// // 아이디찾기 관련 자바스크립트 ###########
// ###################################################



// ###################################################
// // 비밀번호 재설정 관련 자바스크립트 ###########
           
function wantFindPassword() {
  toFindplzInputIdEmailDomain();
};


function toFindplzInputIdEmailDomain(){

  let toPasswordFindEmailId=document.getElementById("toPasswordFindEmailId").value;
  let toPasswordFindEmailDomain=document.getElementById("toPasswordFindEmailDomain").value;
  let findId=document.getElementById("findId").value;

  if (findId == 0 || findId == "" || toPasswordFindEmailId == 0 || toPasswordFindEmailId == "" || toPasswordFindEmailDomain == 0 || toPasswordFindEmailDomain == ""){
    alert("비밀번호를 찾기위한 ID와 Email을 제대로 입력하였는지 확인해주세요.");
    return false;
  }
  else {
    findPasswordReset();
  }
};
// 비밀번호 찾기(재설정) ajax 함수

function findPasswordReset() {
  $.ajax({
    async: false,
    type: 'POST',
    url: '/user/findpasswordreset/',
    data: JSON.stringify({
        userName: $('#findId').val(),
        emailName: $('#toPasswordFindEmailId').val(),
        emailDomain: $('#toPasswordFindEmailDomain').val(),
    }),
    headers: {
      'X-CSRFTOKEN': $('#csrf_token').val()
    },
    success: function (json) {
      if (json.result == 'True') {
        alert('비밀번호 재설정을 위한 이메일이 발송되었습니다.\n 이메일을 확인해주세요.')
      } 
      else {
          alert('아이디와 이메일이 일치하는 계정이 없습니다.\n 입력하신 정보를 다시 한 번 확인해주세요.')
          return false;
        }
      },
      error: function (xhr, errmsg, err) {
        alert('True alert.' + errmsg);
        console.log(xhr.status + ": " + xhr.responseText);
      }
    })}



function resetPasswordPage() {
  let resetID = document.getElementById("resetID").value;
  let resetPassword1 = document.getElementById("resetPassword1").value;
  let resetPassword2 = document.getElementById("resetPassword2").value;
  if (resetID==0 || resetID=="" || resetPassword1==0 || resetPassword1=="" || resetPassword2==0 || resetPassword2=="" ) {
    alert("입력하지 않은 부분이 있는지 확인해주세요.");
    return false; 
  }
  
  if (resetPassword1 < 8 ||resetPassword1 > 20 || resetPassword2 < 8 || resetPassword2 > 20) {
    alert('새로운 비밀번호는 8글자이상 20글자 이하로 입력해주세요.')
    return false;
  }
  
    if (resetPassword1 != resetPassword2) {
      alert('비밀번호와 재입력비밀번호가 서로 다릅니다.')
      return false;
    }
    
   else {
    ToresetPasswordFindEmail();
    
  }
}

function resetPasswordAjax () {
  $.ajax({
    async: false,
    type: 'POST',
    url: '/user/fromeamilpasswordreset/',
    data: JSON.stringify({
        resetID: $('#resetID').val(),
        resetPassword1: $('#resetPassword1').val(),
        resetPassword2: $('#resetPassword2').val(),
    }),
    headers: {
      'X-CSRFTOKEN': $('#csrf_token').val()
    },
    success: function (json) {
        if (json.result == 'False') {
          alert('비밀번호 변경에 실패했습니다.')
        }
        else {
          alert('패스워드가 변경이 되었습니다.\n새로운 비밀번호로 로그인해주세요.')
          window.close();
        }
        },
        error: function (xhr, errmsg, err) {
          alert('유저존재여부에 관한 Ajax오류입니다.');
          // console.log(xhr.status + ": " + xhr.responseText);
        }
      })}


function ToresetPasswordFindEmail(){
  $.ajax({
    async: false,
    type: 'POST',
    url: '/user/toresetpasswordfindemail/',
    data: JSON.stringify({
        resetID: $('#resetID').val(),
    }),
    headers: {
      'X-CSRFTOKEN': $('#csrf_token').val()
    },
    success: function (json) {
        if (json.result == 'True') {
          resetPasswordAjax();
        }
        else {
          alert('입력한 아이디는 없는 계정입니다.')
          return false;
        }
        },
        error: function (xhr, errmsg, err) {
          alert('에러가 발생합니다.\n좀 더 개선된 모습을 선보이도록 하겠습니다.');
          // console.log(xhr.status + ": " + xhr.responseText);
        }
      })}



// // 비밀번호 재설정 관련 자바스크립트 ###########
// ###################################################
////////// Ajax /////////////