let card = document.getElementsByClassName("card");

setTimeout(function(){ 
      for(var i =0; i<card.length; i++) {
   card[i].classList.remove("preShow")
}
},2000);



function change_user(){
   window.location.href = 'http://127.0.0.1:8000/user/change_user_page/'
}

function delete_user(){
   window.location.href = 'http://127.0.0.1:8000/user/delete_user_page/'
   
}