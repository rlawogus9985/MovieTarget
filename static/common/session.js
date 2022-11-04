// sessionStorage.getItem("selected_director"); sessionstorage 세션에서 key로 value 뽑는 코드 언젠가 필요할지도?

function sessionDirectorDataImport() {
    let selected_director = document.getElementById("selected_director").value;
    sessionStorage.setItem("selected_director",selected_director);
    
}

function sessionGenreDataImport() {
    let selected_genre = document.getElementById("selected_genre").value;
    sessionStorage.setItem("selected_genre",selected_genre);
}

function sessionActorsDataImport() {
    let selected_actor1 = document.getElementById("selected_actor1").value;
    let selected_actor2 = document.getElementById("selected_actor2").value;
    let selected_actor3 = document.getElementById("selected_actor3").value;
    sessionStorage.setItem("selected_actor1",selected_actor1);
    sessionStorage.setItem("selected_actor2",selected_actor2);
    sessionStorage.setItem("selected_actor3",selected_actor3);
}


