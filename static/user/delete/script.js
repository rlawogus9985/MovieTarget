function deleteFormCheckMent() {
    alert("회원탈퇴가 완료되었습니다.");
    return true;
}

window.history.forward(); function noBack(){ 
    window.history.forward();
}

// 

var particle;

function main(){
    if (particles == null) {
        particles= document.getElementById("particles");
    }
    var np = document.documentElement.clientWidth / 29;
    particles.innerHTML = "";
    for (var i = 0; i < np; i++) {
        var w = document.documentElement.clientWidth;
        var h = document.documentElement.clientHeight;
        var rndw = Math.floor(Math.random() * w ) + 1;
        var rndh = Math.floor(Math.random() * h ) + 1;
        var widthpt = Math.floor(Math.random() * 8) + 3;
        var opty = Math.floor(Math.random() * 5) + 2;
        var anima = Math.floor(Math.random() * 12) + 8;

        var div = document.createElement("div");
        div.classList.add("particle");
        div.style.marginLeft = rndw+"px";
        div.style.marginTop = rndh+"px";
        div.style.width = widthpt+"px";
        div.style.height = widthpt+"px";
        div.style.background = "white";
        div.style.opacity = opty;
        div.style.animation = "move "+anima+"s ease-in infinite ";
        particles.appendChild(div);
    }
}
window.addEventListener("resize", main);
window.addEventListener("load", main);