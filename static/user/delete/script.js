function questionModal() {
    document.getElementById('deleteUserBt').addEventListener('click', function() {
        // 모달창 띄우기
        modal('my_modal');
    }); 
}
 



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



function modal(id) {
    var zIndex = 9999;
    var modal = document.getElementById(id);

    // 모달 div 뒤에 희끄무레한 레이어
    var bg = document.createElement('div');
    bg.setStyle({
        position: 'fixed',
        zIndex: zIndex,
        left: '0px',
        top: '0px',
        width: '100%',
        height: '100%',
        overflow: 'auto',
        // 레이어 색갈은 여기서 바꾸면 됨
        backgroundColor: 'rgba(0,0,0,0.4)'
    });
    document.body.append(bg);

    // 닫기 버튼 처리, 시꺼먼 레이어와 모달 div 지우기
    modal.querySelector('.modal_close_btn').addEventListener('click', function() {
        bg.remove();
        modal.style.display = 'none';
    });

    modal.setStyle({
        position: 'fixed',
        display: 'block',
        boxShadow: '0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19)',

        // 시꺼먼 레이어 보다 한칸 위에 보이기
        zIndex: zIndex + 1,

        // div center 정렬
        top: '50%',
        left: '50%',
        transform: 'translate(-50%, -50%)',
        msTransform: 'translate(-50%, -50%)',
        webkitTransform: 'translate(-50%, -50%)'
    });
}

// Element 에 style 한번에 오브젝트로 설정하는 함수 추가
Element.prototype.setStyle = function(styles) {
    for (var k in styles) this.style[k] = styles[k];
    return this;
};


function reasonAjax() {
    $.ajax({
      type: "POST",
      async: false,
      url: "/user/delete_user_reason/",
      data: JSON.stringify({
        reason: $("#reason").val(),
      }),
      headers: {
        "X-CSRFTOKEN": $("#csrf_token").val(),
      },
      success: function (json) {
        if (json.result == "True") {
        //   alert("reason이 ajax로 view를 다녀왔습니다.");
        //   modal.style.display = 'none';
          document.getElementById("my_modal").style.display = 'none';
          
          userDeleteRealUpdate();
          logoutAjax();

          location.href="http://127.0.0.1:8000/"
        } else {
          alert("reason이 없습니다.")
        }
      },
      error: function (xhr, errmsg, err) {
        alert("에러가 발생했습니다." + errmsg);
        console.log(xhr.status + ": " + xhr.responseText);
      },
    });
  }


function userDeleteRealUpdate() {
$.ajax({
    async: false,
    type: "POST",
    url: "/user/delete_user/",
    data: JSON.stringify({
    }),
    headers: {
    "X-CSRFTOKEN": $("#csrf_token").val(),
    },
    success: function (json) {
    if (json.result == "True") {
    } else {
    }
    },
    error: function (xhr, errmsg, err) {
        alert('에러가 발생했습니다.' + errmsg)
        console.log(xhr.status + ": " + xhr.responseText);
    },
}); 
}


function logoutAjax() {
  $.ajax({
    type: "POST",
    url: "/user/logout/",
    data: JSON.stringify({
    }),
    headers: {
      "X-CSRFTOKEN": $("#csrf_token").val(),
    },
    success: function (json) {
      if (json.result == "True") {
      } else {        
      }
    },
    error: function (xhr, errmsg, err) {
      alert("에러가 발생했습니다." + errmsg);
      console.log(xhr.status + ": " + xhr.responseText);
    },
  });
}