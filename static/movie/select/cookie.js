window.onload = function(){
    if((document.getElementById("selected_actor1").value) != null) {
        let selected_actor1 = document.getElementById("selected_actor1").value
        setCookie("selected_actor1",selected_actor1, 1); //하루 지나면 만료
    } else if((document.getElementById("selected_actor2").value) != null) {
        let selected_actor2 = document.getElementById("selected_actor2").value
        setCookie("selected_actor2",selected_actor2, 1); 
    } else if((document.getElementById("selected_actor3").value) != null) {
        let selected_actor3 = document.getElementById("selected_actor3").value
        setCookie("selected_actor3",selected_actor3, 1); 
    }
    
    
}


////// 배우 3명 선택시 CSS 선택자 컨트롤을 위한 Javscript에서 cookie에 값넣는 코드들

// deprecation 되는 내장함수 escape()를[페이지의 인코딩이 무엇이건 유니코드로 인코딩 해서 주고 받는] -> 대체하기위한 사용자 정의 함수
function _escape(text) {
    let res = '', i;
    for(i = 0; i < text.length; i ++) {
      let c = text.charCodeAt(i);
      if(c < 256) res += encodeURIComponent(text[i]);
      else res += '%u' + c.toString(16).toUpperCase();
    }
    return res;
  }
  // 자바스크립트에서 쿠키를 만드는 함수 정의
    function setCookie(key, value, expiredays) {
    let todayDate = new Date();
    todayDate.setDate(todayDate.getDate() + expiredays)

    document.cookie = key + "=" + _escape(value) + "; path=/; expires=" + todayDate.toUTCString()+";";
    }
  ////// 배우 3명 선택시 CSS 선택자 컨트롤을 위한 Javscript에서 cookie에 값넣는 코드들