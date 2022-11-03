let card = document.getElementsByClassName("card");

setTimeout(function(){ 
      for(var i =0; i<card.length; i++) {
   card[i].classList.remove("preShow")
}
},2000);

