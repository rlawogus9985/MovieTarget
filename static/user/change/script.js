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
    // document.getElementById("changeName").value = changename
    // document.getElementById("originName").value = originname
    document.getElementById("changePassword1").value = changepassword1
    document.getElementById("changePassword2").value = changepassword2
    alert("회원정보수정이 완료되었습니다.")
    document.getElementById("userChange").submit();

}

// document.getElementsByClassName('w-btn-outline w-btn-gray-outline').addEventListener('click', e => {
//     window.history.forward();
//   })