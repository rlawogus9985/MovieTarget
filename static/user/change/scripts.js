function changeFormIdCheckMent() {
    let changename = document.getElementById("changeName").value;
    let originname = document.getElementById("originName").value;
    // let changepassword = document.getElementById("changePassword").value;
    if (changename == originname) {
        document.getElementById("changeUserBt") = changename
        alert("접속중인 ID와 수정하려는 ID가 일치합니다.")
        true
    } else if (changename != originname) {
        alert("접속중인 ID와 수정하려는 ID가 불일치합니다.")
        false
    }
    document.getElementById("userChange").submit();
    return
}

// window.history.forward(); function noBack(){ 
//     window.history.forward();
//   }
