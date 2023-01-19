function changeFormIdCheckMent() {
    // 회원정보 변경시 예외처리기능
    // let changename = document.getElementById("changeName").value;
    let originname = document.getElementById("originName").value;
    let changepassword1 = document.getElementById("changePassword1").value;
    let changepassword2 = document.getElementById("changePassword2").value;

    // if (originname==0 || changename=='') {
    //     alert("ID를 입력해주세요.");
    //     return false;
    // }

    // else if (originname != changename) {
    //     alert("접속중인 ID와 수정하려는 ID가 불일치합니다.");
    //     return false; }
    //  else

    if (changepassword1==0 || changepassword1=='') {
        alert("PW를 입력해주세요.");
        return false;
    } else if (changepassword1.length < 8 || changepassword1.length > 20) {
        alert("PW는 8자이상 20자 미만 입니다. PW 글자 수를 확인해 주세요.")
        return false;
    } else if (changepassword1 != changepassword2) {
        alert("비밀번호를 다시 확인해 주세요.");
        return false;
    }
    passwordCheckAjax();
    // document.getElementById("changeName").value = changename
    // document.getElementById("originName").value = originname
    // document.getElementById("changePassword1").value = changepassword1
    // document.getElementById("changePassword2").value = changepassword2
    // alert("회원정보수정이 완료되었습니다.")
    // document.getElementById("userChange").submit();

}

// document.getElementsByClassName('w-btn-outline w-btn-gray-outline').addEventListener('click', e => {
//     window.history.forward();
//   })

function passwordCheckAjax() {
    $.ajax({
        // async: false,
        type: 'POST',
        url: '/user/password_check_ajax/',
        data: JSON.stringify({
            changepassword1: $('#changePassword1').val(),
        }),
        headers: {
            'X-CSRFTOKEN': $('#csrf_token').val()
        },
        success: function (json) {
            if (json.result == 'True') {
                let changepassword1 = document.getElementById("changePassword1").value;
                let changepassword2 = document.getElementById("changePassword2").value;
                document.getElementById("changePassword1").value = changepassword1
                document.getElementById("changePassword2").value = changepassword2
                alert("회원정보수정이 완료되었습니다.")
                document.getElementById("userChange").submit();
            } else  {
                alert('변경하고자 하는 비밀번호와 현재 비밀번호가 일치합니다.\n다시 입력해주세요.')
                return false;
            } 
        },
        error: function (xhr, errmsg, err) {
            alert('에러가 발생했습니다.' + errmsg)
            console.log(xhr.status + ": " + xhr.responseText);
        },
    }); 
}
  