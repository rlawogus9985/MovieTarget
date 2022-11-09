function deleteFormCheckMent() {
    
    alert("회원탈퇴가 완료되었습니다.");
    return true;
}

window.history.forward(); function noBack(){ 
    window.history.forward();
}

function info_user(){
    window.location.href = 'http://127.0.0.1:8000/user/profile/'
    
 }